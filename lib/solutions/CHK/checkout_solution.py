

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    price_table ={
        "A": {
            "price" : 50,
            "offer" : True,
            "item_offer": False,
            "required_unit_for_offer" : {"3": 130,"5":120},
            
             },
        "B":  {
            "price" : 30,
            "offer" : True,
            "item_offer": False,
            "required_unit_for_offer" : 2,
            
             },
        "C" : {"price" : 20, "offer" : False ,"item_offer": False},
        "D": {"price" : 15, "offer" : False,"item_offer": False},
        "E" : {
            "price" :40 ,
            "offer" : False,
            "item_offer": True,
            "required_unit_for_offer":{
                                        "2":{
                                            "free_unit":1,
                                            "free_item":"B"
                                            }
                                        }
                }
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
                    product_list = list(map(int ,price_table[product]["required_unit_for_offer"].keys()))
                    product_list.sort()
                    if unit < min(product_list):
                        total_payment += unit * price_table[products]["price"]
                    else:
                        if str(unit) in price_table[products]["required_unit_for_offer"]:
                            total_payment +=  price_table[products]["required_unit_for_offer"][str(unit)]
                        else:
                            closest_unit =  min(product_list,key=lambda x: abs(x-unit))
                            print(closest_unit)
                            # if unit < closest_unit:

                            # extra_unit = unit % price_table[products]["required_unit_for_offer"]
                            # pair_of_unit  = (unit - extra_unit) // price_table[products]["required_unit_for_offer"]
                            # total_price = pair_of_unit * price_table[products]["special_price"] + extra_unit * price_table[products]["price"]
                            # total_payment += total_price
                    
                else:
                    total_payment += (unit * price_table[products]["price"])
            return total_payment
        else:
            return -1
        


print(checkout("AAAA"))


