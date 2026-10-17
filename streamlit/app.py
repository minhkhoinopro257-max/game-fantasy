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
    ],
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
