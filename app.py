import base64
import os
import streamlit as st
import streamlit.components.v1 as components

# Cấu hình trang
st.set_page_config(
    page_title="Dragon Rescue Knight - 2D RPG", page_icon="🐉", layout="centered"
)


# Hàm tự động tải lại trang tương thích mọi phiên bản Streamlit
def safe_rerun():
  if hasattr(st, "rerun"):
    st.rerun()
  else:
    st.experimental_rerun()


# Hàm tìm và đọc file ảnh sang Base64 (không phân biệt chữ hoa/thường)
def get_image_base64(candidates):
  existing_files = {}
  try:
    for f in os.listdir("."):
      existing_files[f.lower()] = f
  except Exception:
    pass

  for name in candidates:
    real_path = None
    if os.path.exists(name):
      real_path = name
    elif name.lower() in existing_files:
      real_path = existing_files[name.lower()]

    if real_path:
      try:
        with open(real_path, "rb") as img_f:
          data = img_f.read()
        ext = real_path.split(".")[-1].lower()
        mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
        b64_str = base64.b64encode(data).decode("utf-8")
        return "data:" + mime + ";base64," + b64_str
      except Exception:
        continue
  return ""


# ================= STAGES & 15 MATH QUESTIONS (ENGLISH) =================
HERO_FILES = ["main.png", "main.jpg", "image_b090fc.png"]
HERO_POSITIONS = [8, 22, 36, 50, 62]

