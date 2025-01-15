import json
from gensim import corpora
from gensim.models import LdaModel
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st
from utils.dict import cloud_stop_word
import platform

def load_stop_words(file_path='stop_words.txt'):
    '''불용어 사전 불러오기'''
    with open(file_path, 'r', encoding='utf-8') as file:
        stop_words = [line.strip() for line in file if line.strip()]
    return stop_words

def wordcloud(result):
    '''워드 클라우드 이미지 생성'''
    with open('summary_crawl_bs.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    with open('summary_crawl_bs.json', 'r', encoding='utf-8') as json_file:
        articles = json.load(json_file)

    if platform.system() == 'Darwin':  # Mac OS
       plt.rc('font', family='AppleGothic')
    else: # windows
       plt.rc('font', family='Malgun Gothic')
    # 마이너스 폰트 깨짐 방지
    plt.rcParams['axes.unicode_minus'] = False

    # 불용어 리스트 정의
    stop_words = cloud_stop_word()
        
    # JSON 파일 로드
    with open('summary_crawl_bs.json', 'r', encoding='utf-8') as json_file:
        articles = json.load(json_file)
    # 문서 전처리
    texts = []
    for article in articles:
        # 내용에서 불용어 제거 및 토큰화
        tokens = article['AI 요약'].split()
        tokens = [word for word in tokens if word not in stop_words]
        texts.append(tokens)

    # 단어 사전 생성
    dictionary = corpora.Dictionary(texts)

    # 문서-단어 행렬 생성
    corpus = [dictionary.doc2bow(text) for text in texts]

    # LDA 모델 학습
    lda_model = LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

    # 모든 주제의 워드 클라우드를 하나의 이미지로 합치기
    # 운영 체제에 따라 폰트 경로 설정
    if platform.system() == 'Darwin':  # Mac OS
        font_path = '/System/Library/Fonts/AppleGothic.ttf'
    else:  # Windows
        font_path = 'C:/Windows/Fonts/malgun.ttf'

    # WordCloud 생성
    combined_wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        font_path=font_path  # 자동으로 폰트 경로 설정
    )

    # 각 주제의 단어 빈도를 합산
    combined_frequencies = {}

    for i in range(lda_model.num_topics):
        word_dict = dict(lda_model.show_topic(i, topn=50))  # 각 주제의 상위 50개 단어
        for word, freq in word_dict.items():
            if word in combined_frequencies:
                combined_frequencies[word] += freq
            else:
                combined_frequencies[word] = freq

    # 합쳐진 단어 빈도로 워드 클라우드 생성
    combined_wordcloud.generate_from_frequencies(combined_frequencies)
    sorted_frequencies = sorted(combined_frequencies.items(), key=lambda x: x[1], reverse=True)  # 빈도수 기준으로 정렬

    # 워드 클라우드 시각화
    plt.figure(figsize=(10, 5))
    plt.imshow(combined_wordcloud, interpolation='bilinear')
    plt.axis('off')  # 축 표시 제거
    plt.title('모든 주제의 워드 클라우드')
    st.pyplot(plt)

    return sorted_frequencies, articles
