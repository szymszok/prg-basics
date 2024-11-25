import statistics 
def sec_largest(arr):
    sort = sorted(arr)
    return sort[-2]

def diff(arr):
    maxx = max(arr)
    minn = min(arr)
    return maxx - minn

def median(arr):
    return statistics.median(arr)

def two_element(arr):
    arr1 = []
    maxx = max(arr)
    arr1.append(maxx)
    minn = min(arr)
    arr1.append(minn)
    return arr1

def string(arr):
    
    return '-'.join(map(str,arr))


arr = [7,3,8,5,2]

print('Numbers: ', arr)
print('Second largest number', sec_largest(arr))
print('Difference between max and min', diff(arr))
print('Median: ',median(arr))
print('Max and Min number in array: ', two_element(arr))
print('Separated: ',string(arr))
