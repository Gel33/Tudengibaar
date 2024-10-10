import random

def adjust_price(drink, drinks):
    # Store the current price before adjustment
    previous_price = drink['current_price']

    # Increase the price of the sold drink
    drink['current_price'] = min(drink['current_price'] + 0.12, drink.get('max_price', float('inf')))  # Increase price by 12 cents, not exceeding max

    # Update the price history
    drink['price_history'].append(drink['current_price'])

    # Decrease the price of 3 random drinks
    available_drinks = [d for d in drinks if d['name'] != drink['name']]
    random_drinks = random.sample(available_drinks, min(3, len(available_drinks)))  # Avoids error if fewer than 3 drinks
    for d in random_drinks:
        d['current_price'] = max(d['current_price'] - 0.04, d['min_price'])  # Decrease price by 4 cents, not below min
        # Update the price history
        d['price_history'].append(d['current_price'])

    drink['current_price'] = round(drink['current_price'], 2)

