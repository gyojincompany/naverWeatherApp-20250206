# 해외 도시 날씨 크롤링 테스트
import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4

weatherArea = "도쿄"
weatherHtml = requests.get(f"https://search.naver.com/search.naver?query={weatherArea}+날씨")
# print(weatherHtml) -> 200 코드가 반환되면 올바른 요청
soup = BeautifulSoup(weatherHtml.text, "html.parser")
# print(soup.prettify())
areaText = soup.find("h2",{"class":"title"}).text.strip()  # 날씨를 조회하려는 지역명
print(f"조회지역 : {areaText}")
# nowTemperText = soup.find("div",{"class":"temperature_text"}).text.strip()  # 현재 온도
# nowTemperText = nowTemperText[5:]  # "현재 온도" 텍스트를 제외한 현재온도 값만 추출(슬라이싱)
# print(f"현재온도 : {nowTemperText}")
nowTemperText = soup.select("div.temperature_text>strong")[0].text.strip()
nowTemperText = nowTemperText[5:]  # "현재 온도" 텍스트를 제외한 현재온도 값만 추출(슬라이싱)
print(f"현재온도 : {nowTemperText}")
todayWeatherText = soup.select("div.temperature_text>p.summary")[0].text.strip()  # 해외 도시 날씨 문자(맑음)
print(todayWeatherText)
senseTempText = soup.select("p.summary>span.text>em")[0].text.strip()  # 해외 도시 체감 온도
print(f"체감온도 : {senseTempText}")
