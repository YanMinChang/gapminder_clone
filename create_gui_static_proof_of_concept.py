import tkinter as tk
from tkinter import ttk
import plotly.express as px
import sqlite3
import pandas as pd
import matplotlib.animation as animation
import matplotlib.pyplot as plt

connection = sqlite3.connect("data/gapminder.db")
plotting_df = pd.read_sql("""SELECT * FROM plotting;""", con=connection)
connection.close()

fig_plotly = px.scatter(plotting_df, x="gdp_per_capita", y="life_expectancy",
                         animation_frame="dt_year", animation_group="country_name",
                         size="population", color="continent", hover_name="country_name", 
                         size_max=100, range_x=[500, 100000], range_y=[20, 90], log_x=True,
                         title="Gapminder Clone 1800-2023")

def generate_static_plot(selected_year):
    connection = sqlite3.connect("data/gapminder.db")
    plotting_df = pd.read_sql("""SELECT * FROM plotting;""", con=connection)
    
    # 根據選擇的年份生成靜態圖表
    fig_static = px.scatter(
        plotting_df[plotting_df["dt_year"] == selected_year], 
        x="gdp_per_capita", 
        y="life_expectancy",
        size="population", 
        color="continent", 
        hover_name="country_name", 
        size_max=100,
        log_x=True,
        title=f"Gapminder 散點圖 - {selected_year}"
    )
    # 在瀏覽器中顯示圖表，而不是保存為文件 ***二選一
    fig_static.show()
    
    # # 存成html並在瀏覽器中顯示圖表 ***二選一
    # fig_static.write_html(f"gapminder_clone_{selected_year}.html", auto_open=True)
    print(f"已生成 {selected_year} 年的 Gapminder 散點圖！")

def create_gui():
    root = tk.Tk()
    root.title('oxxo.studio')
    root.geometry('300x200')

    # 生成年份列表，從2000到2023年（根據當前日期）
    years = list(range(2000, 2024))
    
    # 下拉選單包含年份選項
    box = ttk.Combobox(root, values=years)
    box.pack(pady=10)

    # 按鈕以生成靜態圖表
    def on_button_click():
        selected_year = box.get()
        if selected_year:
            generate_static_plot(int(selected_year))
            plt.show()  

    button = tk.Button(root, text='生成靜態圖', command=on_button_click)
    button.pack(pady=10)

    # 結束按鈕
    def on_exit():
        root.destroy()  # 關閉主窗口

    exit_button = tk.Button(root, text='結束', command=on_exit)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()


# 1. 導入模組與設定資料庫連線
# python
# 複製程式碼
# import tkinter as tk
# from tkinter import ttk
# import plotly.express as px
# import sqlite3
# import pandas as pd
# import matplotlib.animation as animation
# import matplotlib.pyplot as plt
# 原因與功能：
# tkinter 與 ttk： 用於建立圖形介面（GUI），讓使用者可以通過互動選單操作程式。
# plotly.express： 用於繪製互動式圖表，簡化圖表生成過程。
# sqlite3： 用來連接 SQLite 資料庫，讀取存放的 Gapminder 資料。
# pandas： 進行資料操作與處理，便於處理 SQL 結果。
# matplotlib.animation 與 matplotlib.pyplot： 製作與顯示靜態圖表，提供替代的圖形呈現。
# 這段程式碼是準備工作，導入必要的工具來處理資料與建立互動功能。

# 2. 資料庫讀取與資料準備
# python
# 複製程式碼
# connection = sqlite3.connect("data/gapminder.db")
# plotting_df = pd.read_sql("""SELECT * FROM plotting;""", con=connection)
# connection.close()
# 原因與功能：
# sqlite3.connect("data/gapminder.db")： 連接本地 SQLite 資料庫，以提取需要繪製圖表的數據。
# pd.read_sql()： 使用 Pandas 將 SQL 查詢結果轉為 DataFrame，方便進行資料處理與繪圖。
# connection.close()： 關閉資料庫連線，避免資源浪費或潛在衝突。
# 這部分將資料庫中的 plotting 資料表提取成 DataFrame，為圖表生成準備資料。

