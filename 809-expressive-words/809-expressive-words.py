class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        compressed_char = [s[0]]
        compressed_freq = [1]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                compressed_freq[-1]+=1
            else:
                compressed_char.append(s[i])
                compressed_freq.append(1)
        res = 0
        for word in words:
            compressed_char_word = [word[0]]
            compressed_freq_word = [1]
            for i in range(1,len(word)):
                if word[i]==word[i-1]:
                    compressed_freq_word[-1]+=1
                else:
                    compressed_char_word.append(word[i])
                    compressed_freq_word.append(1)
            if compressed_char_word==compressed_char:
                ok = 1
                for j in range(len(compressed_char_word)):
                    if compressed_freq[j]!=compressed_freq_word[j]:
                        if compressed_freq[j]<3 or compressed_freq[j]<compressed_freq_word[j]:
                            ok = 0 
                            break 
                res += ok
        return res