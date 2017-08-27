class Character():
    """Class for representing a COC character."""
    def __init__(self):
        """Constructs an empty character."""
        self.basic_info = { "Name": "",
                "Player": "",
                "Occupation": "",
                "Age": 0,
                "Sex": "",
                "Residence": "",
                "Birthplace": ""
                }
        self.characteristics = { "STR": 0,
                "DEX": 0,
                "INT": 0,
                "CON": 0,
                "APP": 0,
                "POW": 0,
                "SIZ": 0,
                "EDU": 0,
                "Move Rate": 0}
        self.status = { "HP": 0,
                "Sanity": 0,
                "Luck": 0,
                "MP": 0}
        self.combact_stat = {"Damage Bonus": "",
                "Build": 0,
                "Dodge": 0}
        self.skills = {}
        self.weapons = {}
        self.backstory = {"Personal Description": [],
                "Ideology/Beliefs": [],
                "Significant People": [],
                "Meaningful Locations": [],
                "Treasured Possessions": [],
                "Traits": [],
                "Injuries & Scars": [],
                "Phobias & Manias": [],
                "Arcane Tomes, Spells & Artifacts":[],
                "Encounters with Strange Entities": []}
        self.inventory = []
        self.financial_status = {"Spending Level": 0,
                "Cash": 0,
                "Unspecified Assets": 0,
                "Assets": []}

    def update(self):
        """Update stats according to their dependencies."""
        pass

    def generate(self, generator):
        """Use generator to generate stats.

        generator: a generator object, must implement generate_* functions in class Generator."""
        generator.generate_basic_info(self)
        generator.generate_characteristics(self)
        generator.generate_status(self)
        generator.generate_combact_stat(self)
        generator.generate_skills(self)
        generator.generate_weapons(self)
        generator.generate_backstory(self)
        generator.generate_inventory(self)
        generator.generate_financial_status(self)

    def dump(self, f, fmt="json"):
        """Dump to file."""
        pass

    def load(self, f, fmt="json"):
        """Load from file."""
        pass

    def dumps(self, fmt="json"):
        """Dump to string."""
        pass

    def loads(self, string, fmt="json"):
        """Load from string."""
        pass


