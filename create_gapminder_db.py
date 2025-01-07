file_names = ["ddf--datapoints--gdp_pcap--by--country--time",
              "ddf--datapoints--lex--by--country--time",
              "ddf--datapoints--pop--by--country--time",
              "ddf--entities--geo--country"]
table_names = ["gdp_per_capita", "life_expectancy", "population", "geography"]
import pandas as pd

df_dict = dict()
for file_name, table_name in zip(file_names, table_names):
    file_path = f"data/{file_name}.csv"
    df = pd.read_csv(file_path)
    df_dict[table_name] = df


# 以 sqlite3 與 pandas 建立資料庫 gapminder.db
# 來源：https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html

import sqlite3

connection = sqlite3.connect("data/gapminder.db")
for k, v in df_dict.items():
    v.to_sql(name=k, con=connection, index=False, if_exists="replace")
# connection.close()

# 在 gapminder.db 建立一個檢視表 plotting
drop_view_sql = """
DROP VIEW IF EXISTS plotting;
"""
create_view_sql = """
CREATE VIEW plotting AS
SELECT geography.name AS country_name,
       gdp_per_capita.time AS dt_year,
       gdp_per_capita.gdp_pcap AS gdp_per_capita,
       geography.world_4region AS continent,
       life_expectancy.lex AS life_expectancy,
       population.pop AS population
  FROM gdp_per_capita
  JOIN geography
    ON gdp_per_capita.country = geography.country
  JOIN life_expectancy
    ON gdp_per_capita.country = life_expectancy.country AND
       gdp_per_capita.time = life_expectancy.time
  JOIN population
    ON gdp_per_capita.country = population.country AND
       gdp_per_capita.time = population.time
 WHERE gdp_per_capita.time < 2024;
"""
cur = connection.cursor()
cur.execute(drop_view_sql)
cur.execute(create_view_sql)
connection.close()
# 概念驗證
