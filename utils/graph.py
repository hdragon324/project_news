import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator
import math
import platform

def JGDH(data):
    st.write("종가동향 옵션을 선택했습니다.")
    # 제목 정의
    title = {
        0: '0 ~ 3개월',
        1: '3 ~ 6개월',
        2: '6 ~ 9개월',
        3: '9 ~ 12개월'
    }
   
    # DataFrame으로 변환 및 정렬
    df = pd.DataFrame(data)
    df['날짜'] = pd.to_datetime(df['날짜'], format='%Y%m%d')
    df = df.sort_values(by='날짜')  # 날짜 순으로 정렬
   
    # 데이터를 4등분
    num_subplots = 4
    chunk_size = math.ceil(len(df) / num_subplots)  # 각 subplot의 데이터 개수
    chunks = [df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size)]
    # Subplot 생성
    fig, axes = plt.subplots(num_subplots, 1, figsize=(10, 12))
    for i, chunk in enumerate(chunks):
        ax = axes[i]
        ax.bar(chunk['날짜'], chunk['종가'], color='#FFB600', label=f'범위 {i+1}')
        # 각 subplot의 y축 범위를 해당 구간 데이터로 설정
        y_min = chunk['저가'].min() * 0.995  # 여유를 두기 위해 99.5%
        y_max = chunk['고가'].max() * 1.005  # 여유를 두기 위해 100.5%
        ax.set_ylim(y_min, y_max)
       
        # x축에 최소 12개의 날짜 표시
        ax.xaxis.set_major_locator(MaxNLocator(nbins=12))  # x축의 날짜 개수를 최소 12로 설정
       
        # 제목 및 레이블
        ax.set_title(f"최근 {title[i]} 종가 동향", fontsize=15, fontweight='bold')  # 제목 볼드체
        ax.set_xlabel("날짜", fontsize=12)
        ax.set_ylabel("종가 (원)", fontsize=12)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.tick_params(axis='x', rotation=45)
    # 레이아웃 조정 및 Streamlit에 출력
    plt.tight_layout()
    st.pyplot(fig)

def JGBG(data):
    st.write("각 지수별 종가 비교 그래프를 표시합니다.")
    # 각 지수의 종가 데이터와 날짜를 DataFrame으로 변환
    dates = []
    snp500_close = []
    nasdaq_close = []
    dji_close = []
    for entry in data['S&P 500']:
        dates.append(entry['날짜'])
        snp500_close.append(entry['종가'])
    for entry in data['나스닥 종합']:
        nasdaq_close.append(entry['종가'])
    for entry in data['다우 산업']:
        dji_close.append(entry['종가'])
    # 날짜 형식 변환 및 DataFrame 생성
    df = pd.DataFrame({
        '날짜': pd.to_datetime(dates),
        'S&P 500': snp500_close,
        '나스닥 종합': nasdaq_close,
        '다우 산업': dji_close
    })
    # 인덱스를 날짜로 설정
    df.set_index('날짜', inplace=True)
    # 시계열 그래프 그리기
    fig, ax1 = plt.subplots(figsize=(12, 6))
    # S&P 500 선 그리기
    ax1.plot(df.index, df['S&P 500'], label='S&P 500', color='blue')
    ax1.set_ylabel('S&P 500', fontsize=15, color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    # 두 번째 Y축 생성
    ax2 = ax1.twinx()
    ax2.spines['right'].set_position(('outward', 60))  # 오른쪽으로 이동
    ax2.plot(df.index, df['나스닥 종합'], label='나스닥 종합', color='orange')
    ax2.set_ylabel('나스닥 종합', fontsize=15, color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')
    # 세 번째 Y축 생성
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 120))  # 오른쪽으로 더 이동
    ax3.plot(df.index, df['다우 산업'], label='다우 산업', color='green')
    ax3.set_ylabel('다우 산업', fontsize=15, color='green')
    ax3.tick_params(axis='y', labelcolor='green')
    # 그래프 제목 및 레이블 설정
    plt.title('S&P 500, 나스닥 종합, 다우 산업 종가 비교', fontsize=20, fontweight='bold')  # 제목 볼드체
    ax1.set_xlabel('날짜', fontsize=15)
    # 범례 설정
    fig.tight_layout()
    plt.grid()
    plt.show()
    st.pyplot(fig)

