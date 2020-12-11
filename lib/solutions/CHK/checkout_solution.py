

# noinspection PyUnusedLocal
# skus = unicode string
import re
def checkout(skus):
    price_table ={
        # "A": {
        #     "price" : 50,
        #     "required_unit_for_offer" : 3,
        #     "special_price" : 130 
        #      },
        # "B":  {
        #     "price" : 30,
        #     "required_unit_for_offer" : 2,
        #     "special_price" : 45 
        #      },
        # "C" : 20,
        # "D": 15,
        
    }

    skus = skus.upper()

    if type(skus) == str and not skus.isdigit():

        if len(skus) == 1:
            if type(price_table[skus]) == int:
                return price_table[skus]
            else:
                return price_table[skus]["price"]
        else:
            match  = re.match(r"([0-9])([a-z]+)",skus,re.I)
            if match:
                item = match.groups()
                if len(item[1]) == 1:
                    if type(price_table[item[1]]) == int:
                        return int(item[0]) * price_table[item[1]]
                    else:
                        required_unit = price_table[item[1]]["required_unit_for_offer"]
                        if int(item[0]) == required_unit:
                            return price_table[item[1]]["special_price"]
                        else:
                            remaining_unit = int(item[0]) % price_table[item[1]]["required_unit_for_offer"]
                            discounted_unit = (int(item[0]) - remaining_unit) // price_table[item[1]]["required_unit_for_offer"]
                            final_total = discounted_unit * price_table[item[1]]["special_price"] + remaining_unit * price_table[item[1]]["price"]
                            return final_total
                else:
                    return -1
            else:
                return -1
    else:
        return -1


print(checkout(""))

