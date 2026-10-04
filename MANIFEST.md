# Integrity manifest

This file records Git's content-addressed blob IDs for the core 545-character artifact
and the reference data used to verify it. These are Git blob SHA-1 identifiers, not raw-file
SHA-256 hashes; changing the file contents changes the blob ID.

| Path | Size | Git blob SHA |
|---|---:|---|
| `c/tree3.c` | 545 bytes | `8e210e0bfebd20a367fa16cc5352dbd6e4886749` |
| `python/tree3.py` | 349 bytes | `78b7242f7642c4b5edef53cfe4bc8b45aecc4723` |
| `test/pairs_end.txt` | 114,276 bytes | `d2741d67cd9fd5a1f7a8795b64348bd79f51659b` |
| `test/expected.txt` | 6,000 bytes | `6e97eecbf2056e7adb2d9db7ba141a51d4d4061b` |
| `test/T8.sh` | 496 bytes | `85c2946e7a95435e6c5632a0213ded516fab008f` |
| `test/check8.sh` | 1,844 bytes | `18aee10449bd4ee9b98bc5417aa1c0203f93da73` |

The canonical 545-character C source is additionally preserved as `c/history/049_545.c`
with the same blob ID as `c/tree3.c`.

The canonical Python source is additionally preserved as `python/15_349_s348.py`
with the same blob ID as `python/tree3.py`.

For long-term archival use, pin a specific commit as well as these blob IDs. The milestone
commit linked from the README identifies the source at the point the 545-character version
was recorded.
