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
        if "breed" == breed
        breed_count.append


