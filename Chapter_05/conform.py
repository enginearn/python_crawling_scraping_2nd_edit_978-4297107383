import pandas as pd
from plot_historical_data import parse_year_and_month
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

df_exchange = pd.read_csv(
    "data/exchange.csv",
    encoding="cp932",
    names=["date", "USD", "rate"],
    header=1,
    index_col=0,
    parse_dates=True,
)

print(df_exchange.fillna(0))
print(df_exchange.USD)

jobs_xlsx = "data/third_table.xlsx"


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
    print(s_jobs.index)
    s_jobs.index = [parse_year_and_month(y, m) for y, m in s_jobs.index]

    return s_jobs


print(job_offer_rate())
print(
    datetime(1973, 1, 1).strftime("%Y-%m-%d"),
    type(datetime(1973, 1, 1).strftime("%Y-%m-%d")),
)
print(datetime.now().strftime("%Y-%m-%d"))

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 1, 5, 2, 8, 5, 6, 2, 2]
z = [4, 6, 3, 5, 7, 8, 3, 5, 6, 9]

labels = ["K", "M", "D", "Ke", "A", "S", "Y", "Ma", "Yo", "J"]

fig, ax = plt.subplots()
ax.bar(
    [n - 0.25 for n in x], y, width=0.25, align="edge", color="darkcyan", label="test1"
)
ax.bar(
    [n + 0.25 for n in x], z, width=-0.25, align="edge", color="coral", label="test2"
)
ax.legend(loc="best")

##
ax.set_xticks(x)
ax.set_xticklabels(labels)
##

plt.show()
