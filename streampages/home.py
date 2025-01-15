import streamlit as st

def home_page():
  # --- Header Section ---
    st.title(":first_place_medal: 모자라지만 착한 사람들(1조)")
    st.subheader("간단한 사이트 구조 설명")
    st.markdown("""
    <div style='text-align: justify; font-size: 18px;'>
    [News] 네이버 뉴스 데이터를 기반으로 생성된 워드 클라우드를 통해 최신 트렌드를 시각적으로 분석할 수 있습니다. 
    또한, 언급량이 가장 높은 5가지 키워드와 관련된 기사를 제공하여 심층적인 정보 탐색이 가능합니다. 
    이를 통해 사용자 여러분은 현재 이슈에 대한 통찰력을 얻고, 관련 뉴스를 손쉽게 확인할 수 있습니다.<br><br>
    [U.S. Stock] 미국을 대표하는 주요 산업 지수인 S&P 500, NASDAQ, 다우 존스를 다양한 시각화 그래프를 통해 분석합니다. 
    각 지수의 변화 추세와 상관관계를 시각적으로 표현하여 투자자 여러분이 시장의 흐름을 한눈에 이해할 수 있도록 돕습니다.
    </div>
    """, unsafe_allow_html=True)
    # --- Key Features Section ---
    st.markdown("## 🧑‍🧑‍🧒‍🧒 팀원 소개")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("### 🕵🏻‍♂️ 허 용")
        st.write("110453815234 신한 (많이 급해요)")
    with col2:
        st.markdown("### 🧙‍♂️ 박수빈")
        st.write("영파여자고등학교 밴드동아리 'mute' 출신(박수 담당)")
    with col3:
        st.markdown("### 🦸 이현승")
        st.write("팀원들 감정 쓰레기통")
    with col4:
        st.markdown("### 🧟‍♀️ 조서형")
        st.write("취미가 데드리프트")

    # --- Footer ---
    st.markdown("""
    <hr>
    <div style='text-align: center; font-size: 14px;'>
        © 2025 Dumb but kind Association | All Rights Reserved
    </div>
    """, unsafe_allow_html=True)

