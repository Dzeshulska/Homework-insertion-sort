# insertion sort
arr = [2,1,3,5,2]
arr_lenght = len(arr)

for i in range(1, arr_lenght):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] == arr[j-1], arr[j]
            
        else:
            break

print(arr)            