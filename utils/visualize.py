import streamlit as st
import matplotlib.pyplot as plt

def cloud_Frequency(sorted_frequencies):
    '''클라우드 빈도 그래프'''
    # 상위 5개 단어 출력
    top_n = 5
    top_words = sorted_frequencies[:top_n]  # 상위 5개 단어 선택

    # 상위 5개 단어와 빈도 분리
    words, frequencies = zip(*top_words)

    # 빈도를 역순으로 정렬
    words = list(reversed(words))
    frequencies = list(reversed(frequencies))

    # 가로 바 차트 그리기
    plt.figure(figsize=(7, 8))
    plt.barh(words, frequencies, color='skyblue')
    plt.title('상위 5개 단어(빈도)')
    plt.xlabel('빈도')
    plt.ylabel('단어')
    st.pyplot(plt)

    return words

def matching_articles(keywords, articles):
    '''빈도 순위에 따른 뉴스 불러오기'''
    rank = 5
    for word in keywords:
        with st.expander(f"#### TOP{rank} **{word}**"):
            rank -= 1
            matching_articles = [
                article for article in articles if word in article["AI 요약"]
            ]
            if matching_articles:
                for article in matching_articles[:2]:  # 최대 2개 뉴스 출력
                    st.write(f"- **제목**: {article['제목']}")
                    st.write(f" **요약** : {article['AI 요약']}")
            else:
                st.write(f"- 관련 뉴스가 없습니다.")
 