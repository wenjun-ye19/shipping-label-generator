# The purpose of this program is to create 
# a shipping label through user input

# Based on Singapore Address Context
# Source: https://www.addressexamples.com/singapore-address-format/

# Line 1: [Recipient Name]
# Line 2: [block/building/house number] [street name]
# Line 3: [unit number] [building name]
# Line 4: [Locality/Country + Postal_code]
# Line 5: [Country] -this is kinda redundant
# Line 6: [PO-BOX]
# Some house do not have unit number and/or building name
# PO Box is optional as not all have one.


def get_label(*args, **kwargs):
    """
    Prints the output recipient name and address based on the given arguments and keyword arguments.

    Parameters:
    *args: Variable-length argument list of recipient names.
    **kwargs: Arbitrary keyword arguments for address details. Accepted keywords are:
        - block_num (str): The block number of the address.
        - street (str): The street name of the address.
        - unit (str): The unit number of the address.
        - building_name (str): The name of the building.
        - postal_code (str): The postal code of the address.
        - po_box (str): The PO box number of the address.

    Returns:
    None
    """
    # Output Recipient Name
    if args:
        for name in args:
            print(name, end=" ")
    else:
        print("No name!")
        print("Please try again!")
    
    print()
    
    if "po_box" not in kwargs:
        if "building_name" not in kwargs:
            if "unit" not in kwargs:
                if not any(key in kwargs for key in ("block_num", "street", "postal_code")):
                    print("Not a valid address!")
                    print("Please retype the address.")
                else:
                    print(f"{kwargs.get('block_num')} {kwargs.get('street')}")
                    print(f"{kwargs.get('postal_code')}")
            else:
                print(f"{kwargs.get('block_num')} {kwargs.get('street')}")
                print(f"{kwargs.get('unit')}")
                print(f"{kwargs.get('postal_code')}")
        else:
            print(f"{kwargs.get('block_num')} {kwargs.get('street')}")
            print(f"{kwargs.get('unit')} {kwargs.get('building_name')}")
            print(f"{kwargs.get('postal_code')}")
    else:
        print(f"{kwargs.get('block_num')} {kwargs.get('street')}")
        print(f"{kwargs.get('unit')} {kwargs.get('building_name')}")
        print(f"{kwargs.get('postal_code')}")
        print(f"{kwargs.get('po_box')}")



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
    po_box = input("Enter PO Box (where applicable): ")
    print("--------------------------------------------------------")
    print("Your shipping label has been generated:\n")

    get_label(name, 
            block_num = house_num,
            street = street_name,
            unit = unit_num,
            building_name = building_name,
            postal_code = postal_code,
            po_box = po_box)
    if not input("Would you like to generate another shipping label? (y/n): ").lower() == 'y':
        running = False
        print("Thanks for using the program!")
