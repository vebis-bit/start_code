import tkinter as tk

class CustomGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom GUI")

        self.sidebar = tk.Frame(self.root, width=200, bg='lightgrey')
        self.sidebar.pack(side='left', fill='y')

        self.view_1 = tk.Frame(self.root, bg='white')
        self.view_2 = tk.Frame(self.root, bg='white')
        self.view_3 = tk.Frame(self.root, bg='white')

        self.current_view = None

        self.create_sidebar()
        self.create_table(self.view_1)
        self.show_view(self.view_1)

    def create_sidebar(self):
        button_1 = tk.Button(self.sidebar, text="View 1", command=lambda: self.show_view(self.view_1))
        button_1.pack(pady=10, padx=5, fill='x')

        button_2 = tk.Button(self.sidebar, text="View 2", command=lambda: self.show_view(self.view_2))
        button_2.pack(pady=10, padx=5, fill='x')

        button_3 = tk.Button(self.sidebar, text="View 3", command=lambda: self.show_view(self.view_3))
        button_3.pack(pady=10, padx=5, fill='x')

    def show_view(self, view):
        if self.current_view:
            self.current_view.pack_forget()

        view.pack(fill='both', expand=True)
        self.current_view = view

    def create_table(self, parent):
        # Creating a simple table using labels in the first view
        labels = [['Mat', 'Mengde (g)', 'Occupation'],
                  ['Kjøtt', '30', 'Engineer'],
                  ['Ost', '25', 'Designer'],
                  ['Brød', '35', 'Teacher']]

        for i, row in enumerate(labels):
            for j, text in enumerate(row):
                label = tk.Label(parent, text=text, width=15, relief=tk.RIDGE)
                label.grid(row=i, column=j, padx=5, pady=5)


def main():
    root = tk.Tk()
    root.geometry("600x400")

    app = CustomGUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()