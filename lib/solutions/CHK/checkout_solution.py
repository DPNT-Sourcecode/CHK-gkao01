

# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    price_table ={
        "A": {
            "price" : 50,
            "offer" : True,
            "item_offer": False,
            "required_unit_for_offer" : {"3": 130,"5":200},
            
             },
        "B":  {
            "price" : 30,
            "offer" : True,
            "item_offer": False,
            "required_unit_for_offer" : {"2": 45},
            
             },
        "C" : {"price" : 20, "offer" : False ,"item_offer": False},
        "D": {"price" : 15, "offer" : False,"item_offer": False},
        "E" : {
            "price" :40 ,
            "offer" : False,
            "item_offer": True,
            "required_unit_for_offer" : {
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
            discount_for_free_item = 0

            for product in price_table:
                if product in order_detail:
                    no_of_unit[product] = order_detail.count(product)
         
            for products, unit in no_of_unit.items():

                # ccalculating price based offer
                try:
                    product_list = list(map(int ,price_table[products]["required_unit_for_offer"].keys()))
                    product_list.sort()
                    print("product_list",product_list)
                except:
                    pass
                if price_table[products]["offer"] == True:
                    sum_of_offer_price  = sum(price_table[products]["required_unit_for_offer"].values())



                    if unit < min(product_list):
                        total_payment += unit * price_table[products]["price"]
                    elif unit in product_list:
                        total_payment += price_table[products]["required_unit_for_offer"][str(unit)]
                    else:
                        start_index = 0
                        offer_count = {}
                        sorted_producted_list = product_list[::-1]
                        for offer_item in sorted_producted_list:
                            offer_count[str(offer_item)] = 0
                        print("offer_item", offer_count)
                        print("sorted product", sorted_producted_list)

                        while unit >= min(sorted_producted_list):
                            if unit > sorted_producted_list[start_index]:
                                unit = unit - sorted_producted_list[start_index]

                                if str(sorted_producted_list[start_index]) in offer_count.keys():
                                    offer_count[str(sorted_producted_list[start_index])] += 1
                                
                                if unit < sorted_producted_list[start_index]:
                                    start_index += 1
                            
                            else:
                                unit = unit -sorted_producted_list[start_index +1 ]
                                if str(sorted_producted_list[start_index + 1]) in offer_count.keys():
                                    offer_count[str(sorted_producted_list[start_index +1])] + 1

                                    

                    
                else:
                    #calculating item based offer
                    if price_table[products]["item_offer"] == True:
                        product_list = list(map(int ,price_table[products]["required_unit_for_offer"].keys()))
                        product_list.sort()
                        if unit < min(product_list):
                            total_payment += unit * price_table[products]["price"]
                        else:
                            if str(unit) in price_table[products]["required_unit_for_offer"]:
                                if price_table[products]["required_unit_for_offer"][str(unit)]["free_item"] in no_of_unit.keys():
                                    total_payment += unit * price_table[products]["price"]
                                    discount_for_free_item += price_table["B"]["price"]
                                else:
                                    total_payment += unit * price_table[products]["price"]
                            else:
                                closest_unit = min(product_list,key=lambda x: abs(x-unit))
                                if price_table[products]["required_unit_for_offer"][str(closest_unit)]["free_item"]  in no_of_unit.keys():
                                    if  unit > closest_unit:
                                        total_price = payment_generater(unit,closest_unit,price_table,products,True)
                                        total_payment += total_price[0]
                                        discount_for_free_item += total_price[1]
                                    else:
                                        closest_unit = product_list[product_list.index(closest_unit)-1]
                                        total_price = payment_generater(unit,closest_unit,price_table,products,True)
                                        total_payment += total_price[0]
                                        discount_for_free_item += total_price[1]

                                else:
                                    total_payment += unit * price_table[products]["price"]   
                    else:
                        total_payment += (unit * price_table[products]["price"])
            return total_payment - discount_for_free_item
        else:
            return -1
        

def payment_generater(unit,closest_unit,price_table,products,item_free):
    extra_unit = unit % closest_unit
    pair_of_unit  = (unit - extra_unit) // closest_unit
    if item_free:
        total = unit * price_table[products]["price"]
        discount_price = pair_of_unit * price_table[products]["required_unit_for_offer"][str(closest_unit)]["free_unit"] * price_table[price_table[products]["required_unit_for_offer"][str(closest_unit)]["free_item"]]["price"]
        return (total,discount_price)
    else:
        total_price = pair_of_unit * int(price_table[products]["required_unit_for_offer"][str(closest_unit)]) + extra_unit * price_table[products]["price"]
        return total_price


print(checkout("AAAA"))



