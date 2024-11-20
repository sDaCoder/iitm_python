def total_price(fruit_prices: dict, purchases: list[tuple]) -> float:
    price: float = 0
    for purchase in purchases:
        fruit = purchase[0]
        quantity = purchase[1]
        price += quantity * fruit_prices[fruit]
    return price

def total_price_no_loops(fruit_prices: dict, purchases: list[tuple]) -> float:
    price: float = sum([quantity * fruit_prices[fruit] for fruit, quantity in purchases])
    return price

def find_cheapest_fruit(fruit_prices: dict) -> str:
    '''
    Find the cheapest fruit from the fruit_prices dict, do not use min function

    Arguments:
    fruit_prices: dict - fruit name as key and price as value

    Return:
    cheapest_fruit: str - the fruit with the lowest price
    '''
    cheapFruit: str = ""
    cheapest: float = float('inf')
    for fruit, price in fruit_prices.items():
        if price < cheapest:
            cheapFruit = fruit
            cheapest = price
    return cheapFruit

def find_cheapest_fruit_no_loops(fruit_prices:dict) -> str:
    '''
    Find the cheapest fruit using min function. Do not use loops
    '''
    return min(fruit_prices, key = lambda k: fruit_prices[k])

# grouping
def group_fruits(fruits:list) -> dict:
    '''
    Group the fruits based on the first letter of the names. Assume first letters will be upper case.

    Arguments:
    fruits - list: list of fruit names

    Return:
    dict: dict with the first letters as keys and list of fruits sorted in ascending order as values.
    '''
    L = []
    for fruit in fruits:
        L.append(fruit[0])

    dic = {}
    for letter in L:
        fruit_list = []
        for fruit in fruits:
            if fruit.startswith(letter):
                fruit_list.append(fruit)
        fruit_list.sort()
        dic[letter] = fruit_list
    return dic

# binning
def bin_fruits(fruit_prices: dict) -> dict:
    '''
    Classify the fruits as cheap, affordable and costly based on the fruit prices. Create a dictionary with the classification as keys and a set of fruits in that category.

    cheap - less than 3 (not inclusive)
    affordable - between 3 and 6 (both inclusive)
    costly - greater than 6 (not inclusive)

    Arguments:
    fruit_prices: dict - dictionary with fruits as keys and prices as values

    Return:
    binned_fruits: dict - dictionary with category as key and a set of fruits in that category as values.
    '''
    dic = {}
    l_cheap = set()
    l_affordable = set()
    l_costly = set()
    for fruit, price in fruit_prices.items():
        if price < 3:
            l_cheap.add(fruit)
        elif 3 <= price <= 6:
            l_affordable.add(fruit)
        else:
            l_costly.add(fruit)
    dic["affordable"] = l_affordable
    dic["cheap"] = l_cheap
    dic["costly"] = l_costly
    return dic
