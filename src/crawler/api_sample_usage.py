import requests
import json
import xmltodict


# API URL
url = "http://data4library.kr/api/usageAnalysisList"

# API Key 가져오기
with open("/home/mjy/Age2/book_reco/config/book_api.json", "r") as f:
    api_key = json.load(f)["api_key"]

# ISBN 13 가져오기
# isbn13 = "9791198682550"    # 너에게 들려주는 단단한 말
isbn13 = "9791130667584"

# Parameter
params = {
    "authKey": api_key,
    "isbn13": isbn13,
    # "format": "xml"
}

try:
    print("=== API에 GET 요청 보내기 ===")
    get_response = requests.get(url, params=params)
    get_response.raise_for_status()     # HTTP 상태 코드(200, 404, 500 등) 확인
    data = xmltodict.parse(get_response.content)
    with open("/home/mjy/Age2/book_reco/output/api_sample_usage.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(data)

except requests.exceptions.RequestException as e:
    print("API 호출 실패:", e)
