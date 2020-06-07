def calc_discount(price, discount):
    while True:
        try:
            price = float(input("How much does your item cost? \n... \n$"))
            discount = float(input("Is there a discount? \nExample: 25% discount = enter \'25\'\n..."))
        except ValueError:
            print("Please enter a valid number. \n...")
            continue
        else:        
            discount_value = discount/100
            discount_amount = price * discount_value
            new_price = price - discount_amount
            print("The price of ${} with {}% discount is ${}. ".format(price, discount, new_price))
            print("You saved a total of ${}. ".format(discount_amount))
            break

# price and discount

calc_discount(0, 0)
