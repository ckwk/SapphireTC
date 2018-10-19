import pandas

type_chart = pandas.read_csv('type_chartV2.csv', index_col='type')
type_headers = list(type_chart)


class Type:
    def __init__(self, name, index):
        # Initialize type variables (eff for effectiveness)
        self.name = name
        self.eff_table = {}
        self.notable_eff_table = {}

        # Assign effectiveness
        for i in range(0, len(type_headers)):  # For each type
            self.eff_table[type_headers[i]] = type_chart.iat[index, i]

            if type_chart.iat[index, i] == 5:  # If effectiveness value is 5, make it 0.5
                self.eff_table[type_headers[i]] = 0.5

        # Set up notable effectiveness table
        self.notable_eff_table = self.eff_table

        for k, v in self.notable_eff_table.items():
            if v != 1:
                self.notable_eff_table[k] = v

    # Returns ineffective_types, s_effective_types lists
    def get_offensive_effectiveness(self,type_list):

        # Initializing lists
        ineffective_types = []
        s_effective_types = []

        # Creating the lists
        for key, value in self.notable_eff_table.items():  # For each item in the notable effects table
            for pkmn_type in range(0, len(type_list)):
                if key == type_list[pkmn_type].name:  # If the name in the notable effects table is the name of a type

                    # If it's super effective, add it to that table and vice versa
                    if value < 1:
                        ineffective_types.append(type_list[pkmn_type])
                    elif value > 1:
                        s_effective_types.append(type_list[pkmn_type])

        return ineffective_types, s_effective_types

    # Returns ineffective_types, s_effective_types lists
    def get_defensive_effectiveness(self,type_list):

        # Initializing lists
        ineffective_types = []
        s_effective_types = []

        # Creating the lists
        for each_type in range(0, len(type_list)):
            current_type = type_list[each_type]

            # Get the offensive effectiveness of each type in the type list
            not_very_effective, super_effective = current_type.get_offensive_effectiveness(type_list)

            for pkmn_type in range(0, len(super_effective)):  # For each type in the list of super effective types
                if self.name == super_effective[pkmn_type].name:  # If my type is in that list
                    s_effective_types.append(current_type)  # Add that type to the list of super effective types

            # Identical to the above action
            for pkmn_type in range(0, len(not_very_effective)):
                if self.name == not_very_effective[pkmn_type].name:
                    ineffective_types.append(current_type)

        return ineffective_types, s_effective_types