def candle_year(data):
    st.write("최근 1년: 주간 가격 변동을 표시합니다.")
    # 데이터프레임 생성
    df = pd.DataFrame(data)
    df.rename(columns={"시가": "Open", "고가": "High", "저가": "Low", "종가": "Close"}, inplace=True)
    # 날짜를 datetime 형식으로 변환
    df['날짜'] = pd.to_datetime(df['날짜'], format='%Y%m%d')
    df['날짜'] = date2num(df['날짜'])  # 날짜를 숫자형으로 변환
    # 캔들차트 그리기
    fig, ax = plt.subplots(figsize=(10, 6))  # 플롯 크기 확대 (10 x 6)
    # 상승봉 (빨간색 계열)
    ax.bar(df['날짜'][df['Close'] >= df['Open']],
           df['Close'][df['Close'] >= df['Open']] - df['Open'][df['Close'] >= df['Open']],
           bottom=df['Open'][df['Close'] >= df['Open']], color='#FF6347', width=0.6)  # Tomato 색상
    ax.bar(df['날짜'][df['Close'] >= df['Open']],
           df['High'][df['Close'] >= df['Open']] - df['Close'][df['Close'] >= df['Open']],
           bottom=df['Close'][df['Close'] >= df['Open']], color='#FF6347', width=0.2)  # Tomato 색상
    ax.bar(df['날짜'][df['Close'] >= df['Open']],
           df['Low'][df['Close'] >= df['Open']] - df['Open'][df['Close'] >= df['Open']],
           bottom=df['Open'][df['Close'] >= df['Open']], color='#FF6347', width=0.2)  # Tomato 색상
   
    # 하락봉 (파란색 계열)
    ax.bar(df['날짜'][df['Close'] < df['Open']],
           df['Close'][df['Close'] < df['Open']] - df['Open'][df['Close'] < df['Open']],
           bottom=df['Open'][df['Close'] < df['Open']], color='#1E90FF', width=0.6)  # DodgerBlue 색상
    ax.bar(df['날짜'][df['Close'] < df['Open']],
           df['High'][df['Close'] < df['Open']] - df['Open'][df['Close'] < df['Open']],
           bottom=df['Open'][df['Close'] < df['Open']], color='#1E90FF', width=0.2)  # DodgerBlue 색상
    ax.bar(df['날짜'][df['Close'] < df['Open']],
           df['Low'][df['Close'] < df['Open']] - df['Close'][df['Close'] < df['Open']],
           bottom=df['Close'][df['Close'] < df['Open']], color='#1E90FF', width=0.2)  # DodgerBlue 색상
   
    # 날짜 포맷 설정
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # 월 단위 포맷 (YYYY-MM)
    ax.xaxis.set_major_locator(mdates.MonthLocator())  # 월 단위 간격 설정
    # x축 레이블 설정
    plt.xticks(rotation=45)
    # 제목 및 레이블 추가
    plt.title('최근 1년: 주간 가격 변동', fontsize=15, fontweight='bold')  # 제목 볼드체
    plt.xlabel('날짜', fontsize=12)
    plt.ylabel('가격', fontsize=12)
    plt.grid(linestyle='--', linewidth=0.4)
    # Streamlit에 그래프 표시
    st.pyplot(fig)

