class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += s + "😀"
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        substring = ""
        for char in s:
            if char == "😀":
                result.append(substring)
                substring = ""
            else:
                substring += char
                
        return result