# 3. 建立互動式 Plotly 圖表
# python
# 複製程式碼
# fig_plotly = px.scatter(
#     plotting_df, x="gdp_per_capita", y="life_expectancy",
#     animation_frame="dt_year", animation_group="country_name",
#     size="population", color="continent", hover_name="country_name", 
#     size_max=100, range_x=[500, 100000], range_y=[20, 90], log_x=True,
#     title="Gapminder Clone 1800-2023"
# )
# 原因與功能：
# px.scatter()： 生成交互式的散點圖，展示各國的 GDP 與壽命之間的關係，並使用年份動畫來動態展示數據變化。
# 參數設置：
# x 和 y： 縱橫座標分別為 GDP 與壽命。
# animation_frame 和 animation_group： 以年份 (dt_year) 作為動畫的切換依據，國家名稱 (country_name) 為動畫追蹤分組。
# size 和 color： 氣泡的大小與顏色分別對應人口數與大陸。
# range_x 和 range_y： 限定數據範圍，使圖表更聚焦。
# log_x=True： GDP 取對數尺度，因其數據範圍跨度較大。
# 這段程式碼旨在展示整體趨勢，並提供互動式的視覺化工具。

# 4. 靜態圖生成函式
# python
# 複製程式碼
# def generate_static_plot(selected_year):
#     connection = sqlite3.connect("data/gapminder.db")
#     plotting_df = pd.read_sql("""SELECT * FROM plotting;""", con=connection)
    
#     # 根據選擇的年份生成靜態圖表
#     fig_static = px.scatter(
#         plotting_df[plotting_df["dt_year"] == selected_year], 
#         x="gdp_per_capita", 
#         y="life_expectancy",
#         size="population", 
#         color="continent", 
#         hover_name="country_name", 
#         size_max=100,
#         log_x=True,
#         title=f"Gapminder 散點圖 - {selected_year}"
#     )
    
#     fig_static.write_html(f"gapminder_clone_{selected_year}.html", auto_open=True)
#     print(f"已生成 {selected_year} 年的 Gapminder 散點圖！")
# 原因與功能：
# generate_static_plot()： 根據使用者選擇的年份，生成對應年份的靜態圖表。
# plotting_df[plotting_df["dt_year"] == selected_year]： 過濾出選定年份的數據，僅繪製該年份的散點圖。
# fig_static.write_html()： 將圖表儲存為 HTML，並立即開啟。
# 動態與靜態圖的對比： 提供靜態版本以便於存檔或分享。
# 這樣設計是為了讓使用者可以按需生成某一特定年份的靜態圖表。

# 5. GUI 設計
# python
# 複製程式碼
# def create_gui():
#     root = tk.Tk()
#     root.title('oxxo.studio')
#     root.geometry('300x200')
# 原因與功能：
# tk.Tk()： 建立主窗口，作為圖形介面的容器。
# root.title()： 設置窗口標題。
# root.geometry()： 指定窗口尺寸，提供簡潔的交互界面。
# 6. 下拉選單與按鈕功能
# python
# 複製程式碼
#     years = list(range(2000, 2024))
#     box = ttk.Combobox(root, values=years)
#     box.pack(pady=10)

#     def on_button_click():
#         selected_year = box.get()
#         if selected_year:
#             generate_static_plot(int(selected_year))
#             plt.show()  

#     button = tk.Button(root, text='生成靜態圖', command=on_button_click)
#     button.pack(pady=10)

#     def on_exit():
#         root.destroy()  # 關閉主窗口

#     exit_button = tk.Button(root, text='結束', command=on_exit)
#     exit_button.pack(pady=10)
# 原因與功能：
# 年份選單：
# ttk.Combobox： 建立年份選單供使用者選擇。
# list(range(2000, 2024))： 限制年份範圍，模擬數據的有效年份。
# 靜態圖按鈕：
# on_button_click()： 讀取選中的年份並調用 generate_static_plot()。
# 結束按鈕：
# on_exit()： 安全關閉 GUI 主窗口。
# 7. 主執行入口
# python
# 複製程式碼
# if __name__ == "__main__":
#     create_gui()
# 原因與功能：
# if __name__ == "__main__":： 確保程式只有在直接執行時才會啟動 GUI，模組導入時不會自動執行。
# 這是 Python 程式的標準入口，避免不必要的執行行為。

