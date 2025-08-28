class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            length = ""
            while s[j] != "#":
                length += s[j]
                j = j + 1
            str = s[j + 1 : (j + 1 + int(length))]
            i = j + 1 + int(length)
            res.append(str)
        return res
