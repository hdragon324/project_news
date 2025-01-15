import streamlit as st
from utils.sidebar import create_sidebar
from streampages.home import home_page
from streampages.news import *
from streampages.stock_market import *

# 세션 초기화
if 'page' not in st.session_state:
    st.session_state.page = "Home"

st.set_page_config(layout="wide",
                   page_title="Dumb&Kind",
                   page_icon="SeSAC_icon.png")

# 사이드바 생성
sub_choose = create_sidebar()

page_mapping = {
    "Home": home_page,
    "S&P 500": sp500_page,
    "NASDAQ": nasdaq_page,
    "Dow Jones": dow_jones_page,
    "Politics": political_page,
    "Economy": economic_page,
    "Society": social_page,
    "Culture/Lifestyle": lifestyle_culture_page,
    "IT/Science": it_science_page,
    "World": world_page
}

# 사이드 바 choose에 따른 세션 초기화
if sub_choose in page_mapping:
    st.session_state.page = sub_choose
if st.session_state.page == sub_choose:
    page_mapping[sub_choose]()

