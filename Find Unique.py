def find_uniq(arr):
    n = 0
    suspect = 0
    for i in range(1, len(arr)):
        print arr[i]
        if arr[i] != arr[0]:
            suspect = arr[i]
            print 'test'
            break
    if suspect != arr[1]:
        #print suspect
        n = suspect
        #print n
    elif arr[1] != arr[2]:
        n = arr[1]
    else:
        n = arr[0]

    print n  # n: unique integer in the array

find_uniq([1,4,1,1,1,1,1,1,1])