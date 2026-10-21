"""Inline data/mindmap.json into site/template.html -> index.html (so it also works from file://)."""
import json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "data/mindmap.json").read_text())
html = (root / "site/template.html").read_text()
# </ inside JSON would close the script tag early.
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
(root / "index.html").write_text(html.replace("/*__DATA__*/null", blob))
print("wrote index.html")
