

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
                        
                        #comparing unit to qulify the max discount
                        while unit >= min(sorted_producted_list):
                            if unit >= sorted_producted_list[start_index]:
                                unit = unit - sorted_producted_list[start_index]

                                if str(sorted_producted_list[start_index]) in offer_count.keys():
                                    offer_count[str(sorted_producted_list[start_index])] += 1
                                
                                if unit < sorted_producted_list[start_index]:
                                    start_index = start_index + 1
                            
                            else:
                                unit = unit - sorted_producted_list[start_index + 1]
                                if str(sorted_producted_list[start_index + 1]) in offer_count.keys():
                                    offer_count[str(sorted_producted_list[start_index +1])] += 1

                        # calculating total payment based on qulified unit 
                        for required_unit , product_count in offer_count.items():
                            total_payment += product_count * price_table[products]["required_unit_for_offer"][required_unit]

                        if unit > 0:
                            total_payment += unit * price_table[products]["price"]

                                    

                    
                else:
                    #calculating item based offer
                    if price_table[products]["item_offer"] == True:
                        
                        # checking dicounnt qulifiy 
                        if unit < min(product_list):
                            total_payment += unit * price_table[products]["price"]

                        else:
                            if str(unit) in price_table[products]["required_unit_for_offer"]:

                                if price_table[products]["required_unit_for_offer"][str(unit)]["free_item"] in no_of_unit.keys():
                                    total_payment += unit * price_table[products]["price"]
                                    discount_for_free_item += price_table[price_table[products]["required_unit_for_offer"][str(unit)]["free_item"]]["price"]
                                else:
                                    total_payment += unit * price_table[products]["price"]

                            else:
                                closest_unit = min(product_list,key=lambda x: abs(x-unit))

                                if price_table[products]["required_unit_for_offer"][str(closest_unit)]["free_item"]  in no_of_unit.keys():

                                    if  unit > closest_unit:
                                        total_price = payment_generater(unit,closest_unit,price_table,products)
                                        total_payment += total_price[0]
                                        discount_for_free_item += total_price[1]
                                    else:
                                        closest_unit = product_list[product_list.index(closest_unit)-1]
                                        total_price = payment_generater(unit,closest_unit,price_table,products)
                                        total_payment += total_price[0]
                                        discount_for_free_item += total_price[1]

                                else:
                                    total_payment += unit * price_table[products]["price"]   
                    else:
                        total_payment += (unit * price_table[products]["price"])
            return total_payment - discount_for_free_item
        else:
            return -1
        
# calculating total payment and discount item price
def payment_generater(unit,closest_unit,price_table,products):
    extra_unit = unit % closest_unit
    pair_of_unit  = (unit - extra_unit) // closest_unit
    total = unit * price_table[products]["price"]
    discount_price = checkout(pair_of_unit * price_table[products]["required_unit_for_offer"][str(closest_unit)]["free_item"])
    return (total,discount_price)
    




print("EEEEBBBB", checkout("EEEEBBBB"))
print("", checkout(""))
print("A", checkout("A"))
print("B", checkout("B"))
print("C", checkout("C"))
print("D", checkout("D"))
print("E", checkout("E"))
print("a", checkout("a"))
print("-", checkout("-"))
print("ABCa", checkout("ABCa"))
print("AxA", checkout("AxA"))
print("AA", checkout("AA"))
print("AAA", checkout("AAA"))
print("AAAA", checkout("AAAA"))
print("AAAAA", checkout("AAAAA"))
print("EE", checkout("EE"))
print("EEB", checkout("EEB"))
print("EEEB", checkout("EEEB"))
print("BBBBE", checkout("BBBBE"))
print("ABCDEABCDE", checkout("ABCDEABCDE"))
print("CCADDEEBBA", checkout("CCADDEEBBA"))
print("AAAAAEEBAAABB", checkout("AAAAAEEBAAABB"))
print("ABCDECBAABCABBAAAEEAA", checkout("ABCDECBAABCABBAAAEEAA"))






