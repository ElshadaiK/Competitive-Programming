def maximumToys(prices, k):
    # Write your code here
    budget = k
    items = []
    for i in range(len(prices)):
        if(prices[i] > k):
            pass
        if(items != [] and prices[i] > budget):
            if(max(items) < prices[i]):
                pass
            else:
                budget += max(items)
                items.remove(max(items))
                budget -= prices[i]
                items.append(prices[i])
        elif(prices[i] > budget):
                pass
        else:
            budget -= prices[i]
            items.append(prices[i])
    return len(items)