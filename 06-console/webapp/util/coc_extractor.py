import re
from hashlib import sha1

WIN = 2000
KW = r'(change\s+(of|in)\s+control|acquir(?:e|es|ing)\s+more\s+than\s+\d+%|voting\s+securit(?:y|ies))'
VERB = r'(shall|terminate|terminat|consent|notice|trigger|due)'

def extract(text):
    findings, seen = [], set()
    for m in re.finditer(KW, text, flags=re.I):
        s = max(0, m.start()-WIN)
        e = min(len(text), m.end()+WIN)
        chunk = text[s:e]
        if not re.search(VERB, chunk, flags=re.I):
            continue
        excerpt = chunk.strip()[:600]
        h = sha1(excerpt.encode('utf-8')).hexdigest()
        if h in seen:
            continue
        seen.add(h)
        findings.append({"start": s, "end": e, "excerpt": excerpt})
    return findings
