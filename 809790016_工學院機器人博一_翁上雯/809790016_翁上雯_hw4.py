#-*-coding:UTF-8 -*-
# 範例程式 EX02_07.py
#
# 下面 zipcode 存放台北市，基隆市，新北市各區的郵遞區號
#
# Q1.如何透過迴圈把台北市的所有郵遞區號列出 
# Q2.如何輸入一個區域名稱，找出這個區域所代表的郵遞區號?  (ex. 輸入:信義區  回傳:201)
# Q3.如何輸入一個郵遞區號後，找出這個郵遞區號所代表的區域? (ex. 輸入:106  回傳:大安區)

zipcode = {"台北市":{"中正區": 100, "大同區": 103, "中山區": 104, "松山區": 105, "大安區": 106, "萬華區": 108, "信義區": 110, "士林區": 111, "北投區": 112, "內湖區": 114, "南港區": 115, "文山區": 116}, "基隆市":{"仁愛區": 200, "信義區": 201, "中正區": 202, "中山區": 203, "安樂區": 204, "暖暖區": 205, "七堵區": 206},"新北市": {"萬里區": 207, "金山區": 208, "板橋區": 220, "汐止區": 221, "深坑區": 222, "石碇區": 223, "瑞芳區": 224, "平溪區": 226, "雙溪區": 227, "貢寮區": 228, "新店區": 231, "坪林區": 232, "烏來區": 233, "永和區": 234, "中和區": 235, "土城區": 236, "三峽區": 237, "樹林區": 238, "鶯歌區": 239, "三重區": 241, "新莊區": 242, "泰山區": 243, "林口區": 244, "蘆洲區": 247, "五股區": 248, "八里區": 249, "淡水區": 251, "三芝區": 252, "石門區": 253}}

def list_zip(city):
    print("輸入的城市：",city)
    print("所有郵遞區號：\n",zipcode[city])
    print("\n")

def area_to_zip(area):
    print("輸入的區域：",area)
    for key_city in zipcode:
        for key_area in zipcode[key_city]:
            if(area in zipcode[key_city]):
                print("(",key_city,", ", zipcode[key_city][area],")")
                break
    print("\n")

def zip_to_area(zip):
    print("輸入的郵遞區號：",zip)    
    for key_city in zipcode:
        for key_area in zipcode[key_city]:
            if(zipcode[key_city][key_area] == zip):
                print("區域：",key_area)
    print("\n")

print("\n====Result of Text Data====")
list_zip("台北市")
area_to_zip("信義區")
zip_to_area(106)

print("\n============")
print("輸入城市名稱（台北市、新北市、基隆市):")
city_name = input()
list_zip(city_name)

print("輸入區域名稱:")
area_name = input()
area_to_zip(area_name)

print("輸入郵遞區號:")
zip_num = int(input())
zip_to_area(zip_num)
