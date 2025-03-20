class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ''
        a,b = a[::-1], b[::-1] #Reverse the string as we go from left to right and addition is right to left
        for i in range(max(len(a), len(b))):
            digita = ord(a[i]) - ord("0") if i< len(a) else 0 #ord is to make the string to digit to add
            digitb = ord(b[i]) - ord("0") if i< len(b) else 0
            total = digita + digitb + carry 
            carry = str(total % 2) #OUTPUT digit stored in carry
            res = carry + res
            carry = total //2 #Carry counted
        if carry:
            res = '1' + res
        return res