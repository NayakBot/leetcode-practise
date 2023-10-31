class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if not pref:
            return pref
        cur = pref[0]
        res = [cur]

        for n in pref[1:]:
            ind = cur ^ n
            res.append(ind)
            cur = cur ^ ind

        return res