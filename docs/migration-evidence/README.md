# Source repository consolidation — 14 November 2026

The original `Data-Analytics` and `DADB` repositories were inspected before their requested removal. This repository is the consolidated location for their preserved source material.

| Source | Preserved default-branch snapshot | Commit records | Recursive trees | Historical blobs |
| --- | --- | ---: | ---: | ---: |
| Data-Analytics | `original-work/Data-Analytics/` (16 files) | 26 | 24 | 32 |
| DADB | `original-work/DADB/` (14 files; already imported) | 19 | 17 | 21 |

Each snapshot's `IMPORT_PROVENANCE.json` records the original commit SHA separately from the root tree SHA and lists every file's Git blob SHA and byte count. All imported files were verified against those source hashes. The DADB maintenance branch's earlier README is preserved as `DADB-maintenance-README.md`.

## What the archives preserve

The two `*-history-20261114.json` archives contain every commit reachable from the captured source refs, complete recursive file trees, and SHA-verified UTF-8 content for every historical file blob. Both branch heads and pull-request head refs are recorded. Each source's one merged PR, its conversation comment, and its empty review/review-comment collections are included. Both sources had no releases at inspection.

These are self-contained API evidence archives. They support reconstructing the file content of any recorded revision. They are **not native Git bundles**, do not attach the original commits to this repository's Git history, and do not preserve live GitHub UI state, repository settings, secrets, Actions logs or unreferenced objects. Repository deletion remains a separate action after verification.

## Academic attribution

`DADB` is the car-sharing database work associated with CSC-40054. `Data-Analytics` contains booking-activity and attendance reporting scripts; its original source does not establish that it was assessed for this module. It is retained as supporting learning material without a coursework-mark claim. Original source files and their historical local paths remain unchanged for provenance. Run historical database-transform scripts only against disposable copies.

## Reproduce archive integrity checks

From the repository root, using Python 3.10 or later:

```bash
python scripts/verify_migration_archive.py docs/migration-evidence/Data-Analytics-history-20261114.json docs/migration-evidence/DADB-history-20261114.json
```

The verifier checks Git blob hashes, byte counts, commit-parent closure, tree/blob closure and recorded refs without executing coursework. Verified locally on 14 November 2026: Data-Analytics 26 commits/24 trees/32 blobs; DADB 19 commits/17 trees/21 blobs. The union contains 52 distinct source blobs. No execution or correctness claim is made for every historical script.
