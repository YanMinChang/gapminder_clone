import sqlite3
import pandas as pd

# 從 plotting 檢視表選取所有的資料
connection = sqlite3.connect("data/gapminder.db")
plotting_df = pd.read_sql("""SELECT * FROM plotting;""", con=connection)
connection.close()
print(plotting_df)


# 成品

# # 透過 matplotlib 模組繪製靜態圖
year_to_plot = 1995 # year_to_plot = 2023
subset_df = plotting_df[plotting_df["dt_year"] == year_to_plot]
lex = subset_df["life_expectancy"].values
gdp_pcap = subset_df["gdp_per_capita"].values
cont = subset_df["continent"].values
color_map = {
    "asia": "r",
    "africa": "g",
    "europe": "b",
    "americas": "c"
}
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
for xi, yi, ci in zip(gdp_pcap, lex, cont):
    ax.scatter(xi, yi, color=color_map[ci])
ax.set_title(f"The world in {year_to_plot}")
ax.set_xlabel("GDP Per Capita(in USD)")
ax.set_ylabel("Life Expectancy")
ax.set_ylim(20, 100)
ax.set_xlim(0, 100000)
plt.show()
# 成品
# 從 plotting 檢視表選取所有的資料
connection = sqlite3.connect("data/gapminder.db")
plotting_df = pd.read_sql("""SELECT * FROM plotting;""", con=connection)
connection.close()




