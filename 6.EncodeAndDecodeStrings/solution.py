class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res = res + i + "#!#" 
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split("#!#")
        res.pop()
        return res
