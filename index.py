import normal_res
import image_res
import cookie
import random
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/cookie", methods=["POST"])
def fortune_cookie():
    ## 포춘 쿠기

    ran = random.randint(0, 26)
    message = cookie.fortune(ran)

    res = normal_res.normal(message)
    
    return jsonify(res)


@app.route("/kospi", methods=["POST"])
def kospi():
    ## kospi

    url = 'https://finance.naver.com/sise/'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    kospi = soup.select_one('#KOSPI_now').text
    kospi = "현재 코스피 지수는 " + kospi + "입니다."
    
    res = normal_res.normal(kospi)
    
   
    
    return jsonify(res)


@app.route("/lotto", methods=["POST"])
def lotto():
    ## lotto 추천 함수

    RandomNum = random.sample(range(1, 45), 6)
    itemLotto = ""
    for i in RandomNum:
        itemLotto = itemLotto + str(i) + ", "
    itemLotto = itemLotto[:-2]

    lotto = "로또번호 추천: " + itemLotto

    res = normal_res.normal(lotto)
    
    
    return jsonify(res)


@app.route("/finance", methods=["POST"])
def finance():
    ## 환율

    url = 'https://finance.naver.com/marketindex/exchangeList.nhn'

    response = requests.get(url).text
    
    soup = BeautifulSoup(response, 'html.parser')

    nation_list = soup.select(".tit")
    finance_list = soup.select(".sale")
    nation = []
    sale = []
    chat = ""
    for i in nation_list:
        i = i.text
        i = i.strip()
        nation.append(i)
    for j in finance_list:
        j = j.text
        sale.append(j)
    for name, currency in zip(nation, sale):
        chat = chat + name + currency + "\n"

    finance = "현재 환율입니다. \n" + chat

    
    res = normal_res.normal(finance)
    
    
    return jsonify(res)


@app.route("/NaverSearch", methods=["POST"])
def NaverSearch():
    ## naver 검색 상위 20

    url = 'https://www.naver.com/'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    item = soup.select_one(".ah_l")
    item1 = soup.find('ul', _class='.ah_l')
    test1 = item.select(".ah_r")
    test2 = item.select(".ah_k")
    rank = []
    subject = []
    chat = ""
    for i in test1:
        i = i.text
        i = i.strip()
        rank.append(i)
    for j in test2:
        j = j.text
        subject.append(j)

    for name, currency in zip(rank, subject):
        chat = chat + "[ "+ name + " ] " + currency + "\n"

    SearchList = "현재 naver 실시간 급상승 검색어! \n" + chat

    res = normal_res.normal(SearchList)

    
    return jsonify(res)


@app.route("/dust", methods=["POST"])
def dust():
    ## 미세먼지

    servicekey = 'R1ELvH7uMyJXVpkSIagSFrNm9EXgOEVkkro57Ug7XlT8kG2ANOwfuNBns4Qp84hI%2BJazWajY0QSievkFUojUMg%3D%3D'
    url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName='+'서울'+'&pageNo=2&numOfRows=1&ServiceKey='+servicekey+'&ver=1.3'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    dust_info = soup.body.pm10grade1h.text
    fine_dust_info = soup.body.pm25grade1h.text

    if dust_info == '1':
        dust_result = '좋다~ \n한강가자~ ٩(^ᴗ^)۶'
    elif dust_info == '2':
        dust_result = '보통'
    elif dust_info == '3':
        dust_result = '나빠요:('
    else:
        dust_result = '매우매우매우 나쁘다'

    if fine_dust_info == '1':
        fine_dust_result = '좋음'
    elif fine_dust_info == '2':
        fine_dust_result = '보통'
    elif fine_dust_info == '3':
        fine_dust_result = '나쁨 \n\n폐 속에 초미세먼지를 얻었습니다 +1'
    else:
        fine_dust_result = '매우.. 나쁘다.. 초미세먼지.... \n마스크 필수...'

    dust_info = ('{1}\n<{0}>에서 \n미세먼지농도는 {2}입니다.\n미세먼지등급:{3}\n초미세먼지농도:{4}\n초미세먼지등급:{5}'.
          format('서울',
                 soup.body.datatime.text,
                 soup.body.pm10value24.text,
                 dust_result,
                 soup.body.pm25value24.text,
                 fine_dust_result))

    res = normal_res.normal(dust_info)
    
    
    return jsonify(res)


@app.route("/dice", methods=["POST"])
def dice():
    ## 주사위 숫자 랜덤으로 제공

    RandomDice = random.randint(1, 6)
    
    if RandomDice == 1:
        DiceUrl = 'https://cdn.pixabay.com/photo/2014/04/03/10/24/one-310338_960_720.png'
    elif RandomDice == 2:
        DiceUrl = 'https://cdn.pixabay.com/photo/2014/04/03/10/24/two-310337__340.png'
    elif RandomDice == 3:
        DiceUrl = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStUBtn6i4TuQZe6rS80gcaUnA_1eLxgCgOqxxY0pasRVaV7Ztv'
    elif RandomDice == 4:
        DiceUrl = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTV3Lm2Xve_wcjxxJXW6zs-cinvPOE-RJvBi54HiEYg-L7MonQb'
    elif RandomDice == 5:
        DiceUrl = 'https://cdn.pixabay.com/photo/2014/04/03/11/56/dice-312622_960_720.png'
    else:
        DiceUrl = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-f5YFpjsFIftTwUSWiu63Cd0oSE3x4WUf2U1f1VfWCQ6R6v-p'
    
    
    res = image_res.image(DiceUrl)
    

    return jsonify(res)


