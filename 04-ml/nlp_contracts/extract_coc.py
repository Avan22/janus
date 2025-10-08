import sys, re, json, pathlib
WIN = 2000
KW = r'(change\s+(of|in)\s+control|acquir(?:e|es|ing)\s+more\s+than\s+\d+%|voting\s+securit(?:y|ies))'
VERB = r'(shall|terminate|consent|notice|trigger|due)'
def hits(text):
    for m in re.finditer(KW, text, flags=re.I):
        s=max(0,m.start()-WIN); e=min(len(text),m.end()+WIN)
        chunk=text[s:e]
        if not re.search(VERB, chunk, flags=re.I): 
            continue
        yield s, e, chunk.strip()
def main(paths):
    for p in paths:
        t = pathlib.Path(p).read_text(errors='ignore')
        for s,e,chunk in hits(t):
            print(json.dumps({"file":p,"start":s,"end":e,"excerpt":chunk[:500]}))
if __name__ == "__main__":
    if len(sys.argv)<2: 
        print("usage: python extract_coc.py <files...>"); sys.exit(1)
    main(sys.argv[1:])
