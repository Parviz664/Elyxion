#!/usr/bin/env python3
import argparse
import json
import sys

REQUIRED_PASS_FLAGS = [
    "full_source_scope_proven",
    "source_blob_hash_pass",
    "message_completeness_pass",
    "source_parity_pass",
    "attachment_accounting_pass",
    "recovery_pass",
    "independent_copy_readback_pass",
]

REQUIRED_ZERO_COUNTS = [
    "missing_message_count",
    "sequence_gap_count",
    "duplicate_conflict_count",
    "raw_text_mismatch_count",
    "role_mismatch_count",
    "timestamp_mismatch_count",
    "system_record_drop_count",
    "tool_record_drop_count",
    "unresolved_record_count",
    "missing_attachment_count",
    "unresolved_attachment_count",
    "message_hash_mismatch_count",
    "message_chain_break_count",
    "chunk_chain_break_count",
    "receipt_chain_break_count",
    "recovery_mismatch_count",
]

def audit(payload):
    missing_flags = [k for k in REQUIRED_PASS_FLAGS if payload.get(k) is not True]
    nonzero_counts = {k: payload.get(k) for k in REQUIRED_ZERO_COUNTS if payload.get(k) != 0}
    refs = payload.get("required_evidence_refs", {})
    missing_refs = [k for k, v in refs.items() if not isinstance(v, str) or not v.strip()]
    required_ref_names = payload.get("required_ref_names", [])
    absent_ref_names = [k for k in required_ref_names if k not in refs]

    ok = not missing_flags and not nonzero_counts and not missing_refs and not absent_ref_names
    return {
        "missing_or_failed_pass_flags": missing_flags,
        "nonzero_or_missing_block_counts": nonzero_counts,
        "missing_or_blank_evidence_refs": missing_refs,
        "absent_required_ref_names": absent_ref_names,
        "verdict": "PASS_PRECLOSE" if ok else "BLOCK_PRECLOSE",
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input_json")
    args = p.parse_args()
    with open(args.input_json, "r", encoding="utf-8") as f:
        payload = json.load(f)
    json.dump(audit(payload), sys.stdout, ensure_ascii=False, separators=(",", ":"))
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()
