def normal(message):
    ## 기본 res 텍스트 문법
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": message,
                    }
                }
            ]
        }
    }
    
    
    return res