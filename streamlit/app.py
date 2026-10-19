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
    100% { transform: translateX(10
