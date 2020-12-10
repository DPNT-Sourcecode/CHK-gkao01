

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if type(friend_name) == str:
        return friend_name
    else:
        error  =  "Plese provide only string "
        return error

hello("hello world")


