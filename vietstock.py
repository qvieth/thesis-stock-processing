import glob
import os
import subprocess
import stock_name

for stock in stock_name.fintech.split(" "):
    subprocess.run(
        [
            "xdg-open",
            f"https://finance.vietstock.vn/data/ExportTradingResult?Code={stock}&FromDate=2022-08-25&ToDate=2022-08-25&ExportType=excel&Cols=VHTT&ExchangeID=1",
        ]
    )
# f"https://finance.vietstock.vn/data/ExportTradingResult?Code=FPT&OrderBy=&OrderDirection=desc&PageIndex=1&PageSize=10&FromDate=2022-08-26&ToDate=2022-08-26&ExportType=excel&Cols=VHTT%2CGTGDKL&ExchangeID=1",

# f"https://finance.vietstock.vn/data/ExportTradingResult?Code=FPT&FromDate=2022-08-26&ToDate=2022-08-26&ExportType=excel&Cols=VHTT&ExchangeID=1",
