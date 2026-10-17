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
