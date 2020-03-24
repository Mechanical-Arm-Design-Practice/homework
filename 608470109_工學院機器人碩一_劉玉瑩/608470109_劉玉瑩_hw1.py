math_pass={"Tom", "John", "Mary", "Jimmy", "Sunny", "Amy"}
english_pass={"John", "Mary" , "Tony" , "Bob" , "Pony", "Tom", "Alice"}

print("數學及格但英文不及格的名單:",math_pass-english_pass)
print("數學不及格但英文及格的名單:",english_pass-math_pass)
print("兩科都及格的名單:",english_pass & math_pass)

score= {"Tom": [80, 100, 90, 95],"John": [100, 93, 75, 80]}
def score_average(x):
    sum=0
    for i in x:
        sum+=i
        sum /= len(x)
    return sum

print("Tom 平均成績：",score_average(score.get("Tom")))
print("John 平均成績：",score_average(score.get("John")))
