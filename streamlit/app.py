import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Math Boss Battle 2D", page_icon="⚔️", layout="centered")

QUESTIONS = {
    1: [
        {"q": r"Câu 1: Giải phương trình $x^2 - 5x + 6 = 0$", "options": ["x=2 hoặc x=3", "x=-2 hoặc x=-3", "x=1 hoặc x=6", "x=0"], "ans": 0},
        {"q": r"Câu 2: Rút gọn $A = \frac{\sqrt{12}+\sqrt{27}-\sqrt{3}}{\sqrt{3}}$", "options": ["3", "4", "5", "sqrt(3)"], "ans": 1},
        {"q": r"Câu 3: Giải phương trình $\frac{2}{x-1}+\frac{1}{x+1}=1$", "options": ["x=0 hoặc x=3", "x=1 hoặc x=2", "x=3", "Vô nghiệm"], "ans": 0},
        {"q": r"Câu 4: Giải hệ $\begin{cases}2x+y=7\\x-y=2\end{cases}$", "options": ["(x=3, y=1)", "(x=1, y=3)", "(x=2, y=3)", "(x=4, y=-1)"], "ans": 0},
        {"q": r"Câu 5: HCN có chu vi 34cm, diện tích 60cm². Tính (Dài, Rộng)", "options": ["12cm và 5cm", "10cm và 6cm", "15cm và 4cm", "9cm và 8cm"], "ans": 0},
    ],import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Dũng Sĩ Toán Học - Đánh Boss LTV",
    page_icon="⚔️",
    layout="centered"
)

