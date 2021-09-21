def count_positives_sum_negatives(arr):
    positive=negative=0
    if arr==[]: return[]
    for i in range (0,len(arr)):
        if arr[i]>0: positive+=1
        else: negative+=arr[i]
    arr=[positive,negative]

    return(arr)