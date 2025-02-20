class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) #sorts strings in cache to check if the strings are same
        return Counter(s) == Counter (t) #creates hashmap for both and check if they are same