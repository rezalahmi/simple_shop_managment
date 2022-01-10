import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class Window:
    def __init__(self):
        self.MyWindow = tk.Tk()
        self.width = 700
        self.height = 600
        self.geometry = "1x1"
        self.title = "Mehran Ommani Shop Management Project"

    def createWindow(self):
        self.MyWindow.minsize(width=self.width, height=self.height)
        self.MyWindow.geometry(self.geometry)
        self.MyWindow.title(self.title)

    def showTab(self):
        tabs = ttk.Notebook(self.MyWindow)
        root = tk.Frame(tabs)
        root2 = tk.Frame(tabs)
        # add two tabs to the MyWindow
        tabs.add(root, text='Sell')
        tabs.add(root2, text='Stock')
        tabs.pack(expand=1, fill="both")
        # design the tab Sell
        dateL = tk.Label(root, text="Date", bg="DodgerBlue2", width=12, font=('arial', 15, 'bold'))
        dateL.grid(row=0, column=0, padx=7, pady=7)
        # show date
        dateE = DateEntry(root, width=12, font=('arial', 15, 'bold'))
        dateE.grid(row=0, column=1, padx=7, pady=7)
        # show labels
        l_Product = tk.Label(root, text="Product", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
        l_Product.grid(row=1, column=0, padx=7, pady=7)

        l_Price = tk.Label(root, text="Price", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
        l_Price.grid(row=1, column=1, padx=7, pady=7)

        l_Quantity = tk.Label(root, text="Quantity", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
        l_Quantity.grid(row=1, column=2, padx=7, pady=7)

        t_billarea = tk.Text(root)
        t_billarea.place(x=9, y=150, height=100, width=250)
        t_viewarea = tk.Text(root)
        t_viewarea.place(x=440, y=150, height=100, width=250)

        submitbtn = tk.Button(root, text="Bill", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

        submitbtn.grid(row=6, column=0, padx=7, pady=7)

        viewbtn = tk.Button(root, text="View All Sellings", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

        viewbtn.grid(row=6, column=2, padx=7, pady=7)
        # design tab stock
        dateL = tk.Label(root2, text="Date", bg="DodgerBlue2", width=12, font=('arial', 15, 'bold'))
        dateL.grid(row=0, column=0, padx=7, pady=7)

        dateE2 = DateEntry(root2, width=12, font=('arial', 15, 'bold'))
        dateE2.grid(row=0, column=1, padx=7, pady=7)

        l_Product = tk.Label(root2, text="Product", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
        l_Product.grid(row=1, column=0, padx=7, pady=7)

        l_Price = tk.Label(root2, text="Price", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
        l_Price.grid(row=2, column=0, padx=7, pady=7)

        l_Quantity = tk.Label(root2, text="Quantity", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=12)
        l_Quantity.grid(row=3, column=0, padx=7, pady=7)

        Name = tk.Entry(root2, font=('arial', 15, 'bold'), width=12)
        Name.grid(row=1, column=1, padx=7, pady=7)

        Price = tk.Entry(root2, font=('arial', 15, 'bold'), width=12)
        Price.grid(row=2, column=1, padx=7, pady=7)

        Qty = tk.Entry(root2, font=('arial', 15, 'bold'), width=12)
        Qty.grid(row=3, column=1, padx=7, pady=7)

        addbtn = tk.Button(root2, text="Add", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

        addbtn.grid(row=4, column=1, padx=7, pady=7)

        viewarea2 = tk.Text(root2)
        viewarea2.grid(row=5, column=0, columnspan=2)

        viewbtn2 = tk.Button(root2, text="View Stock", font=('arial', 15, 'bold'), bg="DodgerBlue2", width=20)

        viewbtn2.grid(row=4, column=0, padx=7, pady=7)

    def showWindow(self):
        self.createWindow()
        self.showTab()
        self.MyWindow.mainloop()


myshop = Window()
myshop.showWindow()
