class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            print(sorted_str)
            if sorted_str in result:
                result[sorted_str].append(strs[i])
            else:
                result[sorted_str] = [strs[i]]
        return list(result.values())
