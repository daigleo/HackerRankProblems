def maximumToys(prices, budget):
    prices = sorted(prices)
    total_price = 0
    count = 0

    for item in prices:
        if item + total_price > budget:
            break
        total_price += item
        count += 1

    return count


if __name__ == '__main__':
    budget = 50
    items = [1, 12, 5, 111, 200, 1000, 10]

    print(maximumToys(items, budget))