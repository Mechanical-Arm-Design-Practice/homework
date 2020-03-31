a = input("輸入任意整數數值: ")

while 1:
    if(a.isdecimal()==True):
        print("此數值為正整數： ",a)
        break
    else:
        a = input("重新輸入數值： ")
        continue