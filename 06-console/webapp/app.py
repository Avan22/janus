from flask import Flask, render_template, request, jsonify, Response
import csv
from io import StringIO

from util.coc_extractor import extract as extract_coc
from util.pdf_text import pdf_bytes_to_text
from quant.qubo import run as run_qubo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/api/extract")
def api_extract():
    if "file" not in request.files:
        return jsonify({"error": "no file"}), 400
    f = request.files["file"]
    raw = f.read()
    name = (f.filename or "").lower()
    text = pdf_bytes_to_text(raw) if name.endswith(".pdf") else raw.decode(errors="ignore")
    findings = extract_coc(text)
    return jsonify({"count": len(findings), "findings": findings})

@app.post("/api/extract.csv")
def api_extract_csv():
    if "file" not in request.files:
        return Response("no file", status=400)
    f = request.files["file"]
    raw = f.read()
    name = (f.filename or "").lower()
    text = pdf_bytes_to_text(raw) if name.endswith(".pdf") else raw.decode(errors="ignore")
    findings = extract_coc(text)

    buf = StringIO()
    w = csv.writer(buf)
    w.writerow(["start", "end", "excerpt"])
    for it in findings:
        w.writerow([it["start"], it["end"], it["excerpt"]])
    data = buf.getvalue().encode("utf-8")
    return Response(
        data,
        headers={"Content-Disposition": "attachment; filename=findings.csv"},
        mimetype="text/csv; charset=utf-8",
    )

@app.get("/api/qubo")
def api_qubo():
    return jsonify(run_qubo())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
