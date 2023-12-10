# Note: *args = tuple, **kwargs = dict

# The purpose of this program is to create 
# a shipping label through user input

# Based on Singapore Address Context
# Source: https://www.addressexamples.com/singapore-address-format/

# Line 1: [Recipient Name]
# Line 2: [block/building/house number] [street name]
# Line 3: [unit number] [building name]
# Line 4: [Locality/Country + Postal_code]
# Line 5: [Country]
# Line 6: [PO-BOX]
# Some house do not have unit number and/or building name
# PO Box is optional as not all have one.

# Next step:
# Create a login mechanism and interface

def get_label(*args, **kwargs):
    # Output Recipient Name
    if len(args) != 0:
        for name in args:
            print(name, end=" ")
    else:
        print("No name!")
        print("Please try again!")
    
    print()
    
    if "po_box" not in kwargs:
        
        if "building_name" not in kwargs:
            
            if "unit" not in kwargs:
                
                if "block_num" or "street" or "postal_code" or "country" not in kwargs:
                    print("Not a valid address!")
                    print("Please retype the address.")
                else:
                    print(f"{kwargs.get("block_num")} {kwargs.get("street")}")
                    print(f"{kwargs.get("postal_code")}")
                    print(f"{kwargs.get("country")}")
            else:
                print(f"{kwargs.get("block_num")} {kwargs.get("street")}")
                print(f"{kwargs.get("unit")}")
                print(f"{kwargs.get("postal_code")}")
                print(f"{kwargs.get("country")}")
        
        else:
            print(f"{kwargs.get("block_num")} {kwargs.get("street")}")
            print(f"{kwargs.get("unit")} {kwargs.get("building_name")}")
            print(f"{kwargs.get("postal_code")}")
            print(f"{kwargs.get("country")}")
    
    else:
        print(f"{kwargs.get("block_num")} {kwargs.get("street")}")
        print(f"{kwargs.get("unit")} {kwargs.get("building_name")}")
        print(f"{kwargs.get("postal_code")}")
        print(f"{kwargs.get("country")}")
        print(f"{kwargs.get("po_box")}")



running = True

while running:
        
    name = input("Enter the recipient name: ")
    print("--------------------------------------------------------")
    house_num = input("Enter block/building/house number: ")
    print("--------------------------------------------------------")
    street_name = input("Enter street name: ")
    print("-------------------------------------------------")
    unit_num = input("Enter unit number (where applicable): ")
    print("--------------------------------------------------------")
    building_name = input("Enter building name (where applicable): ")
    print("--------------------------------------------------------")
    postal_code = input("Enter postal code: ")
    print("--------------------------------------------------------")
    country = input("Enter country: ")
    print("--------------------------------------------------------")
    po_box = input("Enter PO Box (where applicable): ")
    print("--------------------------------------------------------")
    print("Your shipping label has been generated:\n")

    get_label(name, 
            block_num = house_num,
            street = street_name,
            unit = unit_num,
            building_name = building_name,
            postal_code = postal_code,
            country = country,
            po_box = po_box)
    if not input("Would you like to generate another shipping label? (y/n): ").lower() == 'y':
        running = False

# Login interface (I need a higher skill level for this, so work in progress)
# login_attempt = 0
# admin = "user1"
# admin_password = "1234" # Note: Only use such passwords for demos.

# while running and login_attempt < 4:

#     user_name = input("Enter username: ")
#     password_entered = input("Enter password: ")
        
#     if user_name == admin and password_entered == admin_password:
#         name = input("Enter the recipient name: ")
#         print("--------------------------------------------------------")
#         house_num = input("Enter block/building/house number: ")
#         print("--------------------------------------------------------")
#         street_name = input("Enter street name: ")
#         print("-------------------------------------------------")
#         unit_num = input("Enter unit number (where applicable): ")
#         print("--------------------------------------------------------")
#         building_name = input("Enter building name (where applicable): ")
#         print("--------------------------------------------------------")
#         postal_code = input("Enter postal code: ")
#         print("--------------------------------------------------------")
#         country = input("Enter country: ")
#         print("--------------------------------------------------------")
#         po_box = input("Enter PO Box (where applicable): ")
#         print("--------------------------------------------------------")
#         print("Your shipping label has been generated:\n")
    
#         get_label(name, 
#                 block_num = house_num,
#                 street = street_name,
#                 unit = unit_num,
#                 building_name = building_name,
#                 postal_code = postal_code,
#                 country = country,
#                 po_box = po_box)
#         if not input("Would you like to generate another shipping label? (y/n): ").lower() == 'y':
#             running = False
#         else:
#             continue # here lies the problem.
#     else:
#         login_attempt += 1
#         if login_attempt < 4:
#             print(f"You only have {4 - login_attempt} attempt(s) left")
#         else:
#             print("You have run out of attempts! You do not have the login details.")
#             print("We are reporting this to the relevant authorities!")
