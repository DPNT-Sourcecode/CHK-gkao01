

# noinspection PyUnusedLocal
# skus = unicode string
import re
def checkout(skus):
    price_table ={
        "A": {
            "price" : 50,
            "offer" : True
            "required_unit_for_offer" : 3,
            "special_price" : 130 
             },
        "B":  {
            "price" : 30,
            "offer" : True
            "required_unit_for_offer" : 2,
            "special_price" : 45 
             },
        "C" : {"price" : 20, "offer" : False },
        "D": {"price" : 15, "offer" : False} 
    }

    if len(skus) <= 1:
        if len(skus) == 0:
            return 0
        else:
            try:
                return price_table[skus]["price"]
            except:
                return -1
    else:
        if skus.isupper() and skus.isalpha():
            order_detail = list(skus)
            total_payment = 0
            no_of_unit = {}

            for product in price_table:
                if product in order_detail:
                    no_of_unit[product] = order_detail.count(product)

            for products, unit in no_of_unit.items():
                if price_table[products]["offer"] == True:
                    if price_table[products]["required_unit_for_offer"] == unit:
                        total_payment += price_table[products]["special_price"]
                    else:
                        extra_unit = unit % price_table[products]["required_unit_for_offer"]
                        pair_of_unit  = (unit - extra_unit) // price_table[products]["required_unit_for_offer"]
                        total_price = pair_of_unit * price_table[products]["special_price"] + extra_unit * price_table[products]["price"]
                        total_payment += total_price
                    
                else:
                    total_payment += (unit * price_table[products]["price"])
            return total_payment
        else:
            return -1
        




print(checkout("A2"))

