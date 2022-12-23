class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = dict()
        for i in s:
            if i not in hashmap.keys():
                hashmap[i] = 1
            else:
                hashmap[i] = hashmap[i] + 1
        for j in t:
            if j not in hashmap.keys():
                return False
            if hashmap[j] == 0:
                return False
            hashmap[j] -= 1
        return True


#%%
a = " adsd"
# for i in range(len(a)):
for i in a:
    print(i)
# %%
a = dict()
a['1'] = 0
a.get('1')
# %%
a=[1,2,3]
i = 1
a.index(2,0,1)
a.index(2,2,3)
# %%