# ================= CSS 2D FANTASY RPG =================
st.markdown("""
<style>
.battle-arena {
    background: linear-gradient(180deg, #1a1c2e 0%, #2d1b4e 60%, #1e3c40 100%);
    border: 4px solid #ffd700;
    border-radius: 16px;
    padding: 25px;
    color: white;
    box-shadow: 0 8px 25px rgba(0,0,0,0.6);
    margin-bottom: 20px;
    position: relative;
    overflow: hidden;
}
.stage-banner {
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    color: #ffd700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 15px;
    text-shadow: 2px 2px 4px #000;
}
.fighters-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
}
.fighter-box {
    text-align: center;
    width: 42%;
    background: rgba(0, 0, 0, 0.35);
    padding: 15px;
    border-radius: 12px;
    border: 2px solid rgba(255, 255, 255, 0.15);
}
.sprite {
    font-size: 72px;
    line-height: 1.1;
    display: inline-block;
    animation: float 2.2s infinite ease-in-out;
}
.vs-badge {
    font-size: 32px;
    font-weight: 900;
    color: #ff4b4b;
    text-shadow: 0 0 10px #ff0000;
}
.hp-bar-bg {
    background: #333;
    border-radius: 8px;
    height: 18px;
    width: 100%;
    margin-top: 8px;
    overflow: hidden;
    border: 1px solid #fff;
}
.hp-bar-fill-hero {
    background: linear-gradient(90deg, #00e676, #66ffa6);
    height: 100%;
    transition: width 0.4s ease;
}
.hp-bar-fill-boss {
    background: linear-gradient(90deg, #ff1744, #ff616f);
    height: 100%;
    transition: width 0.4s ease;
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}
.quest-card {
    background: #262730;
    border-left: 6px solid #ffd700;
    padding: 18px;
    border-radius: 10px;
    color: #ffffff;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ================= DỮ LIỆU 3 MÀN CHƠI & 15 CÂU HỎI =================
STAGES = {
    1: {
        "name": "Màn 1: Khu Rừng Khởi Nguyên (Cơ bản)",
        "boss_name": "Goblin Đại Số",
        "boss_sprite": "👺",
        "questions": [
            {
                "id": 1,
                "title": "Câu 1: Giải phương trình bậc hai",
                "latex": r"x^2 - 5x + 6 = 0",
                "desc": "Tìm tập nghiệm của phương trình trên:",
                "options": ["x = 2 hoặc x = 3", "x = -2 hoặc x = -3", "x = 1 hoặc x = 6", "x = -1 hoặc x = 6"],
                "answer": "x = 2 hoặc x = 3",
                "explanation": r"Ta có: $x^2 - 5x + 6 = 0 \iff (x - 2)(x - 3) = 0 \iff x = 2$ hoặc $x = 3$."
            },
            {
                "id": 2,
                "title": "Câu 2: Rút gọn biểu thức chứa căn",
                "latex": r"A = \frac{\sqrt{12} + \sqrt{27} - \sqrt{3}}{\sqrt{3}}",
                "desc": "Giá trị rút gọn của biểu thức A là:",
                "options": ["4", "5", "3", "4√3"],
                "answer": "4",
                "explanation": r"Vì $\sqrt{12} = 2\sqrt{3}$ và $\sqrt{27} = 3\sqrt{3}$, nên $A = \frac{2\sqrt{3} + 3\sqrt{3} - \sqrt{3}}{\sqrt{3}} = \frac{4\sqrt{3}}{\sqrt{3}} = 4$."
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
                "explanation": r"Quy đồng khử mẫu: $2(x+1) + (x-1) = x^2 - 1 \iff x^2 - 3x - 2 = 0$. Ta có $\Delta = (-3)^2 - 4(1)(-2) = 17 > 0 \implies x = \frac{3 \pm \sqrt{17}}{2}$ (thỏa mãn ĐK)."
            },
            {
                "id": 4,
                "title": "Câu 4: Giải hệ phương trình bậc nhất hai ẩn",
                "latex": r"\begin{cases} 2x + y = 7 \\ x - y = 2 \end{cases}",
                "desc": "Cặp nghiệm (x; y) của hệ phương trình là:",
                "options": ["(3; 1)", "(2; 3)", "(4; -1)", "(3; -1)"],
                "answer": "(3; 1)",
                "explanation": r"Cộng từng vế hai phương trình: $3x = 9 \implies x = 3$. Thay $x = 3$ vào phương trình dưới: $3 - y = 2 \implies y = 1$. Vậy nghiệm là $(3; 1)$."
            },
            {
                "id": 5,
                "title": "Câu 5: Bài toán thực tế hình học",
                "latex": r"\text{Chu vi } = 34\text{ cm}, \quad \text{Diện tích } = 60\text{ cm}^2",
                "desc": "Tìm chiều dài và chiều rộng của hình chữ nhật:",
                "options": [
                    "Chiều dài 12 cm, chiều rộng 5 cm",
                    "Chiều dài 10 cm, chiều rộng 6 cm",
                    "Chiều dài 15 cm, chiều rộng 4 cm",
                    "Chiều dài 14 cm, chiều rộng 3 cm"
                ],
                "answer": "Chiều dài 12 cm, chiều rộng 5 cm",
                "explanation": r"Nửa chu vi là $34 : 2 = 17\text{ cm}$. Gọi hai kích thước là $a, b$ thì $a + b = 17$ và $ab = 60$. Theo định lý Vi-ét đảo, $a, b$ là nghiệm của $X^2 - 17X + 60 = 0 \implies X = 12$ hoặc $X = 5$."
            }
        ]
    },
    2: {
        "name": "Màn 2: Pháo Đài Tuyển Sinh Lớp 10 (Trung bình - Khó)",
        "boss_name": "Hiệp Sĩ Bóng Đêm",
        "boss_sprite": "👹",
        "questions": [
            {
                "id": 6,
                "title": "Câu 6: Phương trình bậc hai chứa tham số",
                "latex": r"x^2 - 2(m+1)x + m^2 + 1 = 0",
                "desc": "Tìm điều kiện của m để phương trình có hai nghiệm phân biệt:",
                "options": ["m > 0", "m ≥ 0", "m > -1", "m ≠ 0"],
                "answer": "m > 0",
                "explanation": r"Ta có $\Delta' = (m+1)^2 - (m^2 + 1) = m^2 + 2m + 1 - m^2 - 1 = 2m$. Để phương trình có hai nghiệm phân biệt thì $\Delta' > 0 \iff 2m > 0 \iff m > 0$."
            },
            {
                "id": 7,
                "title": "Câu 7: Giải phương trình bằng phương pháp đặt ẩn phụ",
                "latex": r"\frac{x+1}{x-2} + \frac{x-2}{x+1} = \frac{5}{2} \quad (x \ne 2,\ x \ne -1)",
                "desc": "Tập nghiệm S của phương trình trên là:",
                "options": ["S = {-4; 5}", "S = {4; -5}", "S = {1; 2}", "S = {-2; 5}"],
                "answer": "S = {-4; 5}",
                "explanation": r"Đặt $t = \frac{x+1}{x-2}$ ($t \ne 0$). Phương trình trở thành $t + \frac{1}{t} = \frac{5}{2} \iff 2t^2 - 5t + 2 = 0 \iff t = 2$ hoặc $t = \frac{1}{2}$. Với $t = 2 \implies x = 5$; với $t = \frac{1}{2} \implies x = -4$."
            },
            {
                "id": 8,
                "title": "Câu 8: Bài toán năng suất công việc",
                "latex": r"\begin{cases} \frac{1}{x} + \frac{1}{y} = \frac{1}{6} \\ \frac{5}{x} + \frac{4}{y} = \frac{3}{4} \end{cases}",
                "desc": "Hai người cùng làm một công việc thì xong trong 6 giờ. Nếu người 1 làm 5 giờ và người 2 làm 4 giờ thì được 3/4 công việc. Hỏi làm riêng một mình thì mỗi người mất bao lâu?",
                "options": [
                    "Người 1: 12 giờ, Người 2: 12 giờ",
                    "Người 1: 10 giờ, Người 2: 15 giờ",
                    "Người 1: 8 giờ, Người 2: 24 giờ",
                    "Người 1: 9 giờ, Người 2: 18 giờ"
                ],
                "answer": "Người 1: 12 giờ, Người 2: 12 giờ",
                "explanation": r"Từ $\frac{1}{x} + \frac{1}{y} = \frac{1}{6} \implies \frac{4}{x} + \frac{4}{y} = \frac{2}{3}$. Lấy phương trình hai trừ đi ta được: $\frac{1}{x} = \frac{3}{4} - \frac{2}{3} = \frac{1}{12} \implies x = 12$ giờ, suy ra $y = 12$ giờ."
            },
            {
                "id": 9,
                "title": "Câu 9: Hệ thức lượng trong tam giác vuông",
                "latex": r"\triangle ABC \text{ vuông tại } A,\ AH \perp BC,\ AB = 6\text{ cm},\ AC = 8\text{ cm}",
                "desc": "Tính lần lượt độ dài các đoạn thẳng BC, AH, BH, CH:",
                "options": [
                    "BC = 10 cm; AH = 4,8 cm; BH = 3,6 cm; CH = 6,4 cm",
                    "BC = 10 cm; AH = 4,5 cm; BH = 3,5 cm; CH = 6,5 cm",
                    "BC = 14 cm; AH = 4,8 cm; BH = 6 cm; CH = 8 cm",
                    "BC = 10 cm; AH = 5 cm; BH = 3,6 cm; CH = 6,4 cm"
                ],
                "answer": "BC = 10 cm; AH = 4,8 cm; BH = 3,6 cm; CH = 6,4 cm",
                "explanation": r"Theo Pytago: $BC = \sqrt{6^2 + 8^2} = 10\text{ cm}$. Hệ thức lượng: $AH = \frac{AB \cdot AC}{BC} = 4,8\text{ cm}$; $BH = \frac{AB^2}{BC} = 3,6\text{ cm}$; $CH = 10 - 3,6 = 6,4\text{ cm}$."
            },
            {
                "id": 10,
                "title": "Câu 10: Sự tương giao giữa Parabol (P) và đường thẳng d",
                "latex": r"(P): y = x^2 \quad \text{và} \quad d: y = (m-1)x + 2 \quad (x_1^2 + x_2^2 = 10)",
                "desc": "Tìm m để d cắt (P) tại hai điểm phân biệt thỏa mãn điều kiện trên:",
                "options": [
                    "m = 1 ± √6",
                    "m = 1 ± √10",
                    "m = -1 ± √6",
                    "m = 2 hoặc m = -4"
                ],
                "answer": "m = 1 ± √6",
                "explanation": r"Phương trình hoành độ giao điểm: $x^2 - (m-1)x - 2 = 0$ luôn có 2 nghiệm phân biệt vì $ac = -2 < 0$. Theo Vi-ét: $x_1 + x_2 = m - 1$ và $x_1 x_2 = -2$. Ta có $x_1^2 + x_2^2 = (x_1+x_2)^2 - 2x_1 x_2 = (m-1)^2 + 4 = 10 \iff (m-1)^2 = 6 \iff m = 1 \pm \sqrt{6}$."
            }
        ]
    },
    3: {
        "name": "Màn 3: Đỉnh Núi Rồng Chuyên Lương Thế Vinh (Khó - Nâng cao)",
        "boss_name": "Rồng Hắc Ám LTV",
        "boss_sprite": "🐉",
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
                "explanation": r"Chuyển vế: $\sqrt{2x-1} = 4 - \sqrt{x+5}$ (với $\frac{1}{2} \le x \le 11$). Bình phương 2 vế rút gọn được $8\sqrt{x+5} = 22 - x$. Bình phương lần 2: $64(x+5) = (22-x)^2 \iff x^2 - 108x + 164 = 0$. Giải ra $x = 54 - 8\sqrt{43}$ (nhận) và $x = 54 + 8\sqrt{43}$ (loại vì lớn hơn 11)."
            },
            {
                "id": 12,
                "title": "Câu 12: Bất đẳng thức Cauchy-Schwarz",
                "latex": r"a, b > 0,\ a + b = 1. \quad \text{Chứng minh: } \frac{1}{a} + \frac{1}{b} \ge 4",
                "desc": "Dấu bằng của bất đẳng thức xảy ra khi nào?",
                "options": [
                    "a = b = 1/2",
                    "a = b = 1",
                    "a = 1/4 và b = 3/4",
                    "a = b = 2"
                ],
                "answer": "a = b = 1/2",
                "explanation": r"Áp dụng BĐT Cauchy-Schwarz dạng phân thức: $\frac{1}{a} + \frac{1}{b} \ge \frac{(1+1)^2}{a+b} = \frac{4}{1} = 4$. Dấu bằng xảy ra khi và chỉ khi $a = b = \frac{1}{2}$."
            },
            {
                "id": 13,
                "title": "Câu 13: Phương trình nghiệm nguyên",
                "latex": r"x^2 - y^2 = 21 \quad (x, y \in \mathbb{Z})",
                "desc": "Tất cả các cặp số nguyên dương (x; y) thỏa mãn phương trình là:",
                "options": [
                    "(11; 10), (5; 2) cùng các cặp đổi dấu âm tương ứng (tổng 8 cặp)",
                    "(11; 10) và (7; 3)",
                    "(5; 2) và (6; 3)",
                    "Chỉ có duy nhất (5; 2)"
                ],
                "answer": "(11; 10), (5; 2) cùng các cặp đổi dấu âm tương ứng (tổng 8 cặp)",
                "explanation": r"Đưa về phương trình tích: $(x - y)(x + y) = 21$. Xét các ước nguyên của 21 là $\{\pm 1; \pm 3; \pm 7; \pm 21\}$, ta tìm được 8 cặp nghiệm nguyên: $(\pm 11; \pm 10)$ và $(\pm 5; \pm 2)$."
            },
            {
                "id": 14,
                "title": "Câu 14: Hình học nâng cao - Tứ giác nội tiếp & Trực tâm",
                "latex": r"\triangle ABC \text{ nhọn, đường cao } BE, CF \text{ cắt nhau tại } H",
                "desc": "Chọn khẳng định ĐÚNG về tứ giác AEHF và đường thẳng AH:",
                "options": [
                    "AEHF nội tiếp đường tròn đường kính AH; AH ⊥ BC (và AH ⊥ EF khi ΔABC cân tại A)",
                    "AEHF nội tiếp đường tròn đường kính EF; AH đi qua trung điểm BC",
                    "AEHF không nội tiếp; AH là phân giác góc A",
                    "AEHF nội tiếp đường tròn đường kính BC"
                ],
                "answer": "AEHF nội tiếp đường tròn đường kính AH; AH ⊥ BC (và AH ⊥ EF khi ΔABC cân tại A)",
                "explanation": r"a) Ta có $\widehat{AEH} = \widehat{AFH} = 90^\circ \implies \widehat{AEH} + \widehat{AFH} = 180^\circ$ nên tứ giác $AEHF$ nội tiếp đường tròn đường kính $AH$. b) Vì $H$ là trực tâm $\triangle ABC$ nên $AH \perp BC$ (ngoài ra $OA \perp EF$ với $O$ là tâm ngoại tiếp, và $AH \perp EF$ khi $\triangle ABC$ cân tại $A$)."
            },
            {
                "id": 15,
                "title": "Câu 15: Bài toán cực trị đại số",
                "latex": r"x, y > 0,\ xy = 1. \quad \text{Tìm GTNN của } P = x^2 + y^2 + x + y",
                "desc": "Giá trị nhỏ nhất (Min) của biểu thức P và điểm rơi là:",
                "options": [
                    "Min P = 4 khi x = y = 1",
                    "Min P = 2 khi x = y = 1",
                    "Min P = 6 khi x = y = 1",
                    "Min P = 4 khi x = 2, y = 1/2"
                ],
                "answer": "Min P = 4 khi x = y = 1",
                "explanation": r"Áp dụng BĐT AM-GM (Cauchy) cho hai số dương: $x^2 + y^2 \ge 2xy = 2$ và $x + y \ge 2\sqrt{xy} = 2$. Cộng vế theo vế ta được $P \ge 2 + 2 = 4$. Dấu bằng xảy ra khi và chỉ khi $x = y = 1$."
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
    st.session_state.combat_log = "⚔️ Cuộc chiến bắt đầu! Hãy giải toán để tung đòn tấn công Boss!"
    st.session_state.last_explanation = None
    st.session_state.game_over = False
    st.session_state.victory = False

def restart_game():
    st.session_state.stage = 1
    st.session_state.q_index = 0
    st.session_state.hero_hp = 100
    st.session_state.boss_hp = 100
    st.session_state.score = 0
    st.session_state.combat_log = "⚔️ Cuộc chiến bắt đầu lại! Chúc Dũng Sĩ may mắn!"
    st.session_state.last_explanation = None
    st.session_state.game_over = False
    st.session_state.victory = False

# ================= GIAO DIỆN CHÍNH =================
st.title("⚔️ Dũng Sĩ Toán Học: Chinh Phục Đỉnh LTV")

# Kiểm tra trạng thái thắng / thua
if st.session_state.victory:
    st.balloons()
    st.success("🏆 CHÚC MỪNG DŨNG SĨ! Bạn đã đánh bại Rồng Hắc Ám LTV và phá đảo cả 3 màn chơi!")
    st.metric("Tổng điểm vinh quang", f"{st.session_state.score} EXP")
    if st.button("🔄 Chơi lại từ đầu"):
        restart_game()
        st.rerun()
    st.stop()

if st.session_state.game_over:
    st.error("💀 Dũng Sĩ đã kiệt sức! Hãy ôn tập kỹ lời giải và thử sức lại nhé!")
    if st.button("🔄 Phục hồi và Chơi lại"):
        restart_game()
        st.rerun()
    st.stop()

current_stage = STAGES[st.session_state.stage]
current_q = current_stage["questions"][st.session_state.q_index]

# Khung cảnh chiến đấu 2D
st.markdown(f"""
<div class="battle-arena">
    <div class="stage-banner">{current_stage["name"]}</div>
    <div class="fighters-row">
        <div class="fighter-box">
            <div class="sprite">🧙‍♂️</div>
            <div style="font-weight:bold; margin-top:5px;">Dũng Sĩ Toán Học</div>
            <div class="hp-bar-bg">
                <div class="hp-bar-fill-hero" style="width: {st.session_state.hero_hp}%;"></div>
            </div>
            <small>HP: {st.session_state.hero_hp}/100 | EXP: {st.session_state.score}</small>
        </div>
        <div class="vs-badge">VS</div>
        <div class="fighter-box">
            <div class="sprite">{current_stage["boss_sprite"]}</div>
            <div style="font-weight:bold; margin-top:5px;">{current_stage["boss_name"]}</div>
            <div class="hp-bar-bg">
                <div class="hp-bar-fill-boss" style="width: {st.session_state.boss_hp}%;"></div>
            </div>
            <small>HP: {st.session_state.boss_hp}/100</small>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Nhật ký chiến đấu
st.info(st.session_state.combat_log)
if st.session_state.last_explanation:
    with st.expander("📖 Xem lời giải chi tiết của đòn đánh vừa rồi", expanded=True):
        st.markdown(st.session_state.last_explanation)

# Hiển thị câu hỏi hiện tại
st.markdown(f"""
<div class="quest-card">
    <h4>📜 {current_q["title"]}</h4>
    <p>{current_q["desc"]}</p>
</div>
""", unsafe_allow_html=True)

st.latex(current_q["latex"])

with st.form(key=f"form_q_{current_q['id']}"):
    user_choice = st.radio(
        "Chọn tuyệt chiêu (Đáp án của bạn):",
        current_q["options"],
        index=None
    )
    submit_btn = st.form_submit_button("⚡ Tung Tuyệt Chiêu!")

    if submit_btn:
        if user_choice is None:
            st.warning("⚠️ Bạn hãy chọn một đáp án trước khi tung chiêu nhé!")
        else:
            st.session_state.last_explanation = f"**Đáp án đúng:** `{current_q['answer']}`\n\n**Giải thích:** {current_q['explanation']}"
            if user_choice == current_q["answer"]:
                st.session_state.boss_hp -= 20
                st.session_state.score += 100
                st.session_state.combat_log = f"💥 CHÍNH XÁC! Bạn gây 20 sát thương chuẩn lên {current_stage['boss_name']}!"
                
                # Chuyển câu hoặc chuyển màn
                if st.session_state.q_index + 1 < len(current_stage["questions"]):
                    st.session_state.q_index += 1
                else:
                    if st.session_state.stage < 3:
                        st.session_state.stage += 1
                        st.session_state.q_index = 0
                        st.session_state.boss_hp = 100
                        st.session_state.combat_log = f"🎉 BẠN ĐÃ HẠ GỤC {current_stage['boss_name']}! Tiến vào Màn {st.session_state.stage}!"
                    else:
                        st.session_state.victory = True
            else:
                st.session_state.hero_hp -= 25
                st.session_state.combat_log = f"🛡️ CHỆCH MỤC TIÊU! {current_stage['boss_name']} phản đòn khiến bạn mất 25 HP! Hãy xem lời giải bên dưới và thử lại!"
                if st.session_state.hero_hp <= 0:
                    st.session_state.game_over = True
            
            st.rerun()

    2: [
        {"q": r"Câu 6: Tìm m để $x^2-2(m+1)x+m^2+1=0$ có 2 nghiệm phân biệt", "options": ["m > 0", "m > -1/2", "m < 0", "Mọi m"], "ans": 1},
        {"q": r"Câu 7: Giải $\frac{x+1}{x-2}+\frac{x-2}{x+1}=\frac{5}{2}$", "options": ["x=5 hoặc x=-4", "x=2 hoặc x=-1", "x=0", "x=3"], "ans": 0},
        {"q": r"Câu 8: Hai người chung công việc mất 6h. Người 1 làm 5h, người 2 làm 4h được 3/4 việc. Thời gian 1 mình?", "options": ["Người I: 10h, Người II: 15h", "Người I: 12h, Người II: 12h", "Người I: 8h, Người II: 16h", "Khác"], "ans": 0},
        {"q": r"Câu 9: $\Delta ABC$ vuông tại A, AH cao. AB=6, AC=8. Tính BC & AH", "options": ["BC=10cm, AH=4.8cm", "BC=10cm, AH=5cm", "BC=12cm, AH=4.8cm", "BC=14cm, AH=6cm"], "ans": 0},
        {"q": r"Câu 10: Tìm m để $(d): y=(m-1)x+2$ cắt $(P): y=x^2$ thỏa $x_1^2+x_2^2=10$", "options": ["m=3 hoặc m=-1", "m=2", "m=0", "m=-3"], "ans": 0},
    ],
    3: [
        {"q": r"Câu 11: Giải phương trình $\sqrt{x+5}+\sqrt{2x-1}=4$", "options": ["x = 4", "x = 1", "x = 5", "Vô nghiệm"], "ans": 0},
        {"q": r"Câu 12: Cho a,b > 0 và a+b=1. Giá trị nhỏ nhất của $\frac{1}{a}+\frac{1}{b}$ là?", "options": ["4", "2", "8", "1"], "ans": 0},
        {"q": r"Câu 13: Cặp số nguyên (x,y) thỏa $x^2-y^2=21$ có số lượng là:", "options": ["8 cặp", "4 cặp", "2 cặp", "12 cặp"], "ans": 0},
        {"q": r"Câu 14: Tam giác ABC nhọn, đường cao BE, CF cắt tại H. Tứ giác AEHF là?", "options": ["Tứ giác nội tiếp", "Hình bình hành", "Hình thoi", "Hình thang"], "ans": 0},
        {"q": r"Câu 15: Cho x,y > 0 và xy=1. Giá trị nhỏ nhất của $P=x^2+y^2+x+y$ là?", "options": ["4", "2", "6", "2sqrt(2)"], "ans": 0},
    ]
}

