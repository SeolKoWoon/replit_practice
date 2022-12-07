n = int(input(5))
data = list(map(int, input(2,3,1,2,2).split()))
data.sort()

result = 0
count = 0 

for i in data: 
    count += 1 
    if count >= i:
        result += 1 
        count = 0

print(result) # 총 그룹의 수 출력