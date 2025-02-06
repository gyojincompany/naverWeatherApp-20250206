import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4

weatherArea = "제주"
weatherHtml = requests.get(f"https://search.naver.com/search.naver?query={weatherArea}+날씨")
# print(weatherHtml) -> 200 코드가 반환되면 올바른 요청
soup = BeautifulSoup(weatherHtml.text, "html.parser")
# print(soup.prettify())
areaText = soup.find("h2",{"class":"title"}).text.strip()  # 날씨를 조회하려는 지역명
print(f"조회지역 : {areaText}")

nowTemperText = soup.find("div",{"class":"temperature_text"}).text.strip()  # 현재 온도
nowTemperText = nowTemperText[5:]  # "현재 온도" 텍스트를 제외한 현재온도 값만 추출(슬라이싱)
print(f"현재온도 : {nowTemperText}")
yesterdayTemperText = soup.find("p", {"class":"summary"}).text.strip()  # 어제와의 온도 비교
yesterdayTemperText = yesterdayTemperText[:15].strip()  # 어제와의 온도 비교값만 추출
print(f"어제와의 온도비교 : {yesterdayTemperText}")
weatherText = soup.find("span",{"class":"weather before_slash"}).text.strip()  # 오늘 날씨 텍스트
print(f"오늘의 날씨 : {weatherText}")
senseTemperText = soup.find("dd",{"class":"desc"}).text.strip()  # 체감온도
print(f"체감온도 : {senseTemperText}")
# todayWeatherInfo = soup.find("ul",{"class":"today_chart_list"}).text.strip()
# print(todayWeatherInfo)
todayWeatherInfo = soup.select("ul.today_chart_list>li")  #li 들을 list 타입으로 반환->미세먼지, 초미세먼지, 자외선, 일몰
# print(todayWeatherInfo)

dustInfo1 = todayWeatherInfo[0].find("span",{"class":"txt"}).text.strip()  # 미세먼지 정보
print(f"미세먼지 : {dustInfo1}")
dustInfo2 = todayWeatherInfo[1].find("span",{"class":"txt"}).text.strip()  # 초미세먼지 정보
print(f"초미세먼지 : {dustInfo2}")