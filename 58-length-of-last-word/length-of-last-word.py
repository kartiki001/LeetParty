class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1]) # Split the string based on spaces -> converts it to list. return length of -1th indexed string in the list