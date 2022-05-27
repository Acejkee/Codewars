def first_non_consecutive(arr):
    for i,j in enumerate(arr,arr[0]):
        if i!=j:
            return j