square = []
n = 1
while n <=10:
    square.append(n * n)
    n = n+1
print(square)
print("loop ended")   
print()
x = int(input("Enter the number for search:"))
i = 0
while i < len(square):
    if square[i] == x:
        print("Found at index",i)
    i=i+1

