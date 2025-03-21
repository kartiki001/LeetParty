class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1] #converted int to string and checked it reverse of sting returns is same as original string