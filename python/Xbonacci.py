def Xbonacci(signature,n):
    newsig = signature
    x= len(signature)
    for i in range(n):
        lastthree = signature[-x:]
        nextItem = sum(lastthree)
        newsig.append(nextItem)
    return newsig[0:n]


# test.describe("Basic tests")
# test.assert_equals(Xbonacci([0,1],10),[0,1,1,2,3,5,8,13,21,34])
# test.assert_equals(Xbonacci([1,1],10),[1,1,2,3,5,8,13,21,34,55])
# test.assert_equals(Xbonacci([0,0,0,0,1],10),[0,0,0,0,1,1,2,4,8,16])
# test.assert_equals(Xbonacci([1,0,0,0,0,0,1],10),[1,0,0,0,0,0,1,2,3,6])
# test.assert_equals(Xbonacci([1,0,0,0,0,0,0,0,0,0],20),[1,0,0,0,0,0,0,0,0,0,1,1,2,4,8,16,32,64,128,256])
