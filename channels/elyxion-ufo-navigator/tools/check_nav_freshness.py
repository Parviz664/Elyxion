#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
POLICY = BASE / "NAV_FRESHNESS_POLICY_V0_2.json"

def git_output(*args):
    return subprocess.check_output(["git", *args], text=True, stderr=subprocess.DEVNULL).strip()

def resolve_branch_head(ref, self_ref):
    if ref == self_ref:
        return git_output("rev-parse", "HEAD")
    remote_ref = f"refs/remotes/origin/{ref}"
    try:
        return git_output("rev-parse", remote_ref)
    except subprocess.CalledProcessError:
        try:
            line = git_output("ls-remote", "origin", f"refs/heads/{ref}")
            return line.split()[0] if line else None
        except subprocess.CalledProcessError:
            return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--fail-on-stale", action="store_true")
    args = parser.parse_args()

    policy = json.loads(POLICY.read_text(encoding="utf-8"))
    self_ref = "channel/elyxion-ufo-navigator-v0.1"

    source_states = {}
    stale_sources = set()
    unknown_sources = set()

    for source in policy["sources"]:
        sid = source["id"]
        current = resolve_branch_head(source["ref"], self_ref)
        mode = source["tracking_mode"]

        if mode == "SELF_CURRENT_HEAD":
            state = "FRESH" if current else "UNKNOWN"
        elif not current:
            state = "UNKNOWN"
        elif current == source["observed_head"]:
            state = "FRESH"
        else:
            state = "STALE"

        if state == "STALE":
            stale_sources.add(sid)
        if state == "UNKNOWN":
            unknown_sources.add(sid)

        source_states[sid] = {
            "state": state,
            "observed_head": source.get("observed_head"),
            "current_head": current,
            "ref": source["ref"],
        }

    subjects = []
    for dep in policy["dependencies"]:
        states = [source_states[s]["state"] for s in dep["source_ids"]]
        if "STALE" in states:
            state = "STALE"
        elif "UNKNOWN" in states:
            state = "UNKNOWN"
        else:
            state = "FRESH"
        subjects.append({
            "subject_kind": dep["subject_kind"],
            "subject_id": dep["subject_id"],
            "freshness": state,
            "source_ids": dep["source_ids"],
        })

    stale_subjects = [x for x in subjects if x["freshness"] == "STALE"]
    unknown_subjects = [x for x in subjects if x["freshness"] == "UNKNOWN"]

    result = {
        "policy_id": policy["policy_id"],
        "source_states": source_states,
        "subjects": subjects,
        "stale_sources": sorted(stale_sources),
        "unknown_sources": sorted(unknown_sources),
        "targeted_recovery_required": bool(stale_subjects),
        "global_recovery_required": False,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for sid, state in source_states.items():
            print(f"{sid}: {state['state']} ({state['ref']})")
        print(f"STALE_SUBJECTS={len(stale_subjects)}")
        print(f"UNKNOWN_SUBJECTS={len(unknown_subjects)}")
        print("GLOBAL_RECOVERY_REQUIRED=false")

    if unknown_subjects:
        return 2
    if args.fail_on_stale and stale_subjects:
        return 3
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
