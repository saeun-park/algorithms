class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        
        dict1, dict2 = {}, {}

        for cur1, cur2 in (word1, word2):
            dict1[cur1] = dict1.get(cur1, 0)+1
            dict2[cur2] = dict2.get(cur2, 0)+1

        return sorted(dict1.values()) == sorted(dict2.values())