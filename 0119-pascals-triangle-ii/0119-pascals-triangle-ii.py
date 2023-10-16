class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = []
        a.append([1])
        if rowIndex == 0:
            return a[0]
        
        a.append([1,1])
        if rowIndex == 1:
            return a[1]
        
        for i in range(2, rowIndex+1):
            a.append([1])
            for j in range(i-1):
                a[i].append(a[i-1][j]+a[i-1][j+1])
            a[i].append(1)
    
        return a[i]