from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        str_finals = {}

        for me in strs:
            mydict = {}
            for i in me:
                mydict[i] = 1 + mydict.get(i,0)
            flag = False
            for k, v in str_dict.items():
                if mydict == v:
                    flag = True
                    str_finals[k].append(me)
            if not flag:
                str_dict[me] = mydict
                str_finals[me] = [me]
        return list(str_finals.values())
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            print(ans['q'])

            ans[tuple(count)].append(s)
        return ans.values()

a = Solution()
b = a.groupAnagrams1(["eat","tea","tan","ate","nat","bat"])
print(b)