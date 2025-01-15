import streamlit as st
from utils.graph import *
from utils.crawl import infos # 최신의 해외 증시를 불러옴

def sp500_page():
    infos()
    load_data = load_stock_data()
    data = load_data['S&P 500']
    st.title("S&P 500")
    #두개의 열 생성
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**관련 정보**")  # 볼드체 제목 추가
        st.markdown("거래소: Standard & Poor's Corp Indices  \n"
                    "기준통화: USD  \n"
                    "거래시간(한국시간 기준): 23:30 - 06:00")
    with col2:
        st.markdown("**지수 설명**") # 볼드체 제목 추가
        st.write("미국의 국제신용평가기관인 S&P에서 작성하는 주가 지수로, 뉴욕증권거래소에 상장된 500개의 우량종목으로 이루어진 지수")
    with col3:
        st.metric(label="**전일 종가**", value=data[0]["종가"], delta=data[0]["전일대비"])
    

    option = st.selectbox(
        "그래프 옵션 변경:",
        ["각 지수별 종가 비교","최근 1년: 주간 가격 변동", '최근 12주: 주간 가격 변동', '최근 40일간의 캔들 차트', "종가동향"]
    )
    if option == "각 지수별 종가 비교":
        JGBG(load_data)
    elif option == "최근 1년: 주간 가격 변동":
        candle_year(data)
    elif option == "최근 12주: 주간 가격 변동":
        candle_week(data)
    elif option == '최근 40일간의 캔들 차트':
        candle_day(data)
    elif option == "종가동향":
        JGDH(data)

def nasdaq_page():
    infos()
    st.title("나스닥 종합")
    load_data = load_stock_data()
    data = load_data['나스닥 종합']
    #두개의 열 생성
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**관련 정보**")  # 볼드체 제목 추가
        st.markdown("거래소: NASDAQ Stock Market  \n"
                    "기준통화: USD  \n"
                    "거래시간(한국시간 기준): 23:30 - 06:00")
    with col2:
        st.markdown("**지수 설명**") # 볼드체 제목 추가
        st.write("하이테크·중소기업의 주식을 장외에서 거래하는 나스닥 시장의 종합지수")
    with col3:
        st.metric(label="**전일 종가**", value=data[0]["종가"], delta=data[0]["전일대비"])
    option = st.selectbox(
        "그래프 옵션 변경",
        ["각 지수별 종가 비교","최근 1년: 주간 가격 변동", '최근 12주: 주간 가격 변동', '최근 40일간의 캔들 차트', "종가동향"]
    )
    if option == "각 지수별 종가 비교":
        JGBG(load_data)
    elif option == "최근 1년: 주간 가격 변동":
        candle_year(data)
    elif option == "최근 12주: 주간 가격 변동":
        candle_week(data)
    elif option == '최근 40일간의 캔들 차트':
        candle_day(data)
    elif option == "종가동향":
        JGDH(data)

def dow_jones_page():
    infos()
    st.title("다우 산업")
    load_data = load_stock_data()
    data = load_data['다우 산업']
    #두개의 열 생성
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**관련 정보**")  # 볼드체 제목 추가
        st.markdown("거래소: 뉴욕증권거래소 (NYSE)  \n"
                    "기준통화: USD  \n"
                    "거래시간(한국시간 기준): 23:30 - 06:00")
    with col2:
        st.markdown("**지수 설명**") # 볼드체 제목 추가
        st.write("미국 다우존스사가 미국 주식시장을 대표할 수 있는 30개의 우량 주식들을 표본으로 채택하여 시장가격을 평균하여 산출하는 지수")
    with col3:
        st.metric(label="**전일 종가**", value=data[0]["종가"], delta=data[0]["전일대비"])
    
    option = st.selectbox(
        "그래프 옵션 변경",
        ["각 지수별 종가 비교","최근 1년: 주간 가격 변동", '최근 12주: 주간 가격 변동', '최근 40일간의 캔들 차트', "종가동향"]
    )
    if option == "각 지수별 종가 비교":
        JGBG(load_data)
    elif option == "최근 1년: 주간 가격 변동":
        candle_year(data)
    elif option == "최근 12주: 주간 가격 변동":
        candle_week(data)
    elif option == '최근 40일간의 캔들 차트':
        candle_day(data)
    elif option == "종가동향":
        JGDH(data)