# Mốc máu theo yêu cầu: Boss 1 = 3 HP, Boss 2 = 5 HP, Boss 3 = 7 HP
BOSS_HP_MAP = {1: 3, 2: 5, 3: 7}
boss_names = ["1. Sát Thủ Áo Đen", "2. Phù Thủy Xương", "3. Nữ Hoàng Bóng Tối"]

# Khởi tạo trạng thái game
if 'stage' not in st.session_state: st.session_state.stage = 1
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'player_hp' not in st.session_state: st.session_state.player_hp = 10
if 'boss_hp' not in st.session_state: st.session_state.boss_hp = BOSS_HP_MAP[1]
if 'last_result' not in st.session_state: st.session_state.last_result = 'none'

st.title("⚔️ Math Boss Battle 2D - Fantasy")

# Render khung canvas 2D
max_bhp = BOSS_HP_MAP[st.session_state.stage]
iframe_url = f"game_canvas.html?stage={st.session_state.stage}&php={st.session_state.player_hp}&bhp={st.session_state.boss_hp}&max_bhp={max_bhp}&result={st.session_state.last_result}"
components.iframe(iframe_url, height=280)

st.subheader(f"🛡️ Màn {st.session_state.stage}: {boss_names[st.session_state.stage-1]}")
curr_q = QUESTIONS[st.session_state.stage][st.session_state.q_idx]