STAGES = {
    1: {
        "name": "Stage 1: Dark Forest Ruins (Basic)",
        "story": (
            "The Knight crosses the ruined forest toward the castle. The Dark"
            " Assassin is blocking the path on the right side!"
        ),
        "boss_name": "Dark Assassin",
        "boss_files": ["boss1.png", "boss1.jpg", "image_b09486.png"],
        "boss_emoji": "🥷",
        "bg_files": ["bg1.jpg", "bg1.png", "image_b0955a.jpg"],
        "bg_fallback": (
            "linear-gradient(180deg, #1b1b1b 0%, #3a3a3a 70%, #111111 100%)"
        ),
        "questions": [
            {
                "id": 1,
                "title": "Question 1: Solve Quadratic Equation",
                "latex": r"x^2 - 5x + 6 = 0",
                "desc": (
                    "Find the roots of the equation to step forward through"
                    " the forest:"
                ),
                "options": [
                    "x = 2 or x = 3",
                    "x = -2 or x = -3",
                    "x = 1 or x = 6",
                    "x = -1 or x = 6",
                ],
                "answer": "x = 2 or x = 3",
                "explanation": (
                    "We have: $x^2 - 5x + 6 = 0 \\iff (x - 2)(x - 3) = 0 \\iff x"
                    " = 2$ or $x = 3$."
                ),
            },
            {
                "id": 2,
                "title": "Question 2: Simplify Radical Expression",
                "latex": r"A = \frac{\sqrt{12} + \sqrt{27} - \sqrt{3}}{\sqrt{3}}",
                "desc": "Find the simplified value of expression A:",
                "options": ["4", "5", "3", "4√3"],
                "answer": "4",
                "explanation": (
                    "Since $\\sqrt{12} = 2\\sqrt{3}$and$\\sqrt{27} ="
                    " 3\\sqrt{3}$, we get $A = \\frac{2\\sqrt{3} + 3\\sqrt{3} -"
                    " \\sqrt{3}}{\\sqrt{3}} = \\frac{4\\sqrt{3}}{\\sqrt{3}} ="
                    " 4$."
                ),
            },
            {
                "id": 3,
                "title": "Question 3: Equation with Unknown in Denominator",
                "latex": r"\frac{2}{x-1} + \frac{1}{x+1} = 1 \quad (x \ne 1,\ x \ne -1)",
                "desc": "Find the root of the equation:",
                "options": [
                    "x = (3 ± √17) / 2",
                    "x = (3 ± √15) / 2",
                    "x = 2 or x = -1",
                    "x = (-3 ± √17) / 2",
                ],
                "answer": "x = (3 ± √17) / 2",
                "explanation": (
                    "Common denominator: $2(x+1) + (x-1) = x^2 - 1 \\iff x^2 -"
                    " 3x - 2 = 0$. Discriminant $\\Delta = 17 > 0 \\implies x ="
                    " \\frac{3 \\pm \\sqrt{17}}{2}$ (valid)."
                ),
            },
            {
                "id": 4,
                "title": "Question 4: Linear System of Equations",
                "latex": r"\begin{cases} 2x + y = 7 \\ x - y = 2 \end{cases}",
                "desc": "Find the solution pair (x; y):",
                "options": ["(3; 1)", "(2; 3)", "(4; -1)", "(3; -1)"],
                "answer": "(3; 1)",
                "explanation": (
                    "Add both equations: $3x = 9 \\implies x = 3$. Substitute $x"
                    " = 3$ into the second equation: $3 - y = 2 \\implies y ="
                    " 1$. Solution is $(3; 1)$."
                ),
            },
            {
                "id": 5,
                "title": "Question 5: Practical Geometry Word Problem",
                "latex": r"2(a + b) = 34, \quad a \cdot b = 60",
                "desc": (
                    "A rectangle has a perimeter of 34 cm and an area of 60"
                    " cm². Find length a and width b:"
                ),
                "options": [
                    "Length 12 cm, Width 5 cm",
                    "Length 10 cm, Width 6 cm",
                    "Length 15 cm, Width 4 cm",
                    "Length 14 cm, Width 3 cm",
                ],
                "answer": "Length 12 cm, Width 5 cm",
                "explanation": (
                    "Semi-perimeter is $34 : 2 = 17\\text{ cm}$. We have $a + b ="
                    " 17$ and $ab = 60$. By converse Vieta's theorem, $a, b$ are"
                    " roots of $X^2 - 17X + 60 = 0 \\implies a = 12\\text{ cm},"
                    " b = 5\\text{ cm}$."
                ),
            },
        ],
    },
    2: {
        "name": "Stage 2: Castle Gate (High School Entrance Level)",
        "story": (
            "The Dragon is imprisoned at the top of the tower! The Knight must"
            " cross the castle field and defeat the Red Fire Reaper!"
        ),
        "boss_name": "Red Fire Reaper",
        "boss_files": ["boss2.png", "boss2.jpg", "image_b094c4.png"],
        "boss_emoji": "💀",
        "bg_files": ["bg2.png", "bg2.jpg", "image_b0e738.png"],
        "bg_fallback": (
            "linear-gradient(180deg, #3a7bd5 0%, #3a6073 70%, #16222a 100%)"
        ),
        "questions": [
            {
                "id": 6,
                "title": "Question 6: Quadratic Equation with Parameter",
                "latex": r"x^2 - 2(m+1)x + m^2 + 1 = 0",
                "desc": (
                    "Find the condition of m for the equation to have two"
                    " distinct roots:"
                ),
                "options": ["m > 0", "m ≥ 0", "m > -1", "m ≠ 0"],
                "answer": "m > 0",
                "explanation": (
                    "We have $\\Delta' = (m+1)^2 - (m^2 + 1) = 2m$. For two"
                    " distinct roots, $\\Delta' > 0 \\iff 2m > 0 \\iff m > 0$."
                ),
            },
            {
                "id": 7,
                "title": "Question 7: Equation by Substitution",
                "latex": r"\frac{x+1}{x-2} + \frac{x-2}{x+1} = \frac{5}{2} \quad (x \ne 2,\ x \ne -1)",
                "desc": "Find the solution set S:",
                "options": [
                    "S = {-4; 5}",
                    "S = {4; -5}",
                    "S = {1; 2}",
                    "S = {-2; 5}",
                ],
                "answer": "S = {-4; 5}",
                "explanation": (
                    "Let $t = \\frac{x+1}{x-2}$ ($t \\ne 0$). The equation"
                    " becomes $t + \\frac{1}{t} = \\frac{5}{2} \\iff 2t^2 - 5t +"
                    " 2 = 0 \\iff t = 2$ or $t = \\frac{1}{2}$. Solving gives"
                    " $x = 5$ or $x = -4$."
                ),
            },
            {
                "id": 8,
                "title": "Question 8: Work Rate Problem",
                "latex": r"\begin{cases} \frac{1}{x} + \frac{1}{y} = \frac{1}{6} \\ \frac{5}{x} + \frac{4}{y} = \frac{3}{4} \end{cases}",
                "desc": (
                    "Two people working together finish in 6 hours. If person 1"
                    " works 5h and person 2 works 4h, they finish 3/4 of the"
                    " job. Find individual completion times:"
                ),
                "options": [
                    "Person 1: 12 hrs, Person 2: 12 hrs",
                    "Person 1: 10 hrs, Person 2: 15 hrs",
                    "Person 1: 8 hrs, Person 2: 24 hrs",
                    "Person 1: 9 hrs, Person 2: 18 hrs",
                ],
                "answer": "Person 1: 12 hrs, Person 2: 12 hrs",
                "explanation": (
                    "From $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{6} \\implies"
                    " \\frac{4}{x} + \\frac{4}{y} = \\frac{2}{3}$. Subtracting"
                    " from the second equation: $\\frac{1}{x} = \\frac{3}{4} -"
                    " \\frac{2}{3} = \\frac{1}{12} \\implies x = 12$hrs,$y ="
                    " 12$ hrs."
                ),
            },
            {
                "id": 9,
                "title": "Question 9: Metric Relations in Right Triangle",
                "latex": r"AB = 6\text{ cm},\ AC = 8\text{ cm},\ AH \perp BC",
                "desc": (
                    "In right triangle ABC with altitude AH, calculate BC, AH,"
                    " BH, CH:"
                ),
                "options": [
                    (
                        "BC = 10 cm; AH = 4.8 cm; BH = 3.6 cm; CH = 6.4 cm"
                    ),
                    (
                        "BC = 10 cm; AH = 4.5 cm; BH = 3.5 cm; CH = 6.5 cm"
                    ),
                    ("BC = 14 cm; AH = 4.8 cm; BH = 6 cm; CH = 8 cm"),
                    (
                        "BC = 10 cm; AH = 5 cm; BH = 3.6 cm; CH = 6.4 cm"
                    ),
                ],
                "answer": (
                    "BC = 10 cm; AH = 4.8 cm; BH = 3.6 cm; CH = 6.4 cm"
                ),
                "explanation": (
                    "Pythagoras: $BC = \\sqrt{6^2 + 8^2} = 10\\text{ cm}$. Metric"
                    " relations: $AH = \\frac{AB \\cdot AC}{BC} = 4.8\\text{ cm}$;"
                    " $BH = \\frac{AB^2}{BC} = 3.6\\text{ cm}$;$CH = 10 - 3.6 ="
                    " 6.4\\text{ cm}$."
                ),
            },
            {
                "id": 10,
                "title": (
                    "Question 10: Intersection of Parabola and Line"
                ),
                "latex": r"(P): y = x^2,\quad d: y = (m-1)x + 2,\quad x_1^2 + x_2^2 = 10",
                "desc": (
                    "Find m for d to intersect (P) at two distinct points"
                    " satisfying the condition:"
                ),
                "options": [
                    "m = 1 ± √6",
                    "m = 1 ± √10",
                    "m = -1 ± √6",
                    "m = 2 or m = -4",
                ],
                "answer": "m = 1 ± √6",
                "explanation": (
                    "Intersection equation: $x^2 - (m-1)x - 2 = 0$ always has"
                    " two distinct roots since $ac = -2 < 0$. By Vieta: $x_1^2 +"
                    " x_2^2 = (x_1+x_2)^2 - 2x_1 x_2 = (m-1)^2 + 4 = 10 \\iff m"
                    " = 1 \\pm \\sqrt{6}$."
                ),
            },
        ],
    },
    3: {
        "name": "Stage 3: Throne Hall (Gifted Math Level)",
        "story": (
            "The Knight advances along the red carpet of the throne hall! The"
            " Evil Princess sits on the throne with her guards ready to"
            " execute you if you calculate incorrectly!"
        ),
        "boss_name": "Evil Princess",
        "boss_files": ["boss3.jpg", "boss3.png", "image_b0951d.jpg"],
        "boss_emoji": "👸",
        "bg_files": ["bg3.jpg", "bg3.png", "image_b0e7d3.jpg"],
        "bg_fallback": "linear-gradient(180deg, #4b1248 0%, #f0c27b 100%)",
        "questions": [
            {
                "id": 11,
                "title": "Question 11: Irrational Equation with Radicals",
                "latex": r"\sqrt{x+5} + \sqrt{2x-1} = 4",
                "desc": "Find the root of the equation (Condition: x ≥ 1/2):",
                "options": [
                    "x = 54 - 8√43 (approx 1.54)",
                    "x = 4",
                    "x = 54 + 8√43",
                    "x = 5",
                ],
                "answer": "x = 54 - 8√43 (approx 1.54)",
                "explanation": (
                    "Rearrange: $\\sqrt{2x-1} = 4 - \\sqrt{x+5}$(with$\\frac{1}{2}"
                    " \\le x \\le 11$). Squaring both sides gives $8\\sqrt{x+5}"
                    " = 22 - x$. Squaring again: $x^2 - 108x + 164 = 0 \\implies"
                    " x = 54 - 8\\sqrt{43}$ (valid)."
                ),
            },
            {
                "id": 12,
                "title": "Question 12: Cauchy-Schwarz Inequality",
                "latex": r"a, b > 0,\quad a + b = 1 \implies \frac{1}{a} + \frac{1}{b} \ge 4",
                "desc": (
                    "When does equality hold in the Cauchy-Schwarz"
                    " inequality?"
                ),
                "options": [
                    "a = b = 1/2",
                    "a = b = 1",
                    "a = 1/4 and b = 3/4",
                    "a = b = 2",
                ],
                "answer": "a = b = 1/2",
                "explanation": (
                    "Applying Cauchy-Schwarz: $\\frac{1}{a} + \\frac{1}{b} \\ge"
                    " \\frac{(1+1)^2}{a+b} = 4$. Equality holds if and only if"
                    " $a = b = \\frac{1}{2}$."
                ),
            },
            {
                "id": 13,
                "title": "Question 13: Diophantine Equation",
                "latex": r"x^2 - y^2 = 21 \quad (x, y \in \mathbb{Z})",
                "desc": "Find all integer solution pairs (x; y):",
                "options": [
                    "(±11; ±10) and (±5; ±2) (total 8 pairs)",
                    "(11; 10) and (7; 3)",
                    "(5; 2) and (6; 3)",
                    "Only (5; 2)",
                ],
                "answer": "(±11; ±10) and (±5; ±2) (total 8 pairs)",
                "explanation": (
                    "Factorize: $(x - y)(x + y) = 21$. Checking integer"
                    " divisors of 21 ($\\pm 1; \\pm 3; \\pm 7; \\pm 21$), we find"
                    " 8 solution pairs: $(\\pm 11; \\pm 10)$ and $(\\pm 5; \\pm" " 2)$."
                ),
            },
            {
                "id": 14,
                "title": (
                    "Question 14: Advanced Geometry - Cyclic Quadrilateral"
                ),
                "latex": r"BE \perp AC,\quad CF \perp AB,\quad BE \cap CF = \{H\}",
                "desc": (
                    "In acute triangle ABC with altitudes BE and CF meeting at"
                    " H, choose the CORRECT statement:"
                ),
                "options": [
                    (
                        "AEHF is cyclic with diameter AH; AH ⊥ BC (and AH ⊥ EF"
                        " when ΔABC is isosceles at A)"
                    ),
                    (
                        "AEHF is cyclic with diameter EF; AH passes through"
                        " the midpoint of BC"
                    ),
                    (
                        "AEHF is not cyclic; AH is the angle bisector of"
                        " angle A"
                    ),
                    "AEHF is cyclic with diameter BC",
                ],
                "answer": (
                    "AEHF is cyclic with diameter AH; AH ⊥ BC (and AH ⊥ EF when"
                    " ΔABC is isosceles at A)"
                ),
                "explanation": (
                    "Since $\\widehat{AEH} + \\widehat{AFH} = 90^\\circ +"
                    " 90^\\circ = 180^\\circ$, quadrilateral $AEHF$ is cyclic"
                    " with diameter $AH$. Since $H$ is the orthocenter of"
                    " $\\triangle ABC$, $AH \\perp BC$."
                ),
            },
            {
                "id": 15,
                "title": "Question 15: Algebraic Extremum (Final Decisive Blow)",
                "latex": r"x, y > 0,\quad xy = 1,\quad P = x^2 + y^2 + x + y",
                "desc": "Find the minimum value (Min) of P and the equality case:",
                "options": [
                    "Min P = 4 when x = y = 1",
                    "Min P = 2 when x = y = 1",
                    "Min P = 6 when x = y = 1",
                    "Min P = 4 when x = 2, y = 1/2",
                ],
                "answer": "Min P = 4 when x = y = 1",
                "explanation": (
                    "Applying AM-GM inequality for positive numbers: $x^2 + y^2"
                    " \\ge 2xy = 2$ and $x + y \\ge 2\\sqrt{xy} = 2$. Adding"
                    " them gives $P \\ge 4$. Equality occurs when $x = y = 1$."
                ),
            },
        ],
    },
}

