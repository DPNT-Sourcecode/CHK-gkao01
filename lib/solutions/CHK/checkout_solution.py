

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_table ={
        "A": 50,
        "B": 30,
        "C" : 20,
        "D": 15,
        "special_offer": {
            "3A" : 130,
            "2B" : 45
        }
    }

    if type(skus) == str:
        if len(skus) == 1:
            return checkout[skus]
    else:
        return -1

