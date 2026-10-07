#!/usr/bin/env python3
from materialize_evidence import materialize

def main():
    bad=[]
    boundary=materialize("EVID_NAV_GLOBAL_C0_BOUNDARY","M1_EXACT_ARTIFACT")
    author=materialize("EVID_AUTHOR_GLOBAL_C0_EXISTS","M1_EXACT_ARTIFACT")
    unknown=materialize("EVID_DOES_NOT_EXIST","M1_EXACT_ARTIFACT")

    if boundary["result"]!="MATERIALIZED" or boundary["integrity"]!="MATCH":bad.append("boundary")
    if author["result"]!="MATERIALIZED" or author["integrity"]!="MATCH":bad.append("author")
    if author["source_identity"].get("source_kind")!="CURRENT_AUTHOR_DECLARATION":bad.append("author-source-kind")
    if boundary["body_handling"]["durably_duplicated"] is not False:bad.append("boundary-copy")
    if unknown["result"]!="BLOCKED":bad.append("unknown-evidence")

    if bad:
        for x in bad:print("FAIL:",x)
        return 1
    print("PASS: self materialization + author declaration + blocked unknown evidence")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