@app.route("/temperature", methods=["POST"])
def temperature():
    ## 기온 크롤링 하여 현재 기온 제공

    enc_location = "서울날씨"

    url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
    
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    temp = soup.select_one('.info_temperature').text

    temperature = "현재 기온은 " + temp + "입니다 :)"

    res = normal_res.normal(temperature)
    
    
    return jsonify(res)

@app.route("/heat", methods=["POST"])
def heat():
    now = datetime.now()
    hourdata = ('{0}{1:02d}{2:02d}{3:02d}'.format(now.year,now.month,now.day,now.hour))
    servicekey = 'R1ELvH7uMyJXVpkSIagSFrNm9EXgOEVkkro57Ug7XlT8kG2ANOwfuNBns4Qp84hI%2BJazWajY0QSievkFUojUMg%3D%3D'
    url = 'http://newsky2.kma.go.kr/iros/RetrieveLifeIndexService3/getSensoryHeatLifeList?ServiceKey=' + servicekey + '&areaNo=1100000000&&requestCode=A20&time=' + hourdata
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    
    HeatData = []
    HeatStd = []
    HeatData.append(int(soup.body.h3.text))
    HeatData.append(int(soup.body.h6.text))
    HeatData.append(int(soup.body.h9.text))
    HeatData.append(int(soup.body.h12.text))

    for i in HeatData:
        if i >= 31:
            HeatStd.append('매우위험')
        elif i >= 28:
            HeatStd.append('위험')
        elif i >= 25:
            HeatStd.append('경고')
        elif i >= 21:
            HeatStd.append('주의')
        else:
            HeatStd.append('관심')
    
    
    heat = ('더위 체감지수 측정시간은 {0}월 {1}일 {2}시입니다.\n측정시간으로 부터 3시간 후인{3}시의 더위 체감지수 등급은 {4}입니다.\n측정시간으로 부터 6시간 후인{5}시의 더위 체감지수 등급은 {6}입니다.\n측정시간으로 부터 9시간 후인{7}시의 더위 체감지수 등급은 {8}입니다.\n측정시간으로 부터 12시간 후인{9}시의 더위 체감지수 등급은 {10}입니다.'.
         format(soup.body.date.text[4:6], soup.body.date.text[6:8], soup.body.date.text[8:10], now.hour+3,HeatStd[0],
               now.hour+6, HeatStd[1],
               now.hour+9, HeatStd[2],
               now.hour+12, HeatStd[3]))
    
    res = normal_res.normal(heat)
    
    
    return jsonify(res)


@app.route("/food", methods=["POST"])
def food():
    ##식중독 지수를 알려주는 함수

    now = datetime.now()
    hourdata = ('{0}{1:02d}{2:02d}{3:02d}'.format( now.year, now.month, now.day,now.hour ))
    servicekey = 'R1ELvH7uMyJXVpkSIagSFrNm9EXgOEVkkro57Ug7XlT8kG2ANOwfuNBns4Qp84hI%2BJazWajY0QSievkFUojUMg%3D%3D'
    url = 'http://newsky2.kma.go.kr/iros/RetrieveLifeIndexService3/getFsnLifeList?serviceKey=' + servicekey + '&areaNo=1100000000&time=' + hourdata
    
    response = requests.get(url).text
    soup=BeautifulSoup(response, 'html.parser')
    
    food_poison = []
    result = []
    
    food_poison.append(int(soup.body.today.text))
    food_poison.append(int(soup.body.tomorrow.text))

    for i in food_poison:
        if i >= 95:
            result.append('위험')
        elif i >= 70:
            result.append('경고')
        elif i >= 35:
            result.append('주의')
        elif i == '':
            result.append('오전 6시부터 공개')
        else:
            result.append('관심')
    
    
    result = ('식중독 최근 측정시간은 {0}월 {1}일 {2}시입니다. \n오늘의 식중독지수 등급은 {3}입니다. \n내일의 식중독지수 등급은 {4}입니다.'.
         format(soup.body.date.text[4:6], soup.body.date.text[6:8], soup.body.date.text[8:10], result[0], result[1]))
    
    res = normal_res.normal(result)
    
    
    return jsonify(res)


@app.route("/ultraviolet", methods=["POST"])
def ultraviolet():
    ## 자외선 지수 보여주는 함수

    url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=자외선'
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    uv = soup.select_one('.txt_state').text
    uv = int(uv)

    if uv <= 2:
        ultraviolet = '자외선 지수 낮은 상태입니다. 편하게 다니세요'
    elif uv <= 5:
        ultraviolet = '자외선 지수 보통 상태입니다. 선크림 발라주세요.'
    elif uv <= 7:
        ultraviolet = '자외선 지수 높음 상태입니다. 선크림 필수에요!'
    elif uv <= 10:
        ultraviolet = '자외선 지수 매우 높음입니다. 실외활동 자제해주세요.'
    elif uv >= 11:
        ultraviolet = '자외선 지수 위험입니다. 나가면 죽어요!!'
    else:
        ultraviolet = '지금 에러났네요. 고쳐놓을께요 ㅠㅠ'

    res = normal_res.normal(ultraviolet)


    return jsonify(res)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', threaded = True)
