/* KidsPlay — gallery filters and the coloring canvas. */
document.addEventListener("DOMContentLoaded", () => {
  setupGalleryFilters();
  setupColoringPage();
});

/* ---------- Gallery category filters ---------- */
function setupGalleryFilters() {
  const filters = document.querySelectorAll(".filter-btn");
  const cards = document.querySelectorAll("#card-grid .card");
  const emptyMessage = document.getElementById("empty-message");
  if (!filters.length || !cards.length) return;

  filters.forEach((button) => {
    button.addEventListener("click", () => {
      const chosen = button.dataset.filter;

      filters.forEach((other) => {
        const active = other === button;
        other.classList.toggle("active", active);
        other.setAttribute("aria-pressed", String(active));
      });

      let visible = 0;
      cards.forEach((card) => {
        const show = chosen === "all" || card.dataset.category === chosen;
        card.hidden = !show;
        if (show) visible += 1;
      });

      if (emptyMessage) emptyMessage.hidden = visible !== 0;
    });
  });
}

/* ---------- Coloring page ---------- */
function setupColoringPage() {
  const page = document.querySelector(".color-page");
  if (!page) return;

  const frame = document.getElementById("canvas-frame");
  const parts = frame ? Array.from(frame.querySelectorAll(".color-part")) : [];
  const swatches = Array.from(document.querySelectorAll(".swatch"));
  const eraser = document.getElementById("eraser");
  const resetButton = document.getElementById("reset");
  const surpriseButton = document.getElementById("surprise");
  const downloadButton = document.getElementById("download");
  const caption = document.getElementById("canvas-caption");
  const selectedDot = document.getElementById("selected-dot");
  const selectedName = document.getElementById("selected-name");

  if (!parts.length || !swatches.length) return;

  // Remember the original colors so "Start Over" can restore them.
  // Parts sharing a data-part name (two eyes, a mane, ...) are painted together.
  const groups = new Map();
  parts.forEach((part) => {
    part.dataset.defaultFill = part.getAttribute("fill") || "#ffffff";
    part.setAttribute("tabindex", "0");
    part.setAttribute("role", "button");
    const label = (part.dataset.part || "part").replace(/-/g, " ");
    part.setAttribute("aria-label", `Color the ${label}`);

    const name = part.dataset.part || "part";
    if (!groups.has(name)) groups.set(name, []);
    groups.get(name).push(part);
  });

  let currentColor = swatches[0].dataset.color;
  let currentName = swatches[0].title || "Color";

  const happyWords = [
    "Great job!",
    "Beautiful!",
    "So colorful!",
    "Wow, nice!",
    "You are an artist!",
    "Looking good!",
  ];

  function say(text) {
    if (!caption) return;
    caption.textContent = text;
    caption.classList.remove("pop");
    void caption.offsetWidth; // restart the little animation
    caption.classList.add("pop");
  }

  function paint(element, color) {
    element.setAttribute("fill", color);
  }

  function selectSwatch(swatch) {
    swatches.forEach((other) => {
      const active = other === swatch;
      other.classList.toggle("selected", active);
      other.setAttribute("aria-pressed", String(active));
    });
    currentColor = swatch.dataset.color;
    currentName = swatch.title || "Color";
    if (selectedDot) selectedDot.style.backgroundColor = currentColor;
    if (selectedName) selectedName.textContent = currentName;
    if (eraser) {
      eraser.classList.remove("active");
      eraser.setAttribute("aria-pressed", "false");
    }
    say(`You picked ${currentName}! Now tap the picture.`);
  }

  parts.forEach((part) => {
    part.addEventListener("click", () => {
      groups.get(part.dataset.part || "part").forEach((element) => paint(element, currentColor));
      say(happyWords[Math.floor(Math.random() * happyWords.length)]);
    });

    part.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        part.click();
      }
    });
  });

  swatches.forEach((swatch) => swatch.addEventListener("click", () => selectSwatch(swatch)));

  if (eraser) {
    eraser.addEventListener("click", () => {
      currentColor = "#ffffff";
      currentName = "Eraser";
      swatches.forEach((swatch) => {
        swatch.classList.remove("selected");
        swatch.setAttribute("aria-pressed", "false");
      });
      eraser.classList.add("active");
      eraser.setAttribute("aria-pressed", "true");
      if (selectedDot) selectedDot.style.backgroundColor = "#ffffff";
      if (selectedName) selectedName.textContent = "Eraser";
      say("Eraser is on! Tap a part to make it white.");
    });
  }

  if (resetButton) {
    resetButton.addEventListener("click", () => {
      parts.forEach((part) => paint(part, part.dataset.defaultFill));
      say("Fresh page! Let's color again.");
    });
  }

  if (surpriseButton) {
    surpriseButton.addEventListener("click", () => {
      const funColors = [
        "#ff4d4d", "#ff922b", "#ffd43b", "#51cf66", "#22b8cf",
        "#4dabf7", "#9775fa", "#f06595", "#ffc9a9", "#a5d8ff",
        "#d0bfff", "#fcc419",
      ];

      groups.forEach((elements) => {
        const color = funColors[Math.floor(Math.random() * funColors.length)];
        elements.forEach((element) => paint(element, color));
      });

      say("Ta-da! A colorful surprise!");
    });
  }

  if (downloadButton) {
    downloadButton.addEventListener("click", () => {
      const svg = frame.querySelector("svg");
      if (!svg) return;

      const copy = svg.cloneNode(true);
      copy.setAttribute("xmlns", "http://www.w3.org/2000/svg");
      copy.setAttribute("width", "800");
      copy.setAttribute("height", "800");

      const source = new XMLSerializer().serializeToString(copy);
      const url = URL.createObjectURL(new Blob([source], { type: "image/svg+xml;charset=utf-8" }));
      const image = new Image();

      image.onload = () => {
        const canvas = document.createElement("canvas");
        canvas.width = 800;
        canvas.height = 800;
        const context = canvas.getContext("2d");
        context.fillStyle = "#ffffff";
        context.fillRect(0, 0, 800, 800);
        context.drawImage(image, 0, 0, 800, 800);
        URL.revokeObjectURL(url);

        canvas.toBlob((blob) => {
          if (!blob) {
            say("Sorry, the picture could not be saved.");
            return;
          }
          const link = document.createElement("a");
          link.href = URL.createObjectURL(blob);
          link.download = `${page.dataset.slug || "kidsplay"}-my-art.png`;
          link.click();
          setTimeout(() => URL.revokeObjectURL(link.href), 1000);
          say("Saved! Show your masterpiece to someone!");
        }, "image/png");
      };

      image.onerror = () => {
        URL.revokeObjectURL(url);
        say("Sorry, the picture could not be saved.");
      };

      image.src = url;
    });
  }
}
