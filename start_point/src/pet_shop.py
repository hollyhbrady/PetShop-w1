# WRITE YOUR FUNCTIONS HERE

# didnt get this on my own. I was confused by def setUp and was treating the pet shop dict like it was embedded din another list and dict etc
# Took me approx two hours. Dan explained the first one
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# couldnt get it on my own. I was trying to create a till and assigned in the value of total_cash + cash
# Took approx an hour and half of fails until I looked at Dans example
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold
    return pet_shop["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    breed_count = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_count.append("breed")
    return breed_count

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

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

# I had del(pet) as my last line - why does that not work? if the last function works?

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

