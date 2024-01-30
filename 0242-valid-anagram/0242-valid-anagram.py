class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list, t_list  = list(s), list(t)
        map_s = {}
        map_t = {}
        c = True

        if len(s_list) == len(t_list):
            for i in range(len(s_list)):
                ch1 = s_list[i]
                ch2 = t_list[i]

                if ch1 in map_s:
                    map_s[ch1] += 1
                else:
                    map_s[ch1] = 0
                    map_s[ch1] += 1

                if ch2 in map_t:
                    map_t[ch2] += 1
                else:
                    map_t[ch2] = 0
                    map_t[ch2] += 1

            for i in range(len(s_list)):
                ch1 = s_list[i]
                ch2 = t_list[i]

                if ch2 in map_s and ch2 in map_t and map_s[ch2] == map_t[ch2]:
                    continue
                else:
                    c=False
                    break


        else:
            c = False
            return c
        return c