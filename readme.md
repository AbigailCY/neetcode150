### Arrays & Hashing

1. 217 - Contains Duplicate
   - Hashset: set()
2. 242 - Valid Anagram
   - Hashmap: dict()

3. 1 - two sum
   - `dict.get(num) = None`	`dict.get(num, 0)`
   - hashmap get: O(1)
   - List.index(value, start, end): O(n) but reduce memory

4. 49 - Group Anagrams
   - the key must be unique and immutable. This means that a Python Tuple can be a key whereas a Python List can not. 
   - `collections.defaultdict(list)`
   - approach count:  `ord("a")= 97, ord("d-a") = 3`  O(NK)
   - approach sorted str: `key = tuple(sorted(s))`  O(NKlog(k))

5. 347 - Top K Frequent Elements

   - Heapq???

   - less than nlogn ---> O(n):

     reverse dic to freq (freq can have duplicate values)


6. 238 - Product of Array Except Self
   - prefix and suffix

### Two Pointers



### Sliding Window



### Stack



### Binary Search



### Linked List



### Trees



### Tries



### Heap / Priority Queue



### Backtracking



### Graphs



### Advanced Graphs



### 2-D Dynamic Programming



### Greedy



### Math & Geometry



### Bit Manipulation