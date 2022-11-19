import requests
import json
import stock_name
import os

# |%%--%%| <BDZN1cXASK|ZJrnIs04eY>

os.chdir("/home/qvieth/programming/thesis_/marketcap_financial/data/")
for stock_code in stock_name.fintech.split(" "):
    data = []
    current_page = 1
    total_page = 100
    while current_page <= total_page:
        res = requests.get(
            f"https://vcbs.com.vn/api/v1/stock-quotes/price-histories?stock_symbol={stock_code}&page={current_page}&locale=vi&limit=200"
        )
        total_page = res.json()["meta"]["totalPages"]
        data.extend(res.json()["data"])
        current_page += 1
        print(current_page)

    with open(f"{stock_code}.json", "w") as writer:
        json.dump(data, writer)

# test
