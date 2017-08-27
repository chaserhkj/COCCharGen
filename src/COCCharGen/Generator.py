class Generator():
    """Virtual class for Generators."""
    def generate_char(self, char):
        self.generate_basic_info(char)
        self.generate_characteristics(char)
        self.generate_status(char)
        self.generate_combact_stat(char)
        self.generate_skills(char)
        self.generate_weapons(char)
        self.generate_backstory(char)
        self.generate_inventory(char)
        self.generate_financial_status(char)

    def generate_basic_info(self, char):
        pass
    def generate_characteristics(self, char):
        pass
    def generate_status(self, char):
        pass
    def generate_combact_stat(self, char):
        pass
    def generate_skills(self, char):
        pass
    def generate_weapons(self, char):
        pass
    def generate_backstory(self, char):
        pass
    def generate_inventory(self, char):
        pass
    def generate_financial_status(self, char):
        pass
