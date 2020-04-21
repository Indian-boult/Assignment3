def myreduce(fun, arr):
    result = arr[0]
    for i in range(1,len(arr)):
        result = fun(result, arr[i])
    return result


input_arr = [1,2,3,4,5]
print(myreduce((lambda x, y: x+y), input_arr))