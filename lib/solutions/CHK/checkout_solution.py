

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table ={
        "A": {
            "price" : 50,
            "required_unit_for_offer" : 3,
            "special_price" : 130 
             },
        "B":  {
            "price" : 30,
            "required_unit_for_offer" : 2,
            "special_price" : 45 
             },
        "C" : 20,
        "D": 15,
        
    }
    skus = skus.upper()
    if type(skus) == str and not skus.isdigit():
        if len(skus) == 1:
            if type(price_table[skus]) == int:
                return price_table[skus]
            else:
                return price_table[skus]["price"]
        else:
            pass


    else:
        return -1


print(checkout("c"))

