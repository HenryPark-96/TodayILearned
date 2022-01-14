# random 모듈 불러오기
import random

# 숫자 통 (1 ~ 45)
numbers = range(1, 46)

# 숫자 통에서 6개를 sample
lotto_num = random.sample(numbers, 6)

# print
print(lotto_num)
print('---------------------------------------------')

# sample one
a = random.sample(range(1, 46), 6)

print(a)
print('---------------------------------------------')

print(random.sample(range(1, 46), 1))
print('---------------------------------------------')

# 5번 번호 '리스트'를 뽑는다.
for i in range(5):
    #numbers 리스트에서 6개를 ramdom하게 뽑는다. 
    lotto_number = random.sample(numbers, 6)
    # 정렬되게 출력한다.
    print(sorted(lotto_number))

print('---------------------------------------------')
# use function
def lotto_function(n):

    for i in range(n):
        print(random.sample(numbers, 6))

lotto_function(6)