"""KidsPlay - a tiny coloring website for young children."""

from flask import Flask, abort, render_template

from drawings import CATEGORIES, DRAWINGS

app = Flask(__name__)

PALETTE = [
    {"name": "Red", "hex": "#ff4d4d"},
    {"name": "Orange", "hex": "#ff922b"},
    {"name": "Yellow", "hex": "#ffd43b"},
    {"name": "Green", "hex": "#51cf66"},
    {"name": "Teal", "hex": "#22b8cf"},
    {"name": "Blue", "hex": "#4dabf7"},
    {"name": "Purple", "hex": "#9775fa"},
    {"name": "Pink", "hex": "#f06595"},
    {"name": "Brown", "hex": "#a0613a"},
    {"name": "Black", "hex": "#343a40"},
    {"name": "Grey", "hex": "#adb5bd"},
    {"name": "White", "hex": "#ffffff"},
    {"name": "Mint", "hex": "#8ce99a"},
    {"name": "Sky", "hex": "#a5d8ff"},
    {"name": "Peach", "hex": "#ffc9a9"},
    {"name": "Lavender", "hex": "#d0bfff"},
    {"name": "Gold", "hex": "#fcc419"},
    {"name": "Coral", "hex": "#ff8787"},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        drawings=DRAWINGS,
        categories=CATEGORIES,
        total=len(DRAWINGS),
    )


@app.route("/color/<slug>")
def color(slug):
    drawing = DRAWINGS.get(slug)
    if drawing is None:
        abort(404)
    return render_template(
        "color.html",
        drawing=drawing,
        slug=slug,
        palette=PALETTE,
        drawings=DRAWINGS,
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
