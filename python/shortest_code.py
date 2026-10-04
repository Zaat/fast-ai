"""Find the shortest known equivalent of a Python program.

The true minimum (Kolmogorov complexity) is uncomputable, so this returns
an UPPER BOUND: the shortest version it can find that behaves the same.
"""
import contextlib, io, itertools, multiprocessing as mp
import python_minifier

def _run(code, q):
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(code, {"__name__": "__main__"})
        q.put(buf.getvalue())
    except Exception as ex:
        q.put(f"<error {type(ex).__name__}>")

def output_of(code, timeout=5.0):
    """Run code in a separate process and return its printed output (None on timeout)."""
    q = mp.Queue(); p = mp.Process(target=_run, args=(code, q)); p.start(); p.join(timeout)
    if p.is_alive():
        p.kill(); return None
    return q.get() if not q.empty() else None

def _brute_force(target, max_len):
    """Search tiny expressions e such that print(e) reproduces the output exactly."""
    alphabet = "0123456789+-*/%()'"
    for n in range(1, max_len + 1):
        for chars in itertools.product(alphabet, repeat=n):
            expr = "".join(chars)
            if "**" in expr:            # avoid huge powers that could hang
                continue
            try:
                val = eval(expr, {"__builtins__": {}})
            except Exception:
                continue
            if f"{val}\n" == target:
                return f"print({expr})"
    return None

def shortest_code(code, timeout=5.0, brute_max=4):
    """Return (length, code, method) for the shortest equivalent found."""
    target = output_of(code, timeout)
    best, method = code, "original"
    try:
        mini = python_minifier.minify(code, rename_globals=True, remove_literal_statements=True)
        if len(mini) < len(best) and output_of(mini, timeout) == target:
            best, method = mini, "minified"
    except Exception:
        pass
    if target is not None and not target.startswith("<error") and brute_max:
        bf = _brute_force(target, brute_max)
        if bf and len(bf) < len(best):
            best, method = bf, "brute-force search"
    return len(best), best, method

if __name__ == "__main__":
    demo = """total = 0
for number in range(1, 11):
    total = total + number
print(total)
"""
    print(shortest_code(demo))
    tree = open("s375.py").read().replace("range(3)", "range(2)")
    n, code, how = shortest_code(tree, brute_max=0)
    print(n, how); print(code)
