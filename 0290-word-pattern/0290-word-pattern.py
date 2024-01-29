class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")

        map_patt, map_s ={}, {}
        c = True

        if len(pattern) != len(s_list):
            c = False
        else:
            for i in range(len(pattern)):
                ch1 = pattern[i]
                ch2 = s_list[i]

                if ((ch1 in map_patt and map_patt[ch1] != ch2) or 
                    (ch2 in map_s and map_s[ch2] != ch1)):
                    c = False
                    break
                else:
                    map_patt[ch1] = ch2
                    map_s[ch2] = ch1
        return c