st.latex(curr_q["q"])
choice = st.radio("Chọn đáp án đúng:", curr_q["options"], key=f"ans_{st.session_state.stage}_{st.session_state.q_idx}")

if st.button("⚔️ Tung đòn giải toán!"):
    selected_idx = curr_q["options"].index(choice)
    if selected_idx == curr_q["ans"]:
        st.session_state.last_result = 'correct'
        st.success("🎯 Chính xác! Boss mất 1 HP!")
        st.session_state.boss_hp -= 1
    else:
        st.session_state.last_result = 'wrong'
        st.error("💥 Sai rồi! Bạn mất 1 HP!")
        st.session_state.player_hp -= 1

    # Kiểm tra điều kiện thắng/thua
    if st.session_state.boss_hp <= 0:
        st.balloons()
        if st.session_state.stage < 3:
            st.session_state.stage += 1
            st.session_state.q_idx = 0
            st.session_state.boss_hp = BOSS_HP_MAP[st.session_state.stage]
            st.success(f"🏆 Đã hạ gục Boss Màn {st.session_state.stage-1}! Chuyển sang Màn {st.session_state.stage}!")
        else:
            st.title("🎉 CHÚC MỪNG BẠN ĐÃ ĐÁNH BẠI NỮ HOÀNG & PHÁ ĐẢO TOÀN BỘ GAME!")
    elif st.session_state.player_hp <= 0:
        st.error("💀 BẠN ĐÃ CẠN MÁU! Hãy tải lại trang để chơi lại từ đầu.")
    else:
        st.session_state.q_idx = (st.session_state.q_idx + 1) % len(QUESTIONS[st.session_state.stage])
    st.rerun()
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <style>
    body {
      margin: 0;
      background-color: #0b091a;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      overflow: hidden;
    }
    canvas {
      border: 4px solid #ff8906;
      border-radius: 12px;
      box-shadow: 0 0 25px rgba(255, 137, 6, 0.4);
      background: #12121a;
    }
  </style>
