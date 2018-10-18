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

    def print_effectiveness(self):
        print("Not very effective against:")
        for low_k, low_v in self.notable_eff_table.items():
            if low_v < 1:
                print(low_k)
        print("Super effective against:")
        for high_k, high_v in self.notable_eff_table.items():
            if high_v > 1:
                print(high_k)


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
        current_type.print_effectiveness()


