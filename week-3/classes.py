from typing import List


class Ecosystem:
    '''
    Blueprint for the Ecosystem objects
    '''

    def __init__(self, name: str, description: str, biodiversity_index: float):
        '''
        Initializes the Ecosystem objects
        '''
        self.name = name
        self.description = description
        self.biodiversity_index = biodiversity_index

    def update_description(self, description: str):
        '''
        Updates the ecosystem's descrition
        '''
        self.description = description

    def __str__(self):
        '''
        Show the ecosystem details
        '''
        return f"Ecosystem name: {self.name} \
                description: {self.description} \
                    biodiversity index: {self.biodiversity_index}"


class Forest(Ecosystem):
    '''
    Blueprint for Forest objects
    '''

    def __init__(self, name: str, description: str, biodiversity_index: float,
                 tree_species: List[str], carbon_sequestration_rate: float):
        '''
        Initializes the Forest object
        '''
        super().__init__(name, description, biodiversity_index)
        self.tree_species = tree_species
        self.carbon_sequestration_rate = carbon_sequestration_rate

    def add_tree_species(self, species: str):
        '''
        Adds a tree species to the list of tree species
        '''
        self.tree_species.append(species)

    def __str__(self):
        '''
        Shows the tree species in the forest
        '''
        return f"Tree species in {self.name} forest include: {','.join(self.tree_species)}"


class Wildlife:
    '''
    Blueprint for Wildlife objects
    '''

    def habitat(self):
        '''
        Shows the wildlife's habitat
        '''
        return "Wildlife habitat"


class Mammal(Wildlife):
    '''
    Blueprint for Mammal objects
    '''

    def habitat(self):
        '''
        Shows the mammal's habitat
        '''
        return "Mammal habitat"


class Bird(Wildlife):
    '''
    Blueprint for Bird objects
    '''

    def habitat(self):
        '''
        Shows the wildlife's habitat
        '''
        return "Bird habitat"
