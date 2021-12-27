def solution(arr1, arr2, k):
    arr2.sort()
    result = 0
    for num in arr1:
        if abs(num - arr2[0]) <= k or abs(num-arr2[-1]) <= k:
            continue
        else:
            result += 1
    return result


a = [3, 4, 5]
b = [12, 8, 10]
d = 4
print(solution(a, b, d))



# 3
# 2

# [5,4,3,2,1]


def bs(arr, left, right, k):
    n = len(arr) 
    if left + 1 >= right:
        if left < right:
            if right < n and arr[right] < k:
                return arr[right]
            elif left < n and arr[left] <= k:
                return arr[left]
            else:
                return arr[0]
        elif left == right:
            if left < n and arr[right] <= k:
                return arr[left]
            else:
                return arr[0]
    mid = (left + right) // 2
    if arr[mid] == k:
        return bs(arr, mid + 1, right, k)
    elif arr[mid] < k:
        return bs(arr, mid, right, k)
    else:
        return bs(arr, left, mid - 1, k)
a = [-3]
target = -3

print(bs(a, 0, len(a) - 1, target))