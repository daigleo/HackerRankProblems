def getMinimumCost(k, c):
    flowers_purchased = k * [0]
    i = 0
    c = sorted(c, reverse=True)
    bill = 0
    for price_of_flower in c:
        flowers_purchased[i] += 1
        bill += flowers_purchased[i] * price_of_flower
        i += 1
        if i >= k:
            i = 0
    return bill

def getMinimumCost2(k, c):
    return sum((i // k + 1) * price 
                for i, price in enumerate(sorted(c, reverse=True))
            )



if __name__ == "__main__":
    costs = [[2, 5, 6], [2, 5, 6], [1, 3, 5, 7, 9]]
    group_sizes = [3, 2, 3]
    answers = [13, 15, 29]

    for cost, group_size, answer in zip(costs, group_sizes, answers):
        result = getMinimumCost(group_size, cost)
        print(result == answer)
        result = getMinimumCost2(group_size, cost)
        print(result == answer)