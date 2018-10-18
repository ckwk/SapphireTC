import pandas

# Create type chart references
type_chart = pandas.read_csv('type_chartV2.csv', index_col='type')
type_headers = list(type_chart)


class Type:
    def __init__(self, name, index):
        # Initialize type variables (eff for effectiveness)
        self.name = name
        self.eff_table = {}
        self.notable_eff_table = {}
        self.notable_eff_labels = []
        self.notable_eff_values = []
        self.multiplier = 1

        # Assign effectiveness
        for i in range(0, len(type_headers)):  # For each type
            self.eff_table[type_headers[i]] = type_chart.iat[index, i]

            if type_chart.iat[index, i] == 5:  # If effectiveness value is 5, make it 0.5
                self.eff_table[type_headers[i]] = 0.5

        # Set up notable effectiveness table
        self.notable_eff_table = self.eff_table

        for k, v in self.notable_eff_table.items():
            if v != 1:
                self.notable_eff_labels.append(k)
                self.notable_eff_values.append(v)
        self.notable_eff_table = dict(zip(self.notable_eff_labels,self.notable_eff_values))

    def get_offensive_effectiveness(self,type_list):
        ineffective_types = []
        s_effective_types = []

        for key, value in self.notable_eff_table.items():
            for pkmn_type in range(0, len(type_list)):
                if key == type_list[pkmn_type].name:
                    if value < 1:
                        ineffective_types.append(type_list[pkmn_type])
                    elif value > 1:
                        s_effective_types.append(type_list[pkmn_type])
        return ineffective_types, s_effective_types


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
        not_very_effective, super_effective = type_list[i].get_offensive_effectiveness(type_list)

        # Actually printing the effectiveness
        print("That type is super effective against:")
        for pkmn_type in range(0, len(super_effective)):
            print(super_effective[pkmn_type].name)

        print("That type is not very effective against:")
        for pkmn_type in range(0, len(not_very_effective)):
            print(not_very_effective[pkmn_type].name)