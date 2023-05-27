from collections import Counter  
list = [1,2,3,4,1,2,6,7,3,8,1,2,2]  
answer=Counter()
answer = Counter(list)  
print(answer[2])  