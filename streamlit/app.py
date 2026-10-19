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
    font-size: 32px;
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

/* Hoạt họa Game Over: Lính canh lao vào đánh gục Main */
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
        "story": "Tên Killer bất ngờ chặn đường!",
        "boss_name": "Killer",
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
                "answer": "Chiều dài
