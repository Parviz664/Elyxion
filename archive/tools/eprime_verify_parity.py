#!/usr/bin/env python3
import argparse
import json
import sys

ROLE_MAP = {
    "user": "user",
    "assistant": "assistant",
    "system": "system_if_exported",
    "tool": "tool_if_exported",
    "unknown": "opaque_unknown",
}

def verify(payload):
    source = payload["source_records"]
    archive = payload["archive_records"]
    provenance = payload["provenance_records"]
    attachments = payload.get("attachment_records", [])

    report = {
        "source_record_count": len(source),
        "archive_record_count": len(archive),
        "order_mismatch_count": 0,
        "role_mismatch_count": 0,
        "boundary_mismatch_count": 0,
        "timestamp_mismatch_count": 0,
        "attachment_mismatch_count": 0,
        "system_record_drop_count": 0,
        "tool_record_drop_count": 0,
        "opaque_unresolved_count": 0,
        "raw_text_mismatch_count": 0,
        "source_ref_mismatch_count": 0,
    }

    if len(source) != len(archive) or len(source) != len(provenance):
        report["boundary_mismatch_count"] += abs(len(source) - len(archive))
        report["boundary_mismatch_count"] += abs(len(source) - len(provenance))

    n = min(len(source), len(archive), len(provenance))
    for i in range(n):
        s = source[i]
        a = archive[i]
        p = provenance[i]
        expected_sequence = i + 1

        if s["source_order_index"] != expected_sequence or a["sequence"] != expected_sequence or p["sequence"] != expected_sequence or p["source_order_index"] != s["source_order_index"]:
            report["order_mismatch_count"] += 1

        expected_role = ROLE_MAP.get(s["source_record_kind"], "opaque_unknown")
        if a["role"] != expected_role or p["archive_role"] != expected_role or p["source_record_kind"] != s["source_record_kind"]:
            report["role_mismatch_count"] += 1

        if a["sequence"] != p["sequence"]:
            report["boundary_mismatch_count"] += 1

        if a["raw_text"] != s["raw_text"]:
            report["raw_text_mismatch_count"] += 1

        if p["timestamp_state"] != s["timestamp_state"] or p["source_timestamp_raw_or_exact"] != s["source_timestamp_raw_or_exact"]:
            report["timestamp_mismatch_count"] += 1

        if a["source_ref"] != p["source_ref"]:
            report["source_ref_mismatch_count"] += 1

        source_attachments = s.get("attachments", [])
        bound = sorted(
            [x for x in attachments if x["message_sequence"] == a["sequence"]],
            key=lambda x: x["attachment_index"],
        )
        if p["attachment_count"] != len(source_attachments) or len(bound) != len(source_attachments):
            report["attachment_mismatch_count"] += 1
        else:
            for expected, observed in zip(source_attachments, bound):
                if (
                    expected["attachment_index"] != observed["attachment_index"]
                    or expected["attachment_type"] != observed["attachment_type"]
                    or expected["source_ref"] != observed["source_ref"]
                ):
                    report["attachment_mismatch_count"] += 1
                    break

        if s["source_record_kind"] == "unknown":
            report["opaque_unresolved_count"] += 1

    archived_kinds = {p["source_record_kind"] for p in provenance}
    if any(s["source_record_kind"] == "system" for s in source) and "system" not in archived_kinds:
        report["system_record_drop_count"] += 1
    if any(s["source_record_kind"] == "tool" for s in source) and "tool" not in archived_kinds:
        report["tool_record_drop_count"] += 1

    mismatch_fields = [
        k for k in report
        if k.endswith("_count") and k not in ("source_record_count", "archive_record_count")
    ]
    ok = (
        report["source_record_count"] == report["archive_record_count"]
        and len(source) == len(provenance)
        and all(report[k] == 0 for k in mismatch_fields)
    )
    report["verdict"] = "PASS_PARITY" if ok else "BLOCK_PARITY"
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json")
    args = parser.parse_args()
    with open(args.input_json, "r", encoding="utf-8") as f:
        payload = json.load(f)
    json.dump(verify(payload), sys.stdout, ensure_ascii=False, separators=(",", ":"))
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()
