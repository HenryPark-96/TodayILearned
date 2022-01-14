a = int(input("오늘의 농도는 얼마입니까? : "))

if a > 151 :
    print('terrible')
elif 81 < a <150 :
    print('bad')
elif 31 < a < 80 :
    print('soso')
else :
    print('good enough')
