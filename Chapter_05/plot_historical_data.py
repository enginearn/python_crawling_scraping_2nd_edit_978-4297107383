#!/usr/bin/env python3

import sys
from datetime import datetime
import japanize_matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# plt.rcParams['font.family'] = 'Hack NF'
# plt.rcParams["font.size"] = 10

exchange_csv = "data/exchange.csv"
jgbcm_csv = "data/jgbcm_all.csv"
jobs_xlsx = "data/third_table.xlsx"
encoding = "utf-8"
encode_cp932 = "cp932"
save_dir = "graph_images"
ext = "png"
dpi = 500
# image_name = input('Enter image name: ') + '.' + ext
image_name = "plot_historica_data" + "." + ext


def exchange():
    """_summary_

    Returns:
        _type_: _description_
    """
    df_exchange = pd.read_csv(
        exchange_csv,
        encoding=encode_cp932,
        names=["date", "USD", "rate"],
        header=1,
        index_col=0,
        parse_dates=True,
    )
    return df_exchange


def jgbcm() -> pd.DataFrame:
    """_summary_

    Returns:
        _type_: _description_
    """
    df_jgbcm = pd.read_csv(
        jgbcm_csv,
        encoding=encode_cp932,
        header=1,
        index_col=0,
        parse_dates=True,
        date_parser=parse_japanese_date,
        na_values=["-"],
    )
    return df_jgbcm


def job_offer_rate() -> pd.DataFrame:
    """Docstring"""
    df_jobs = pd.read_excel(
        jobs_xlsx,
        sheet_name=0,
        skiprows=[0, 1, 2, 4],
        skipfooter=3,
        usecols="A,U:AF",
        index_col=0,
    )
    df_jobs.columns = [c.split(".")[0] for c in df_jobs.columns]
    s_jobs = df_jobs.stack()
    s_jobs.index = [parse_year_and_month(y, m) for y, m in s_jobs.index]

    return s_jobs


def parse_japanese_date(s: str) -> datetime:
    """Docstring"""
    base_years = {"E": 1596, "M": 1868, "T": 1912, "S": 1925, "H": 1988, "R": 2018}
    era = s[0]
    year, month, day = s[1:].split(".")
    year = base_years[era] + int(year)

    return datetime(year, int(month), int(day))


def parse_year_and_month(year: str, month: str) -> datetime:
    """Docstring"""
    year = int(year[:-1])
    month = int(month[:-1])
    year += 1900 if year >= 63 else 2000

    return datetime(year, month, 1)
    # return datetime(year, month, 1).strftime("%Y-%m-%d")


def plot_and_save_graph():
    """Docstring"""
    label_exchange = "USD/JPY"
    label_jgbcm_1 = "1年国債金利"
    label_jgbcm_5 = "5年国債金利"
    label_jgbcm_10 = "10年国債金利"
    label_job_rate = "求人倍率"

    min_data = datetime(1973, 1, 1)
    max_data = datetime.now()

    df_exchange = exchange()
    print(f"df_exchange: \n{df_exchange}")
    # 1つ目のグラフを作成
    plt.subplot(3, 1, 1)  # 3 rows, 1 column, 1st subplot
    plt.plot(df_exchange.index, df_exchange.USD, label=label_exchange)
    plt.xlim([min_data, max_data])
    plt.ylim(50, 250)
    plt.legend("best")

    df_jgbcm = jgbcm()
    print(f"df_jgbcm: \n{df_jgbcm}")
    # 2つ目のグラフを作成
    plt.subplot(3, 1, 2)  # 3 rows, 1 column, 2nd subplot
    plt.plot(df_jgbcm.index, df_jgbcm["1年"], label=label_jgbcm_1)
    plt.plot(df_jgbcm.index, df_jgbcm["5年"], label=label_jgbcm_5)
    plt.plot(df_jgbcm.index, df_jgbcm["10年"], label=label_jgbcm_10)
    plt.xlim([min_data, max_data])
    plt.legend("best")

    df_job_rate = job_offer_rate()
    print(f"df_job_rate: \n{df_job_rate}")
    # 3つ目のグラフを作成
    plt.subplot(3, 1, 3)  # 3 rows, 1 column, 3rd subplot
    plt.plot(df_job_rate.index, df_job_rate, label=label_job_rate)
    plt.xlim([min_data, max_data])
    plt.ylim(0.0, 2.0)
    plt.axhline(y=1.0, color="gray", linestyle="dotted")
    plt.legend("best")

    plt.savefig(save_dir + "/" + image_name, dpi=dpi)


def main():
    """Docstring"""
    plot_and_save_graph()


if __name__ == "__main__":
    main()
    sys.exit(0)
