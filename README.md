# KidsPlay 🎨

A simple, cheerful coloring website built with Flask — made for children under 10.
Kids pick a color, tap parts of a drawing to paint them, and save their artwork.

## What's inside

- **10 coloring pages**: cat, lion, butterfly, fish, elephant, owl, turtle, robot, rocket, and a house.
- **Big colorful palette** with 18 bright colors and an eraser.
- **Fun tools**: *Surprise Me* (random colors), *Start Over* (reset), and *Save Picture* (downloads a PNG).
- **Category filters** on the gallery: Animals, Cartoons, and Houses.
- **Kid-friendly design**: big buttons, thick outlines, playful fonts, and encouraging messages.
- Works with mouse, touch, and keyboard (Tab + Enter/Space).

## Run it locally

```bash
pip install -r requirements.txt
python app.py
```

Then open <http://localhost:5000> in a browser.

## Project structure

```
KidsPlay/
├── app.py                 # Flask routes and the color palette
├── drawings.py            # All the SVG coloring pages
├── templates/
│   ├── base.html          # Shared layout
│   ├── index.html         # Gallery and how-to
│   ├── color.html         # Coloring canvas and tools
│   └── 404.html
└── static/
    ├── css/style.css      # Playful theme and layout
    └── js/coloring.js     # Coloring, filters, and PNG download
```

## Adding your own picture

Add a new entry to `DRAWINGS` in `drawings.py`. Each drawing needs a `slug`, `name`,
`emoji`, `category`, `category_label`, `description`, and an `svg` string. Give every
clickable shape `class="color-part"` and a `data-part="name"`; shapes with the same
`data-part` are colored together. Decorative lines should have `pointer-events="none"`
so taps pass through to the shapes below.
