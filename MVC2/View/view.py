import tkinter as tk
from tkinter import messagebox
from View.cow import Cow
from View.goat import Goat

class View:
    def __init__(self, controller):
        self.controller = controller
        self.total_milk_production = 0  # Variable to keep track of the total milk produced
        self.root = tk.Tk()
        self.root.title("ระบบรีดนมวัวและไล่แพะ")
        self.root.geometry("400x300")

        self.createUI()
        self.root.mainloop()

    def createUI(self):
        # Title label
        title_label = tk.Label(self.root, text="ระบบรีดนมวัวและไล่แพะ", font=("Arial", 16))
        title_label.pack(pady=10)

        # Label for input prompt
        self.label_cow_id = tk.Label(self.root, text="กรอกรหัสวัว:", font=("Arial", 12))
        self.label_cow_id.pack(pady=5)

        # Entry field for Cow ID input
        self.entry_cow_id = tk.Entry(self.root, width=20, font=("Arial", 12))
        self.entry_cow_id.pack(pady=5)

        # Submit button
        submit_button = tk.Button(self.root, text="Submit", font=("Arial", 12), command=self.submit_data)
        submit_button.pack(pady=10)

        # Back button to clear input and reset focus
        back_button = tk.Button(self.root, text="Reset", font=("Arial", 12), command=self.reset_input)
        back_button.pack(pady=5)

        # Label to display the total milk production
        self.total_milk_label = tk.Label(self.root, text="จำนวนน้ำนมทั้งหมดที่ผลิตได้: 0 ลิตร", font=("Arial", 12))
        self.total_milk_label.pack(pady=10)

    def validate_cow_id(self, cow_id):
        """Validate that the cow ID is an 8-digit number not starting with 0."""
        return cow_id.isdigit() and len(cow_id) == 8 and cow_id[0] != '0'

    def submit_data(self):
        """Handle data submission and display results based on cow type and teats."""
        cow_id = self.entry_cow_id.get()
        if self.validate_cow_id(cow_id):
            cow_id_exists = self.controller.check_cow_id(cow_id)
            if cow_id_exists:
                animal_type = self.controller.get_type(cow_id)
                if animal_type == "cow":
                    eligibility = self.controller.check_milking_eligibility(cow_id)
                    if eligibility == "สามารถรีดนมได้":
                        self.display_cow_window(cow_id)
                    elif eligibility == "ไม่สมบูรณ์ไม่สามารถรีดนมได้":
                        self.handle_incomplete_cow(cow_id)
                    else:
                        messagebox.showinfo("Result", eligibility)
                elif animal_type == "goat":
                    self.display_goat_window()
            else:
                messagebox.showerror("Error", f"รหัสวัว: {cow_id} ไม่พบในข้อมูล")
            self.reset_input()
        else:
            messagebox.showerror("Error", "รหัสวัวต้องเป็นเลข 8 หลักและตัวแรกไม่ใช่ 0")

    def display_cow_window(self, cow_id):
        """Open the Cow window when the cow is eligible for milking and calculate milk production."""
        Cow(self.controller)
        milk_produced = self.controller.calculate_milk_production(cow_id)
        self.total_milk_production += milk_produced  # Update the total milk production
        messagebox.showinfo("Milk Production", f"วัว ID {cow_id} ผลิตน้ำนมได้ {milk_produced} ลิตร")
        self.controller.update_teats_after_milking(cow_id)
        self.update_total_milk_label()  # Update the display of total milk production
        self.reset_input()

    def handle_incomplete_cow(self, cow_id):
        """Handle a cow with 3 teats that has a chance to become complete again."""
        self.controller.update_teats_if_incomplete(cow_id)
        updated_eligibility = self.controller.check_milking_eligibility(cow_id)
        if updated_eligibility == "สามารถรีดนมได้":
            messagebox.showinfo("Success", f"วัว ID {cow_id} กลับมาสมบูรณ์และสามารถรีดนมได้แล้ว!")
            self.display_cow_window(cow_id)
        else:
            messagebox.showinfo("Result", f"วัว ID {cow_id} ยังไม่สมบูรณ์ รีดนมไม่ได้")
        self.reset_input()

    def display_goat_window(self):
        """Open the Goat window when the ID belongs to a goat."""
        Goat(self.controller)
        self.reset_input()

    def update_total_milk_label(self):
        """Update the total milk production label."""
        self.total_milk_label.config(text=f"จำนวนน้ำนมทั้งหมดที่ผลิตได้: {self.total_milk_production} ลิตร")

    def reset_input(self):
        """Reset the input field and return focus to the main screen."""
        self.entry_cow_id.delete(0, tk.END)
        self.entry_cow_id.focus_set()
