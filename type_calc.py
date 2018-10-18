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
type_list = [normal, fight, flying, poison, ground, rock, bug, ghost, steel,
             fire, water, grass, electric, psychic, ice, dragon, dark, fairy]

# Get user input
user_input = input("Type a Pokemon Type: ")

# Print the effectiveness
for i in range(0, len(type_list)):
    if user_input == type_list[i].name:

        # Get the types that the chosen type is (not) effective against
        not_very_effective_o, super_effective_o = type_list[i].get_offensive_effectiveness(type_list)
        not_very_effective_d, super_effective_d = type_list[i].get_defensive_effectiveness(type_list)

        # Actually printing the effectiveness
        print("That type is super effective against:")
        for pkmn_type in range(0, len(super_effective_o)):
            print(super_effective_o[pkmn_type].name)

        print("That type is not very effective against:")
        for pkmn_type in range(0, len(not_very_effective_o)):
            print(not_very_effective_o[pkmn_type].name)

        print("That type is weak to:")
        for pkmn_type in range(0, len(super_effective_d)):
            print(super_effective_d[pkmn_type].name)

        print("That type is strong against:")
        for pkmn_type in range(0, len(not_very_effective_d)):
            print(not_very_effective_d[pkmn_type].name)
