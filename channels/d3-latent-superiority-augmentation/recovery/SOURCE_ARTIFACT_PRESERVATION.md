# SOURCE_ARTIFACT_PRESERVATION

## What is preserved directly in this recovery branch

- exact recovered AUTHOR_RAW fragments from 2026-02-16/17;
- exact artifact identifiers, versions, patch IDs, names and critical contract fields for v1.1/v1.2/v1.3;
- detailed version deltas and topology changes;
- provenance of assistant outputs vs user-supplied artifacts;
- current v1.3 authority/boundaries/interfaces;
- explicit gaps/UNKNOWNs.

## What is not byte-for-byte duplicated here

The entire large JSON bodies of user-supplied v1.1, v1.2 and v1.3 are not copied byte-for-byte into this recovery branch in this first recovery pass.

Reason:
this recovery prioritizes verified semantic/provenance reconstruction and avoids claiming byte-exact preservation where a direct export of the conversation message bytes was not available through the repository/files tooling.

Evidence status:
- v1.1 exact artifact is visible in the source conversation.
- v1.2 exact artifact is visible in the source conversation.
- v1.3 exact artifact is visible in the source conversation.
- this GitHub branch stores semantically detailed recovery, not a byte-perfect chat archive.

This is a preserved gap, not silently treated as complete archival capture.

## Rule

Do not call this branch a byte-perfect transcript archive.
It is a strong semantic/provenance recovery with explicit source-artifact archival gap.
