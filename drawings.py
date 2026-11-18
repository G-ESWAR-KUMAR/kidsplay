"""SVG coloring pages for KidsPlay.

Every colorable shape has:
  class="color-part"
  data-part="<name>"   (shapes with the same name are painted together)
Decorative outlines use pointer-events="none" so clicks reach the shape below.
"""

DRAWINGS = {
    "kitty": {
        "name": "Happy Kitty",
        "emoji": "🐱",
        "category": "animals",
        "category_label": "Animal",
        "description": "A fluffy little cat with a shiny bell.",
        "svg": """
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" class="coloring-svg" role="img" aria-label="Cat to color">
  <g stroke="#3a3a3a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
    <polygon class="color-part" data-part="left-ear" points="88,140 100,45 168,108" fill="#ffd1dc"/>
    <polygon class="color-part" data-part="right-ear" points="312,140 300,45 232,108" fill="#ffd1dc"/>
    <polygon class="color-part" data-part="inner-ear" points="104,126 113,72 150,108" fill="#ff9eb5"/>
    <polygon class="color-part" data-part="inner-ear" points="296,126 287,72 250,108" fill="#ff9eb5"/>
    <ellipse class="color-part" data-part="head" cx="200" cy="215" rx="132" ry="118" fill="#ffe0a3"/>
    <ellipse class="color-part" data-part="eye" cx="155" cy="195" rx="24" ry="28" fill="#ffffff"/>
    <ellipse class="color-part" data-part="eye" cx="245" cy="195" rx="24" ry="28" fill="#ffffff"/>
    <ellipse cx="155" cy="198" rx="9" ry="14" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <ellipse cx="245" cy="198" rx="9" ry="14" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <circle class="color-part" data-part="cheek" cx="118" cy="248" r="20" fill="#ffb3c1"/>
    <circle class="color-part" data-part="cheek" cx="282" cy="248" r="20" fill="#ffb3c1"/>
    <path class="color-part" data-part="nose" d="M188,232 L212,232 L200,250 Z" fill="#ff7a90"/>
    <path d="M200,250 Q200,268 184,268 M200,250 Q200,268 216,268" fill="none" stroke="#3a3a3a" stroke-width="3" pointer-events="none"/>
    <path d="M96,240 L55,232 M96,252 L52,258 M304,240 L345,232 M304,252 L348,258" fill="none" stroke="#3a3a3a" stroke-width="3" pointer-events="none"/>
    <path class="color-part" data-part="collar" d="M120,300 Q200,345 280,300 L272,320 Q200,362 128,320 Z" fill="#ff6b6b"/>
    <circle class="color-part" data-part="bell" cx="200" cy="338" r="14" fill="#ffd93d"/>
  </g>
</svg>""",
    },
    "lion": {
        "name": "Friendly Lion",
        "emoji": "🦁",
        "category": "animals",
        "category_label": "Animal",
        "description": "A king of the jungle with a big golden mane.",
        "svg": """
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" class="coloring-svg" role="img" aria-label="Lion to color">
  <g stroke="#3a3a3a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
    <circle class="color-part" data-part="mane" cx="200" cy="200" r="118" fill="#f4a261"/>
    <circle class="color-part" data-part="mane" cx="200" cy="70" r="42" fill="#f4a261"/>
    <circle class="color-part" data-part="mane" cx="265" cy="87" r="42" fill="#f4a261"/>
    <circle class="color-part" data-part="mane" cx="313" cy="135" r="42" fill="#f4a261"/>
    <circle class="color-part" data-part="mane" cx="330" cy="200" r="42" fill="#f4a261"/>
    <circle class="color-part" data-part="mane" cx="313" cy="265" r="42" fill="#f4a261"/>
    <circle class="color-part" data-part="mane" cx="265" cy="313" r="42" fill="#f4a261"/>
    <circle class="color-part" data-part="mane" cx="200" cy="330" r="42" fill="#f4a261"/>
    <circle class="color-part" data-part="mane" cx="135" cy="313" r="42" fill="#f4a261"/>
    <circle class="color-part" data-part="mane" cx="87" cy="265" r="42" fill="#f4a261"/>
    <circle class="color-part" data-part="mane" cx="70" cy="200" r="42" fill="#f4a261"/>
    <circle class="color-part" data-part="mane" cx="87" cy="135" r="42" fill="#f4a261"/>
    <circle class="color-part" data-part="mane" cx="135" cy="87" r="42" fill="#f4a261"/>
    <circle class="color-part" data-part="face" cx="200" cy="200" r="92" fill="#ffd39b"/>
    <circle class="color-part" data-part="ear" cx="128" cy="132" r="26" fill="#ffd39b"/>
    <circle class="color-part" data-part="ear" cx="272" cy="132" r="26" fill="#ffd39b"/>
    <circle class="color-part" data-part="inner-ear" cx="128" cy="132" r="13" fill="#ff9f8a"/>
    <circle class="color-part" data-part="inner-ear" cx="272" cy="132" r="13" fill="#ff9f8a"/>
    <ellipse class="color-part" data-part="eye" cx="164" cy="182" rx="17" ry="21" fill="#ffffff"/>
    <ellipse class="color-part" data-part="eye" cx="236" cy="182" rx="17" ry="21" fill="#ffffff"/>
    <circle cx="164" cy="185" r="7" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <circle cx="236" cy="185" r="7" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <circle class="color-part" data-part="muzzle" cx="178" cy="238" r="29" fill="#fff3d6"/>
    <circle class="color-part" data-part="muzzle" cx="222" cy="238" r="29" fill="#fff3d6"/>
    <path class="color-part" data-part="nose" d="M188,228 L212,228 L200,246 Z" fill="#8b4a3a"/>
    <path d="M200,246 Q200,266 182,264 M200,246 Q200,266 218,264" fill="none" stroke="#3a3a3a" stroke-width="3" pointer-events="none"/>
  </g>
</svg>""",
    },
    "butterfly": {
        "name": "Butterfly",
        "emoji": "🦋",
        "category": "animals",
        "category_label": "Animal",
        "description": "A butterfly with big, beautiful wings.",
        "svg": """
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" class="coloring-svg" role="img" aria-label="Butterfly to color">
  <g stroke="#3a3a3a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
    <path class="color-part" data-part="upper-wing" d="M192,175 C140,70 40,70 40,145 C40,205 120,205 192,195 Z" fill="#ffb3de"/>
    <path class="color-part" data-part="upper-wing" d="M208,175 C260,70 360,70 360,145 C360,205 280,205 208,195 Z" fill="#ffb3de"/>
    <path class="color-part" data-part="lower-wing" d="M192,200 C130,205 65,235 80,300 C95,355 160,330 192,245 Z" fill="#ffd6a5"/>
    <path class="color-part" data-part="lower-wing" d="M208,200 C270,205 335,235 320,300 C305,355 240,330 208,245 Z" fill="#ffd6a5"/>
    <circle class="color-part" data-part="spots" cx="100" cy="135" r="16" fill="#ffffff"/>
    <circle class="color-part" data-part="spots" cx="300" cy="135" r="16" fill="#ffffff"/>
    <circle class="color-part" data-part="spots" cx="120" cy="275" r="13" fill="#ffffff"/>
    <circle class="color-part" data-part="spots" cx="280" cy="275" r="13" fill="#ffffff"/>
    <path d="M192,120 Q175,80 155,70 M208,120 Q225,80 245,70" fill="none" stroke="#3a3a3a" stroke-width="4" pointer-events="none"/>
    <circle class="color-part" data-part="antenna-tip" cx="153" cy="68" r="9" fill="#ff6b6b"/>
    <circle class="color-part" data-part="antenna-tip" cx="247" cy="68" r="9" fill="#ff6b6b"/>
    <ellipse class="color-part" data-part="body" cx="200" cy="205" rx="16" ry="78" fill="#9775fa"/>
    <circle class="color-part" data-part="head" cx="200" cy="122" r="24" fill="#9775fa"/>
    <circle cx="192" cy="118" r="5" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <circle cx="208" cy="118" r="5" fill="#3a3a3a" stroke="none" pointer-events="none"/>
  </g>
</svg>""",
    },
    "fish": {
        "name": "Little Fish",
        "emoji": "🐠",
        "category": "animals",
        "category_label": "Animal",
        "description": "A happy fish swimming with bubbles.",
        "svg": """
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" class="coloring-svg" role="img" aria-label="Fish to color">
  <g stroke="#3a3a3a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
    <circle class="color-part" data-part="bubble" cx="340" cy="95" r="16" fill="#e7f5ff"/>
    <circle class="color-part" data-part="bubble" cx="368" cy="60" r="11" fill="#e7f5ff"/>
    <circle class="color-part" data-part="bubble" cx="330" cy="48" r="8" fill="#e7f5ff"/>
    <polygon class="color-part" data-part="tail" points="298,200 372,138 372,262" fill="#4dabf7"/>
    <polygon class="color-part" data-part="top-fin" points="150,135 192,78 232,132" fill="#74c0fc"/>
    <polygon class="color-part" data-part="bottom-fin" points="155,268 196,322 235,268" fill="#74c0fc"/>
    <ellipse class="color-part" data-part="body" cx="188" cy="200" rx="112" ry="76" fill="#74c0fc"/>
    <circle class="color-part" data-part="scales" cx="165" cy="160" r="12" fill="#a5d8ff"/>
    <circle class="color-part" data-part="scales" cx="205" cy="156" r="12" fill="#a5d8ff"/>
    <circle class="color-part" data-part="scales" cx="245" cy="162" r="12" fill="#a5d8ff"/>
    <circle class="color-part" data-part="scales" cx="180" cy="205" r="12" fill="#a5d8ff"/>
    <circle class="color-part" data-part="scales" cx="220" cy="205" r="12" fill="#a5d8ff"/>
    <circle class="color-part" data-part="scales" cx="258" cy="212" r="12" fill="#a5d8ff"/>
    <path class="color-part" data-part="side-fin" d="M180,225 C205,240 225,255 210,275 C190,275 175,250 180,225 Z" fill="#339af0"/>
    <circle class="color-part" data-part="eye" cx="135" cy="182" r="17" fill="#ffffff"/>
    <circle cx="138" cy="183" r="8" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <path d="M85,205 Q98,218 112,205" fill="none" stroke="#3a3a3a" stroke-width="3" pointer-events="none"/>
  </g>
</svg>""",
    },
    "elephant": {
        "name": "Elephant",
        "emoji": "🐘",
        "category": "animals",
        "category_label": "Animal",
        "description": "A gentle elephant with a curly trunk.",
        "svg": """
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" class="coloring-svg" role="img" aria-label="Elephant to color">
  <g stroke="#3a3a3a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
    <ellipse class="color-part" data-part="ear" cx="105" cy="180" rx="72" ry="92" fill="#b8c7d9"/>
    <ellipse class="color-part" data-part="ear" cx="295" cy="180" rx="72" ry="92" fill="#b8c7d9"/>
    <ellipse class="color-part" data-part="inner-ear" cx="100" cy="185" rx="45" ry="62" fill="#f3a6b6"/>
    <ellipse class="color-part" data-part="inner-ear" cx="300" cy="185" rx="45" ry="62" fill="#f3a6b6"/>
    <circle class="color-part" data-part="head" cx="200" cy="185" r="98" fill="#c7d6e5"/>
    <path class="color-part" data-part="trunk" d="M168,232 C158,300 172,348 205,350 C236,352 248,322 232,300 C222,286 218,266 230,238 Z" fill="#c7d6e5"/>
    <ellipse class="color-part" data-part="eye" cx="163" cy="170" rx="13" ry="16" fill="#ffffff"/>
    <ellipse class="color-part" data-part="eye" cx="237" cy="170" rx="13" ry="16" fill="#ffffff"/>
    <circle cx="165" cy="173" r="6" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <circle cx="235" cy="173" r="6" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <path class="color-part" data-part="tusk" d="M172,255 C160,285 165,300 178,305 C180,280 180,265 178,252 Z" fill="#ffffff"/>
    <path class="color-part" data-part="tusk" d="M228,255 C240,285 235,300 222,305 C220,280 220,265 222,252 Z" fill="#ffffff"/>
  </g>
</svg>""",
    },
    "owl": {
        "name": "Wise Owl",
        "emoji": "🦉",
        "category": "animals",
        "category_label": "Animal",
        "description": "A sleepy owl sitting on a branch.",
        "svg": """
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" class="coloring-svg" role="img" aria-label="Owl to color">
  <g stroke="#3a3a3a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
    <rect class="color-part" data-part="branch" x="70" y="360" width="260" height="18" rx="9" fill="#a16207"/>
    <path class="color-part" data-part="tuft" d="M120,125 L135,70 L170,105 Z" fill="#a78bfa"/>
    <path class="color-part" data-part="tuft" d="M280,125 L265,70 L230,105 Z" fill="#a78bfa"/>
    <ellipse class="color-part" data-part="body" cx="200" cy="220" rx="112" ry="130" fill="#a78bfa"/>
    <path class="color-part" data-part="wing" d="M105,185 C62,220 65,300 115,325 C145,300 145,220 105,185 Z" fill="#8b5cf6"/>
    <path class="color-part" data-part="wing" d="M295,185 C338,220 335,300 285,325 C255,300 255,220 295,185 Z" fill="#8b5cf6"/>
    <ellipse class="color-part" data-part="belly" cx="200" cy="275" rx="66" ry="62" fill="#fde68a"/>
    <circle class="color-part" data-part="eye-disk" cx="160" cy="170" r="46" fill="#fff7ed"/>
    <circle class="color-part" data-part="eye-disk" cx="240" cy="170" r="46" fill="#fff7ed"/>
    <circle class="color-part" data-part="eye" cx="160" cy="172" r="22" fill="#ffd43b"/>
    <circle class="color-part" data-part="eye" cx="240" cy="172" r="22" fill="#ffd43b"/>
    <circle cx="160" cy="174" r="10" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <circle cx="240" cy="174" r="10" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <path class="color-part" data-part="beak" d="M200,200 L184,228 L216,228 Z" fill="#fb923c"/>
    <path class="color-part" data-part="feet" d="M165,345 Q150,365 170,365 Q180,365 180,345 Z" fill="#fb923c"/>
    <path class="color-part" data-part="feet" d="M235,345 Q250,365 230,365 Q220,365 220,345 Z" fill="#fb923c"/>
  </g>
</svg>""",
    },
    "turtle": {
        "name": "Turtle",
        "emoji": "🐢",
        "category": "animals",
        "category_label": "Animal",
        "description": "A slow and steady turtle with a round shell.",
        "svg": """
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" class="coloring-svg" role="img" aria-label="Turtle to color">
  <g stroke="#3a3a3a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
    <polygon class="color-part" data-part="tail" points="88,220 50,205 60,240" fill="#51cf66"/>
    <ellipse class="color-part" data-part="leg" cx="120" cy="285" rx="30" ry="22" fill="#8ce99a"/>
    <ellipse class="color-part" data-part="leg" cx="280" cy="285" rx="30" ry="22" fill="#8ce99a"/>
    <ellipse class="color-part" data-part="leg" cx="130" cy="150" rx="26" ry="20" fill="#8ce99a"/>
    <ellipse class="color-part" data-part="leg" cx="270" cy="150" rx="26" ry="20" fill="#8ce99a"/>
    <circle class="color-part" data-part="shell" cx="200" cy="210" r="105" fill="#51cf66"/>
    <circle class="color-part" data-part="shell-pattern" cx="200" cy="210" r="42" fill="#2f9e44"/>
    <path d="M200,168 L200,252 M158,210 L242,210 M170,180 L230,240 M230,180 L170,240" fill="none" stroke="#2b8a3e" stroke-width="3" pointer-events="none"/>
    <circle class="color-part" data-part="head" cx="330" cy="195" r="42" fill="#8ce99a"/>
    <circle class="color-part" data-part="eye" cx="342" cy="185" r="8" fill="#ffffff"/>
    <circle cx="344" cy="186" r="4" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <path d="M345,205 Q355,212 362,205" fill="none" stroke="#3a3a3a" stroke-width="3" pointer-events="none"/>
  </g>
</svg>""",
    },
    "robot": {
        "name": "Robot Buddy",
        "emoji": "🤖",
        "category": "cartoons",
        "category_label": "Cartoon",
        "description": "A friendly robot with shiny buttons.",
        "svg": """
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" class="coloring-svg" role="img" aria-label="Robot to color">
  <g stroke="#3a3a3a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
    <path d="M200,90 L200,52" fill="none" stroke="#3a3a3a" stroke-width="5" pointer-events="none"/>
    <circle class="color-part" data-part="antenna" cx="200" cy="45" r="12" fill="#ff6b6b"/>
    <rect class="color-part" data-part="head" x="120" y="88" width="160" height="112" rx="22" fill="#a5d8ff"/>
    <circle class="color-part" data-part="eye" cx="160" cy="135" r="20" fill="#ffffff"/>
    <circle class="color-part" data-part="eye" cx="240" cy="135" r="20" fill="#ffffff"/>
    <circle cx="160" cy="138" r="8" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <circle cx="240" cy="138" r="8" fill="#3a3a3a" stroke="none" pointer-events="none"/>
    <rect class="color-part" data-part="mouth" x="168" y="170" width="64" height="18" rx="6" fill="#3a3a3a"/>
    <path d="M180,170 L180,188 M192,170 L192,188 M204,170 L204,188 M216,170 L216,188" fill="none" stroke="#ffffff" stroke-width="2" pointer-events="none"/>
    <rect class="color-part" data-part="body" x="132" y="212" width="136" height="122" rx="16" fill="#74c0fc"/>
    <rect class="color-part" data-part="panel" x="155" y="240" width="90" height="66" rx="10" fill="#e7f5ff"/>
    <circle class="color-part" data-part="button" cx="178" cy="262" r="10" fill="#ff6b6b"/>
    <circle class="color-part" data-part="button" cx="222" cy="262" r="10" fill="#ffd43b"/>
    <circle class="color-part" data-part="button" cx="200" cy="285" r="10" fill="#51cf66"/>
    <rect class="color-part" data-part="arm" x="72" y="225" width="46" height="95" rx="20" fill="#74c0fc"/>
    <rect class="color-part" data-part="arm" x="282" y="225" width="46" height="95" rx="20" fill="#74c0fc"/>
    <rect class="color-part" data-part="hand" x="66" y="312" width="58" height="32" rx="14" fill="#ffd43b"/>
    <rect class="color-part" data-part="hand" x="276" y="312" width="58" height="32" rx="14" fill="#ffd43b"/>
    <rect class="color-part" data-part="leg" x="155" y="332" width="38" height="45" rx="8" fill="#74c0fc"/>
    <rect class="color-part" data-part="leg" x="207" y="332" width="38" height="45" rx="8" fill="#74c0fc"/>
    <rect class="color-part" data-part="foot" x="140" y="370" width="60" height="22" rx="10" fill="#ff6b6b"/>
    <rect class="color-part" data-part="foot" x="200" y="370" width="60" height="22" rx="10" fill="#ff6b6b"/>
  </g>
</svg>""",
    },
    "rocket": {
        "name": "Space Rocket",
        "emoji": "🚀",
        "category": "cartoons",
        "category_label": "Cartoon",
        "description": "Blast off into a sky full of stars!",
        "svg": """
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" class="coloring-svg" role="img" aria-label="Rocket to color">
  <g stroke="#3a3a3a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
    <path class="color-part" data-part="star" d="M60,90 L66,104 L80,110 L66,116 L60,130 L54,116 L40,110 L54,104 Z" fill="#ffd43b"/>
    <path class="color-part" data-part="star" d="M340,160 L344,170 L354,174 L344,178 L340,188 L336,178 L326,174 L336,170 Z" fill="#ffd43b"/>
    <path class="color-part" data-part="star" d="M85,190 L89,200 L99,204 L89,208 L85,218 L81,208 L71,204 L81,200 Z" fill="#ffd43b"/>
    <path class="color-part" data-part="flame" d="M170,282 C165,330 200,370 200,370 C200,370 235,330 230,282 C215,300 185,300 170,282 Z" fill="#ff922b"/>
    <path class="color-part" data-part="flame-inner" d="M186,290 C185,320 200,342 200,342 C200,342 215,320 214,290 Z" fill="#ffd43b"/>
    <polygon class="color-part" data-part="fin" points="148,215 100,290 150,275" fill="#ff6b6b"/>
    <polygon class="color-part" data-part="fin" points="252,215 300,290 250,275" fill="#ff6b6b"/>
    <path class="color-part" data-part="body" d="M200,48 C238,88 252,175 248,278 L152,278 C148,175 162,88 200,48 Z" fill="#f8f9fa"/>
    <path class="color-part" data-part="nose" d="M200,48 C218,64 230,88 236,110 L164,110 C170,88 182,64 200,48 Z" fill="#ff6b6b"/>
    <circle class="color-part" data-part="window" cx="200" cy="155" r="34" fill="#3a3a3a"/>
    <circle class="color-part" data-part="glass" cx="200" cy="155" r="26" fill="#74c0fc"/>
    <rect class="color-part" data-part="band" x="152" y="225" width="96" height="22" fill="#ffd43b"/>
  </g>
</svg>""",
    },
    "house": {
        "name": "Dream House",
        "emoji": "🏠",
        "category": "homes",
        "category_label": "House",
        "description": "A cozy little house with a sunny garden.",
        "svg": """
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" class="coloring-svg" role="img" aria-label="House to color">
  <g stroke="#3a3a3a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
    <rect class="color-part" data-part="grass" x="30" y="330" width="340" height="52" rx="20" fill="#8ce99a"/>
    <circle class="color-part" data-part="sun" cx="345" cy="62" r="27" fill="#ffd43b"/>
    <path d="M345,20 L345,8 M345,116 L345,104 M303,62 L291,62 M399,62 L387,62 M315,32 L307,24 M375,92 L383,100 M375,32 L383,24 M315,92 L307,100" fill="none" stroke="#ffd43b" stroke-width="4" pointer-events="none"/>
    <rect class="color-part" data-part="wall" x="80" y="165" width="240" height="170" fill="#ffe066"/>
    <rect class="color-part" data-part="chimney" x="255" y="92" width="36" height="70" fill="#ff8787"/>
    <polygon class="color-part" data-part="roof" points="60,172 200,70 340,172" fill="#ff6b6b"/>
    <rect class="color-part" data-part="window" x="105" y="200" width="55" height="55" rx="4" fill="#74c0fc"/>
    <rect class="color-part" data-part="window" x="240" y="200" width="55" height="55" rx="4" fill="#74c0fc"/>
    <path d="M132,200 L132,255 M105,227 L160,227 M267,200 L267,255 M240,227 L295,227" fill="none" stroke="#3a3a3a" stroke-width="3" pointer-events="none"/>
    <rect class="color-part" data-part="door" x="168" y="245" width="64" height="90" rx="6" fill="#ff9f43"/>
    <circle class="color-part" data-part="knob" cx="218" cy="292" r="5" fill="#ffd43b"/>
    <circle class="color-part" data-part="flower" cx="70" cy="352" r="8" fill="#ff6b6b"/>
    <circle class="color-part" data-part="flower" cx="330" cy="352" r="8" fill="#ff6b6b"/>
    <circle class="color-part" data-part="flower" cx="95" cy="365" r="8" fill="#9775fa"/>
    <circle class="color-part" data-part="flower" cx="305" cy="365" r="8" fill="#9775fa"/>
  </g>
</svg>""",
    },
}

CATEGORIES = [
    {"id": "all", "label": "All Pictures", "emoji": "✨"},
    {"id": "animals", "label": "Animals", "emoji": "🐾"},
    {"id": "cartoons", "label": "Cartoons", "emoji": "🤖"},
    {"id": "homes", "label": "Houses", "emoji": "🏡"},
]
