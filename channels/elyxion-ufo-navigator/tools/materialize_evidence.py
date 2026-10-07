#!/usr/bin/env python3
import argparse, json, subprocess
from pathlib import Path

B=Path(__file__).resolve().parents[1]
INDEX=json.loads((B/"NAV_EVIDENCE_INDEX_V0_2.json").read_text())
AUTHOR_PATH=B/"NAV_AUTHOR_DECLARATIONS_V0_1.json"
AUTHOR=json.loads(AUTHOR_PATH.read_text())
BY_ID={x["evidence_id"]:x for x in INDEX["entries"]}

def git(*args):
    try:
        return subprocess.check_output(["git",*args],cwd=B.parent.parent.parent,text=True,stderr=subprocess.DEVNULL).strip()
    except Exception:
        return None

def git_blob_for_path(path):
    return git("hash-object",str(B.parent.parent.parent/path))

def materialize(evidence_id,requested_level):
    e=BY_ID.get(evidence_id)
    if not e:
        return {
          "receipt_id":f"MAT_UNKNOWN_{evidence_id}",
          "evidence_id":evidence_id,
          "requested_level":requested_level,
          "result":"BLOCKED",
          "source_identity":{"reason":"UNKNOWN_EVIDENCE_ID"},
          "integrity":"UNKNOWN",
          "body_handling":{"characters_read":0,"durably_duplicated":False},
          "semantic_status":"NOT_PERFORMED"
        }

    if e["source_type"]=="AUTHOR_DECLARATION":
        decl=next((x for x in AUTHOR["declarations"] if x["id"]==e["declaration_id"]),None)
        if not decl:
            result="BLOCKED"; integrity="UNKNOWN"; n=0
        else:
            result="MATERIALIZED"; integrity="MATCH"; n=len(json.dumps(decl,ensure_ascii=False))
        return {
          "receipt_id":f"MAT_{evidence_id}_{requested_level}",
          "evidence_id":evidence_id,
          "requested_level":requested_level,
          "result":result,
          "source_identity":{
            "ref":"channel/elyxion-ufo-navigator-v0.1",
            "path":"channels/elyxion-ufo-navigator/NAV_AUTHOR_DECLARATIONS_V0_1.json",
            "observed_blob_sha":git_blob_for_path(Path("channels/elyxion-ufo-navigator/NAV_AUTHOR_DECLARATIONS_V0_1.json")),
            "declaration_id":e["declaration_id"],
            "source_kind":"CURRENT_AUTHOR_DECLARATION"
          },
          "integrity":integrity,
          "body_handling":{"characters_read":n,"durably_duplicated":False},
          "semantic_status":"NOT_PERFORMED"
        }

    path=Path(e["path"])
    repo_root=B.parent.parent.parent
    local=repo_root/path

    if e["tracking_mode"]=="SELF_RESOLVE_AT_PACK_BUILD":
        if not local.exists():
            return {
              "receipt_id":f"MAT_{evidence_id}_{requested_level}",
              "evidence_id":evidence_id,"requested_level":requested_level,
              "result":"BLOCKED",
              "source_identity":{"ref":e["ref"],"path":e["path"],"reason":"SELF_FILE_UNAVAILABLE"},
              "integrity":"UNKNOWN",
              "body_handling":{"characters_read":0,"durably_duplicated":False},
              "semantic_status":"NOT_PERFORMED"
            }
        body=local.read_text()
        return {
          "receipt_id":f"MAT_{evidence_id}_{requested_level}",
          "evidence_id":evidence_id,"requested_level":requested_level,
          "result":"MATERIALIZED",
          "source_identity":{"ref":e["ref"],"path":e["path"],"observed_blob_sha":git_blob_for_path(path)},
          "integrity":"MATCH",
          "body_handling":{"characters_read":len(body),"durably_duplicated":False},
          "semantic_status":"NOT_PERFORMED"
        }

    expected=e.get("observed_blob_sha")
    if not expected or git("cat-file","-e",expected+"^{blob}") is None:
        return {
          "receipt_id":f"MAT_{evidence_id}_{requested_level}",
          "evidence_id":evidence_id,"requested_level":requested_level,
          "result":"BLOCKED",
          "source_identity":{"ref":e.get("ref"),"path":e.get("path"),"expected_blob_sha":expected,"reason":"PINNED_BLOB_UNAVAILABLE_IN_CHECKOUT"},
          "integrity":"UNKNOWN",
          "body_handling":{"characters_read":0,"durably_duplicated":False},
          "semantic_status":"NOT_PERFORMED"
        }
    body=git("cat-file","-p",expected) or ""
    return {
      "receipt_id":f"MAT_{evidence_id}_{requested_level}",
      "evidence_id":evidence_id,"requested_level":requested_level,
      "result":"MATERIALIZED",
      "source_identity":{"ref":e["ref"],"path":e["path"],"expected_blob_sha":expected,"observed_blob_sha":expected},
      "integrity":"MATCH",
      "body_handling":{"characters_read":len(body),"durably_duplicated":False},
      "semantic_status":"NOT_PERFORMED"
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("evidence_id")
    p.add_argument("--level",default="M1_EXACT_ARTIFACT")
    a=p.parse_args()
    r=materialize(a.evidence_id,a.level)
    print(json.dumps(r,indent=2,ensure_ascii=False))
    return 0 if r["result"]=="MATERIALIZED" else 2

if __name__=="__main__":
    raise SystemExit(main())
