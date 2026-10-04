# Test environment

All logs in `logs/` were produced in this environment on 2026-10-04.

```
gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
Linux 6.18.44-fc-v64 x86_64 GNU/Linux
model name	: Intel(R) Xeon(R) Processor @ 2.10GHz
CPU cores: 2
Python 3.13.15
ldd (Ubuntu GLIBC 2.39-0ubuntu8.9) 2.39
```

The program depends on gcc behaviour (implicit int, K&R parameters, GNU `?:`, built-in `realloc`). Other gcc versions should behave the same, but this is the version that was tested.
