# 1 
# didnt get this on my own. I was confused by def setUp and was treating the pet shop dict like it was embedded din another list and dict etc
# Took me approx two hours. Dan explained the first one
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# 2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# 3
# couldnt get it on my own. I was trying to create a till and assigned in the value of total_cash + cash
# Took approx an hour and half of fails until I looked at Dans example
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    return pet_shop["admin"]["total_cash"]

# 4
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# 5
def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold
    return pet_shop["admin"]["pets_sold"]

# 6
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# 7
def get_pets_by_breed(pet_shop, breed):
    breed_count = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_count.append("breed")
    return breed_count

# 8
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

    # ^^ Help from Kieran to get this from below

    # def find_pet_by_name(pet_shop, name):
    #     name_list = []
    #     for pet in pet_shop["pets"]:
    #         if pet["name"] == name:
    #             name_list.append("name")
    #     return name_list

    # ("name" == name) in pet_shop["pets"]
    # if False:
    #     return None # This one works for .assertIsNone line 130

    # ("name" == name) in pet_shop["pets"] #False is not none
    # if True:
    #     return pet_shop["pets"]["name"]
    # else: 
    #     return None    

    # return pet_shop(["pets"]["name"] == name)
#   go through the list of pets 
#   find the one with name of Arthur

# find specified pet and delete them from the list

# 9
def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

# I had del(pet) as my last line - why does that not work? if the last function works?

# 10
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

# 11
def get_customer_cash(customers):
    return customers["cash"]
    # doesnt this just look at the cash of the first customer?
    # why does the test have customers[0]?

# 12
def remove_customer_cash(customers, value):
    customers["cash"] -= value
    # return customers["cash"] - realised I didnt need this return

# 13
def get_customer_pet_count(customers):
    # pet_count = 0
    # customers["pets"].append(pet_count)
    # return pet_count

    #logic behind trying this was create a var and then add to it if there was a result in customers pets. Looking back on it, i dont know why I did that.

    return len(customers["pets"])

# I asked Lina for help on hte next one and she told me this one was wrong and to use len

# 14
def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)
    
    # customers["pets"] = new_pet["name"] # trying to add the new pet name to a customer
    # customers["pets"].append(new_pet) # trying to append the whole new_pet dict to customers pet key
    
    

