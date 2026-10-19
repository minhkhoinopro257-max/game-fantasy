import streamlit as st
import base64
import os

# Cấu hình trang
st.set_page_config(
    page_title="Hiệp Sĩ Giải Cứu Rồng - Toán 9 & Ôn Thi 10",
    page_icon="🐉",
    layout="centered"
)

# Hàm tự động tải lại trang tương thích mọi phiên bản Streamlit
def safe_rerun():
    if hasattr(st, "rerun"):
        st.rerun()
    else:
        st.experimental_rerun()

# Hàm đọc file ảnh sang Base64 để nhúng trực tiếp vào đồ họa 2D CSS
def get_image_base64(file_candidates):
    for filename in file_candidates:
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                data = f.read()
            ext = filename.split(".")[-1].lower()
            mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
            return f"data:{mime};base64,{base64.b64encode(data).decode()}"
    return None

def render_sprite_html(file_candidates, fallback_emoji, extra_class=""):
    b64 = get_image_base64(file_candidates)
    if b64:
        return f'<img src="{b64}" class="pixel-sprite {extra_class}">'
    return f'<div class="emoji-sprite {extra_class}">{fallback_emoji}</div>'

# ================= CSS ĐỒ HỌA 2D & HIỆU ỨNG HOẠT HỌA =================
st.markdown("""
<style>
.battle-arena {
    border: 4px solid #ffd700;
    border-radius: 16px;
    padding: 22px;
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    margin-bottom: 20px;
    background-size: cover;
    background-position: center;
    position: relative;
    overflow: hidden;
    min-height: 310px;
}
.arena-overlay {
    background: rgba(10, 12, 22, 0.68);
    border-radius: 12px;
    padding: 15px;
    backdrop-filter: blur(2px);
}
.stage-banner {
    text-align: center;
    font-size: 20px;
    font-weight: 900;
    color: #ffd700;
    text-transform: uppercase;
    margin-bottom: 12px;
    text-shadow: 2px 2px 6px #000;
}
.fighters-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
}
.fighter-box {
    text-align: center;
    width: 43%;
    background: rgba(0, 0, 0, 0.65);
    padding: 15px;
    border-radius: 12px;
    border: 2px solid rgba(255, 215, 0, 0.4);
}
.pixel-sprite {
    height: 125px;
    width: auto;
    object-fit: contain;
    image-rendering: pixelated;
    border-radius: 8px;
    animation: float 2s infinite ease-in-out;
}
.emoji-sprite {
    font-size: 75px;
    line-height: 1.1;
    display: inline-block;
    animation: float 2s infinite ease-in-out;
}
.vs-badge {
    font-size: 30px;
    font-weight: 900;
    color: #ff3b3b;
    text-shadow: 0 0 12px #ff0000, 2px 2px 2px #000;
}
.hp-bar-bg {
    background: #2b2b2b;
    border-radius: 8px;
    height: 16px;
    width: 100%;
    margin-top: 8px;
    overflow: hidden;
    border: 1px solid #fff;
}
.hp-bar-fill-hero {
    background: linear-gradient(90deg, #00e676, #66ffa6);
    height: 100%;
}
.hp-bar-fill-boss {
    background: linear-gradient(90deg, #ff1744, #ff616f);
    height: 100%;
}
.quest-card {
    background: #1e2029;
    border-left: 6px solid #ffd700;
    padding: 16px;
    border-radius: 10px;
    color: #ffffff;
    margin-bottom: 12px;
}

/* Hoạt họa nhân vật nhấp nhô */
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
}

/* Hoạt họa Game Over: Lính canh lao vào đánh gục Hiệp Sĩ */
.dead-knight {
    transform: rotate(-90deg) scale(0.85) !important;
    filter: grayscale(100%) brightness(60%);
    animation: none !important;
}
.guard-attack-left {
    display: inline-block;
    font-size: 55px;
    animation: rushRight 0.8s infinite alternate ease-in-out;
}
.guard-attack-right {
    display: inline-block;
    font-size: 55px;
    animation: rushLeft 0.8s infinite alternate ease-in-out;
}
@keyframes rushRight {
    0% { transform: translateX(-25px); }
    100% { transform: translateX(10px) rotate(15deg); }
}
@keyframes rushLeft {
    0% { transform: translateX(25px); }
    100% { transform: translateX(-10px) rotate(-15deg); }
}

/* Hoạt họa Phá Đảo: Công chúa bị đánh bay & Rồng bay đi */
.princess-blast-off {
    animation: blastOff 3.5s forwards ease-in !important;
}
@keyframes blastOff {
    0% { transform: translate(0, 0) rotate(0deg) scale(1); opacity: 1; }
    30% { transform: translate(60px, -80px) rotate(360deg) scale(0.7); opacity: 0.9; }
    100% { transform: translate(350px, -400px) rotate(1440deg) scale(0); opacity: 0; }
}
.dragon-fly-free {
    font-size: 85px;
    display: inline-block;
    animation: dragonFly 4s infinite ease-in-out;
}
@keyframes dragonFly {
    0% { transform: translate(-120px, 30px) scale(0.8); }
    50% { transform: translate(20px, -35px) scale(1.15); }
    100% { transform: translate(160px, -90px) scale(0.9); }
}
</style>
""", unsafe_allow_html=True)

