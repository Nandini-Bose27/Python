import random
import time

list1 = [0, 1]
count =0 

n = int(input("Enter n: ")) 
total = n*n

#initalizing list
arr = [[0 for _ in range(n)] for _ in range(n)]

#randomly setting 1 or 0 to 2d list
for i in range(n):
    for j in range(n):
        arr[i][j] = random.choice(list1)

print(arr)

#logic
start_time = time.time()

for i in range(n):
    for j in range(n):
        if(arr[i][j]==1):
            
            arr[i][j]=0
            print("room cleaned is", i, j)
            count+=1

end_time = time.time()

print("the number of rooms cleaned is", count)

print("the room cleaning efficiencyis", (count/total)*100)
            
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")
