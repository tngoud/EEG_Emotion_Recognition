def selectionSort(arr, n):
    # code here
    # select the minimum element from the rest of elements, and push it
    for i in range(n):
        j = i
        for k in range(i, n):
            if arr[k] < arr[j]:
                j = k
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def bubbleSort(arr,n):

    # push the maximum element by swapping the adjacent elements
    for i in range(n):

        for j in range(i, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

def insertionSort(arr, n):

        # sorts the all the elements upto a certain point
        for i in range(n):

            for j in range(i, 0, -1):

                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]

        return arr

def mergeSort(arr,n):

    def merge(start, end):

        i = start
        j = (start + end)//2 + 1
        print(start, end, i,j)
        while i <= (start + end)//2 and j <= end:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                j+=1
            i+=1

            print(i,j)

        print(start, end, arr)




    def divide(start, end):

        # print(start, end)
        if start == end:
            return


        divide(start, (start + end) // 2)
        divide((start + end) // 2 + 1, end)

        merge(start, end)


    divide(0, n)
    return arr

# 0,8 -> 0,4 -> 0,2 -> 0,1


# print(bubbleSort([3,2,2,3,2,5,895,3], 8))
# print(selectionSort([3,2,2,3,2,5,895,3], 8))
# print(insertionSort([3,2,2,3,2,5,895,3], 8))
print(mergeSort([3,2,2,3,2,5,895,3], 7))