# ================= INITIALIZE SESSION STATE =================
if "stage" not in st.session_state:
  st.session_state.stage = 1
  st.session_state.q_index = 0
  st.session_state.prev_x = -12
  st.session_state.curr_x = HERO_POSITIONS[0]
  st.session_state.action_state = "enter"
  st.session_state.step_counter = 1
  st.session_state.boss_hp = 100
  st.session_state.score = 0
  st.session_state.combat_log = (
      "⚔️ The knight has entered the arena! Solve each question correctly to"
      " step forward and slash the Boss!"
  )
  st.session_state.last_explanation = None


def restart_game():
  st.session_state.stage = 1
  st.session_state.q_index = 0
  st.session_state.prev_x = -12
  st.session_state.curr_x = HERO_POSITIONS[0]
  st.session_state.action_state = "enter"
  st.session_state.step_counter += 1
  st.session_state.boss_hp = 100
  st.session_state.score = 0
  st.session_state.combat_log = (
      "⚔️ The knight has revived and restarted the journey!"
  )
  st.session_state.last_explanation = None


# ================= RENDER 2D GAME CANVAS FUNCTION (ENGLISH + ⚔️ SWORD ONLY) =================
def render_2d_game_canvas(stage_data, q_idx, prev_x, curr_x, state, boss_hp, score):
  hero_b64 = get_image_base64(HERO_FILES)
  boss_b64 = get_image_base64(stage_data["boss_files"])
  bg_b64 = get_image_base64(stage_data["bg_files"])

  if bg_b64:
    bg_css = "background-image: url('" + bg_b64 + "');"
  else:
    bg_css = "background: " + stage_data["bg_fallback"] + ";"

  if hero_b64:
    hero_visual = '<img src="' + hero_b64 + '" class="sprite-img">'
  else:
    hero_visual = '<div class="emoji-actor">🤺</div>'

  if boss_b64:
    boss_visual = '<img src="' + boss_b64 + '" class="sprite-img">'
  else:
    boss_visual = (
        '<div class="emoji-actor">' + stage_data["boss_emoji"] + "</div>"
    )

  hero_hp_pct = 0 if state == "dead" else 100
  step_num = min(q_idx + 1, 5)

  dots_html = ""
  for i, pos in enumerate(HERO_POSITIONS):
    dot_color = "#00e676" if i <= q_idx else "#666666"
    dots_html += (
        '<div class="step-dot" style="left:'
        + str(pos)
        + "%; background:"
        + dot_color
        + ';"></div>'
    )

  sword_fx = ""
  extra_actors = ""

  if state == "enter":
    hero_anim = "heroEnter 1.3s forwards ease-out"
    boss_anim = "none"
  elif state == "walk_attack":
    hero_anim = "heroWalkSlash 1.8s forwards ease-in-out"
    boss_anim = "bossHit 1.8s forwards ease-in-out"
    # Chỉ dùng icon ⚔️ cho hiệu ứng chiến đấu
    sword_fx = '<div class="sword-wave">⚔️</div>'
  elif state == "stage_clear":
    hero_anim = "heroExitRight 2.6s forwards ease-in-out"
    boss_anim = "bossDefeat 2.6s forwards ease-out"
    sword_fx = '<div class="sword-wave">⚔️</div>'
  elif state == "victory":
    hero_anim = "heroVictoryPose 1.5s forwards ease-out"
    boss_anim = "princessFlyAway 3.0s forwards ease-in"
    sword_fx = '<div class="sword-wave">⚔️</div>'
    extra_actors = '<div class="dragon-free">🐉✨</div>'
  else:  # state == "dead"
    hero_anim = "heroDead 1.4s forwards ease-in"
    boss_anim = "none"
    extra_actors = (
        '<div class="guard-left">💂‍♂️⚔️</div>'
        '<div class="guard-right">⚔️💂‍♂️</div>'
    )

  guard_left_target = max(2, curr_x - 8)
  guard_right_target = min(84, curr_x + 8)

  html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: sans-serif; }}
        body {{ background: transparent; overflow: hidden; }}
        .game-wrapper {{
            width: 100%;
            border: 4px solid #ffd700;
            border-radius: 16px;
            overflow: hidden;
            background: #141622;
            box-shadow: 0 8px 24px rgba(0,0,0,0.8);
        }}
        .hud {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 16px;
            background: #141622;
            color: #ffffff;
            border-bottom: 3px solid #ffd700;
            font-size: 13px;
        }}
        .hp-bar {{
            width: 140px;
            height: 12px;
            background: #333;
            border: 1px solid #fff;
            border-radius: 6px;
            overflow: hidden;
            margin: 4px 0;
        }}
        .hp-hero {{ width: {hero_hp_pct}%; height: 100%; background: linear-gradient(90deg, #00e676, #69f0ae); }}
        .hp-boss {{ width: {boss_hp}%; height: 100%; background: linear-gradient(90deg, #ff1744, #ff616f); transition: width 0.4s; }}
        .viewport {{
            position: relative;
            width: 100%;
            height: 310px;
            {bg_css}
            background-size: cover;
            background-position: center bottom;
            overflow: hidden;
        }}
        .ground-line {{
            position: absolute;
            bottom: 22px;
            left: 8%;
            width: 68%;
            height: 5px;
            background: rgba(255, 215, 0, 0.4);
            border-radius: 3px;
        }}
        .step-dot {{
            position: absolute;
            bottom: 18px;
            width: 13px;
            height: 13px;
            border-radius: 50%;
            border: 2px solid #000;
            z-index: 2;
        }}
        .actor {{
            position: absolute;
            bottom: 26px;
            text-align: center;
            z-index: 5;
        }}
        .name-tag {{
            background: rgba(0,0,0,0.78);
            color: #ffd700;
            font-size: 11px;
            font-weight: bold;
            padding: 2px 7px;
            border-radius: 6px;
            border: 1px solid #ffd700;
            margin-bottom: 3px;
            white-space: nowrap;
        }}
        .sprite-img {{
            height: 115px;
            width: auto;
            object-fit: contain;
            image-rendering: pixelated;
            filter: drop-shadow(0 5px 8px rgba(0,0,0,0.9));
        }}
        .emoji-actor {{
            font-size: 68px;
            line-height: 1.1;
            filter: drop-shadow(0 5px 8px rgba(0,0,0,0.9));
        }}
        #hero-box {{
            left: {curr_x}%;
            animation: {hero_anim};
        }}
        #boss-box {{
            right: 8%;
            animation: {boss_anim};
        }}
        .sword-wave {{
            position: absolute;
            bottom: 65px;
            font-size: 46px;
            z-index: 8;
            opacity: 0;
            animation: swordFly 1.8s forwards;
        }}
        .dragon-free {{
            position: absolute;
            font-size: 80px;
            z-index: 10;
            animation: dragonFly 4s infinite ease-in-out;
        }}
        .guard-left {{
            position: absolute;
            bottom: 26px;
            font-size: 58px;
            z-index: 9;
            animation: guardLeft 1.1s forwards ease-out;
        }}
        .guard-right {{
            position: absolute;
            bottom: 26px;
            font-size: 58px;
            z-index: 9;
            animation: guardRight 1.1s forwards ease-out;
        }}

        @keyframes heroEnter {{
            0% {{ left: -12%; transform: translateY(0px); }}
            25% {{ transform: translateY(-12px) rotate(-4deg); }}
            50% {{ transform: translateY(0px) rotate(4deg); }}
            75% {{ transform: translateY(-12px) rotate(-4deg); }}
            100% {{ left: {curr_x}%; transform: translateY(0px) rotate(0deg); }}
        }}
        @keyframes heroWalkSlash {{
            0% {{ left: {prev_x}%; transform: translateY(0px) scale(1); }}
            15% {{ transform: translateY(-14px) rotate(-4deg); }}
            30% {{ left: {curr_x}%; transform: translateY(0px) rotate(4deg); }}
            50% {{ left: 68%; transform: translateY(-10px) scale(1.15) rotate(12deg); }}
            75% {{ left: {curr_x}%; transform: translateY(0px) scale(1) rotate(0deg); }}
            100% {{ left: {curr_x}%; transform: translateY(0px) scale(1); }}
        }}
        @keyframes heroExitRight {{
            0% {{ left: {prev_x}%; transform: translateY(0px); }}
            25% {{ left: 72%; transform: translateY(-14px) scale(1.15) rotate(10deg); }}
            45% {{ left: 80%; transform: translateY(0px) scale(1); }}
            65% {{ left: 90%; transform: translateY(-12px) rotate(-4deg); }}
            85% {{ left: 98%; transform: translateY(0px) rotate(4deg); }}
            100% {{ left: 108%; transform: translateY(0px); }}
        }}
        @keyframes heroVictoryPose {{
            0% {{ left: {prev_x}%; }}
            40% {{ left: 70%; transform: scale(1.2) rotate(12deg); }}
            100% {{ left: 48%; transform: scale(1.1) rotate(0deg); }}
        }}
        @keyframes swordFly {{
            0%, 25% {{ left: {curr_x}%; opacity: 0; transform: scale(0.5); }}
            45% {{ left: {curr_x + 12}%; opacity: 1; transform: scale(1.2); }}
            65% {{ left: 76%; opacity: 1; transform: scale(1.5); }}
            80%, 100% {{ left: 82%; opacity: 0; transform: scale(1.8); }}
        }}
        @keyframes bossHit {{
            0%, 45% {{ right: 8%; transform: translateX(0); filter: brightness(1); }}
            55% {{ right: 4%; transform: translateX(16px) rotate(12deg); filter: brightness(2.2); }}
            75% {{ right: 8%; transform: translateX(-5px) rotate(-5deg); }}
            100% {{ right: 8%; transform: translateX(0); filter: brightness(1); }}
        }}
        @keyframes bossDefeat {{
            0%, 25% {{ right: 8%; transform: rotate(0deg) scale(1); opacity: 1; }}
            55% {{ right: 4%; transform: translateY(30px) rotate(90deg) scale(0.85); opacity: 0.6; }}
            100% {{ right: 4%; transform: translateY(45px) rotate(90deg) scale(0.75); opacity: 0.15; }}
        }}
        @keyframes princessFlyAway {{
            0%, 25% {{ right: 8%; bottom: 26px; transform: rotate(0deg) scale(1); opacity: 1; }}
            55% {{ right: -4%; bottom: 160px; transform: rotate(540deg) scale(0.7); opacity: 0.9; }}
            100% {{ right: -25%; bottom: 380px; transform: rotate(1440deg) scale(0); opacity: 0; }}
        }}
        @keyframes dragonFly {{
            0% {{ left: -15%; top: 150px; transform: scale(0.7); }}
            50% {{ left: 45%; top: 30px; transform: scale(1.2) rotate(-8deg); }}
            100% {{ left: 110%; top: -20px; transform: scale(0.9) rotate(-15deg); }}
        }}
        @keyframes guardLeft {{
            0% {{ left: -12%; }}
            60%, 100% {{ left: {guard_left_target}%; transform: rotate(12deg); }}
        }}
        @keyframes guardRight {{
            0% {{ left: 105%; }}
            60%, 100% {{ left: {guard_right_target}%; transform: rotate(-12deg); }}
        }}
        @keyframes heroDead {{
            0%, 45% {{ left: {curr_x}%; transform: rotate(0deg); filter: grayscale(0%); }}
            75%, 100% {{ left: {curr_x}%; transform: translateY(25px) rotate(-90deg) scale(0.85); filter: grayscale(100%) brightness(55%); }}
        }}
    </style>
    </head>
    <body>
    <div class="game-wrapper">
        <div class="hud">
            <div>
                <strong>🤺 Dragon Rescue Knight</strong> (Step {step_num}/5)
                <div class="hp-bar"><div class="hp-hero"></div></div>
                <span>❤️ 1 Life | Score: {score} EXP</span>
            </div>
            <div style="text-align:center; color:#ffd700; font-weight:bold; font-size:15px;">
                {stage_data["name"]}
            </div>
            <div style="text-align:right;">
                <strong>{stage_data["boss_name"]}</strong>
                <div class="hp-bar"><div class="hp-boss"></div></div>
                <span>Boss HP: {boss_hp}/100</span>
            </div>
        </div>
        <div class="viewport">
            <div class="ground-line"></div>
            {dots_html}
            {sword_fx}
            {extra_actors}
            <div id="hero-box" class="actor">
                <div class="name-tag">Knight</div>
                {hero_visual}
            </div>
            <div id="boss-box" class="actor">
                <div class="name-tag" style="color:#ff8a80; border-color:#ff5252;">{stage_data["boss_name"]}</div>
                {boss_visual}
            </div>
        </div>
    </div>
    </body>
    </html>
    """
  components.html(html_code, height=405, scrolling=False)


# ================= MAIN UI =================
st.title("🐉 Dragon Rescue Knight - 2D Animation")

current_stage = STAGES[st.session_state.stage]
state = st.session_state.action_state

# Render 2D viewport
render_2d_game_canvas(
    stage_data=current_stage,
    q_idx=st.session_state.q_index,
    prev_x=st.session_state.prev_x,
    curr_x=st.session_state.curr_x,
    state=state,
    boss_hp=st.session_state.boss_hp,
    score=st.session_state.score,
)

# Combat log & Explanation
st.info(st.session_state.combat_log)
if st.session_state.last_explanation:
  with st.expander(
      "📖 View Detailed Explanation",
      expanded=(state in ["dead", "stage_clear", "victory"]),
  ):
    st.markdown(st.session_state.last_explanation)

# ================= STAGE CLEAR / VICTORY / DEFEAT HANDLING =================
if state == "victory":
  st.balloons()
  st.success(
      "🏆 TOTAL VICTORY! The Evil Princess has been blasted away from the"
      f" tower and the Dragon flies free! Total Score: **{st.session_state.score}"
      " EXP**"
  )
  if st.button("🔄 Restart Journey from Beginning", type="primary"):
    restart_game()
    safe_rerun()
  st.stop()

if state == "dead":
  st.error(
      "💀 YOU WERE DEFEATED BY THE GUARDS! Getting even 1 question wrong allows"
      " the guards to ambush and finish you off!"
  )
  if st.button("🔄 Revive and Retry!", type="primary"):
    restart_game()
    safe_rerun()
  st.stop()

if state == "stage_clear":
  st.success(
      f"🎉 You defeated **{current_stage['boss_name']}**! The knight marches"
      " across the screen to the next stage!"
  )
  if st.button(
      f"🚪 Proceed to Stage {st.session_state.stage + 1} ➡️", type="primary"
  ):
    st.session_state.stage += 1
    st.session_state.q_index = 0
    st.session_state.prev_x = -12
    st.session_state.curr_x = HERO_POSITIONS[0]
    st.session_state.boss_hp = 100
    st.session_state.action_state = "enter"
    st.session_state.step_counter += 1
    st.session_state.combat_log = (
        f"⚔️ Knight entered Stage {st.session_state.stage}! Solve math problems"
        " to advance!"
    )
    safe_rerun()
  st.stop()

# ================= MATH QUESTION INTERFACE =================
current_q = current_stage["questions"][st.session_state.q_index]

st.subheader(
    f"📜 {current_q['title']} (Step {st.session_state.q_index + 1}/5 - Stage"
    f" {st.session_state.stage})"
)
st.caption(current_stage["story"])
st.write(f"**Task:** {current_q['desc']}")
st.latex(current_q["latex"])

user_choice = st.radio(
    "Choose the correct answer to make the knight step forward and swing"
    " sword (1 wrong answer means instant death):",
    current_q["options"],
    key=f"q_radio_{current_q['id']}_{st.session_state.step_counter}",
)

if st.button("⚡ Move Forward & Swing Sword!", type="primary"):
  st.session_state.step_counter += 1
  st.session_state.last_explanation = (
      f"**Correct Answer:** `{current_q['answer']}`\n\n**Detailed"
      f" Explanation:** {current_q['explanation']}"
  )

  if user_choice == current_q["answer"]:
    st.session_state.boss_hp -= 20
    st.session_state.score += 100

    if st.session_state.q_index + 1 < len(current_stage["questions"]):
      st.session_state.prev_x = HERO_POSITIONS[st.session_state.q_index]
      st.session_state.q_index += 1
      st.session_state.curr_x = HERO_POSITIONS[st.session_state.q_index]
      st.session_state.action_state = "walk_attack"
      st.session_state.combat
