#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
POLICY = BASE / "NAV_FRESHNESS_POLICY_V0_1.json"

def git_output(*args):
    return subprocess.check_output(["git", *args], text=True).strip()

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
    args = parser.parse_args()

    policy = json.loads(POLICY.read_text(encoding="utf-8"))
    self_ref = "channel/elyxion-ufo-navigator-v0.1"

    source_states = {}
    stale_sources = set()

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
            stale_sources.add(sid)

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

    result = {
        "policy_id": policy["policy_id"],
        "source_states": source_states,
        "subjects": subjects,
        "stale_sources": sorted(stale_sources),
        "global_recovery_required": False,
        "targeted_recovery_required": any(x["freshness"] == "STALE" for x in subjects),
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for sid, state in source_states.items():
            print(f"{sid}: {state['state']} ({state['ref']})")
        stale_subjects = [x for x in subjects if x["freshness"] == "STALE"]
        print(f"STALE_SUBJECTS={len(stale_subjects)}")
        print("GLOBAL_RECOVERY_REQUIRED=false")

    return 1 if any(x["freshness"] == "UNKNOWN" for x in subjects) else 0

if __name__ == "__main__":
    raise SystemExit(main())
