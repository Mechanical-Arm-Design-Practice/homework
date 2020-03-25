 math_pass={'Tom','John','Mary','Jimmy','Sunny','Amy'}
eng_pass={'John','Mary','Tony','Bob','Pony','Tom','Alice'}
print('數學及格但英文不及格的人有',math_pass-eng_pass)
print('數學不及格但英文及格的人有',eng_pass-math_pass)
print('兩科都及格的人有',math_pass&eng_pass)
print('我不知道全班有多少同學，但數學和英文至少有一科及格的人有',math_pass|eng_pass,'\n')



 Score={'Tom':[80,100,90,95],'John':[100,93,75,80]}
print('Tom的平均分數是',sum(Score['Tom'])/len(Score['Tom']))
print('John的平均分數是',sum(Score['John'])/len(Score['John']),'\n')