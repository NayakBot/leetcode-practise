class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)

        counter = Counter()
        arr_deque = deque(arr)

        while True:
            first = arr_deque.popleft()
            second = arr_deque.popleft()

            if first > second:
                counter[first] += 1
                arr_deque.appendleft(first)
                arr_deque.append(second)
            else:
                counter[second] += 1
                arr_deque.appendleft(second)
                arr_deque.append(first)

            if counter[first] == k:
                return first
            if counter[second] == k:
                return second