def candle_week(data):
    st.write("최근 12주: 주간 가격 변동을 표시합니다.")
    # 데이터프레임 생성
    df = pd.DataFrame(data)
    df.rename(columns={"시가": "Open", "고가": "High", "저가": "Low", "종가": "Close"}, inplace=True)
    # 날짜를 datetime 형식으로 변환
    df['날짜'] = pd.to_datetime(df['날짜'], format='%Y%m%d')
    # 가장 최근 날짜를 기준으로 12주간의 데이터 필터링
    latest_date = df['날짜'].max()
    start_date = latest_date - pd.Timedelta(weeks=12)
    df_recent = df[df['날짜'] >= start_date].copy()  # 복사본을 만들어서 변경
    # 날짜를 숫자 값으로 변환 (matplotlib에서 사용)
    df_recent['날짜'] = date2num(df_recent['날짜'])
    # 캔들차트 그리기
    fig, ax = plt.subplots(figsize=(10, 6))  # 플롯 크기 확대 (10 x 6)
   
    # 상승봉 (빨간색 계열)
    ax.bar(df_recent['날짜'][df_recent['Close'] >= df_recent['Open']],
           df_recent['Close'][df_recent['Close'] >= df_recent['Open']] - df_recent['Open'][df_recent['Close'] >= df_recent['Open']],
           bottom=df_recent['Open'][df_recent['Close'] >= df_recent['Open']],
           color='#FF6347', width=0.6)  # Tomato 색상
    ax.bar(df_recent['날짜'][df_recent['Close'] >= df_recent['Open']],
           df_recent['High'][df_recent['Close'] >= df_recent['Open']] - df_recent['Close'][df_recent['Close'] >= df_recent['Open']],
           bottom=df_recent['Close'][df_recent['Close'] >= df_recent['Open']],
           color='#FF6347', width=0.2)  # Tomato 색상
    ax.bar(df_recent['날짜'][df_recent['Close'] >= df_recent['Open']],
           df_recent['Low'][df_recent['Close'] >= df_recent['Open']] - df_recent['Open'][df_recent['Close'] >= df_recent['Open']],
           bottom=df_recent['Open'][df_recent['Close'] >= df_recent['Open']],
           color='#FF6347', width=0.2)  # Tomato 색상
   
    # 하락봉 (파란색 계열)
    ax.bar(df_recent['날짜'][df_recent['Close'] < df_recent['Open']],
           df_recent['Close'][df_recent['Close'] < df_recent['Open']] - df_recent['Open'][df_recent['Close'] < df_recent['Open']],
           bottom=df_recent['Open'][df_recent['Close'] < df_recent['Open']],
           color='#1E90FF', width=0.6)  # DodgerBlue 색상
    ax.bar(df_recent['날짜'][df_recent['Close'] < df_recent['Open']],
           df_recent['High'][df_recent['Close'] < df_recent['Open']] - df_recent['Open'][df_recent['Close'] < df_recent['Open']],
           bottom=df_recent['Open'][df_recent['Close'] < df_recent['Open']],
           color='#1E90FF', width=0.2)  # DodgerBlue 색상
    ax.bar(df_recent['날짜'][df_recent['Close'] < df_recent['Open']],
           df_recent['Low'][df_recent['Close'] < df_recent['Open']] - df_recent['Close'][df_recent['Close'] < df_recent['Open']],
           bottom=df_recent['Close'][df_recent['Close'] < df_recent['Open']],
           color='#1E90FF', width=0.2)  # DodgerBlue 색상
   
    # 날짜 포맷 설정
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # 주 단위 포맷 (YYYY-MM-DD)
    ax.xaxis.set_major_locator(mdates.WeekdayLocator())  # 주 단위 간격 설정
    # x축 레이블 설정
    plt.xticks(rotation=45)
    # 제목 및 레이블 추가
    plt.title('최근 12주: 주간 가격 변동', fontsize=15, fontweight='bold')  # 제목 볼드체
    plt.xlabel('날짜', fontsize=12)
    plt.ylabel('가격', fontsize=12)
    plt.grid(linestyle='--', linewidth=0.4)
    # Streamlit에 그래프 표시
    st.pyplot(fig)

