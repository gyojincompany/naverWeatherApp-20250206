import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4

weatherHtml = requests.get("https://search.naver.com/search.naver?query=대구+날씨")
# print(weatherHtml) -> 200 코드가 반환되면 올바른 요청
soup = BeautifulSoup(weatherHtml.text, "html.parser")
# print(soup.prettify())
areaText = soup.find("h2",{"class":"title"}).text.strip()  # 닐씨를 조회하려는 지역명
print(areaText)

