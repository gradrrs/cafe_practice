import tkinter as tk
from tkinter import messagebox

class MainView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Кафе приложение")

        self.menu_var = tk.StringVar()
        self.quantity_var = tk.IntVar()

        self.menu_label = tk.Label(self.root, text="Меню")
        self.menu_label.pack()

        self.menu_dropdown = tk.OptionMenu(self.root, self.menu_var, "")
        self.menu_dropdown.pack()

        self.quantity_label = tk.Label(self.root, text="Количество")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(self.root, textvariable=self.quantity_var)
        self.quantity_entry.pack()

        self.submit_button = tk.Button(self.root, text="Подтвердить", command=self.submit_order)
        self.submit_button.pack()

        self.load_menu()

    def load_menu(self):
        menu_items = self.controller.load_menu()
        if menu_items:
            item_names = [item["name"] for item in menu_items]
            self.menu_var.set(item_names[0])
            self.menu_dropdown["menu"].delete(0, "end")
            for item in item_names:
                self.menu_dropdown["menu"].add_command(label=item, command=lambda v=item: self.menu_var.set(v))

    def submit_order(self):
        item = self.menu_var.get()
        quantity = self.quantity_var.get()
        if quantity <= 0:
            messagebox.showerror("Error", "Нужно указать значение больше 0")
            return
        response = self.controller.submit_order(item, quantity)
        if response.get("status") == "success":
            messagebox.showinfo("Подтверждение", "Заказ подтвержден")
        else:
            messagebox.showerror("Ошибка", "Ошибка при получении заказа")

    def run(self):
        self.root.mainloop()