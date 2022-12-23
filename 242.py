
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # hashmap = dict()
        # for i in s:
        #     if i not in hashmap.keys():
        #         hashmap[i] = 1
        #     else:
        #         hashmap[i] = hashmap[i] + 1
        # for j in t:
        #     if j not in hashmap.keys():
        #         return False
        #     if hashmap[j] == 0:
        #         return False
        #     hashmap[j] -= 1
        # return True
        # if tuple(sorted(s)) == tuple(sorted(t)):
        #     return True
        # return False
        if len(s) != len(t):
            return False
        ss= [0]*26
        tt= [0]*26
        for i in range(len(s)):
            ss[ord(s[i])-ord('a')] += 1
            tt[ord(t[i])-ord('a')] += 1
        if tuple(ss) == tuple(tt):
            return True
        return False



#%%
a = " adsd"
# for i in range(len(a)):
for i in a:
    print(i)
# %%
a = dict()
a['1'] = [2]
a['2'] = [4,5]
# a.get('1',0)
list(a.values())
a['1'].append(3)
a['1']
# %%
a=[1,2,3]
i = 1
# a.index(2,0,1)
# a.index(2,2,3)
a.append(4)
a
# %%
a = set()
a.add(1)
a.add(2)
list(a)
# %%
import collections
collections.defaultdict(list)
# %%
tuple([0] * 26)
# %%
ord("a")
# %%
a='abbcca'
sorted(a)
# %%
