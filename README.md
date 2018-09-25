# 107-1 Python Advanced Software Development
JUN-HAN, CHEN
## Week_1 :
### Course:
1. Install [Anaconda](https://www.anaconda.com/download/)
2. Execute [Jupyter Notebook](https://jupyter.readthedocs.io/en/latest/install.html#installing-jupyter-using-anaconda-and-conda)
3. Create and Use GitHub
   - [Tutorial](https://git-scm.com/book/zh-tw/v1/%E9%96%8B%E5%A7%8B)
   - [README.md Tutorial](http://xianbai.me/learn-md/article/about/readme.html)
   - [Git command cheat sheet](https://github.com/joshnh/Git-Commands)   
4. Read 91APP dataset
### Homework:
[week1_hw.ipynb](https://github.com/Hank421Chen/STASD/blob/master/week_1/week_1_first_meet.ipynb)
1. Use basic function of Pandas to know 91APP datas
2. Slice and filter the datas
3. Group the datas (groupby)
4. Draw Pie chart of DiscountType
### Reference:
- Course[GitHub](https://pecu.gitbooks.io/python_/content/)
- Course[Gitbook](https://github.com/NTU-CSX-Project/107-1PythonSampleCode)
- [Python Cheat Sheet](https://pecu.gitbooks.io/python_/content/week1/4-python-basic-i.html)
- [Pandas Cheat Sheet](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)
-----
## Week_2 :
### [Course](https://github.com/Hank421Chen/STASD/tree/master/week_2/Courses):
1. climate1_getStationInfo.ipynb ( Use web crawler to get data of the weather station part1 )
2. climate2_getClimate.ipynb ( Use web crawler to get data of the weather station part2 )
3. final.ipynb 91APP 交易資料訂單配送城市整理 (六都) part1
4. clean_cityUnite.ipynb 91APP 交易資料訂單配送城市整理 (六都) part2
5. Final_project.ipynb 整合 91APP 資料與氣象資料
### [Homework](https://github.com/Hank421Chen/STASD/tree/master/week_2/Practice):
[week2_hw.ipynb](https://github.com/Hank421Chen/STASD/blob/master/week_2/Homework/week2_hw.ipynb)
- 爬取氣象資料（降雨量、溫度）
- 將爬取到的氣象資料，任意選擇一個地區，透過日期對應，合併出 91APP 消費金額與氣象的整合資料
- 新資料欄位：SalesOrderSlaveDateTime、City、SalesOrderTotalPayment、【降雨量、溫度】
- 爬取[台灣期貨交易所](https://www.taifex.com.tw/chinese/index.asp)中的每日台灣加權指數最高價、最低價、開盤價與交易量並合併911APP資料以供未來探討股市漲跌與網購的相關性
### Reference:
- [NTU-CSX-Project/107-1PythonSampleCode](https://github.com/NTU-CSX-Project/107-1PythonSampleCode)
- [kevinkevin556/STASD/week 2/climate.py](https://github.com/kevinkevin556/STASD/blob/master/week%202/climate.py)
