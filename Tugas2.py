def bubble_sort(keyword, data):

    for i in range (len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]
    return binary_search(keyword,data)

def binary_search(keyword,data):
    left = 0
    right = len(data) - 1

    while left <= right :
        mid = (left+right)//2
        if str(data[mid]).lower() > keyword.lower():
            right = mid - 1
        elif str(data[mid]).lower() < keyword.lower():
            left = mid + 1
        else:
            print(data)
            print(f"Keyword {keyword} has found at indeks {mid}")
            return mid
    
    print(f"Keyword {keyword} not found")
    return -1

data = [20103023, 20103002, 20103019, 20103001, 20103017, 20103005, 20103011, 
        20103003, 20103009, 20103021,20103006, 20103015, 20103013, 20103007]
keyword = input("Input keyword :")
bubble_sort(keyword,data)