from bs4 import BeautifulSoup
import requests
import json

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

def fetch_link_list(sid):
    '''뉴스 카테고리 5페이지의 URL 목록 return'''
    cursor = 0
    link_list = []
    for _ in range(2):
        URL = f'https://news.naver.com/section/template/SECTION_ARTICLE_LIST?sid={sid}&next={cursor}'
        
        response = requests.get(URL, headers=header)
        datas = response.json()
        text = datas['renderedComponent']['SECTION_ARTICLE_LIST']
        soup = BeautifulSoup(text,'html.parser')

        # '더보기' 헤드에 있는 뉴스로 cursor 변경
        cursor = soup.select_one('div._PERSIST_META')['data-cursor']

        # cursor가 가리키는 뉴스로부터 1페이지 분량 URL 추출
        links = soup.select('a.sa_thumb_link')
        link_list += [link.attrs['href'] for link in links]

    return link_list

def fetch_summary_data(article_url):
    '''뉴스의 AI 요약봇의 제목, 본문을 dictionary형으로 return'''
    parts = article_url.split('/')
    extracted_part = f'{parts[5]}/{parts[6]}'
    extracted_part
    URL = f'https://tts.news.naver.com/article/{extracted_part}/summary?callback=callback&JSON'

    response = requests.get(URL, headers=header)
    fetchs = BeautifulSoup(response.text, 'html.parser')
    json_string = response.text.replace("/**/callback(","")[:-2]
    summary_bot = json.loads(json_string)

    news_data = {
    '제목' : summary_bot["title"],
    'AI 요약': summary_bot["summary"].replace("<br/><br/>","")
}
    return news_data

def infos():
    '''네이버 증권의 해외 증시 240일 crawl'''
    header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    symbol = {
            '다우 산업':'DJI@DJI',
            '나스닥 종합':'NAS@IXIC',
            'S&P 500':'SPI@SPX'
    }
    result = {}
    def info_crawl(symbol):
        num, count = 1, 0
        infos = []
        while count <= 240:
            URL = f'https://finance.naver.com/world/worldDayListJson.naver?symbol={symbol}&fdtc=0&page={num}'
            response = requests.get(URL, headers=header)
            text = response.json()
            num += 1
            for info in text:
                info_data = {
                    '날짜':info['xymd'],
                    '종가':info['clos'],
                    '전일대비':info['diff'],
                    '시가':info['open'],
                    '고가':info['high'],
                    '저가':info['low'],
                }
                infos.append(info_data)
                count += 1
        return infos

    for k, v in symbol.items():
        info_result = []
        info_result += info_crawl(v)
        result[k] = info_result
    with open('financial_crawl.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)