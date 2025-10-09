import re

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SECRETISH = re.compile(r"(api[_-]?key|token|secret|bearer|AKIA|ASIA)", re.I)

def looks_safe(text: str) -> bool:
    if EMAIL.search(text): return False
    if SECRETISH.search(text): return False
    return True

if __name__ == "__main__":
    import sys, pathlib
    bad = []
    for p in sys.argv[1:]:
        t = pathlib.Path(p).read_text(errors="ignore")
        if not looks_safe(t):
            bad.append(p)
    if bad:
        print("unsafe:", ",".join(bad))
        sys.exit(1)
    print("all_safe")
