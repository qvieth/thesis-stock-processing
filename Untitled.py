import glob
import pandas as pd
import numpy as np
import stock_name

# |%%--%%| <UK1K2Aur4D|tdzeQZqAZa>

industry = "fintech"
industry_code = "FT_"
stock_code_list = stock_name.fintech.split(" ")

# |%%--%%| <tdzeQZqAZa|TmDbJNbo1G>


def extract_marketcap(stock_code):
    file_name = glob.glob(f"/home/qvieth/Downloads/*{stock_code}*.xlsx")[0]
    df_vietstock = pd.read_excel(file_name, header=6)
    return df_vietstock.iloc[0, 1]


def load_df(
    stock_code,
    start_date="2022-08-26",
    end_date="2015-01-01",
    columns=[
        "exchangeCode",
        "stockSymbol",
        "sessionDate",
        "priceClose",
        "priceCloseAdjust",
    ],
):
    df = pd.read_json(f"data/{stock_code}.json")
    # process the dataframe to needed shape
    # slice needed columns
    df_processed = df.loc[:, columns]
    # filter by date
    df_processed = df_processed[
        (df_processed["sessionDate"] <= start_date)
        & (df_processed["sessionDate"] >= end_date)
    ]
    # trim datetime
    df_processed["sessionDate"] = pd.to_datetime(
        df_processed["sessionDate"]
    ).dt.strftime("%Y-%m-%d")
    # set index
    df_processed = df_processed.set_index("sessionDate")
    return df_processed


def calculate_marketcap(stock_code):
    marketcap = extract_marketcap(stock_code)

    def map_marketcap(arg):
        nonlocal marketcap
        if np.isnan(arg):
            return marketcap
        else:
            marketcap = marketcap * (1 + arg)
            return marketcap

    # calculate marketcap
    df_processed = load_df(stock_code)
    df_processed.insert(0, "perc_change", df_processed["priceCloseAdjust"].pct_change())
    # df_processed["perc_change"].fillna(0,inplace=True) # replace na with 0
    df_processed.insert(0, "marketCap", df_processed["perc_change"].map(map_marketcap))
    return df_processed


# |%%--%%| <TmDbJNbo1G|NT3pRU3vUp>

df_array = []
for stock_code in stock_code_list:
    df_array.append(calculate_marketcap(stock_code))

# |%%--%%| <NT3pRU3vUp|mpPiejW6SM>


for i, v in enumerate(df_array):
    df_array[i] = df_array[i][df_array[i]["exchangeCode"] == "HOSE"]
    df_array[i] = df_array[i].loc[:, ["marketCap", "perc_change"]]
    df_array[i] = df_array[i].rename(
        columns={
            "marketCap": f"{industry_code}mc{i+1}",
            "perc_change": f"{industry_code}r{i+1}",
        }
    )


# |%%--%%| <mpPiejW6SM|DhyDInCfJU>

final = pd.DataFrame()
# final = pd.concat(df_array, axis=1, keys=stock_code_list, join="outer")
final = pd.concat(df_array, axis=1, join="outer")
final.to_excel(f"concated_{industry}.xlsx", sheet_name=f"{industry}")