</head>
<body>
  <canvas id="gameWorld" width="700" height="350"></canvas>
  <script>
    const canvas = document.getElementById('gameWorld');
    const ctx = canvas.getContext('2d');

    const params = new URLSearchParams(window.location.search);
    const stage = parseInt(params.get('stage')) || 1;
    const playerHp = parseInt(params.get('php')) || 10;
    const bossHp = parseInt(params.get('bhp')) || 3;
    const maxBossHp = parseInt(params.get('max_bhp')) || 3;
    const actionState = params.get('result') || 'idle'; // 'idle', 'player_attack', 'boss_attack'

    const bossNames = ["1. Sát Thủ Áo Đen", "2. Phù Thủy Xương", "3. Nữ Hoàng Bóng Tối"];

    // Load hình ảnh nhân vật & boss từ GitHub repo
    const playerImg = new Image(); playerImg.src = "nhân vật chính.jpg";
    const bossImgs = [new Image(), new Image(), new Image()];
    bossImgs[0].src = "boss 1.jpg";
    bossImgs[1].src = "boss 2.jpg";
    bossImgs[2].src = "boss 3.jpg";

    let pCols = 5, pRows = 4;
    let pFrameW = 0, pFrameH = 0;
    let animFrame = 0;

    Promise.all([
      new Promise(res => playerImg.onload = res),
      new Promise(res => bossImgs[0].onload = res),
      new Promise(res => bossImgs[1].onload = res),
      new Promise(res => bossImgs[2].onload = res)
    ]).then(() => {
      pFrameW = playerImg.width / pCols;
      pFrameH = playerImg.height / pRows;
      setInterval(renderWorld, 100);
    });

    // Vẽ thế giới 2D theo bối cảnh từng màn
    fnMapBackground = () => {
      if (stage === 1) {
        // Màn 1: Khu rừng / Ngục tối u tối
        ctx.fillStyle = "#161622"; ctx.fillRect(0, 0, 700, 350);
        ctx.fillStyle = "#1e1e2f"; // Các trụ đá background
        ctx.fillRect(80, 50, 40, 220); ctx.fillRect(550, 50, 50, 220);
        ctx.fillStyle = "#0f0f14"; ctx.fillRect(0, 270, 700, 80); // Sàn đất
      } else if (stage === 2) {
        // Màn 2: Hang động nham thạch lửa
        let grad = ctx.createLinearGradient(0, 0, 0, 350);
        grad.addColorStop(0, "#2c0b0e"); grad.addColorStop(1, "#120304");
        ctx.fillStyle = grad; ctx.fillRect(0, 0, 700, 350);
        // Nham thạch chảy bên dưới
        ctx.fillStyle = "#ff3800"; ctx.fillRect(0, 310, 700, 40);
        ctx.fillStyle = "#ffa200"; ctx.fillRect(0, 300, 700, 10);
        ctx.fillStyle = "#1a0505"; ctx.fillRect(0, 270, 700, 35); // Sàn đá hang
      } else {
        // Màn 3: Lâu đài bầu trời của Nữ Hoàng
        let grad = ctx.createLinearGradient(0, 0, 0, 350);
        grad.addColorStop(0, "#1f1035"); grad.addColorStop(1, "#43285c");
        ctx.fillStyle = grad; ctx.fillRect(0, 0, 700, 350);
        // Cột cẩm thạch hoàng gia
        ctx.fillStyle = "#2d1647"; ctx.fillRect(100, 30, 30, 240); ctx.fillRect(570, 30, 30, 240);
        ctx.fillStyle = "#140a21"; ctx.fillRect(0, 270, 700, 80); // Sàn hoa cương
      }
      // Đường ranh giới sàn 2D
      ctx.strokeStyle = "#ff8906"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(0, 270); ctx.lineTo(700, 270); ctx.stroke();
    }

    function renderWorld() {
      ctx.clearRect(0, 0, 700, 350);
      fnMapBackground();

      // Tọa độ 2D của nhân vật & boss
      let pX = 120, pY = 180;
      let bX = 500, bY = 165;

      // Xử lý hiệu ứng hành động trong thế giới 2D
      if (actionState === 'player_attack') {
        pX += 60; // Nhân vật lao lên tấn công
        if (stage === 1) {
          // Hiệu ứng đấm / chém cận chiến
          ctx.fillStyle = "#00ffff"; ctx.beginPath(); ctx.arc(pX + 50, pY + 30, 25, 0, Math.PI*2); ctx.fill();
        } else if (stage === 2) {
          // Hiệu ứng chưởng nước bay về phía boss
          ctx.fillStyle = "#00b4d8"; ctx.beginPath(); ctx.arc(pX + 80, pY + 30, 15, 0, Math.PI*2); ctx.fill();
          ctx.fillStyle = "#90e0ef"; ctx.beginPath(); ctx.arc(pX + 90, pY + 30, 8, 0, Math.PI*2); ctx.fill();
        } else if (stage === 3) {
          // Triệu hồi Boss 1 & Boss 2 lên đánh Nữ Hoàng
          if (bossImgs[0].complete) ctx.drawImage(bossImgs[0], 380, 175, 55, 90);
          if (bossImgs[1].complete) ctx.drawImage(bossImgs[1], 435, 170, 55, 90);
        }
      } else if (actionState === 'boss_attack') {
        if (stage === 1) {
          bX -= 40; // Sát thủ lao tới chém nhân vật
        } else if (stage === 2) {
          // Phù thủy xương tung cầu lửa bay vào nhân vật
          ctx.fillStyle = "#ff4800"; ctx.beginPath(); ctx.arc(320, 200, 20, 0, Math.PI*2); ctx.fill();
          ctx.fillStyle = "#ffdd00"; ctx.beginPath(); ctx.arc(315, 200, 10, 0, Math.PI*2); ctx.fill();
        } else if (stage === 3) {
          // Nữ hoàng triệu hồi sét giáng từ trên trời xuống nhân vật
          ctx.strokeStyle = "#ffff00"; ctx.lineWidth = 5;
          ctx.beginPath(); ctx.moveTo(150, 0); ctx.lineTo(135, 120); ctx.lineTo(160, 190); ctx.lineTo(145, 270); ctx.stroke();
        }
      }

      // 1. Vẽ Nhân vật chính (Player 2D)
      if (playerImg.complete && pFrameW > 0) {
        let pRow = 0; // Đứng yên
        if (actionState === 'player_attack') pRow = 2; // Động tác đánh
        else if (actionState === 'boss_attack') pRow = 1; // Bị tấn công / né

        let srcX = (animFrame % pCols) * pFrameW;
        let srcY = pRow * pFrameH;
        ctx.drawImage(playerImg, srcX, srcY, pFrameW, pFrameH, pX, pY, 60, 90);
        animFrame++;
      }

      // 2. Vẽ Boss 2D tương ứng màn
      let currentBoss = bossImgs[stage - 1];
      if (currentBoss.complete) {
        ctx.drawImage(currentBoss, bX, bY, 75, 105);
      }

      // 3. Giao diện HUD Thanh Máu RPG 2D trên màn hình game
      // HP Player (10 máu)
      ctx.fillStyle = "rgba(0,0,0,0.7)"; ctx.fillRect(20, 15, 200, 30);
      ctx.strokeStyle = "#ff8906"; ctx.lineWidth = 2; ctx.strokeRect(20, 15, 200, 30);
      ctx.fillStyle = "#ff4d4d"; ctx.fillRect(25, 20, (playerHp / 10) * 190, 20);
      ctx.fillStyle = "#ffffff"; ctx.font = "bold 13px monospace";
      ctx.fillText(`Hiệp Sĩ: ${playerHp}/10 HP`, 40, 32);

      // HP Boss (Biến động theo từng màn: 3, 5, 7 máu)
      ctx.fillStyle = "rgba(0,0,0,0.7)"; ctx.fillRect(480, 15, 200, 30);
      ctx.strokeStyle = "#e53170"; ctx.lineWidth = 2; ctx.strokeRect(480, 15, 200, 30);
      ctx.fillStyle = "#00ff88"; ctx.fillRect(485, 20, (bossHp / maxBossHp) * 190, 20);
      ctx.fillStyle = "#ffffff";
      ctx.fillText(`${bossNames[stage - 1]}: ${bossHp}/${maxBossHp}`, 495, 32);
    }
  </script>
</body>
</html>
