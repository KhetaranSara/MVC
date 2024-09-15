import tkinter as tk
from tkinter import messagebox

class Goat:
    def __init__(self,controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Goat Found")
        self.root.geometry("300x200")  # กำหนดขนาดหน้าต่าง

        # สร้าง Label แสดงหัวข้อ
        self.label = tk.Label(self.root, text="นี่คือแพะ", font=("Arial", 14))
        self.label.pack(pady=20)

        # สร้างปุ่มสำหรับรีดนม
        self.milk_button = tk.Button(self.root, text="ไล่แพะ", command=self.milk_cow, font=("Arial", 12), bg="lightblue")
        self.milk_button.pack(pady=10)

        # เริ่มการทำงานของหน้าต่างหลัก
        self.root.mainloop()

    def milk_cow(self):
        # แสดงข้อความแจ้งเตือนเมื่อรีดนม
        
        messagebox.showinfo("ไล่แพะ", "แพะกลับขึนเขาแล้ว")

# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    Goat()
