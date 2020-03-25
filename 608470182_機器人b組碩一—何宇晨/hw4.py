#-*-coding:UTF-8 -*-
# 範例程式 EX02_07.py
#
# 下面 zipcode 存放台北市，基隆市，新北市各區的郵遞區號
# 提示：會用兩層for迴圈items方法
#
# Q1.如何透過迴圈把台北市的所有郵遞區號列出 
# Q2.如何輸入一個區域名稱，找出這個區域所代表的郵遞區號?  (ex. 輸入:信義區  回傳:201)
# Q3.如何輸入一個郵遞區號後，找出這個郵遞區號所代表的區域? (ex. 輸入:106  回傳:大安區)

zipcode = {"台北市":{"中正區": 100, "大同區": 103, "中山區": 104, "松山區": 105, 
                  "大安區": 106, "萬華區": 108, "信義區": 110, "士林區": 111,
                  "北投區": 112, "內湖區": 114, "南港區": 115, "文山區": 116}, 
           "基隆市":{"仁愛區": 200, "信義區": 201, "中正區": 202, "中山區": 203, 
                  "安樂區": 204, "暖暖區": 205, "七堵區": 206},
           "新北市": {"萬里區": 207, "金山區": 208, "板橋區": 220, "汐止區": 221,
                   "深坑區": 222, "石碇區": 223, "瑞芳區": 224, "平溪區": 226, 
                   "雙溪區": 227, "貢寮區": 228, "新店區": 231, "坪林區": 232, 
                   "烏來區": 233, "永和區": 234, "中和區": 235, "土城區": 236, 
                   "三峽區": 237, "樹林區": 238, "鶯歌區": 239, "三重區": 241, 
                   "新莊區": 242, "泰山區": 243, "林口區": 244, "蘆洲區": 247, 
                   "五股區": 248, "八里區": 249, "淡水區": 251, "三芝區": 252, 
                   "石門區": 253}}

def list_zip(self):
    for (area,code) in zipcode[self].items():
        print(area,code)
def area_to_zip(self):
    for (city,data) in zipcode.items():
        for key,v in data.items():
            if key == useer_area:
                print(v)
def zip_to_area(self):
    for (city,data) in zipcode.items():
        for key,v in data.items():
            if v == int(useer_area):
                print(key)


useer_area = input('請輸入想要查詢的地區：')
if useer_area in zipcode.keys() :
    list_zip(useer_area)
elif useer_area.isdigit() is False:
    area_to_zip(useer_area)
elif useer_area.isdigit() is True:
    zip_to_area(useer_area)
else :
    print('找不到你的資訊')