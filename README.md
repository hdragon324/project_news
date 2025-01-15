# Naver 뉴스 및 증권 데이터 분석 및 시각화

### 프로젝트 소개

이 프로젝트는 네이버 뉴스 및 네이버 증권 데이터를 크롤링하여 미국 주요 주가지수(다우존스, S&P 500, 나스닥)를 분석하고 시각화하는 웹 애플리케이션입니다.
사용자는 뉴스 데이터를 기반으로 생성된 워드클라우드와 주요 키워드 분석 결과를 확인할 수 있으며, 각 지수의 그래프를 통해 시각적인 분석이 가능합니다.


### 기능소개

- 네이버 뉴스 데이터 크롤링 및 JSON 저장
- 뉴스 데이터를 기반으로 한 LDA 토픽 모델링 및 워드클라우드 생성
- 가장 빈도수가 높은 단어 5개에 해당하는 뉴스 제목 및 기사 출력
- 다우존스, S&P 500, 나스닥 지수 데이터를 다양한 그래프로 시각화
- Streamlit 기반의 웹 애플리케이션으로 데이터 제공

### 실행화면


### 설치 및 실행 방법

pip install streamlit

pip install pandas

pip install beautifulsoup4

pip install wordcloud

pip install requests

pip install json

pip install matplotlib

pip install gensim

pip install streamlit-option-menu

터미널 창에 streamlit run main.py 입력

### 코드 구조 설명

├── crawler/               # 크롤링 코드
│   ├── news_crawler.py    # 네이버 뉴스 크롤링
│   ├── stock_crawler.py   # 네이버 증권 크롤링
├── analysis/              # 데이터 분석 코드
│   ├── lda_modeling.py    # LDA 모델링 및 워드클라우드 생성
│   └── visualization.py   # 그래프 시각화 코드
├── app.py                 # Streamlit 메인 파일
├── requirements.txt       # 필요한 Python 라이브러리 목록
└── README.md              # 프로젝트 설명서

### 기술 스택 (사용된 언어 및 라이브러리)
- Python
- Streamlit
- BeautifulSoup, Requests (크롤링)
- gensim, wordcloud (LDA 및 워드클라우드)
- matplotlib, seaborn, plotly (데이터 시각화)


### 유의 사항

- 크롤링 시간 소요 (뉴스: 12초 가량/주식: 4~5초 가량)
- 데이터는 크롤링 시점에 따라 달라진다
- 그래프 해석 주의
- 모델링의 한계
- 기사 및 주식 데이터 출처는 모두 네이버

---
### 개발 기간

2025-01-13 ~ 2025-01-15


### 개발자 소개

허용 박수빈 이현승 조서형
