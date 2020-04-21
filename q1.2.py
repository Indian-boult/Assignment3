def myfilter(fun, alphabet):
    result = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in alphabet:
        if(fun(i,vowels)):
            result.append(i)
    return result

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(myfilter((lambda x, y: x in y), alphabet))