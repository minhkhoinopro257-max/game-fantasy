import streamlit as st
import base64
import os

# Cấu hình trang
st.set_page_config(
    page_title="Hiệp Sĩ Giải Cứu Rồng - 2D Adventure",
    page_icon="🐉",
    layout="centered"
)

def safe_rerun():
    if hasattr(st, "rerun"):
        st.rerun()
    else:
        st.experimental_rerun()

# Đọc ảnh sang Base64 để gắn trực tiếp vào khung hình 2D
def get_image_base64(file_candidates):
    for filename in file_candidates:
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                data = f.read()
            ext = filename.split(".")[-1].lower()
            mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
            return f"data:{mime};base64,{base64.b64encode(data).decode()}"
    return None

def render_actor_img(file_candidates, fallback_emoji, css_class="sprite-img"):
    b64 = get_image_base64(file_candidates)
    if b64:
        return f'<img src="{b64}" class="{css_class}">'
    return f'<div class="fallback-emoji {css_class}">{fallback_emoji}</div>'

# ================= DỮ LIỆU NHÂN VẬT & 3 MÀN CHƠI =================
HERO_FILES = ["main.png", "main.jpg", "image_b090fc.png"]

# Tọa độ X (%) của Hiệp sĩ trên khung hình tương ứng với câu hỏi 0, 1, 2, 3, 4
HERO_POSITIONS = [8, 22, 36, 50, 64]

