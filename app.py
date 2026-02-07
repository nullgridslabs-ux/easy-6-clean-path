# easy-6-clean-path/app.py
from flask import Flask, request, send_file
import os

app = Flask(__name__)

BASE = "/tmp/docs"
os.makedirs(BASE, exist_ok=True)

with open("/tmp/secret.txt","w") as f:
    f.write("CTF{easy_path_normalization}")

@app.route("/health")
def health():
    return "ok"

@app.route("/view")
def view():
    p = request.args.get("path","")
    full = os.path.join(BASE, p)
    # BUG: check before normalization
    if not full.startswith(BASE):
        return "blocked",403
    return send_file(os.path.realpath(full))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
