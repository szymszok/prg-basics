def length(text):
    arr = text.split()
    return len(arr)

def ordered(text):
    arr = text.split()
    arr_sorted = sorted(arr, key = len, reverse=True)
    return arr_sorted

def alpha(text):
    arr = text.lower().split()
    return sorted(arr)