from ckwktype import Type

# Initialize all the types and type list
normal = Type('NO', 0)
fight = Type('FI', 1)
flying = Type('FL', 2)
poison = Type('PO', 3)
ground = Type('GR', 4)
rock = Type('RO', 5)
bug = Type('BU', 6)
ghost = Type('GH', 7)
steel = Type('ST', 8)
fire = Type('FR', 9)
water = Type('WA', 10)
grass = Type('GA', 11)
electric = Type('EL', 12)
psychic = Type('PS', 13)
ice = Type('IC', 14)
dragon = Type('DR', 15)
dark = Type('DA', 16)
fairy = Type('FA', 17)
na = Type('NA', 18)
type_list = [normal, fight, flying, poison, ground, rock, bug, ghost, steel,
             fire, water, grass, electric, psychic, ice, dragon, dark, fairy, na]

# Get user input
user_input = input("Type a Pokemon Type: ")


# Calculate how a move of the chosen type would affect other types
# Returns not_very_effective_o and super_effective_o dictionaries
def calc_move_interaction(move_type):
    for i in range(0, len(type_list)):  # For each type in the type list
        if move_type == type_list[i].name:  # Get the chosen type

            # Get the types that the chosen type is (not) effective against
            not_very_effective_o, super_effective_o = type_list[i].get_offensive_effectiveness(type_list)
            return not_very_effective_o, super_effective_o


# Calculate how a pokemon of the chosen type would be affected by attacking types
# Returns not_very_effective_d and super_effective_d dictionaries
def calc_type_interaction(pkmn_type):
    for i in range(0, len(type_list)):  # For each type in the type list
        if pkmn_type == type_list[i].name:  # Get the chosen type

            # Get the types that are (not) effective against the chosen type
            not_very_effective_d, super_effective_d = type_list[i].get_defensive_effectiveness(type_list)
            return not_very_effective_d, super_effective_d


# Calculate how a pokemon with multiple types would be affected by attacking types
# Returns eff_table dictionary
def calc_type_combo_interaction(type1, type2, type3):
    my_types = []  # List to hold the inputted types
    eff_table = {}  # dictionary to put all of the effectivenesses in

    # Adding the inputted types to the my_types list
    for pkmn_type in type_list:
        if pkmn_type.name == type1 or pkmn_type.name == type2 or pkmn_type.name == type3:
            my_types.append(pkmn_type)

    # Calculating type effectiveness per entered type
    for i in range(0, len(my_types)):  # For each type in my_types
        current_type = my_types[i]
        type_n, type_s = calc_type_interaction(current_type.name)  # Calculate the interactions for that type

        # Adding the super effective types to the current_type to the eff_table
        for pkmn_type in type_s:  # For each type in the super effective types
            if pkmn_type.name in eff_table.keys():  # If it's already in the dictionary

                # Multiply the value in the dictionary by the new value
                eff_table[pkmn_type.name] = pkmn_type.eff_table[current_type.name] * eff_table[pkmn_type.name]
            else:
                eff_table[pkmn_type.name] = pkmn_type.eff_table[current_type.name]  # Put it into the dictionary

        # Reapeat for all of the ineffective types
        for pkmn_type in type_n:
            if pkmn_type.name in eff_table.keys():
                eff_table[pkmn_type.name] = pkmn_type.eff_table[current_type.name] * eff_table[pkmn_type.name]
            else:
                eff_table[pkmn_type.name] = pkmn_type.eff_table[current_type.name]

    return eff_table


# Print the effectiveness
for i in range(0, len(type_list)):
    if user_input == type_list[i].name:

        # Get the types that the chosen type is (not) effective against
        not_very_effective_o, super_effective_o = calc_move_interaction(user_input)

        # Get the types that are effective against that type and other chosen types
        defensive_effectiveness = calc_type_combo_interaction(user_input, 'GR', 'WA')

        # Actually printing the effectiveness
        print("That type is super effective against:")
        for pkmn_type in range(0, len(super_effective_o)):
            print(super_effective_o[pkmn_type].name)

        print("That type is not very effective against:")
        for pkmn_type in range(0, len(not_very_effective_o)):
            print(not_very_effective_o[pkmn_type].name)

        print("Type combo interactions:")
        print(defensive_effectiveness)
