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
![image](https://github.com/user-attachments/assets/b5e638a3-40be-44ee-b6da-a7bbc11a9265)


### 설치 및 실행 방법
***import.ipynb 먼저 실행***

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

├── steampages/            # 사이드 바 주요 메뉴의 페이지

│   ├── home.py            # 메인 홈

│   ├── news.py            # 뉴스

│   ├── stock_market.py    # 해외 증시

├── utils/                 # 기능 모음 파일

│   ├── crawl.py           # 뉴스 및 주식 크롤링

│   ├── dict.py            # 불용어 사전

│   ├── graph.py           # 주식 그래프

│   ├── sidebar.py         # 사이드바 생성

│   ├── visualize.py       # 워드 클라우드 기반 뉴스 출력

│   ├── wordcloud.py       # 워드 클라우드 생성

└── README.md              # 프로젝트 설명서

└── import.ipynb           # 설치 모듈 및 라이브러리 모음

└── main.py                # 메인 실행 파일

└── financial_crawl.json   # 실시간으로 주식 크롤링 후 json파일로 저장

└── summary_crawl_bs.json  # 실시간으로 뉴스 크롤링 후 json파일로 저장

└── SeSAC_icon.png         # 이미지 파일

### 기술 스택 (사용된 언어 및 라이브러리)
- Python
- streamlit
- json
- math
- utils
- BeautifulSoup, Requests (크롤링)
- gensim, wordcloud (LDA 및 워드클라우드)
- matplotlib, plotly(데이터 시각화)


### 유의 사항

- 크롤링은 네이버 웹사이트의 구조 변경 시 동작하지 않을 수 있습니다.
- 네이버의 이용약관을 준수해야 하며, 과도한 요청으로 인해 IP가 차단될 수 있습니다.
- 크롤링 시 서버 응답 속도에 따라 데이터 수집 시간이 달라질 수 있습니다.
- 뉴스 데이터는 수집 시점과 키워드에 따라 내용이 달라질 수 있으며, 분석 결과가 고정적이지 않습니다.
- LDA 모델링의 결과는 뉴스 데이터의 양과 품질에 크게 의존합니다.
- 워드클라우드 및 키워드 분석은 단순 참고용이며, 반드시 전문가의 해석이 필요합니다.
- 한글 폰트가 누락된 경우, 그래프가 제대로 표시되지 않을 수 있습니다. matplotlib에서 한글 폰트를 설정해주세요.
- 브라우저 환경 및 해상도에 따라 Streamlit UI가 다르게 보일 수 있습니다.
- 크롤링 및 분석 작업은 대량 데이터 처리 시 성능 저하를 유발할 수 있습니다.
- 워드클라우드 생성 및 그래프 시각화는 고사양 PC에서 원활하게 작동합니다.
- 제공되는 데이터와 분석 결과는 연구 및 학습 목적으로만 사용해야 합니다. 상업적 이용 시 발생하는 법적 문제에 대해 책임지지 않습니다.
- 네이버 뉴스 및 증권 데이터를 사용할 때 저작권 관련 법규를 준수해야 합니다.
- 실행 전에 설치 및 실행방법에 명시된 라이브러리를 모두 설치해야 합니다.
- 사용 중 문제가 발생할 경우, 제공된 디렉토리 구조에 따라 파일을 확인하고 로그를 참조하세요.
- 분석 모델 및 시각화 기능은 지속적인 개선이 필요하며, 일부 한계가 있을 수 있습니다.

---
### 개발 기간

2025-01-13 ~ 2025-01-15


### 개발자 소개

박수빈 이현승 조서형 허용
