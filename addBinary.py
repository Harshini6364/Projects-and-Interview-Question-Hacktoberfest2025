class Solution(object):
    def addBinary(self, a, b):
        i1=int(a,2)
        i2=int(b,2)
        s=i1+i2
        return bin(s)[2:]
