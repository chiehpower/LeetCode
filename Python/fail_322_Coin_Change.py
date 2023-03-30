import time
class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        count = 0
        remain = amount
        coins.sort(reverse=True)
        for i in coins:
            time = remain // i
            if time > 0:
                remain = remain- time * i
                count += time

            print(f"remain: {remain}, i: {i}")
        if remain != 0:
            return -1
        else:
            return count


 
    
if __name__ == "__main__":
    Solution = Solution()

    ## Example 1

    coins = [1,2,5]
    amount = 11

    start = time.time()
    result = Solution.coinChange(coins, amount)
    print("---- Results ----")
    print(result)

    print("Time :", time.time() - start)
    if result != 3:
        print("Example 1 got a wrong answer.")
        raise
    else:
        print("Example 1 Correct!")
        
    ## Example 2

    coins = [2]
    amount = 3

    start = time.time()
    result = Solution.coinChange(coins, amount)
    print("---- Results ----")
    print(result)

    print("Time :", time.time() - start)
    if result != -1:
        print("Example 2 got a wrong answer.")
        raise
    else:
        print("Example 2 Correct!")

    ## Example 3

    coins = [1]
    amount = 0

    start = time.time()
    result = Solution.coinChange(coins, amount)
    print("---- Results ----")
    print(result)

    print("Time :", time.time() - start)
    if result != 0:
        print("Example 3 got a wrong answer.")
        raise
    else:
        print("Example 3 Correct!")


    ## Example 4

    coins = [186,419,83,408]
    amount = 6249

    start = time.time()
    result = Solution.coinChange(coins, amount)
    print("---- Results ----")
    print(result)

    print("Time :", time.time() - start)
    if result != 20:
        print("Example 4 got a wrong answer.")
        raise
    else:
        print("Example 4 Correct!")


