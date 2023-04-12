import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")

        # Creamos la caja de entrada y la ubicamos en la ventana
        self.entry = tk.Entry(master, width=20, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4, pady=5)

        # Creamos los botones numéricos y de operaciones y los ubicamos en la ventana
        button_labels = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "=", "/"
        ]
        self.buttons = []
        for i, label in enumerate(button_labels):
            button = tk.Button(master, text=label, width=5, font=("Arial", 16),
                               command=lambda label=label: self.handle_button_press(label))
            button.grid(row=1 + i // 4, column=i % 4, padx=2, pady=2)
            self.buttons.append(button)

        # Creamos el botón de borrado y lo ubicamos en la ventana
        self.clear_button = tk.Button(master, text="C", width=5, font=("Arial", 16),
                                      command=self.clear_entry)
        self.clear_button.grid(row=5, column=0, padx=2, pady=2)

    def handle_button_press(self, label):
        if label == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except (SyntaxError, ZeroDivisionError):
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, label)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
