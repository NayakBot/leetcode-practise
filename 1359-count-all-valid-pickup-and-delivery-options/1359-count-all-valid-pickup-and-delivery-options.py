class Solution:
    def countOrders(self, n: int) -> int:
        output = 1

        places = 2 * n

        while places > 0:
            choices = (places * (places - 1)) // 2
            output *= choices
            places -= 2

        return output % (1000000000 + 7)

# for a single p1,d1 combination consider n*n-1 ways to places them
# half of them are invalid
# repeat this for all orders