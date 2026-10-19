import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import streamlit.components.v1 as components


def get_base64_image(file_path):
  if os.path.exists(file_path):
    with open(file_path, 'rb') as f:
      data = f.read()
    return f"data:image/png;base64,{base64.b64encode(data).decode('utf-8')}"
  return ''


# Lấy chuỗi base64 chuẩn không bao giờ bị lỗi ngắt dòng
hero_b64 = get_base64_image('hero.png')

# Cấu hình trang
st.set_page_config(
    page_title="Hiệp Sĩ Giải Cứu Rồng - 2D RPG",
    page_icon="🐉",
    layout="centered"
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

# ================= DỮ LIỆU 3 MÀN CHƠI & 15 CÂU HỎI =================
HERO_FILES = ["main.png", "main.jpg", "image_b090fc.png"]
HERO_POSITIONS = [8, 22, 36, 50, 62]

STAGES = {
    1: {
        "name": "Màn 1: Tàn Tích Rừng Đen (Cơ bản)",
        "story": "Hiệp sĩ băng qua khu rừng tàn tích để tiến về lâu đài. Sát Thủ Áo Đen đang chặn đường ở phía bên phải khung hình!",
        "boss_name": "Sát Thủ Áo Đen",
        "boss_files": ["boss1.png", "boss1.jpg", "image_b09486.png"],
        "boss_emoji": "🥷",
        "bg_files": ["bg1.jpg", "bg1.png", "image_b0955a.jpg"],
        "bg_fallback": "linear-gradient(180deg, #1b1b1b 0%, #3a3a3a 70%, #111111 100%)",
        "questions": [
            {
                "id": 1,
                "title": "Câu 1: Giải phương trình bậc hai",
                "latex": r"x^2 - 5x + 6 = 0",
                "desc": "Tìm nghiệm của phương trình để bước tiếp qua khu rừng:",
                "options": ["x = 2 hoặc x = 3", "x = -2 hoặc x = -3", "x = 1 hoặc x = 6", "x = -1 hoặc x = 6"],
                "answer": "x = 2 hoặc x = 3",
                "explanation": "Ta có: $x^2 - 5x + 6 = 0 \\iff (x - 2)(x - 3) = 0 \\iff x = 2$ hoặc $x = 3$."
            },
            {
                "id": 2,
                "title": "Câu 2: Rút gọn biểu thức chứa căn",
                "latex": r"A = \frac{\sqrt{12} + \sqrt{27} - \sqrt{3}}{\sqrt{3}}",
                "desc": "Giá trị rút gọn của biểu thức A là:",
                "options": ["4", "5", "3", "4√3"],
                "answer": "4",
                "explanation": "Vì $\\sqrt{12} = 2\\sqrt{3}$ và $\\sqrt{27} = 3\\sqrt{3}$, nên $A = \\frac{2\\sqrt{3} + 3\\sqrt{3} - \\sqrt{3}}{\\sqrt{3}} = \\frac{4\\sqrt{3}}{\\sqrt{3}} = 4$."
            },
            {
                "id": 3,
                "title": "Câu 3: Giải phương trình chứa ẩn ở mẫu",
                "latex": r"\frac{2}{x-1} + \frac{1}{x+1} = 1 \quad (x \ne 1,\ x \ne -1)",
                "desc": "Nghiệm của phương trình là:",
                "options": [
                    "x = (3 ± √17) / 2",
                    "x = (3 ± √15) / 2",
                    "x = 2 hoặc x = -1",
                    "x = (-3 ± √17) / 2"
                ],
                "answer": "x = (3 ± √17) / 2",
                "explanation": "Quy đồng khử mẫu: $2(x+1) + (x-1) = x^2 - 1 \\iff x^2 - 3x - 2 = 0$. Ta có $\\Delta = 17 > 0 \\implies x = \\frac{3 \\pm \\sqrt{17}}{2}$ (thỏa mãn ĐK)."
            },
            {
                "id": 4,
                "title": "Câu 4: Giải hệ phương trình bậc nhất hai ẩn",
                "latex": r"\begin{cases} 2x + y = 7 \\ x - y = 2 \end{cases}",
                "desc": "Cặp nghiệm (x; y) của hệ phương trình là:",
                "options": ["(3; 1)", "(2; 3)", "(4; -1)", "(3; -1)"],
                "answer": "(3; 1)",
                "explanation": "Cộng từng vế hai phương trình: $3x = 9 \\implies x = 3$. Thay $x = 3$ vào phương trình dưới: $3 - y = 2 \\implies y = 1$. Vậy nghiệm là $(3; 1)$."
            },
            {
                "id": 5,
                "title": "Câu 5: Bài toán thực tế hình học",
                "latex": r"2(a + b) = 34, \quad a \cdot b = 60",
                "desc": "Một hình chữ nhật có chu vi 34 cm và diện tích 60 cm². Tính chiều dài a và chiều rộng b:",
                "options": [
                    "Chiều dài 12 cm, chiều rộng 5 cm",
                    "Chiều dài 10 cm, chiều rộng 6 cm",
                    "Chiều dài 15 cm, chiều rộng 4 cm",
                    "Chiều dài 14 cm, chiều rộng 3 cm"
                ],
                "answer": "Chiều dài 12 cm, chiều rộng 5 cm",
                "explanation": "Nửa chu vi là $34 : 2 = 17\\text{ cm}$. Ta có $a + b = 17$ và $ab = 60$. Theo định lý Vi-ét đảo, $a, b$ là nghiệm của $X^2 - 17X + 60 = 0 \\implies a = 12\\text{ cm}, b = 5\\text{ cm}$."
            }
        ]
    },
    2: {
        "name": "Màn 2: Cổng Lâu Đài Giam Rồng (Tuyển sinh 10)",
        "story": "Rồng thần đang bị giam trên đỉnh tháp! Hiệp sĩ phải băng qua cánh đồng trước lâu đài và đánh bại Tử Thần Lửa Đỏ!",
        "boss_name": "Tử Thần Lửa Đỏ",
        "boss_files": ["boss2.png", "boss2.jpg", "image_b094c4.png"],
        "boss_emoji": "💀",
        "bg_files": ["bg2.png", "bg2.jpg", "image_b0e738.png"],
        "bg_fallback": "linear-gradient(180deg, #3a7bd5 0%, #3a6073 70%, #16222a 100%)",
        "questions": [
            {
                "id": 6,
                "title": "Câu 6: Phương trình bậc hai chứa tham số",
                "latex": r"x^2 - 2(m+1)x + m^2 + 1 = 0",
                "desc": "Tìm điều kiện của m để phương trình có hai nghiệm phân biệt:",
                "options": ["m > 0", "m ≥ 0", "m > -1", "m ≠ 0"],
                "answer": "m > 0",
                "explanation": "Ta có $\\Delta' = (m+1)^2 - (m^2 + 1) = 2m$. Để phương trình có hai nghiệm phân biệt thì $\\Delta' > 0 \\iff 2m > 0 \\iff m > 0$."
            },
            {
                "id": 7,
                "title": "Câu 7: Giải phương trình bằng đặt ẩn phụ",
                "latex": r"\frac{x+1}{x-2} + \frac{x-2}{x+1} = \frac{5}{2} \quad (x \ne 2,\ x \ne -1)",
                "desc": "Tập nghiệm S của phương trình trên là:",
                "options": ["S = {-4; 5}", "S = {4; -5}", "S = {1; 2}", "S = {-2; 5}"],
                "answer": "S = {-4; 5}",
                "explanation": "Đặt $t = \\frac{x+1}{x-2}$ ($t \\ne 0$). Phương trình thành $t + \\frac{1}{t} = \\frac{5}{2} \\iff 2t^2 - 5t + 2 = 0 \\iff t = 2$ hoặc $t = \\frac{1}{2}$. Giải ra $x = 5$ hoặc $x = -4$."
            },
            {
                "id": 8,
                "title": "Câu 8: Bài toán năng suất công việc",
                "latex": r"\begin{cases} \frac{1}{x} + \frac{1}{y} = \frac{1}{6} \\ \frac{5}{x} + \frac{4}{y} = \frac{3}{4} \end{cases}",
                "desc": "Hai người làm chung 6 giờ thì xong. Nếu người 1 làm 5 giờ và người 2 làm 4 giờ thì được 3/4 công việc. Hỏi làm riêng mỗi người mất bao lâu?",
                "options": [
                    "Người 1: 12 giờ, Người 2: 12 giờ",
                    "Người 1: 10 giờ, Người 2: 15 giờ",
                    "Người 1: 8 giờ, Người 2: 24 giờ",
                    "Người 1: 9 giờ, Người 2: 18 giờ"
                ],
                "answer": "Người 1: 12 giờ, Người 2: 12 giờ",
                "explanation": "Từ $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{6} \\implies \\frac{4}{x} + \\frac{4}{y} = \\frac{2}{3}$. Lấy phương trình dưới trừ đi: $\\frac{1}{x} = \\frac{3}{4} - \\frac{2}{3} = \\frac{1}{12} \\implies x = 12$ giờ, $y = 12$ giờ."
            },
            {
                "id": 9,
                "title": "Câu 9: Hệ thức lượng trong tam giác vuông",
                "latex": r"AB = 6\text{ cm},\ AC = 8\text{ cm},\ AH \perp BC",
                "desc": "Cho tam giác ABC vuông tại A, đường cao AH. Tính BC, AH, BH, CH:",
                "options": [
                    "BC = 10 cm; AH = 4,8 cm; BH = 3,6 cm; CH = 6,4 cm",
                    "BC = 10 cm; AH = 4,5 cm; BH = 3,5 cm; CH = 6,5 cm",
                    "BC = 14 cm; AH = 4,8 cm; BH = 6 cm; CH = 8 cm",
                    "BC = 10 cm; AH = 5 cm; BH = 3,6 cm; CH = 6,4 cm"
                ],
                "answer": "BC = 10 cm; AH = 4,8 cm; BH = 3,6 cm; CH = 6,4 cm",
                "explanation": "Theo Pytago: $BC = \\sqrt{6^2 + 8^2} = 10\\text{ cm}$. Hệ thức lượng: $AH = \\frac{AB \\cdot AC}{BC} = 4,8\\text{ cm}$; $BH = \\frac{AB^2}{BC} = 3,6\\text{ cm}$; $CH = 10 - 3,6 = 6,4\\text{ cm}$."
            },
            {
                "id": 10,
                "title": "Câu 10: Sự tương giao giữa Parabol (P) và đường thẳng d",
                "latex": r"(P): y = x^2,\quad d: y = (m-1)x + 2,\quad x_1^2 + x_2^2 = 10",
                "desc": "Tìm m để d cắt (P) tại hai điểm phân biệt thỏa mãn điều kiện trên:",
                "options": [
                    "m = 1 ± √6",
                    "m = 1 ± √10",
                    "m = -1 ± √6",
                    "m = 2 hoặc m = -4"
                ],
                "answer": "m = 1 ± √6",
                "explanation": "Phương trình hoành độ giao điểm: $x^2 - (m-1)x - 2 = 0$ luôn có 2 nghiệm phân biệt vì $ac = -2 < 0$. Theo Vi-ét: $x_1^2 + x_2^2 = (x_1+x_2)^2 - 2x_1 x_2 = (m-1)^2 + 4 = 10 \\iff m = 1 \\pm \\sqrt{6}$."
            }
        ]
    },
    3: {
        "name": "Màn 3: Đại Sảnh Ngai Vàng (Toán Chuyên LTV)",
        "story": "Hiệp sĩ tiến bước dọc theo thảm đỏ đại sảnh! Công Chúa Độc Ác ngự trên ngai vàng cùng đội lính gác sẵn sàng kết liễu nếu bạn tính sai!",
        "boss_name": "Công Chúa Độc Ác",
        "boss_files": ["boss3.jpg", "boss3.png", "image_b0951d.jpg"],
        "boss_emoji": "👸",
        "bg_files": ["bg3.jpg", "bg3.png", "image_b0e7d3.jpg"],
        "bg_fallback": "linear-gradient(180deg, #4b1248 0%, #f0c27b 100%)",
        "questions": [
            {
                "id": 11,
                "title": "Câu 11: Phương trình vô tỉ chứa căn",
                "latex": r"\sqrt{x+5} + \sqrt{2x-1} = 4",
                "desc": "Tìm nghiệm của phương trình trên (ĐK: x ≥ 1/2):",
                "options": [
                    "x = 54 - 8√43 (xấp xỉ 1,54)",
                    "x = 4",
                    "x = 54 + 8√43",
                    "x = 5"
                ],
                "answer": "x = 54 - 8√43 (xấp xỉ 1,54)",
                "explanation": "Chuyển vế: $\\sqrt{2x-1} = 4 - \\sqrt{x+5}$ (với $\\frac{1}{2} \\le x \\le 11$). Bình phương 2 vế rút gọn được $8\\sqrt{x+5} = 22 - x$. Bình phương lần 2: $x^2 - 108x + 164 = 0 \\implies x = 54 - 8\\sqrt{43}$ (thỏa mãn)."
            },
            {
                "id": 12,
                "title": "Câu 12: Bất đẳng thức Cauchy-Schwarz",
                "latex": r"a, b > 0,\quad a + b = 1 \implies \frac{1}{a} + \frac{1}{b} \ge 4",
                "desc": "Dấu bằng của bất đẳng thức xảy ra khi nào?",
                "options": [
                    "a = b = 1/2",
                    "a = b = 1",
                    "a = 1/4 và b = 3/4",
                    "a = b = 2"
                ],
                "answer": "a = b = 1/2",
                "explanation": "Áp dụng BĐT Cauchy-Schwarz dạng phân thức: $\\frac{1}{a} + \\frac{1}{b} \\ge \\frac{(1+1)^2}{a+b} = 4$. Dấu bằng xảy ra khi và chỉ khi $a = b = \\frac{1}{2}$."
            },
            {
                "id": 13,
                "title": "Câu 13: Phương trình nghiệm nguyên",
                "latex": r"x^2 - y^2 = 21 \quad (x, y \in \mathbb{Z})",
                "desc": "Các cặp nghiệm nguyên (x; y) thỏa mãn phương trình là:",
                "options": [
                    "(±11; ±10) và (±5; ±2) (tổng cộng 8 cặp)",
                    "(11; 10) và (7; 3)",
                    "(5; 2) và (6; 3)",
                    "Chỉ có duy nhất (5; 2)"
                ],
                "answer": "(±11; ±10) và (±5; ±2) (tổng cộng 8 cặp)",
                "explanation": "Đưa về phương trình tích: $(x - y)(x + y) = 21$. Xét các ước nguyên của 21 là $\\{\\pm 1; \\pm 3; \\pm 7; \\pm 21\\}$, ta tìm được 8 cặp nghiệm nguyên: $(\\pm 11; \\pm 10)$ và $(\\pm 5; \\pm 2)$."
            },
            {
                "id": 14,
                "title": "Câu 14: Hình học nâng cao - Tứ giác nội tiếp & Trực tâm",
                "latex": r"BE \perp AC,\quad CF \perp AB,\quad BE \cap CF = \{H\}",
                "desc": "Cho tam giác ABC nhọn, hai đường cao BE và CF cắt nhau tại H. Chọn khẳng định ĐÚNG:",
                "options": [
                    "AEHF nội tiếp đường tròn đường kính AH; AH ⊥ BC (và AH ⊥ EF khi ΔABC cân tại A)",
                    "AEHF nội tiếp đường tròn đường kính EF; AH đi qua trung điểm BC",
                    "AEHF không nội tiếp; AH là phân giác góc A",
                    "AEHF nội tiếp đường tròn đường kính BC"
                ],
                "answer": "AEHF nội tiếp đường tròn đường kính AH; AH ⊥ BC (và AH ⊥ EF khi ΔABC cân tại A)",
                "explanation": "Ta có $\\widehat{AEH} + \\widehat{AFH} = 90^\\circ + 90^\\circ = 180^\\circ$ nên tứ giác $AEHF$ nội tiếp đường tròn đường kính $AH$. Vì $H$ là trực tâm $\\triangle ABC$ nên $AH \\perp BC$."
            },
            {
                "id": 15,
                "title": "Câu 15: Bài toán cực trị đại số (Đòn Quyết Định)",
                "latex": r"x, y > 0,\quad xy = 1,\quad P = x^2 + y^2 + x + y",
                "desc": "Giá trị nhỏ nhất (Min) của biểu thức P và điểm rơi là:",
                "options": [
                    "Min P = 4 khi x = y = 1",
                    "Min P = 2 khi x = y = 1",
                    "Min P = 6 khi x = y = 1",
                    "Min P = 4 khi x = 2, y = 1/2"
                ],
                "answer": "Min P = 4 khi x = y = 1",
                "explanation": "Áp dụng BĐT AM-GM (Cauchy) cho hai số dương: $x^2 + y^2 \\ge 2xy = 2$ và $x + y \\ge 2\\sqrt{xy} = 2$. Cộng vế theo vế được $P \\ge 4$. Dấu bằng xảy ra khi $x = y = 1$."
            }
        ]
    }
}

# ================= KHỞI TẠO SESSION STATE =================
if "stage" not in st.session_state:
    st.session_state.stage = 1
    st.session_state.q_index = 0
    st.session_state.prev_x = -12
    st.session_state.curr_x = HERO_POSITIONS[0]
    st.session_state.action_state = "enter"
    st.session_state.step_counter = 1
    st.session_state.boss_hp = 100
    st.session_state.score = 0
    st.session_state.combat_log = "⚔️ Hiệp sĩ bước vào khung hình! Giải đúng mỗi câu để bước lên chém Boss!"
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
    st.session_state.combat_log = "⚔️ Hiệp sĩ đã hồi sinh và bước vào màn chơi từ đầu!"
    st.session_state.last_explanation = None

# ================= HÀM DỰNG KHUNG HÌNH 2D BẰNG HTML5 CANVAS/DOM =================
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
        boss_visual = '<div class="emoji-actor">' + stage_data["boss_emoji"] + '</div>'

    hero_hp_pct = 0 if state == "dead" else 100
    step_num = min(q_idx + 1, 5)

    # Tạo 5 chấm mốc trên đường đi
    dots_html = ""
    for i, pos in enumerate(HERO_POSITIONS):
        dot_color = "#00e676" if i <= q_idx else "#666666"
        dots_html += '<div class="step-dot" style="left:' + str(pos) + '%; background:' + dot_color + ';"></div>'

    # Thiết lập CSS animation tùy theo trạng thái hiện tại
    sword_fx = ""
    extra_actors = ""

    if state == "enter":
        hero_anim = "heroEnter 1.3s forwards ease-out"
        boss_anim = "none"
    elif state == "walk_attack":
        hero_anim = "heroWalkSlash 1.8s forwards ease-in-out"
        boss_anim = "bossHit 1.8s forwards ease-in-out"
        sword_fx = '<div class="sword-wave">⚔️💥</div>'
    elif state == "stage_clear":
        hero_anim = "heroExitRight 2.6s forwards ease-in-out"
        boss_anim = "bossDefeat 2.6s forwards ease-out"
        sword_fx = '<div class="sword-wave">⚡⚔️🔥</div>'
    elif state == "victory":
        hero_anim = "heroVictoryPose 1.5s forwards ease-out"
        boss_anim = "princessFlyAway 3.0s forwards ease-in"
        sword_fx = '<div class="sword-wave">🌟⚔️💥</div>'
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

        /* KEYFRAMES CHUYỂN ĐỘNG QUA KHUNG HÌNH */
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
                <strong>🤺 Hiệp Sĩ Giải Cứu Rồng</strong> (Bước {step_num}/5)
                <div class="hp-bar"><div class="hp-hero"></div></div>
                <span>❤️ 1 Mạng Tử Chiến | Điểm: {score} EXP</span>
            </div>
            <div style="text-align:center; color:#ffd700; font-weight:bold; font-size:15px;">
                {stage_data["name"]}
            </div>
            <div style="text-align:right;">
                <strong>{stage_data["boss_name"]}</strong>
                <div class="hp-bar"><div class="hp-boss"></div></div>
                <span>HP Boss: {boss_hp}/100</span>
            </div>
        </div>
        <div class="viewport">
            <div class="ground-line"></div>
            {dots_html}
            {sword_fx}
            {extra_actors}
            <div id="hero-box" class="actor">
                <div class="name-tag">Hiệp Sĩ</div>
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

# ================= GIAO DIỆN CHÍNH =================
st.title("🐉 Hiệp Sĩ Giải Cứu Rồng - Chuyển Động 2D")

current_stage = STAGES[st.session_state.stage]
state = st.session_state.action_state

# Hiển thị khung hình 2D bằng HTML5 Component (không bao giờ lỗi Markdown)
render_2d_game_canvas(
    stage_data=current_stage,
    q_idx=st.session_state.q_index,
    prev_x=st.session_state.prev_x,
    curr_x=st.session_state.curr_x,
    state=state,
    boss_hp=st.session_state.boss_hp,
    score=st.session_state.score
)

# Nhật ký chiến đấu & Lời giải
st.info(st.session_state.combat_log)
if st.session_state.last_explanation:
    with st.expander("📖 Xem lời giải chi tiết câu vừa rồi", expanded=(state in ["dead", "stage_clear", "victory"])):
        st.markdown(st.session_state.last_explanation)

# ================= XỬ LÝ CHUYỂN MÀN / THẮNG / THUA =================
if state == "victory":
    st.balloons()
    st.success(f"🏆 ĐẠI THẮNG! Công Chúa Độc Ác đã bị đánh bay khỏi tòa tháp và Rồng thần đã tung cánh bay đi tự do! Tổng điểm: **{st.session_state.score} EXP**")
    if st.button("🔄 Chơi lại hành trình từ đầu", type="primary"):
        restart_game()
        safe_rerun()
    st.stop()

if state == "dead":
    st.error("💀 BẠN ĐÃ BỊ LÍNH CANH ĐÁNH CHẾT! Chỉ cần trả lời sai 1 câu, lính gác sẽ lập tức ập vào kết liễu!")
    if st.button("🔄 Hồi sinh và Phục thù ngay!", type="primary"):
        restart_game()
        safe_rerun()
    st.stop()

if state == "stage_clear":
    st.success(f"🎉 Bạn đã đánh bại **{current_stage['boss_name']}**! Hiệp sĩ đã đi bộ xuyên qua khung hình để tiến sang màn kế tiếp!")
    if st.button(f"🚪 Bước sang Màn {st.session_state.stage + 1} ➡️", type="primary"):
        st.session_state.stage += 1
        st.session_state.q_index = 0
        st.session_state.prev_x = -12
        st.session_state.curr_x = HERO_POSITIONS[0]
        st.session_state.boss_hp = 100
        st.session_state.action_state = "enter"
        st.session_state.step_counter += 1
        st.session_state.combat_log = f"⚔️ Hiệp sĩ bước vào khung hình Màn {st.session_state.stage}! Hãy tiếp tục giải toán để tiến lên!"
        safe_rerun()
    st.stop()

# ================= HIỂN THỊ CÂU HỎI TOÁN HỌC =================
current_q = current_stage["questions"][st.session_state.q_index]

st.subheader(f"📜 {current_q['title']} (Bước {st.session_state.q_index + 1}/5 - Màn {st.session_state.stage})")
st.caption(current_stage["story"])
st.write(f"**Yêu cầu:** {current_q['desc']}")
st.latex(current_q["latex"])

user_choice = st.radio(
    "Chọn đáp án đúng để Hiệp sĩ tiến lên phía trước và vung kiếm (Sai 1 câu sẽ bị lính đánh chết):",
    current_q["options"],
    key=f"q_radio_{current_q['id']}_{st.session_state.step_counter}"
)

if st.button("⚡ Tiến Lên & Vung Kiếm Chém Boss!", type="primary"):
    st.session_state.step_counter += 1
    st.session_state.last_explanation = f"**Đáp án đúng:** `{current_q['answer']}`\n\n**Lời giải chi tiết:** {current_q['explanation']}"

    if user_choice == current_q["answer"]:
        st.session_state.boss_hp -= 20
        st.session_state.score += 100

        if st.session_state.q_index + 1 < len(current_stage["questions"]):
            st.session_state.prev_x = HERO_POSITIONS[st.session_state.q_index]
            st.session_state.q_index += 1
            st.session_state.curr_x = HERO_POSITIONS[st.session_state.q_index]
            st.session_state.action_state = "walk_attack"
            st.session_state.combat_log = f"💥 CHÍNH XÁC! Hiệp sĩ tiến lên mốc {st.session_state.q_index + 1}/5 và chém {current_stage['boss_name']} mất 20 HP!"
        else:
            st.session_state.prev_x = HERO_POSITIONS[st.session_state.q_index]
            if st.session_state.stage < 3:
                st.session_state.action_state = "stage_clear"
                st.session_state.combat_log = f"🔥 {current_stage['boss_name'].upper()} ĐÃ GỤC NGÃ! Hiệp sĩ bước qua Boss, đi thẳng ra rìa phải khung hình để qua màn!"
            else:
                st.session_state.action_state = "victory"
                st.session_state.combat_log = "👑 ĐÒN QUYẾT ĐỊNH! Công Chúa Độc Ác bị đánh bay lên trời và Rồng thần tung cánh bay đi!"
    else:
        st.session_state.action_state = "dead"
        st.session_state.combat_log = "💀 SAI RỒI! Lính canh từ hai phía khung hình đã ập vào kết liễu Hiệp sĩ!"

    safe_rerun()
