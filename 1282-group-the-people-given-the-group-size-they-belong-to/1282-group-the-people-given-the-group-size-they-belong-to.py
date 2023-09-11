class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap = {}
        ans = []
        for i, size in enumerate(groupSizes):
            if size in hashmap:
                hashmap[size].append(i)            
            else:
                hashmap[size] = [i]
            
            if len(hashmap[size]) == size:
                ans.append(hashmap[size])
                del hashmap[size]
        
        for _, val in hashmap.items():
            ans.append(val)
            
        return ans