# ================= DỮ LIỆU 3 MÀN CHƠI & 15 CÂU HỎI =================
HERO_FILES = ["main.png", "main.jpg", "image_b090fc.png"]

STAGES = {
    1: {
        "name": "Màn 1: Tàn Tích Rừng Đen (Cơ bản)",
        "story": "Hiệp sĩ tiến vào khu rừng âm u để tìm đường đến lâu đài giải cứu Rồng thần. Tên Sát Thủ Áo Đen bất ngờ chặn đường!",
        "boss_name": "Sát Thủ Áo Đen",
        "boss_files": ["boss1.png", "boss1.jpg", "image_b09486.png"],
        "boss_fallback": "🥷",
        "bg_files": ["bg1.jpg", "bg1.png", "image_b0955a.jpg"],
        "bg_fallback_gradient": "linear-gradient(180deg, #1b1b1b 0%, #3a3a3a 60%, #111111 100%)",
        "questions": [
            {
                "id": 1,
                "title": "Câu 1: Giải phương trình bậc hai",
                "latex": r"x^2 - 5x + 6 = 0",
                "desc": "Tìm tập nghiệm của phương trình trên:",
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
                "explanation": "Quy đồng khử mẫu: $2(x+1) + (x-1) = x^2 - 1 \\iff x^2 - 3x - 2 = 0$. Ta có $\\Delta = (-3)^2 - 4(1)(-2) = 17 > 0 \\implies x = \\frac{3 \\pm \\sqrt{17}}{2}$ (thỏa mãn ĐK)."
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
                "desc": "Một hình chữ nhật có chu vi 34 cm và diện tích 60 cm². Tìm chiều dài a và chiều rộng b:",
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
        "story": "Rồng thần đang bị xích trên đỉnh tháp lâu đài! Để tiến vào trong, Hiệp sĩ phải vượt qua Tử Thần Lửa Đỏ canh cổng!",
        "boss_name": "Tử Thần Lửa Đỏ",
        "boss_files": ["boss2.png", "boss2.jpg", "image_b094c4.png"],
        "boss_fallback": "💀🔥",
        "bg_files": ["bg2.png", "bg2.jpg", "image_b0e738.png"],
        "bg_fallback_gradient": "linear-gradient(180deg, #3a7bd5 0%, #3a6073 60%, #16222a 100%)",
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
                "desc": "Hai người cùng làm chung thì xong trong 6 giờ. Nếu người 1 làm 5 giờ và người 2 làm 4 giờ thì được 3/4 công việc. Hỏi làm một mình thì mỗi người mất bao lâu?",
                "options": [
                    "Người 1: 12 giờ, Người 2: 12 giờ",
                    "Người 1: 10 giờ, Người 2: 15 giờ",
                    "Người 1: 8 giờ, Người 2: 24 giờ",
                    "Người 1: 9 giờ, Người 2: 18 giờ"
                ],
                "answer": "Người 1: 12 giờ, Người 2: 12 giờ",
                "explanation": "Từ $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{6} \\implies \\frac{4}{x} + \\frac{4}{y} = \\frac{2}{3}$. Lấy phương trình dưới trừ đi ta được: $\\frac{1}{x} = \\frac{3}{4} - \\frac{2}{3} = \\frac{1}{12} \\implies x = 12$ giờ, suy ra $y = 12$ giờ."
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
        "story": "Giữa đại sảnh uy nghiêm đầy lính gác, Công Chúa Độc Ác đang nắm giữ chìa khóa giam cầm Rồng thần. Chỉ một sai lầm nhỏ, lính canh sẽ kết liễu bạn!",
        "boss_name": "Công Chúa Độc Ác",
        "boss_files": ["boss3.jpg", "boss3.png", "image_b0951d.jpg"],
        "boss_fallback": "👸👑",
        "bg_files": ["bg3.jpg", "bg3.png", "image_b0e7d3.jpg"],
        "bg_fallback_gradient": "linear-gradient(180deg, #4b1248 0%, #f0c27b 100%)",
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
    st.session_state.hero_hp = 100
    st.session_state.boss_hp = 100
    st.session_state.score = 0
    st.session_state.combat_log = "⚔️ Hành trình giải cứu Rồng bắt đầu! Cẩn thận: Trả lời sai 1 câu sẽ bị lính canh đánh chết ngay lập tức!"
    st.session_state.last_explanation = None
    st.session_state.game_over = False
    st.session_state.victory = False

def restart_game():
    st.session_state.stage = 1
    st.session_state.q_index = 0
    st.session_state.hero_hp = 100
    st.session_state.boss_hp = 100
    st.session_state.score = 0
    st.session_state.combat_log = "⚔️ Hiệp sĩ đã hồi sinh! Hãy giải cứu Rồng thần khỏi Công Chúa Độc Ác!"
    st.session_state.last_explanation = None
    st.session_state.game_over = False
    st.session_state.victory = False

# ================= GIAO DIỆN CHÍNH =================
st.title("🐉 Hiệp Sĩ Giải Cứu Rồng Khỏi Công Chúa Độc Ác")

current_stage = STAGES[st.session_state.stage]
bg_b64 = get_image_base64(current_stage["bg_files"])
bg_style = f"background-image: url('{bg_b64}');" if bg_b64 else f"background: {current_stage['bg_fallback_gradient']};"

# ---------------- MÀN HÌNH CHIẾN THẮNG (CUTSCENE PHÁ ĐẢO) ----------------
if st.session_state.victory:
    st.balloons()
    hero_html = render_sprite_html(HERO_FILES, "🤺")
    princess_html = render_sprite_html(STAGES[3]["boss_files"], "👸👑", extra_class="princess-blast-off")
    
    st.markdown(f"""
    <div class="battle-arena" style="{bg_style}">
        <div class="arena-overlay" style="text-align:center; padding: 25px;">
            <div class="stage-banner">🎉 ĐẠI THẮNG! GIẢI CỨU RỒNG THÀNH CÔNG! 🎉</div>
            <div style="margin: 15px 0;">
                <span class="dragon-fly-free">🐉✨</span>
            </div>
            <div style="display:flex; justify-content:space-around; align-items:center; margin-top:20px;">
                <div>
                    {hero_html}
                    <div style="font-weight:bold; color:#00e676; margin-top:8px;">Hiệp Sĩ Chiến Thắng!</div>
                </div>
                <div style="font-size:40px;">⚡⚔️💥</div>
                <div>
                    {princess_html}
                    <div style="font-weight:bold; color:#ff616f; margin-top:8px;">Công Chúa Bị Đánh Bay!</div>
                </div>
            </div>
            <p style="margin-top:20px; font-size:17px; color:#ffd700;">
                Xiềng xích đã vỡ! Công chúa độc ác bị đánh bay khỏi tòa tháp và Rồng thần đã tung cánh bay về bầu trời tự do!
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.success(f"🏆 Chúc mừng Hiệp Sĩ đã chinh phục toàn bộ 15 thử thách Toán học với số điểm tuyệt đối: **{st.session_state.score} EXP**!")
    if st.session_state.last_explanation:
        with st.expander("📖 Xem lại lời giải Câu 15", expanded=False):
            st.markdown(st.session_state.last_explanation)
    if st.button("🔄 Chơi lại từ đầu", type="primary"):
        restart_game()
        safe_rerun()
    st.stop()

# ---------------- MÀN HÌNH THẤT BẠI (BỊ LÍNH ĐÁNH CHẾT) ----------------
if st.session_state.game_over:
    dead_hero_html = render_sprite_html(HERO_FILES, "🤺", extra_class="dead-knight")
    
    st.markdown(f"""
    <div class="battle-arena" style="{bg_style}">
        <div class="arena-overlay" style="text-align:center; padding: 25px;">
            <div class="stage-banner" style="color:#ff4b4b;">💀 BẠN ĐÃ BỊ LÍNH CANH ĐÁNH GỤC! 💀</div>
            <div style="display:flex; justify-content:center; align-items:center; gap:25px; margin: 25px 0;">
                <div class="guard-attack-left">💂‍♂️⚔️</div>
                <div>{dead_hero_html}</div>
                <div class="guard-attack-right">⚔️💂‍♂️</div>
            </div>
            <p style="color:#ff8a8a; font-size:16px; font-weight:bold;">
                Do giải sai phép tính, đội lính canh của Công Chúa Độc Ác đã ập vào kết liễu Hiệp Sĩ!
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.error("💔 Nhiệm vụ giải cứu Rồng thất bại! Hãy xem kỹ lời giải bên dưới để phục thù nhé!")
    if st.session_state.last_explanation:
        with st.expander("📖 Bí kíp giải câu vừa trả lời sai", expanded=True):
            st.markdown(st.session_state.last_explanation)
    if st.button("🔄 Hồi sinh và Phục thù ngay!", type="primary"):
        restart_game()
        safe_rerun()
    st.stop()

# ---------------- MÀN HÌNH CHIẾN ĐẤU CHÍNH ----------------
current_q = current_stage["questions"][st.session_state.q_index]
hero_sprite_html = render_sprite_html(HERO_FILES, "🤺")
boss_sprite_html = render_sprite_html(current_stage["boss_files"], current_stage["boss_fallback"])

st.markdown(f"""
<div class="battle-arena" style="{bg_style}">
    <div class="arena-overlay">
        <div class="stage-banner">{current_stage["name"]}</div>
        <p style="text-align:center; font-size:14px; color:#e0e0e0; margin-bottom:12px;">
            <i>{current_stage["story"]}</i>
        </p>
        <div class="fighters-row">
            <div class="fighter-box">
                {hero_sprite_html}
                <div style="font-weight:bold; margin-top:8px;">Hiệp Sĩ Giải Cứu Rồng</div>
                <div class="hp-bar-bg">
                    <div class="hp-bar-fill-hero" style="width: {st.session_state.hero_hp}%;"></div>
                </div>
                <small>❤️ 1 Mạng Tử Chiến | EXP: {st.session_state.score}</small>
            </div>
            <div class="vs-badge">⚔️ VS ⚔️</div>
            <div class="fighter-box">
                {boss_sprite_html}
                <div style="font-weight:bold; margin-top:8px;">{current_stage["boss_name"]}</div>
                <div class="hp-bar-bg">
                    <div class="hp-bar-fill-boss" style="width: {st.session_state.boss_hp}%;"></div>
                </div>
                <small>HP Boss: {st.session_state.boss_hp}/100</small>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Nhật ký chiến đấu & lời giải câu trước
st.info(st.session_state.combat_log)
if st.session_state.last_explanation:
    with st.expander("📖 Xem lời giải chi tiết của đòn đánh vừa rồi", expanded=False):
        st.markdown(st.session_state.last_explanation)

# Hiển thị câu hỏi hiện tại
st.markdown(f"""
<div class="quest-card">
    <h4>📜 {current_q["title"]} (Câu {st.session_state.q_index + 1}/5 của Màn {st.session_state.stage})</h4>
    <p>{current_q["desc"]}</p>
</div>
""", unsafe_allow_html=True)

st.latex(current_q["latex"])

user_choice = st.radio(
    "Chọn chiêu thức giải toán (Lưu ý: Sai 1 câu sẽ bị lính đánh chết ngay!):",
    current_q["options"],
    key=f"radio_q_{current_q['id']}"
)

if st.button("⚡ Vung Kiếm Tấn Công!", type="primary"):
    st.session_state.last_explanation = f"**Đáp án đúng:** `{current_q['answer']}`\n\n**Lời giải chi tiết:** {current_q['explanation']}"
    
    if user_choice == current_q["answer"]:
        st.session_state.boss_hp -= 20
        st.session_state.score += 100
        st.session_state.combat_log = f"💥 ĐÒN CHÍ MẠNG! Bạn chém trúng {current_stage['boss_name']} gây 20 sát thương!"
        
        # Kiểm tra qua câu hoặc qua màn
        if st.session_state.q_index + 1 < len(current_stage["questions"]):
            st.session_state.q_index += 1
        else:
            if st.session_state.stage < 3:
                old_boss = current_stage["boss_name"]
                st.session_state.stage += 1
                st.session_state.q_index = 0
                st.session_state.boss_hp = 100
                st.session_state.combat_log = f"🔥 BẠN ĐÃ ĐÁNH BẠI {old_boss.upper()}! Tiến sang Màn {st.session_state.stage}!"
            else:
                st.session_state.victory = True
    else:
        # Trả lời sai 1 câu -> Bị lính đánh chết ngay lập tức
        st.session_state.hero_hp = 0
        st.session_state.game_over = True
    
    safe_rerun()
