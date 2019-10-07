# TAVE 동아리 회원들을 위한 챗봇 개발

- 챗봇 개발 툴 : Kakao I Open Builder

- 서버 : Goorm IDE 활용

  - 무료 서버를 이용했기 때문에 로컬에서 서버를 계속 구동시켜야함

- 개발 언어 : Python

- 프레임 워크 : Flask

#   

##### 개발한 챗봇의 플러스친구 주소

<https://pf.kakao.com/_xfdxbtj>

# 

오픈빌더를 이용하여 TAVE 동아리 회원들이 자주 질문하는 내용들을 시나리오로 구현

***오픈 api***를 사용하고 ***크롤링***으로 데이터를 받아와서 서버와 연동

# 

#### 서버 연동으로 구현한 기능

- 코스피 지수
- 로또 번호
- 주사위
- 환율
- 미세먼지 지수
- 네이버 실시간 검색어 상위 20
- 더위 체감 지수
- 현재 기온

# 

#### 크롤링한 소스 간단 정리

```py
@app.route("/kospi", methods=["POST"])
def kospi():
    ## kospi값 받아오는 함수

    url = 'https://finance.naver.com/sise/'
    ## 환율값을 받아올 url
    
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    ## 받아온 url 내용을 HTML 구조로 변경
    
    kospi = soup.select_one('#KOSPI_now').text
    ## kospi 값만 크롤링
    
    kospi = "현재 코스피 지수는 " + kospi + "입니다."
    
    ## 오픈빌더 연동시 답변 출력을 위한 코드
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": kospi
                    }
                }
            ]
        }
    }
    
    return jsonify(res)


```



텍스트가 아닌 이미지로 답변을 보낼 때, 아래와 같은 방법으로 구현 (ex. 주사위)

```py
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": DiceUrl,
			"altText": "주사위입니다."
                    }
                }
            ]
        }
    }
```



