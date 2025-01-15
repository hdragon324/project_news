from utils.crawl import fetch_link_list, fetch_summary_data
from utils.wordcloud import wordcloud
from utils.visualize import cloud_Frequency, matching_articles
import streamlit as st

def political_page():
    # Streamlit 애플리케이션의 스타일을 조정하기 위해 HTML과 CSS를 사용
    st.markdown(
        """
        <style>
        .vertical-line {
            border-left: 1px solid #d3d3d3;
            height: 100%;
            position: absolute;
            left: 80%;
            top: 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 세로로 나눈 두 개의 열 생성
    col1, col2 = st.columns([2, 1])

    with col1:
        politic = [fetch_summary_data(article) for article in fetch_link_list(100)]
        words, articles = wordcloud(politic)

    with col2:
        keywords  = cloud_Frequency(words)

    # 세션 상태에 데이터를 저장하거나 가져오기
    if "matching_articles_data" not in st.session_state:
        st.session_state.matching_articles_data = {}

    st.divider()
    st.markdown("### <span style='font-size: 28px;'>상위 5개 단어가 포함된 뉴스</span>", unsafe_allow_html=True)
    matching_articles(keywords, articles)

def economic_page():
    # Streamlit 애플리케이션의 스타일을 조정하기 위해 HTML과 CSS를 사용
    st.markdown(
        """
        <style>
        .vertical-line {
            border-left: 1px solid #d3d3d3;
            height: 100%;
            position: absolute;
            left: 80%;
            top: 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 세로로 나눈 두 개의 열 생성
    col1, col2 = st.columns([2, 1])

    with col1:
        economy = [fetch_summary_data(article) for article in fetch_link_list(101)]
        words, articles = wordcloud(economy)

    with col2:
        keywords  = cloud_Frequency(words)

    # 세션 상태에 데이터를 저장하거나 가져오기
    if "matching_articles_data" not in st.session_state:
        st.session_state.matching_articles_data = {}

    st.divider()
    st.markdown("### <span style='font-size: 28px;'>상위 5개 단어가 포함된 뉴스</span>", unsafe_allow_html=True)
    matching_articles(keywords, articles)

def social_page():
    # Streamlit 애플리케이션의 스타일을 조정하기 위해 HTML과 CSS를 사용
    st.markdown(
        """
        <style>
        .vertical-line {
            border-left: 1px solid #d3d3d3;
            height: 100%;
            position: absolute;
            left: 80%;
            top: 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 세로로 나눈 두 개의 열 생성
    col1, col2 = st.columns([2, 1])

    with col1:
        social = [fetch_summary_data(article) for article in fetch_link_list(102)]
        words, articles = wordcloud(social)

    with col2:
        keywords  = cloud_Frequency(words)

    # 세션 상태에 데이터를 저장하거나 가져오기
    if "matching_articles_data" not in st.session_state:
        st.session_state.matching_articles_data = {}

    st.divider()
    st.markdown("### <span style='font-size: 28px;'>상위 5개 단어가 포함된 뉴스</span>", unsafe_allow_html=True)
    matching_articles(keywords, articles)

def lifestyle_culture_page():
    # Streamlit 애플리케이션의 스타일을 조정하기 위해 HTML과 CSS를 사용
    st.markdown(
        """
        <style>
        .vertical-line {
            border-left: 1px solid #d3d3d3;
            height: 100%;
            position: absolute;
            left: 80%;
            top: 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 세로로 나눈 두 개의 열 생성
    col1, col2 = st.columns([2, 1])

    with col1:
        lifestyle = [fetch_summary_data(article) for article in fetch_link_list(103)]
        words, articles = wordcloud(lifestyle)

    with col2:
        keywords  = cloud_Frequency(words)

    # 세션 상태에 데이터를 저장하거나 가져오기
    if "matching_articles_data" not in st.session_state:
        st.session_state.matching_articles_data = {}

    st.divider()
    st.markdown("### <span style='font-size: 28px;'>상위 5개 단어가 포함된 뉴스</span>", unsafe_allow_html=True)
    matching_articles(keywords, articles)

def it_science_page():
    # Streamlit 애플리케이션의 스타일을 조정하기 위해 HTML과 CSS를 사용
    st.markdown(
        """
        <style>
        .vertical-line {
            border-left: 1px solid #d3d3d3;
            height: 100%;
            position: absolute;
            left: 80%;
            top: 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 세로로 나눈 두 개의 열 생성
    col1, col2 = st.columns([2, 1])

    with col1:
        it_science = [fetch_summary_data(article) for article in fetch_link_list(105)]
        words, articles = wordcloud(it_science)

    with col2:
        keywords  = cloud_Frequency(words)

    # 세션 상태에 데이터를 저장하거나 가져오기
    if "matching_articles_data" not in st.session_state:
        st.session_state.matching_articles_data = {}

    st.divider()
    st.markdown("### <span style='font-size: 28px;'>상위 5개 단어가 포함된 뉴스</span>", unsafe_allow_html=True)
    matching_articles(keywords, articles)

def world_page():
    # Streamlit 애플리케이션의 스타일을 조정하기 위해 HTML과 CSS를 사용
    st.markdown(
        """
        <style>
        .vertical-line {
            border-left: 1px solid #d3d3d3;
            height: 100%;
            position: absolute;
            left: 80%;
            top: 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 세로로 나눈 두 개의 열 생성
    col1, col2 = st.columns([2, 1])

    with col1:
        world = [fetch_summary_data(article) for article in fetch_link_list(104)]
        words, articles = wordcloud(world)

    with col2:
        keywords  = cloud_Frequency(words)

    # 세션 상태에 데이터를 저장하거나 가져오기
    if "matching_articles_data" not in st.session_state:
        st.session_state.matching_articles_data = {}

    st.divider()
    st.markdown("### <span style='font-size: 28px;'>상위 5개 단어가 포함된 뉴스</span>", unsafe_allow_html=True)
    matching_articles(keywords, articles)