

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
                                        },
            "free_item" :["B"]
                },
        "F" : {
            "price" : 10 ,
            "offer" : False,
            "item_offer": True,
            "required_unit_for_offer" : {
                                        "2":{
                                            "free_unit":1,
                                            "free_item":"F"
                                            }
                                        },
            "free_item" :["F"]
                },
        "G" : {"price" : 20, "offer" : False ,"item_offer": False},
        "H": {
            "price" : 10,
            "offer" : True,
            "item_offer": False,
            "required_unit_for_offer" : {"5": 45,"10":80},
             },
        "I" : {"price" : 35, "offer" : False ,"item_offer": False},
        "J" : {"price" : 60, "offer" : False ,"item_offer": False},
        "K":  {
            "price" : 70,
            "offer" : True,
            "item_offer": False,
            "required_unit_for_offer" : {"2": 120},
             },
        "L" : {"price" : 90, "offer" : False ,"item_offer": False},
        "M" : {"price" : 15, "offer" : False ,"item_offer": False},
        "N" : {
            "price" : 40 ,
            "offer" : False,
            "item_offer": True,
            "required_unit_for_offer" : {
                                        "3":{
                                            "free_unit":1,
                                            "free_item":"M"
                                            }
                                        },
            "free_item" :["M"]
                },
        "O" : {"price" : 10, "offer" : False ,"item_offer": False},
        "P":  {
            "price" : 50,
            "offer" : True,
            "item_offer": False,
            "required_unit_for_offer" : {"5": 200},
             },
        "Q":  {
            "price" : 30,
            "offer" : True,
            "item_offer": False,
            "required_unit_for_offer" : {"3": 80},
            },
        "R" : {
            "price" : 50 ,
            "offer" : False,
            "item_offer": True,
            "required_unit_for_offer" : {
                                        "3":{
                                            "free_unit":1,
                                            "free_item":"Q"
                                            }
                                        },
            "free_item" :["Q"]
                },
        "S" : {
                "price" : 20, 
                "offer" : False,
                "item_offer": False,
                "group_offer" : True,
                "required_unit_for_offer" : {
                                        "3": ["S","T","X","Y","Z"],
                                        "discount_price" : 45
                                        },
                
                },
        "T" : {
                "price" : 20, 
                "offer" : False,
                "item_offer": False,
                "group_offer" : True,
                "required_unit_for_offer" : {
                                        "3": ["S","T","X","Y","Z"],
                                        "discount_price" : 45
                                        },
        },
        "U" : {
            "price" : 40 ,
            "offer" : False,
            "item_offer": True,
            "required_unit_for_offer" : {
                                        "3":{
                                            "free_unit":1,
                                            "free_item":"U"
                                            }
                                        },
            "free_item" :["U"]
                },
        "V": {
            "price" : 50,
            "offer" : True,
            "item_offer": False,
            "required_unit_for_offer" : {"2": 90,"3":130},
            
             },
        "W" : {"price" : 20, "offer" : False ,"item_offer": False},
        "X" : {
                "price" : 17, 
                "offer" : False,
                "item_offer": False,
                "group_offer" : True,
                "required_unit_for_offer" : {
                                        "3": ["S","T","X","Y","Z"],
                                        "discount_price" : 45
                                        },
        },
        "Y" : {
                "price" : 20, 
                "offer" : False,
                "item_offer": False,
                "group_offer" : True,
                "required_unit_for_offer" : {
                                        "3": ["S","T","X","Y","Z"],
                                        "discount_price" : 45
                                        },
        },
        "Z" : {"price" : 21, 
                "offer" : False,
                "item_offer": False,
                "group_offer" : True,
                "required_unit_for_offer" : {
                                        "3": ["S","T","X","Y","Z"],
                                        "discount_price" : 45
                                        },

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
            group_offer = {}
            group_offer_price = {}
            discount_for_free_item = 0

            for product in order_detail:
                if price_table[product].get("group_offer") == True:
                    group_offer[product] = order_detail.count(product)
                    group_offer_price[str(price_table[product]["price"])] = {}
                    group_offer_price[str(price_table[product]["price"])][product] = order_detail.count(product)

                else:
                    no_of_unit[product] = order_detail.count(product)
            
        
            # calcute total price of group offer pair 
            if bool(group_offer):
                group_offer_total_unit = sum(group_offer.values())

                for group_product , group_unit in group_offer.items():
                    global remaining_unit_group_offer 
                    required_unit_group_offer = list(price_table[group_product]["required_unit_for_offer"].keys())

                    if int(required_unit_group_offer[0]) > group_offer_total_unit:
                        total_payment += price_table[group_product]["price"] * group_unit
                        remaining_unit_group_offer  = 0
                    else:
                        total_remaining_unit  = group_offer_total_unit % int(required_unit_group_offer[0]) 
                        total_group_offer_pair = (group_offer_total_unit - total_remaining_unit) // int(required_unit_group_offer[0])
                        total_payment += total_group_offer_pair * price_table[group_product]["required_unit_for_offer"]["discount_price"]
                        remaining_unit_group_offer = total_remaining_unit
                        break

            #calculate total group offer remaining unit price 
            if remaining_unit_group_offer > 0:

                for remaing_unit_price in sorted(group_offer_price.items()):
                    if remaining_unit_group_offer > 0:

                        if remaining_unit_group_offer >= list(remaing_unit_price[1].values())[0]:
                            remaining_unit_group_offer = remaining_unit_group_offer - list(remaing_unit_price[1].values())[0]
                            total_payment +=  list(remaing_unit_price[1].values())[0] * int(remaing_unit_price[0])
                        else:
                            total_payment += remaining_unit_group_offer * int(remaing_unit_price[0])
                            break

            
            
            for products, unit in no_of_unit.items():

                try:
                    product_list = list(map(int ,price_table[products]["required_unit_for_offer"].keys()))
                    product_list.sort()
                except:
                    pass

                if price_table[products]["item_offer"]:
                    offer_count = {}
                    same_product_free = []
                    min_required_unit =  price_table[products]["required_unit_for_offer"]

                    for free_item in price_table[products]["free_item"]:

                        if free_item in no_of_unit.keys():
                            start_index = 0
                            sorted_producted_list = product_list[::-1]

                            for product in sorted_producted_list:
                                offer_count[str(product)] = 0
   
                            #comparing unit to qulify the max discount
                            while unit >= min(sorted_producted_list):
                                if unit >= sorted_producted_list[start_index]:
                                    unit = unit - sorted_producted_list[start_index]

                                    if free_item == products:
                                        same_product_free.append(free_item)

                                    if str(sorted_producted_list[start_index]) in offer_count.keys():
                                        offer_count[str(sorted_producted_list[start_index])] += 1
                                    
                                    if unit < sorted_producted_list[start_index]:
                                        start_index = start_index + 1
                                
                                else:
                                    unit = unit - sorted_producted_list[start_index + 1]
                                    if str(sorted_producted_list[start_index + 1]) in offer_count.keys():
                                        offer_count[str(sorted_producted_list[start_index +1])] += 1

                    for qulified_unit, pair_of_unit in offer_count.items():
                        # apply max discount on same product 
                        if products in same_product_free:
                            pack_of_discount = int(qulified_unit) + min_required_unit[qulified_unit]["free_unit"]
                            buy_pack = no_of_unit[products] // pack_of_discount
                            buy_individual = no_of_unit[products] % pack_of_discount
                            no_of_unit[products] = int(qulified_unit) * buy_pack + buy_individual
                        else:
                            #apply discount any other product (only for item_offer = True)
                            no_of_unit[min_required_unit[qulified_unit]["free_item"]] = no_of_unit[min_required_unit[qulified_unit]["free_item"]] - (pair_of_unit * min_required_unit[qulified_unit]["free_unit"])

            
         
            for products, unit in no_of_unit.items():

                # ccalculating price based offer
                try:
                    product_list = list(map(int ,price_table[products]["required_unit_for_offer"].keys()))
                    product_list.sort()
                except:
                    pass

                if price_table[products]["offer"] == True and unit > 0:
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
                    if unit > 0:
                        total_payment += (unit * price_table[products]["price"])
            return total_payment - discount_for_free_item
        else:
            return -1
        


    




print("EEEEBBBB", checkout(""))




