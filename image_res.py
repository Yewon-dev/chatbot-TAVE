def image(message):
    ## 이미지 보내주는 res문
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": message,
                        "altText": "주사위입니다."
                    }
                }
            ]
        }
    }
    
    return res