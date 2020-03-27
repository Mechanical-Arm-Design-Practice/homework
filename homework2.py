input_number = 0
while 1:
    print("")
    num_input = input('請輸入一個數字: ')

    if  num_input.isnumeric():
        input_number = int(num_input)
    else:
        print("wrong input!")
        continue

    if input_number > 0 and input_number <10:
        for i in range (input_number+1):
            if i == 0:
                continue
            for j in range (input_number+1):
                if j == 0:
                    continue
                print(i," * ",j," = ",i*j)
    else:
        print("number not in range!!!")
