from typing import List
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = collections.defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        sort_keys = sorted(num_freq.values())
        k_freq = set()
        for i in range(k):
            k_freq.add(sort_keys[len(num_freq.keys())-i-1])

        out = []
        for key, v in num_freq.items():
            if v in k_freq:
                out.append(key)
        return out
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        print(freq)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            print(i)
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

a = Solution()
b = a.topKFrequent1([1,2],2)
print(b)