import streamlit as st
import time
from streamlit_autorefresh import st_autorefresh

# 페이지 레이아웃 세팅
st.set_page_config(page_title="보건실 예약 키오스크 by 딍굴딍굴", layout="wide")

# 세션 상태에 예약 리스트 초기화
if 'reservations' not in st.session_state:
    st.session_state.reservations = []

st.markdown("<h1 style='text-align: center; color: #4CAF50; font-size:60px;'>🏥 보건실 예약 키오스크</h1>", unsafe_allow_html=True)

st.markdown("---")

# 입력 폼
with st.container():
    st.markdown("<h2 style='text-align: center; font-size:40px;'>📋 학생 예약</h2>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        grade = st.number_input("학년", min_value=1, max_value=6, step=1, format="%d")
    with col2:
        class_num = st.number_input("반", min_value=1, max_value=10, step=1, format="%d")
    with col3:
        student_num = st.number_input("번호", min_value=1, max_value=30, step=1, format="%d")
    with col4:
        name = st.text_input("이름")

    if st.button("✅ 예약하기", use_container_width=True):
        if name.strip() == "":
            st.warning("이름을 입력하세요!")
        else:
            new_reservation = {
                'grade': grade,
                'class': class_num,
                'number': student_num,
                'name': name
            }
            st.session_state.reservations.append(new_reservation)
            st.success(f"{grade}학년 {class_num}반 {student_num}번 {name} 예약 완료!")

st.markdown("---")

# 예약 리스트 표시
st.markdown("<h2 style='text-align: center; font-size:40px;'>📝 현재 대기자 명단</h2>", unsafe_allow_html=True)
if len(st.session_state.reservations) > 0:
    for i, r in enumerate(st.session_state.reservations):
        st.markdown(
            f"""
            <div style="border: 2px solid #4CAF50; border-radius: 20px; padding: 15px; margin-bottom: 10px; background-color: #f0fff0; font-size:30px;">
            {i+1}번째 👉 {r['grade']}학년 {r['class']}반 {r['number']}번 {r['name']}
            </div>
            """, 
            unsafe_allow_html=True
        )
else:
    st.markdown("<p style='text-align:center; font-size:30px;'>현재 예약된 학생이 없습니다.</p>", unsafe_allow_html=True)

st.markdown("---")

# 입장 처리
st.markdown("<h2 style='text-align: center; font-size:40px;'>🚪 입장 버튼</h2>", unsafe_allow_html=True)
if st.button("▶️ 다음 학생 입장", use_container_width=True):
    if len(st.session_state.reservations) > 0:
        entered_student = st.session_state.reservations.pop(0)
        st.success(f"{entered_student['grade']}학년 {entered_student['class']}반 {entered_student['number']}번 {entered_student['name']} 학생 입장 완료!")
    else:
        st.warning("현재 대기 중인 학생이 없습니다.")

# 자동 새로고침 기능 (5초마다 새로고침)
st_autorefresh(interval=5000, key="auto_refresh")
time.sleep(0.1)  # 부하 방지용 살짝 지연

