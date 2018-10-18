import pandas

# Create type chart references
type_chart = pandas.read_csv('type_chartV2.csv', index_col='type')
type_headers = list(type_chart)


class Type:
    def __init__(self, name, index):
        # Initialize type variables (eff for effectiveness)
        self.name = name
        self.eff_table = {}
        self.eff_labels = []
        self.eff_values = []
        self.notable_eff_table = {}
        self.notable_eff_labels = []
        self.notable_eff_values = []
        self.multiplier = 1

        # Assign effectiveness
        for i in range(0, len(type_headers)):  # For each type
            if type_chart.iat[index, i] == 5:  # If effectiveness value is 5, make it 0.5
                self.eff_values.append(0.5)
            else:
                self.eff_values.append(type_chart.iat[index, i])

            self.eff_labels.append(type_headers[i])

        self.eff_table = dict(zip(self.eff_labels, self.eff_values))  # Stitch labels and values into a dictionary
        self.notable_eff_table = self.eff_table

        # Set up notable effectiveness table
        for k, v in self.notable_eff_table.items():
            if v != 1:
                self.notable_eff_labels.append(k)
                self.notable_eff_values.append(v)
        self.notable_eff_table = dict(zip(self.notable_eff_labels,self.notable_eff_values))

    def get_offensive_effectiveness(self,type_chart):
        ineffective_types = []
        s_effective_types = []
        for key, value in self.notable_eff_table.items():
            for pkmn_type in range(0, len(type_chart)):
                if key == type_chart[pkmn_type].name:
                    if value < 1:
                        ineffective_types.append(type_chart[pkmn_type])
                    elif value > 1:
                        s_effective_types.append(type_chart[pkmn_type])
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
        current_type = type_list[i]
        not_very_effective, super_effective = current_type.get_offensive_effectiveness(type_list)