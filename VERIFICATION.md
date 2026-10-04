# Independent verification

This page is reserved for verification performed independently of the original golfing sessions.

## Canonical targets

### C

- `c/tree3.c`
- 545 bytes/chars
- Git blob: `8e210e0bfebd20a367fa16cc5352dbd6e4886749`

### Python

- `python/tree3.py`
- 349 stored bytes / 348 source characters + final newline
- Git blob: `78b7242f7642c4b5edef53cfe4bc8b45aecc4723`

## How to verify

For C:

```sh
wc -c c/tree3.c
gcc -w c/tree3.c -o tree3
cd test
bash T8.sh ../c/tree3.c
```

For Python integrity:

```sh
wc -c python/tree3.py
cmp python/tree3.py python/15_349_s348.py
```

The current project CI performs integrity and regression checks automatically, but this file is intended for **independent third-party reproductions**.

## Verification reports

No external verifier has been recorded here yet.

When adding one, include:

- verifier name/handle;
- date;
- operating system;
- CPU architecture;
- gcc version and/or Python version;
- exact commit checked;
- character/byte count;
- harness result;
- any warnings, divergences, or environment-specific notes.

## Suggested report format

```text
Verifier:
Date:
Commit:
OS / architecture:
gcc:
Python:
C count:
C harness:
Python count:
Notes:
```

A third-party success should be added here without rewriting the original project history.
