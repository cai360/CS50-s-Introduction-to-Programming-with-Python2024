menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }


def main():
    get_order()


def get_order():
    total_price = 0
    while True:
        try:
            key = input("Item: ").title()
            if key in menu:
                total_price += menu[key]
                screen(total_price)

        except EOFError:
            break

def screen(p):
    p = print(f"Total: ${p:.2f}")


main()
