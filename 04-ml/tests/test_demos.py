import subprocess, sys, pathlib

def run(cmd):
    subprocess.check_call(cmd, shell=True)

def test_coc_extractor_runs():
    run("python 04-ml/nlp_contracts/extract_coc.py 04-ml/nlp_contracts/samples/*.txt")

def test_qubo_demo_runs():
    run("python 05-quant/qaoa_demo.py")

def test_sanitizer_marks_sample_safe(tmp_path):
    p = tmp_path/"x.txt"
    p.write_text("This document has nothing sensitive.")
    run(f"python 04-ml/eval/sanitize_text.py {p}")
