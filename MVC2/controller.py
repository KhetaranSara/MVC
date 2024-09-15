from View.view import View
from model import Model

class Controller:
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)

    def check_cow_id(self, cow_id):
        return self.model.check_cow_id(cow_id)

    def get_type(self, cow_id):
        return self.model.get_type(cow_id)

    def check_milking_eligibility(self, cow_id):
        return self.model.check_milking_eligibility(cow_id)

    def calculate_milk_production(self, cow_id):
        """Calculate milk production based on the cow's age."""
        return self.model.calculate_milk_production(cow_id)

    def update_teats_after_milking(self, cow_id):
        """Update teats after milking based on probability."""
        self.model.update_teats_after_milking(cow_id)

    def update_teats_if_incomplete(self, cow_id):
        """Update teats if cow is incomplete with 3 teats."""
        self.model.update_teats_if_incomplete(cow_id)
