#!/usr/bin/env python3
import argparse
import hashlib
import json
import sys

FIELD_ORDER = [
    "sequence",
    "role",
    "timestamp",
    "raw_text",
    "attachments_refs",
    "source_ref",
    "previous_message_sha256",
    "message_sha256",
]

def compact_record(record):
    obj = {key: record[key] for key in FIELD_ORDER}
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))

def recover(records):
    if not records:
        return {
            "message_count": 0,
            "sequence_gap_count": 0,
            "conflicting_overlap_count": 0,
            "chain_break_count": 0,
            "terminal_message_sha256": None,
            "recovered_archive_sha256": hashlib.sha256(b"").hexdigest(),
            "verdict": "PASS_RECOVERY",
        }

    ordered = sorted(records, key=lambda r: r["sequence"])
    gaps = 0
    overlaps = 0
    chain_breaks = 0
    seen = {}
    prior_hash = "GENESIS"

    for idx, record in enumerate(ordered):
        seq = record["sequence"]
        expected_seq = ordered[0]["sequence"] + idx
        if seq != expected_seq:
            gaps += 1
        if seq in seen and seen[seq] != record["message_sha256"]:
            overlaps += 1
        seen[seq] = record["message_sha256"]
        if record["previous_message_sha256"] != prior_hash:
            chain_breaks += 1
        prior_hash = record["message_sha256"]

    payload = "\n".join(compact_record(r) for r in ordered).encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    verdict = "PASS_RECOVERY" if gaps == overlaps == chain_breaks == 0 else "BLOCK_RECOVERY"

    return {
        "message_count": len(ordered),
        "first_sequence": ordered[0]["sequence"],
        "last_sequence": ordered[-1]["sequence"],
        "sequence_gap_count": gaps,
        "conflicting_overlap_count": overlaps,
        "chain_break_count": chain_breaks,
        "terminal_message_sha256": ordered[-1]["message_sha256"],
        "recovered_archive_sha256": digest,
        "verdict": verdict,
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json")
    args = parser.parse_args()

    with open(args.input_json, "r", encoding="utf-8") as f:
        payload = json.load(f)

    report = recover(payload["records"])
    json.dump(report, sys.stdout, ensure_ascii=False, separators=(",", ":"))
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()