def candle_day(data):
    st.write("최근 40일간의 캔들 차트을 선택했습니다.")
    # 데이터프레임 생성
    df = pd.DataFrame(data)
    df.rename(columns={"시가": "Open", "고가": "High", "저가": "Low", "종가": "Close"}, inplace=True)
    # 날짜를 datetime 형식으로 변환
    df['날짜'] = pd.to_datetime(df['날짜'], format='%Y%m%d')
    # 가장 최근 날짜를 기준으로 40일간의 데이터 필터링
    latest_date = df['날짜'].max()
    start_date = latest_date - pd.Timedelta(days=40)
    df_recent = df[df['날짜'] >= start_date].copy()  # 복사본을 만들어서 변경
    # 날짜를 숫자 값으로 변환 (matplotlib에서 사용)
    df_recent['날짜'] = date2num(df_recent['날짜'])
    # 캔들차트 그리기
    fig, ax = plt.subplots(figsize=(10, 6))  # 플롯 크기 확대 (10 x 6)
   
    # 상승봉 (빨간색 계열)
    ax.bar(df_recent['날짜'][df_recent['Close'] >= df_recent['Open']],
           df_recent['Close'][df_recent['Close'] >= df_recent['Open']] - df_recent['Open'][df_recent['Close'] >= df_recent['Open']],
           bottom=df_recent['Open'][df_recent['Close'] >= df_recent['Open']], color='#FF6347', width=0.6)  # Tomato 색상
    ax.bar(df_recent['날짜'][df_recent['Close'] >= df_recent['Open']],
           df_recent['High'][df_recent['Close'] >= df_recent['Open']] - df_recent['Close'][df_recent['Close'] >= df_recent['Open']],
           bottom=df_recent['Close'][df_recent['Close'] >= df_recent['Open']], color='#FF6347', width=0.2)  # Tomato 색상
    ax.bar(df_recent['날짜'][df_recent['Close'] >= df_recent['Open']],
           df_recent['Low'][df_recent['Close'] >= df_recent['Open']] - df_recent['Open'][df_recent['Close'] >= df_recent['Open']],
           bottom=df_recent['Open'][df_recent['Close'] >= df_recent['Open']], color='#FF6347', width=0.2)  # Tomato 색상
   
    # 하락봉 (파란색 계열)
    ax.bar(df_recent['날짜'][df_recent['Close'] < df_recent['Open']],
           df_recent['Close'][df_recent['Close'] < df_recent['Open']] - df_recent['Open'][df_recent['Close'] < df_recent['Open']],
           bottom=df_recent['Open'][df_recent['Close'] < df_recent['Open']], color='#1E90FF', width=0.6)  # DodgerBlue 색상
    ax.bar(df_recent['날짜'][df_recent['Close'] < df_recent['Open']],
           df_recent['High'][df_recent['Close'] < df_recent['Open']] - df_recent['Open'][df_recent['Close'] < df_recent['Open']],
           bottom=df_recent['Open'][df_recent['Close'] < df_recent['Open']], color='#1E90FF', width=0.2)  # DodgerBlue 색상
    ax.bar(df_recent['날짜'][df_recent['Close'] < df_recent['Open']],
           df_recent['Low'][df_recent['Close'] < df_recent['Open']] - df_recent['Close'][df_recent['Close'] < df_recent['Open']],
           bottom=df_recent['Close'][df_recent['Close'] < df_recent['Open']], color='#1E90FF', width=0.2)  # DodgerBlue 색상
   
    # 날짜 포맷 설정
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # 일 단위 포맷 (YYYY-MM-DD)
    # x축을 12등분하여 날짜 표시
    ax.xaxis.set_major_locator(mdates.DayLocator())  # 일 단위 간격 설정
    # x축 레이블 설정
    plt.xticks(rotation=45)
    # 제목 및 레이블 추가
    plt.title('최근 40일: 주간 가격 변동', fontsize=15, fontweight='bold')  # 제목 볼드체
    plt.xlabel('날짜', fontsize=12)
    plt.ylabel('가격', fontsize=12)
    plt.grid(linestyle='--', linewidth=0.4)
    # Streamlit에 그래프 표시
    st.pyplot(fig)

def load_stock_data():
    if platform.system() == 'Darwin':  # Mac OS
       plt.rc('font', family='AppleGothic')
    else: # windows
       plt.rc('font', family='Malgun Gothic')
    # 마이너스 폰트 깨짐 방지
    plt.rcParams['axes.unicode_minus'] = False
    # JSON 데이터 로드
    with open('financial_crawl.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data