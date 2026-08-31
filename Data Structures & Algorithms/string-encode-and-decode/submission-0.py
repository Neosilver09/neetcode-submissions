class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            longeur = str(len(word))
            encoded += longeur + "#" + word
        return encoded



    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            j = s.find("#",i)
            length = int(s[i:j])
            word = [letter for letter in s[j+1:j+length+1]]
            word = "".join(word)
            decoded.append(word)
            i += j-i + length + 1
        return decoded



