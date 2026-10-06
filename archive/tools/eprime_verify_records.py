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
]

def canonical_record_bytes(record):
    obj = {key: record[key] for key in FIELD_ORDER}
    text = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return text.encode("utf-8")

def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()

def verify(records):
    gaps = 0
    duplicates = 0
    hash_mismatches = 0
    chain_breaks = 0
    verified = 0
    seen = set()
    previous_hash = "GENESIS"
    message_hashes = []

    for index, record in enumerate(records, start=1):
        sequence = record["sequence"]
        if sequence in seen:
            duplicates += 1
        seen.add(sequence)
        if sequence != index:
            gaps += 1

        if record["previous_message_sha256"] != previous_hash:
            chain_breaks += 1

        observed = sha256_hex(canonical_record_bytes(record))
        expected = record["message_sha256"]
        if observed != expected:
            hash_mismatches += 1
        else:
            verified += 1

        message_hashes.append(expected)
        previous_hash = expected

    chunk_hash = sha256_hex("\n".join(message_hashes).encode("utf-8"))
    verdict = (
        "PASS_COMPLETE"
        if gaps == duplicates == hash_mismatches == chain_breaks == 0
        else "BLOCK_INTEGRITY"
    )
    return {
        "verified_message_hash_count": verified,
        "sequence_gap_count": gaps,
        "duplicate_sequence_count": duplicates,
        "message_hash_mismatch_count": hash_mismatches,
        "message_chain_break_count": chain_breaks,
        "chunk_sha256": chunk_hash,
        "verdict": verdict,
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json")
    args = parser.parse_args()
    with open(args.input_json, "r", encoding="utf-8") as f:
        payload = json.load(f)
    report = verify(payload["records"])
    json.dump(report, sys.stdout, ensure_ascii=False, separators=(",", ":"))
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()
