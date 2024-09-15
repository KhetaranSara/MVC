import pandas as pd
import random

class Model:
    def __init__(self, controller):
        self.controller = controller
        self.csv_path = 'Model/cows_and_goats_data.csv'  # Ensure the correct path to the CSV file
        try:
            self.data = pd.read_csv(self.csv_path, dtype=str)
            self.data['ID'] = self.data['ID'].str.strip()  # Strip extra spaces from IDs
        except FileNotFoundError:
            print(f"Error: ไม่พบไฟล์ที่ {self.csv_path}")
            self.data = pd.DataFrame(columns=['ID', 'Age', 'Number of Teats'])

    def check_cow_id(self, cow_id):
        """Check if the cow ID exists in the data."""
        return cow_id.strip() in self.data['ID'].values

    def get_type(self, cow_id):
        """Retrieve the type of animal (cow or goat) based on cow_id."""
        cow_row = self.data[self.data['ID'] == cow_id.strip()]
        if not cow_row.empty:
            teats = cow_row.iloc[0].get('Number of Teats', None)
            if pd.isna(teats) or teats == '' or teats is None:
                return "goat"
            else:
                return "cow"
        else:
            return None  # Return None if the cow_id is not found

    def check_milking_eligibility(self, cow_id):
        """Check if a cow is eligible for milking based on the number of teats."""
        cow_row = self.data[self.data['ID'] == cow_id.strip()]
        teats = int(cow_row.iloc[0]['Number of Teats'])

        if teats == 4:
            return "สามารถรีดนมได้"
        elif teats == 3:
            return "รีดนมไม่ได้"
        else:
            return "ไม่สมบูรณ์ไม่สามารถรีดนมได้"

    def calculate_milk_production(self, cow_id):
        """Calculate the amount of milk based on the cow's age (years + months)."""
        cow_row = self.data[self.data['ID'] == cow_id.strip()]
        age = cow_row.iloc[0]['Age']
        
        # Extract years and months from the age string format "X ปี Y เดือน"
        try:
            years = int(age.split()[0])  # Extract the number of years
            months = int(age.split()[2])  # Extract the number of months
            milk_production = years + months  # Total liters of milk produced
        except (IndexError, ValueError):
            # Handle cases where the format is not as expected
            milk_production = 0

        return milk_production

    def update_teats_after_milking(self, cow_id):
        """Update the number of teats after milking based on a 5% probability."""
        cow_row = self.data[self.data['ID'] == cow_id.strip()]
        teats = int(cow_row.iloc[0]['Number of Teats'])

        if teats == 4 and random.random() < 0.05:
            self.update_teats(cow_id, 3)
            print(f"วัว ID {cow_id} รีดนมแล้วลดจำนวนเต้าลงเหลือ 3")

    def update_teats_if_incomplete(self, cow_id):
        """Update the number of teats if the cow is incomplete based on a 20% probability."""
        cow_row = self.data[self.data['ID'] == cow_id.strip()]
        teats = int(cow_row.iloc[0]['Number of Teats'])

        if teats == 3 and random.random() < 0.20:
            self.update_teats(cow_id, 4)
            print(f"วัว ID {cow_id} เต้ากลับมาเป็น 4 เต้าอีกครั้ง")

    def update_teats(self, cow_id, teats):
        """Update the number of teats for a specific cow."""
        self.data.loc[self.data['ID'] == cow_id.strip(), 'Number of Teats'] = teats
        self.data.to_csv(self.csv_path, index=False)
