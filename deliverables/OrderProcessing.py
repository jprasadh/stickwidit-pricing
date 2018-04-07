
# Suppose you have 4 different sheet stickers and 4 different individual stickers,
# each with unique product ID.
# Let's say for now that the product ID is a 3-digit number.
# First digit 1 tells you it's an individual sticker, 2 tells you it's a sticker sheet.
# Last couple digits tell you which particular sticker it is.
# Of course, you can change the numbering scheme as you see fit.

# An order is structured as a list of tuples (a list of sublists, each with 2 elements).
# The first element in each tuple is a product ID, and the second element is a quantity.
# For example, order0 is a sample order.
order0 = [[202, 2], [103, 1], [204, 6]]

# Each order has 2 total areas, one for individual stickers and another for sticker sheets
# since they are priced differently.


# This function calculates these areas for any order structured like order0.
# It returns a list [Total area of single stickers, Total area of sticker sheets].
def get_area(order):
    # The stickers have sizes (in sq-ft) given by:
    sizes = {101: 0.5, 102: 0.75, 103: 1.0, 104: 0.006, 201: 1.0, 202: 2.3, 203: 0.9, 204: 2.1}
    singles_area = 0
    sheets_area = 0
    for item in order:
        if item[0] < 200:       # This inequality will have to be adjusted if product ID scheme changes.
            singles_area += item[1] * sizes[item[0]]
        else:
            sheets_area += item[1] * sizes[item[0]]
    return [singles_area, sheets_area]


# Price function for single stickers
def singles_price(area):
    B = 18
    H = 2.75
    r = 0.45
    gamma = 0.0005
    return H + B * (1 + area) ** -(r + gamma * area)


# Price function for sheet stickers
def sheets_price(area):
    B = 22
    H = 2.50
    r = 0.4
    gamma = 0.0004
    return H + B * (1 + area) ** -(r + gamma * area)


# Finally, the total price of an order is given by this function.
def get_total_price(order):
    singles_total = get_area(order)[0] * singles_price(get_area(order)[0])
    sheets_total = get_area(order)[1] * sheets_price(get_area(order)[1])
    # Enforcing minimum order value of $15
    if singles_total + sheets_total < 15:
        order_total = 15
    else:
        order_total = singles_total + sheets_total
    return order_total


very_small_order = [[104, 25]]
print(get_total_price(very_small_order))
