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

    def get_defensive_effectiveness(self,type_list):
        ineffective_types = []
        s_effective_types = []

        for each_type in range(0, len(type_list)):
            current_type = type_list[each_type]
            not_very_effective, super_effective = current_type.get_offensive_effectiveness(type_list)

            for pkmn_type in range(0, len(super_effective)):
                if self.name == super_effective[pkmn_type].name:
                    s_effective_types.append(current_type)

            for pkmn_type in range(0, len(not_very_effective)):
                if self.name == not_very_effective[pkmn_type].name:
                    ineffective_types.append(current_type)

        return ineffective_types, s_effective_types
