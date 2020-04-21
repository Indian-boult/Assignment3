
input_arr = ['x','y','z']
result = [item*num for item in input_arr for num in range(1,5)]
print(result)


input_arr = ['x','y','z']
result = [item*num for num in range(1,5) for item in input_arr]
print(result)

input_arr = [2,3,4]
result = [[item+num] for item in input_arr for num in range(0,3)]
print(result)



input_arr = [2,3,4,5]
result = [[item+num for item in input_arr] for num in range(0,4)]
print(result)


input_arr=[1,2,3]
result = [(b,a) for a in input_arr for b in input_arr]
print(result)