STAGES = {
    1: {
        "name": "Màn 1: Tàn Tích Rừng Đen (Cơ bản)",
        "story": "Hiệp sĩ băng qua khu rừng tàn tích để tiến về lâu đài. Sát Thủ Áo Đen đang chặn ở cổng đá phía bên phải khung hình!",
        "boss_name": "Sát Thủ Áo Đen",
        "boss_files": ["boss1.png", "boss1.jpg", "image_b09486.png"],
        "boss_fallback": "🥷",
        "bg_files": ["bg1.jpg", "bg1.png", "image_b0955a.jpg"],
        "bg_fallback": "linear-gradient(180deg, #1b1b1b 0%, #3a3a3a 70%, #111111 100%)",
        "questions": [
            {
                "id": 1,
                "title": "Câu 1: Giải phương trình bậc hai",
                "latex": r"x^2 - 5x + 6 = 0",
                "desc": "Giải phương trình để bước tiếp qua khu rừng:",
                "options": ["x = 2 hoặc x = 3", "x = -2 hoặc x = -3", "x = 1 hoặc x = 6", "x = -1 hoặc x = 6"],
                "answer": "x = 2 hoặc x = 3",
                "explanation": "Ta có: $x^2 - 5x + 6 = 0 \\iff (x - 2)(x - 3) = 0 \\iff x = 2$ hoặc $x = 3$."
            },
            {
                "id": 2,
                "title": "Câu 2: Rút gọn biểu thức chứa căn",
                "latex": r"A = \frac{\sqrt{12} + \sqrt{27} - \sqrt{3}}{\sqrt{3}}",
                "desc": "Tìm giá trị rút gọn của biểu thức A:",
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
        "boss_fallback": "💀🔥",
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
        "boss_fallback": "👸👑",
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
    st.session_state.action_state = "enter"  # 'enter', 'walk_attack', 'stage_clear', 'dead', 'victory'
    st.session_state.step_counter = 1
    st.session_state.boss_hp = 100
    st.session_state.score = 0
    st.session_state.combat_log = "⚔️ Hiệp sĩ bước vào khung hình! Hãy giải toán để tiến lên phía trước và chém Boss!"
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

# ================= CSS CỐ ĐỊNH CHO KHUNG HÌNH 2D =================
st.markdown("""
<style>
.hud-bar {
    background: #141622;
    border: 3px solid #ffd700;
    border-radius: 12px 12px 0 0;
    padding: 10px 18px;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.hp-track {
    background: #333;
    border: 1px solid #fff;
    border-radius: 6px;
    height: 14px;
    width: 160px;
    overflow: hidden;
    margin-top: 4px;
}
.hp-fill-hero {
    background: linear-gradient(90deg, #00e676, #69f0ae);
    height: 100%;
}
.hp-fill-boss {
    background: linear-gradient(90deg, #ff1744, #ff616f);
    height: 100%;
    transition: width 0.4s ease;
}
.stage-viewport {
    position: relative;
    width: 100%;
    height: 350px;
    border: 4px solid #ffd700;
    border-top: none;
    border-radius: 0 0 16px 16px;
    background-size: cover;
    background-position: center bottom;
    overflow: hidden;
    box-shadow: 0 12px 30px rgba(0,0,0,0.85);
    margin-bottom: 18px;
}
.ground-path {
    position: absolute;
    bottom: 22px;
    left: 8%;
    width: 72%;
    height: 6px;
    background: rgba(255, 215, 0, 0.35);
    border-radius: 4px;
    z-index: 1;
}
.step-dot {
    position: absolute;
    bottom: 18px;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #ffd700;
    border: 2px solid #000;
    z-index: 2;
}
.actor-container {
    position: absolute;
    bottom: 28px;
    z-index: 5;
    text-align: center;
}
.sprite-img {
    height: 120px;
    width: auto;
    object-fit: contain;
    image-rendering: pixelated;
    filter: drop-shadow(0 5px 8px rgba(0,0,0,0.9));
    border-radius: 6px;
}
.fallback-emoji {
    font-size: 72px;
    line-height: 1.1;
    filter: drop-shadow(0 5px 8px rgba(0,0,0,0.9));
}
.actor-label {
    background: rgba(0, 0, 0, 0.75);
    color: #ffd700;
    font-size: 12px;
    font-weight: bold;
    padding: 2px 8px;
    border-radius: 8px;
    border: 1px solid #ffd700;
    margin-bottom: 4px;
    white-space: nowrap;
}
.quest-card {
    background: #1e2029;
    border-left: 6px solid #ffd700;
    padding: 15px;
    border-radius: 10px;
    color: #ffffff;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# ================= HIỂN THỊ TIÊU ĐỀ & KHUNG CẢNH =================
st.title("🐉 Hiệp Sĩ Giải Cứu Rồng - Chuyển Động 2D")

current_stage = STAGES[st.session_state.stage]
bg_b64 = get_image_base64(current_stage["bg_files"])
bg_style = f"background-image: url('{bg_b64}');" if bg_b64 else f"background: {current_stage['bg_fallback']};"

hero_img_html = render_actor_img(HERO_FILES, "🤺")
boss_img_html = render_actor_img(current_stage["boss_files"], current_stage["boss_fallback"])

# Tạo tên animation độc nhất ở mỗi bước để trình duyệt luôn chạy lại chuyển động
anim_id = st.session_state.step_counter
prev_x = st.session_state.prev_x
curr_x = st.session_state.curr_x
state = st.session_state.action_state

# Tạo CSS Keyframes động theo đúng tọa độ bước đi của Hiệp sĩ trên khung hình
dynamic_keyframes = f"""
<style>
/* 1. Hiệp sĩ bước từ ngoài rìa trái vào khung hình */
@keyframes heroEnter_{anim_id} {{
    0% {{ left: -12%; transform: translateY(0px); }}
    20% {{ transform: translateY(-12px) rotate(-3deg); }}
    40% {{ transform: translateY(0px) rotate(3deg); }}
    60% {{ transform: translateY(-12px) rotate(-3deg); }}
    80% {{ transform: translateY(0px) rotate(3deg); }}
    100% {{ left: {curr_x}%; transform: translateY(0px) rotate(0deg); }}
}}

/* 2. Hiệp sĩ đi bộ tới điểm tiếp theo, lao lên chém Boss rồi lùi về điểm đứng */
@keyframes heroWalkSlash_{anim_id} {{
    0% {{ left: {prev_x}%; transform: translateY(0px) scale(1); }}
    15% {{ transform: translateY(-14px) rotate(-4deg); }}
    30% {{ left: {curr_x}%; transform: translateY(0px) rotate(4deg); }}
    50% {{ left: 68%; transform: translateY(-10px) scale(1.15) rotate(12deg); }}
    70% {{ left: {curr_x}%; transform: translateY(0px) scale(1) rotate(0deg); }}
    100% {{ left: {curr_x}%; transform: translateY(0px) scale(1); }}
}}

/* 3. Hiệp sĩ đi bộ xuyên qua khung hình sang phải khi hạ xong Boss màn 1 & 2 */
@keyframes heroExitFrame_{anim_id} {{
    0% {{ left: {prev_x}%; transform: translateY(0px); }}
    20% {{ left: 72%; transform: translateY(-14px) scale(1.15) rotate(10deg); }}
    40% {{ left: 78%; transform: translateY(0px) scale(1); }}
    60% {{ left: 88%; transform: translateY(-12px) rotate(-4deg); }}
    80% {{ left: 98%; transform: translateY(0px) rotate(4deg); }}
    100% {{ left: 108%; transform: translateY(0px); }}
}}

/* Hiệu ứng kiếm khí bay ngang màn hình */
@keyframes swordWave_{anim_id} {{
    0%, 25% {{ left: {curr_x}%; opacity: 0; transform: scale(0.5); }}
    45% {{ left: {curr_x + 10}%; opacity: 1; transform: scale(1.3); }}
    65% {{ left: 78%; opacity: 1; transform: scale(1.6); }}
    75%, 100% {{ left: 82%; opacity: 0; transform: scale(2); }}
}}

/* Hiệu ứng Boss bị trúng đòn văng lùi */
@keyframes bossHit_{anim_id} {{
    0%, 45% {{ right: 8%; transform: translateX(0) rotate(0deg); filter: brightness(1); }}
    55% {{ right: 4%; transform: translateX(18px) rotate(12deg); filter: brightness(2) sepia(1) hue-rotate(-50deg); }}
    70% {{ right: 8%; transform: translateX(-6px) rotate(-5deg); }}
    100% {{ right: 8%; transform: translateX(0) rotate(0deg); filter: brightness(1); }}
}}

/* Hiệu ứng Boss ngã gục khi qua màn */
@keyframes bossDefeated_{anim_id} {{
    0%, 25% {{ right: 8%; transform: rotate(0deg) scale(1); opacity: 1; }}
    50% {{ right: 4%; transform: translateY(30px) rotate(90deg) scale(0.85); opacity: 0.7; }}
    100% {{ right: 4%; transform: translateY(50px) rotate(90deg) scale(0.7); opacity: 0.15; }}
}}

/* Hiệu ứng Công Chúa bị đánh bay khỏi màn hình ở Màn 3 */
@keyframes princessBlastOff_{anim_id} {{
    0%, 20% {{ right: 8%; bottom: 28px; transform: rotate(0deg) scale(1); opacity: 1; }}
    50% {{ right: -5%; bottom: 180px; transform: rotate(540deg) scale(0.7); opacity: 0.9; }}
    100% {{ right: -30%; bottom: 420px; transform: rotate(1440deg) scale(0); opacity: 0; }}
}}

/* Hiệu ứng Rồng thần bay ngang bầu trời tự do */
@keyframes dragonFlyAcross_{anim_id} {{
    0% {{ left: -15%; top: 140px; transform: scale(0.7) rotate(-5deg); opacity: 0; }}
    20% {{ opacity: 1; }}
    50% {{ left: 45%; top: 35px; transform: scale(1.25) rotate(-10deg); opacity: 1; }}
    100% {{ left: 110%; top: -30px; transform: scale(0.9) rotate(-15deg); opacity: 1; }}
}}

/* Hiệu ứng Lính canh lao từ 2 bên khung hình vào chém Hiệp sĩ khi trả lời sai */
@keyframes guardLeftRush_{anim_id} {{
    0% {{ left: -10%; bottom: 28px; }}
    60%, 100% {{ left: {max(0, curr_x - 8)}%; bottom: 28px; transform: rotate(15deg) scale(1.1); }}
}}
@keyframes guardRightRush_{anim_id} {{
    0% {{ left: 105%; bottom: 28px; }}
    60%, 100% {{ left: {min(85, curr_x + 8)}%; bottom: 28px; transform: rotate(-15deg) scale(1.1); }}
}}
@keyframes heroFallDown_{anim_id} {{
    0%, 45% {{ left: {curr_x}%; transform: rotate(0deg); filter: grayscale(0%); }}
    70%, 100% {{ left: {curr_x}%; transform: translateY(25px) rotate(-90deg) scale(0.85); filter: grayscale(100%) brightness(50%); }}
}}
</style>
"""
st.markdown(dynamic_keyframes, unsafe_allow_html=True)

# Xác định class hoạt họa cho Hiệp sĩ, Boss và Hiệu ứng phụ
sword_wave_html = ""
extra_actors_html = ""

if state == "enter":
    hero_anim_style = f"animation: heroEnter_{anim_id} 1.4s forwards ease-out;"
    boss_anim_style = "right: 8%;"
elif state == "walk_attack":
    hero_anim_style = f"animation: heroWalkSlash_{anim_id} 1.8s forwards ease-in-out;"
    boss_anim_style = f"animation: bossHit_{anim_id} 1.8s forwards ease-in-out;"
    sword_wave_html = f'<div style="position:absolute; bottom:65px; font-size:48px; z-index:8; animation: swordWave_{anim_id} 1.8s forwards;">⚔️💥</div>'
elif state == "stage_clear":
    hero_anim_style = f"animation: heroExitFrame_{anim_id} 2.6s forwards ease-in-out;"
    boss_anim_style = f"animation: bossDefeated_{anim_id} 2.6s forwards ease-out;"
    sword_wave_html = f'<div style="position:absolute; bottom:65px; font-size:52px; z-index:8; animation: swordWave_{anim_id} 1.5s forwards;">⚡⚔️🔥</div>'
elif state == "victory":
    hero_anim_style = f"left: 55%; transform: scale(1.1);"
    boss_anim_style = f"animation: princessBlastOff_{anim_id} 3s forwards ease-in;"
    extra_actors_html = f"""
    <div style="position:absolute; font-size:90px; z-index:10; animation: dragonFlyAcross_{anim_id} 4.5s infinite ease-in-out;">
        🐉✨
    </div>
    """
elif state == "dead":
    hero_anim_style = f"animation: heroFallDown_{anim_id} 1.5s forwards ease-in;"
    boss_anim_style = "right: 8%;"
    extra_actors_html = f"""
    <div style="position:absolute; font-size:65px; z-index:9; animation: guardLeftRush_{anim_id} 1.2s forwards ease-out;">💂‍♂️⚔️</div>
    <div style="position:absolute; font-size:65px; z-index:9; animation: guardRightRush_{anim_id} 1.2s forwards ease-out;">⚔️💂‍♂️</div>
    """

# Các chấm mốc bước đi trên mặt đất
dots_html = "".join([
    f'<div class="step-dot" style="left: {pos}%; background: {"#00e676" if idx <= st.session_state.q_index else "#555"};"></div>'
    for idx, pos in enumerate(HERO_POSITIONS)
])

# ================= VẼ KHUNG HÌNH 2D (STAGE VIEWPORT) =================
hero_hp_val = 0 if state == "dead" else 100
st.markdown(f"""
<div class="hud-bar">
    <div>
        <strong>🤺 Hiệp Sĩ Giải Cứu Rồng</strong> (Bước {min(st.session_state.q_index + 1, 5)}/5)<br>
        <div class="hp-track"><div class="hp-fill-hero" style="width: {hero_hp_val}%;"></div></div>
        <small>❤️ 1 Mạng Tử Chiến | Điểm: {st.session_state.score} EXP</small>
    </div>
    <div style="text-align:center; color:#ffd700; font-weight:bold; font-size:16px;">
        {current_stage["name"]}
    </div>
    <div style="text-align:right;">
        <strong>{current_stage["boss_name"]}</strong><br>
        <div class="hp-track"><div class="hp-fill-boss" style="width: {st.session_state.boss_hp}%;"></div></div>
        <small>HP Boss: {st.session_state.boss_hp}/100</small>
    </div>
</div>

<div class="stage-viewport" style="{bg_style}">
    <div class="ground-path"></div>
    {dots_html}
    {sword_wave_html}
    {extra_actors_html}
    <div class="actor-container" style="{hero_anim_style}">
        <div class="actor-label">Hiệp Sĩ</div>
        {hero_img_html}
    </div>
    <div class="actor-container" style="{boss_anim_style}">
        <div class="actor-label" style="color:#ff8a80; border-color:#ff5252;">{current_stage["boss_name"]}</div>
        {boss_img_html}
    </div>
</div>
""", unsafe_allow_html=True)

# Nhật ký chiến đấu & Lời giải
st.info(st.session_state.combat_log)
if st.session_state.last_explanation:
    with st.expander("📖 Xem lời giải chi tiết câu vừa rồi", expanded=(state in ["dead", "stage_clear", "victory"])):
        st.markdown(st.session_state.last_explanation)

# ================= XỬ LÝ CÁC TRẠNG THÁI CHUYỂN MÀN / THẮNG / THUA =================
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
    st.success(f"🎉 Bạn đã đánh bại **{current_stage['boss_name']}**! Hiệp sĩ đã đi xuyên qua khung hình để tiến sang màn kế tiếp!")
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

st.markdown(f"""
<div class="quest-card">
    <h4>📜 {current_q["title"]} (Bước {st.session_state.q_index + 1}/5 tại Màn {st.session_state.stage})</h4>
    <p><i>{current_stage["story"]}</i></p>
    <p><strong>Yêu cầu:</strong> {current_q["desc"]}</p>
</div>
""", unsafe_allow_html=True)

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
        
        # Nếu còn câu hỏi trong màn hiện tại -> Hiệp sĩ bước tới mốc tiếp theo trên khung hình
        if st.session_state.q_index + 1 < len(current_stage["questions"]):
            st.session_state.prev_x = HERO_POSITIONS[st.session_state.q_index]
            st.session_state.q_index += 1
            st.session_state.curr_x = HERO_POSITIONS[st.session_state.q_index]
            st.session_state.action_state = "walk_attack"
            st.session_state.combat_log = f"💥 CHÍNH XÁC! Hiệp sĩ tiến lên vị trí {st.session_state.curr_x}% khung hình và chém {current_stage['boss_name']} mất 20 HP!"
        else:
            # Đã trả lời xong câu thứ 5 của màn
            st.session_state.prev_x = HERO_POSITIONS[st.session_state.q_index]
            if st.session_state.stage < 3:
                st.session_state.action_state = "stage_clear"
                st.session_state.combat_log = f"🔥 {current_stage['boss_name'].upper()} ĐÃ GỤC NGÃ! Hiệp sĩ bước qua xác Boss, đi thẳng sang rìa phải khung hình để qua màn!"
            else:
                st.session_state.action_state = "victory"
                st.session_state.combat_log = "👑 ĐÒN QUYẾT ĐỊNH! Công Chúa Độc Ác bị đánh bay lên trời và Rồng thần tung cánh bay đi!"
    else:
        # Trả lời sai -> Bị lính canh lao từ 2 bên khung hình vào kết liễu tại chỗ
        st.session_state.action_state = "dead"
        st.session_state.combat_log = "💀 SAI RỒI! Lính canh từ hai phía khung hình đã ập vào kết liễu Hiệp sĩ!"
        
    safe_rerun()
