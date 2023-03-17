import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font as tkfont, NW, ttk, CENTER
import tkinter.messagebox as MessageBox
from turtle import update

import controller as controller
import mysql.connector as mysql
import tk as tk
from Tools.scripts.make_ctype import values


class SampleApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Libing Things - Funeral Business System")
        self.iconbitmap("lb_logo.ico")
        self.geometry("1100x600")
        self.configure(background='red')
        self.resizable(0, 0)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (login, inventorymenu, inventorymanage, salesmenu, saleslist, salesbilling):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("login")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

global username_verification
global password_verification
class login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        global framemain
        global username_verification
        global password_verification
        self.photo1 = PhotoImage(file="background.png")
        self.label = Label(self, image=self.photo1)
        self.label.image = self.photo1
        self.label.place(x=0, y=0)
        username_verification = StringVar()
        password_verification = StringVar()
        framemain = Frame(self, width=100, highlightbackground='black', highlightthicknes=3)
        framemain.grid(row=1, column=0, padx=160, pady=100, ipadx=350, ipady=230)
        photo1 = PhotoImage(file="login.png")
        label = Label(framemain, image=photo1)
        label.image = photo1
        label.place(x=-155, y=-100)
        unentry = Entry(framemain, textvariable=username_verification,font=('century gothic', 8, 'italic'))
        unentry.place(x=370, y=300)
        lblun = Label(framemain, text="Username :", fg="white", bg="black", font=('century gothic', 8, 'bold'))
        lblun.place(x=300, y=300)
        def login_verification( event ):
            user_verification = username_verification.get()
            pass_verification = password_verification.get()
            if user_verification == "inventory" and pass_verification == "inventory123":
                controller.show_frame("inventorymenu")
            elif user_verification == "sales" and pass_verification == "sales123":
                controller.show_frame("salesmenu")
            else:
                MessageBox.showerror("System Message", "Either the password or username is incorrect!")


        psentry = Entry(framemain, textvariable=password_verification, show="*")
        psentry.place(x=370, y=330)
        psentry.bind('<Return>', login_verification)
        lblps = Label(framemain, text="Password :", fg="white", bg="black", font=('century gothic', 8, 'bold'))
        lblps.place(x=300, y=330)


class inventorymenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        global frameinventmenu
        global frameinventory
        self.photo1 = PhotoImage(file="background.png")
        self.label = Label(self, image=self.photo1)
        self.label.image = self.photo1
        self.label.place(x=0, y=0)
        frameinventmenu = LabelFrame(self, width=100, highlightbackground='black', highlightthicknes=2,)
        frameinventmenu.grid(row=0, column=1, padx=0, pady=100, ipadx=50, ipady=230)
        photo1 = PhotoImage(file="inventmenu.png")
        label1 = Label(frameinventmenu, image=photo1)
        label1.image = photo1
        label1.place(x=-5, y=-5)
        def inventory():
            controller.show_frame("inventorymanage")


        sales_btn = Button(frameinventmenu, text="Inventory", command=inventory)
        sales_btn.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn.place(x=15, y=5)
        def logout():
            wayOut = tkinter.messagebox.askyesno("System Message",
                                                 "Do you want to log out?")
            if wayOut > 0:
                MessageBox.showinfo("Success", "Thank you!")
                se.set("")
                controller.show_frame("login")
                username_verification.set("")
                password_verification.set("")

        sales_btn2 = Button(frameinventmenu, text="Log-out", command=logout)
        sales_btn2.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn2.place(x=15, y=50)
        frameinventory = Frame(self, width=100, highlightbackground='black', highlightthicknes=2, )
        frameinventory.grid(row=0, column=0, padx=30, pady=100, ipadx=350, ipady=230)
        photo = PhotoImage(file="libinginventorybg.png")
        label = Label(frameinventory, image=photo)
        label.image = photo
        label.place(x=-50, y=0)
class inventorymanage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.photo1 = PhotoImage(file="background.png")
        self.label = Label(self, image=self.photo1)
        self.label.image = self.photo1
        self.label.place(x=0, y=0)
        global frameinvent
        frameinventmenu = LabelFrame(self, width=100, highlightbackground='black', highlightthicknes=2, )
        frameinventmenu.grid(row=0, column=1, padx=0, pady=100, ipadx=50, ipady=230)
        photo1 = PhotoImage(file="inventmenu.png")
        label1 = Label(frameinventmenu, image=photo1)
        label1.image = photo1
        label1.place(x=-5, y=-5)

        def inventory():
            controller.show_frame("inventorymenu")

        sales_btn = Button(frameinventmenu, text="Inventory", command=inventory)
        sales_btn.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn.place(x=15, y=5)

        def logout():
            wayOut = tkinter.messagebox.askyesno("System Message",
                                                 "Do you want to log out?")
            if wayOut > 0:
                MessageBox.showinfo("Success", "Thank you!")
                se.set("")
                controller.show_frame("login")
                username_verification.set("")
                password_verification.set("")

        sales_btn2 = Button(frameinventmenu, text="Log-out", command=logout)
        sales_btn2.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn2.place(x=15, y=50)
        frameinventory = Frame(self, width=100, highlightbackground='black', highlightthicknes=2, )
        frameinventory.grid(row=0, column=0, padx=30, pady=100, ipadx=350, ipady=230)
        photo = PhotoImage(file="libinginventorybg.png")
        label = Label(frameinventory, image=photo)
        label.image = photo
        label.place(x=-50, y=0)

        connectiondb = mysql.connect(host="localhost", user="root", password="", database="libingthings", port=3306)
        cursor = connectiondb.cursor()
        cursor.execute("select * from inventorysales ORDER BY p_id")
        frameinvent = Frame(self, width=100, highlightbackground='black', highlightthicknes=2)
        frameinvent.grid(row=0, column=0, padx=30, pady=100, ipadx=350, ipady=230)
        photo1 = PhotoImage(file="libinginventory.png")
        label = Label(frameinvent, image=photo1)
        label.image = photo1
        label.place(x=-50, y=-0)

        tree = ttk.Treeview(frameinvent)
        tree['show'] = 'headings'

        s = ttk.Style(frameinvent)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica', 11))
        s.configure("Treeview.Heading", font=('Helvetica', 11, "bold"))

        # Define number of columns
        tree["columns"] = ("Product ID", "Product Name", "Price", "Quantity")
        # Ansign the width, minwidth and anchor to the respective columna
        tree.column("Product ID", width=100, minwidth=100)
        tree.column("Product Name", width=150, minwidth=150)
        tree.column("Price", width=150, minwidth=100, anchor=CENTER)
        tree.column("Quantity", width=100, minwidth=100, anchor=CENTER)


        # Assign the heading names to the respective columns
        tree.heading("Product ID", text="Product ID", anchor=CENTER)
        tree.heading("Product Name", text="Product Name", anchor=CENTER)
        tree.heading("Price", text="Price", anchor=CENTER)
        tree.heading("Quantity", text="Quantity", anchor=CENTER)
        tree.configure(height=6)
        i = 0
        for row in cursor:
            if row[0]%2==0:
                tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3]),tags=("even"),)
            else:
                tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3]), tags=("odd"), )
            i = i + 1
        tree.place(x=160, y=250)

        def update(rows):
            tree.delete(*tree.get_children())
            for i in rows:
                tree.insert('', 'end', values=i)

        def search():
            tree.delete(*tree.get_children())
            q2 = se.get()
            query = "SELECT p_id, p_name, p_price, p_qty FROM inventorysales WHERE p_name LIKE '%" + q2 + "%'"
            cursor.execute(query)
            rows = cursor.fetchall()
            update(rows)

        def clear():
            query = "SELECT p_id, p_name, p_price, p_qty FROM inventorysales"
            cursor.execute(query)
            rows = cursor.fetchall()
            search_ent1.delete(0, END)
            update(rows)
        global search_ent1
        global se
        se = StringVar()
        search_ent1 = Entry(frameinvent, font=('arial', 18), width=24,textvariable = se)
        search_ent1.place(x=170, y=200)
        search_btn = Button(frameinvent, text="Search", font=('arial', 13, 'bold'), width=7, bg='gray', fg='white', command=search)
        search_btn.place(x=500, y=200)
        search_clr = Button(frameinvent, text="Clear", font=('arial', 13, 'bold'), width=7, bg='gray', fg='white', command=clear)
        search_clr.place(x=580, y=200)


        pname = StringVar()
        pprice = IntVar()
        pqty = IntVar()

        def select_data(tree):
            curItem = tree.focus()
            values = tree.item(curItem, "values")
            print(values)

            update = Toplevel(self)
            update.title("Libing Things - Update")
            update.iconbitmap("lb_logo.ico")
            update.geometry("350x200")
            update.resizable(0, 0)
            photo1 = PhotoImage(file="upins.png")
            label = Label(update, image=photo1)
            label.image = photo1
            label.place(x=0, y=0)

            l1 = Label(update, text="P Name", width=10, font=('century gothic', 9, 'bold'), bg='black', fg='white')
            e1 = Entry(update, textvariable=pname,font=('century gothic', 9, 'bold'), bg='white', fg='black', width=17)
            l1.place(x=50, y=50)
            e1.place(x=150, y=50)

            l2 = Label(update, text="Price", width=10,font=('century gothic', 9, 'bold'), bg='black', fg='white')
            e2 = Entry(update, textvariable=pprice,font=('century gothic', 9, 'bold'), bg='white', fg='black', width=17)
            l2.place(x=50, y=80)
            e2.place(x=150, y=80)

            l3 = Label(update, text="Quantity", width=10, font=('century gothic', 9, 'bold'), bg='black', fg='white')
            e3 = Entry(update, textvariable=pqty,font=('century gothic', 9, 'bold'), bg='white', fg='black', width=17)
            l3.place(x=50, y=110)
            e3.place(x=150, y=110)

            e1.insert(0, values[1])
            e2.insert(0, values[2])
            e3.insert(0, values[3])

            def update_data():
                nonlocal e1, e2, e3, curItem, values
                p1_name = pname.get()
                p1_price = pprice.get()
                p1_qty = pqty.get()
                tree.item(curItem, values=(values[0], p1_name, p1_price, p1_qty))
                cursor.execute("UPDATE inventorysales SET p_name=%s, p_price=%s, p_qty=%s WHERE p_id=%s",
                           (p1_name, p1_price, p1_qty, values[0]))
                connectiondb.commit()
                MessageBox.showinfo("Success", "Data Updated")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                update.destroy()

            def cancel():
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                update.destroy()

            savebutton = Button(update, text="Update", font=('calibri', 9, 'bold'), width=10, bg='black', fg='white', command=update_data)
            savebutton.place(x=160, y=140)
            cancelbutton = Button(update, text="Cancel", font=('calibri', 9, 'bold'), width=10, bg='black', fg='white', command=cancel)
            cancelbutton.place(x=240, y=140)

        def delete_data(tree):
            selected_item = tree.selection()[0]
            print(tree.item(selected_item)['values'])
            uid = tree.item(selected_item)['values'][0]
            del_query = "DELETE FROM inventorysales WHERE p_id=%s"
            sel_data = (uid,)
            cursor.execute(del_query, sel_data)
            MessageBox.askyesno("System Message","Do you want to delete the record?")
            connectiondb.commit()
            tree.delete(selected_item)
            MessageBox.showinfo("Success", "Data Deleted")
        def add_data(tree):
            add = Toplevel(self)
            add.title("Libing Things - Insert Data")
            add.iconbitmap("lb_logo.ico")
            add.geometry("350x200")
            add.resizable(0, 0)
            photo1 = PhotoImage(file="upins.png")
            label = Label(add, image=photo1)
            label.image = photo1
            label.place(x=0, y=0)

            l1 = Label(add, text="P Name", width=10, font=('century gothic', 9, 'bold'), bg='black', fg='white')
            e1 = Entry(add, textvariable=pname,font=('century gothic', 9, 'bold'), bg='white', fg='black', width=17)
            l1.place(x=50, y=50)
            e1.place(x=150, y=50)

            l2 = Label(add, text="Price", width=10, font=('century gothic', 9, 'bold'), bg='black', fg='white')
            e2 = Entry(add, textvariable=pprice, font=('century gothic', 9, 'bold'), bg='white', fg='black', width=17)
            l2.place(x=50, y=80)
            e2.place(x=150, y=80)

            l3 = Label(add, text="Quantity", width=10, font=('century gothic', 9, 'bold'), bg='black', fg='white')
            e3 = Entry(add, textvariable=pqty, font=('century gothic', 9, 'bold'), bg='white', fg='black', width=17)
            l3.place(x=50, y=110)
            e3.place(x=150, y=110)

            def insert():
                nonlocal  e1, e2, e3

                p2_name = pname.get()
                p2_price = pprice.get()
                p2_qty = pqty.get()
                cursor.execute('INSERT INTO inventorysales(p_name, p_price, p_qty) VALUES (%s,%s,%s)',
                           (p2_name, p2_price, p2_qty))
                print(cursor.lastrowid)
                connectiondb.commit()
                tree.insert('', 'end', text="", values=(cursor.lastrowid, p2_name, p2_price, p2_qty))
                MessageBox.showinfo("Success", "Data Inserted")

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                add.destroy()

            def cancel():
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                add.destroy()

            savebutton = Button(add, text="Insert", font=('calibri', 9, 'bold'), width=10, bg='black', fg='white', command=insert)
            savebutton.place(x=160, y=140)
            cancelbutton = Button(add, text="Cancel", font=('calibri', 9, 'bold'), width=10, bg='black', fg='white', command=cancel)
            cancelbutton.place(x=240, y=140)

        add_btn = Button(frameinvent, text="Add", command=lambda: add_data(tree))
        add_btn.configure(font=('calibri', 9, 'bold'), width=10, bg='black', fg='white')
        add_btn.place(x=460, y=410)

        delete_btn = Button(frameinvent, text="Delete", command=lambda: delete_data(tree))
        delete_btn.configure(font=('calibri', 9, 'bold'), width=10, bg='black', fg='white')
        delete_btn.place(x=525, y=410)

        up_btn = Button(frameinvent, text="Update", command=lambda: select_data(tree))
        up_btn.configure(font=('calibri', 9, 'bold'), width=10, bg='black', fg='white')
        up_btn.place(x=590, y=410)

class salesmenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.photo1 = PhotoImage(file="background.png")
        self.label = Label(self, image=self.photo1)
        self.label.image = self.photo1
        self.label.place(x=0, y=0)
        global framesl
        global framemenu
        framemenu = LabelFrame(self, width=100, highlightbackground='black', highlightthicknes=2)
        framemenu.grid(row=0, column=1, padx=0, pady=100, ipadx=50, ipady=230)
        framesl = Frame(self, width=100, highlightbackground='black', highlightthicknes=2, )
        framesl.grid(row=0, column=0, padx=30, pady=100, ipadx=350, ipady=230)
        photo1 = PhotoImage(file="inventmenu.png")
        label1 = Label(framemenu, image=photo1)
        label1.image = photo1
        label1.place(x=-5, y=-5)
        def pay():
            controller.show_frame("salesbilling")
        def productlist():
            controller.show_frame("saleslist")

        sales_btn = Button(framemenu, text="Payment", command=pay)
        sales_btn.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn.place(x=15, y=1)
        sales_btn2 = Button(framemenu, text="View Product List", command=productlist)
        sales_btn2.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn2.place(x=15, y=45)
        def logout():
            wayOut = tkinter.messagebox.askyesno("System Message",
                                                 "Do you want to log out?")
            if wayOut > 0:
                MessageBox.showinfo("Success", "Thank you!")
                controller.show_frame("login")
                username_verification.set("")
                password_verification.set("")
        global  sales_btn34
        sales_btn34 = Button(framemenu, text="Log-out", command=logout)
        sales_btn34.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn34.place(x=15, y=90)
        photo = PhotoImage(file="libingsalesbg.png")
        label = Label(framesl, image=photo)
        label.image = photo
        label.place(x=-50, y=0)
class saleslist(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.photo1 = PhotoImage(file="background.png")
        self.label = Label(self, image=self.photo1)
        self.label.image = self.photo1
        self.label.place(x=0, y=0)
        global framelist

        framemenu = LabelFrame(self, width=100, highlightbackground='black', highlightthicknes=2)
        framemenu.grid(row=0, column=1, padx=0, pady=100, ipadx=50, ipady=230)
        framesl = Frame(self, width=100, highlightbackground='black', highlightthicknes=2, )
        framesl.grid(row=0, column=0, padx=30, pady=100, ipadx=350, ipady=230)
        photo1 = PhotoImage(file="inventmenu.png")
        label1 = Label(framemenu, image=photo1)
        label1.image = photo1
        label1.place(x=-5, y=-5)

        def pay():
            serc.set("")
            controller.show_frame("salesbilling")

        def productlist():
            serc.set("")
            controller.show_frame("salesmenu")

        sales_btn = Button(framemenu, text="Payment", command=pay)
        sales_btn.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn.place(x=15, y=1)
        sales_btn2 = Button(framemenu, text="View Product List", command=productlist)
        sales_btn2.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn2.place(x=15, y=45)

        def logout():
            wayOut = tkinter.messagebox.askyesno("System Message",
                                                 "Do you want to log out?")
            if wayOut > 0:
                MessageBox.showinfo("Success", "Thank you!")
                product_id.set(0)
                product_qty.set(0)
                product_name.set(0)
                product_price.set(0)
                product_partot.set(0)
                product_qtydtb.set(0)
                product_qtydtb2.set(0)
                product_sales.set(0)
                product_fintot.set(0)
                bill_change.set(0)
                bill_pay.set(0)
                serc.set("")
                tree.delete(*tree.get_children())
                controller.show_frame("login")
                username_verification.set("")
                password_verification.set("")

        sales_btn3 = Button(framemenu, text="Log-out", command=logout)
        sales_btn3.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn3.place(x=15, y=90)
        photo1 = PhotoImage(file="libingsalesbg.png")
        label1 = Label(framesl, image=photo1)
        label1.image = photo1
        label1.place(x=-50, y=0)


        framelist = Frame(self, width=100, highlightbackground='black', highlightthicknes=2, )
        framelist.grid(row=0, column=0, padx=30, pady=100, ipadx=350, ipady=230)
        photo = PhotoImage(file="libingsalesviewproducts.png")
        label = Label(framelist, image=photo)
        label.image = photo
        label.place(x=-50, y=0)

        connectiondb = mysql.connect(host="localhost", user="root", password="", database="libingthings", port=3306)
        cursor = connectiondb.cursor()
        cursor.execute("select * from inventorysales ORDER BY p_id")
        tree3 = ttk.Treeview(framelist)
        tree3['show'] = 'headings'

        s = ttk.Style(framelist)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica', 11))
        s.configure("Treeview.Heading", font=('Helvetica', 11, "bold"))

        # Define number of columns
        tree3["columns"] = ("Product ID", "Product Name", "Price", "Quantity", "Sales")
        # Ansign the width, minwidth and anchor to the respective columna
        tree3.column("Product ID", width=100, minwidth=100)
        tree3.column("Product Name", width=100, minwidth=150)
        tree3.column("Price", width=150, minwidth=100, anchor=CENTER)
        tree3.column("Quantity", width=100, minwidth=100, anchor=CENTER)
        tree3.column("Sales", width=100, minwidth=100, anchor=CENTER)

        # Assign the heading names to the respective columns
        tree3.heading("Product ID", text="PID", anchor=CENTER)
        tree3.heading("Product Name", text="Product Name", anchor=CENTER)
        tree3.heading("Price", text="Price", anchor=CENTER)
        tree3.heading("Quantity", text="Quantity", anchor=CENTER)
        tree3.heading("Sales", text="Sales", anchor=CENTER)
        tree3.configure(height=8)
        i = 0
        for row in cursor:
            tree3.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4]))
            i = i + 1
        tree3.place(x=110, y=250)
        def update(rows):
            tree3.delete(*tree3.get_children())
            for i in rows:
                tree3.insert('', 'end', values=i)

        def search():
            cursor = connectiondb.cursor()
            tree3.delete(*tree3.get_children())
            q2 = search_ent.get()
            query = "SELECT p_id, p_name, p_price, p_qty, p_sales FROM inventorysales WHERE p_name LIKE '%" + q2 + "%'"
            cursor.execute(query)
            rows = cursor.fetchall()
            update(rows)
        def clear():
            cursor = connectiondb.cursor()
            query = "SELECT p_id, p_name, p_price, p_qty, p_sales FROM inventorysales"
            cursor.execute(query)
            rows = cursor.fetchall()
            search_ent.delete(0, END)
            update(rows)
        def back():
            controller.show_frame("salesmenu")

        global serc
        serc = StringVar()
        global search_ent
        search_ent = Entry(framelist, font=('arial', 18), width=24, textvariable = serc)
        search_ent.place(x=170, y=200)
        search_btn = Button(framelist, text="Search", font=('arial', 13, 'bold'), width=7, bg='gray', fg='white',
                        command=search)
        search_btn.place(x=500, y=200)
        search_clr = Button(framelist, text="Clear", font=('arial', 13, 'bold'), width=7, bg='gray', fg='white',
                        command=clear)
        search_clr.place(x=580, y=200)
        search_bck = Button(framelist, text="Back", font=('arial', 13, 'bold'), width=7, bg='gray', fg='white',
                            command=back)
        search_bck.place(x=630, y=20)

class salesbilling(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.photo1 = PhotoImage(file="background.png")
        self.label = Label(self, image=self.photo1)
        self.label.image = self.photo1
        self.label.place(x=0, y=0)
        framemenu = LabelFrame(self, width=100, highlightbackground='black', highlightthicknes=2)
        framemenu.grid(row=0, column=1, padx=0, pady=100, ipadx=50, ipady=230)
        framesl = Frame(self, width=100, highlightbackground='black', highlightthicknes=2, )
        framesl.grid(row=0, column=0, padx=30, pady=100, ipadx=350, ipady=230)
        photo1 = PhotoImage(file="inventmenu.png")
        label1 = Label(framemenu, image=photo1)
        label1.image = photo1
        label1.place(x=-5, y=-5)
        global product_id
        global product_qty
        global product_name
        global product_price
        global product_partot
        global product_qtydtb
        global product_qtydtb2
        global product_sales
        global product_fintot
        global bill_change
        global bill_pay


        def update(rows):
            tree.delete(*tree.get_children())
            for i in rows:
                tree.insert('', 'end', values=i)
        def productlist():

            framemenu12 = LabelFrame(self, width=100, highlightbackground='black', highlightthicknes=2)
            framemenu12.grid(row=0, column=1, padx=0, pady=100, ipadx=50, ipady=230)
            framepro = Frame(self, width=100, highlightbackground='black', highlightthicknes=2, )
            framepro.grid(row=0, column=0, padx=30, pady=100, ipadx=350, ipady=230)
            photo = PhotoImage(file="libingsalesviewproducts.png")
            label = Label(framepro, image=photo)
            label.image = photo
            label.place(x=-50, y=0)
            photo1 = PhotoImage(file="inventmenu.png")
            label1 = Label(framemenu12, image=photo1)
            label1.image = photo1
            label1.place(x=-5, y=-5)

            def pay():
                framemenu12.destroy()
                framepro.destroy()
                controller.show_frame("salesbilling")

            def productlist():
                framemenu12.destroy()
                framepro.destroy()
                controller.show_frame("salesmenu")

            sales_btn = Button(framemenu12, text="Payment", command=pay)
            sales_btn.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
            sales_btn.place(x=15, y=1)
            sales_btn2 = Button(framemenu12, text="View Product List", command=productlist)
            sales_btn2.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
            sales_btn2.place(x=15, y=45)

            def logout():
                wayOut = tkinter.messagebox.askyesno("System Message",
                                                     "Do you want to log out?")
                if wayOut > 0:
                   framemenu12.destroy()
                   framepro.destroy()
                   tree.delete(*tree.get_children())

            sales_btn3 = Button(framemenu12, text="Log-out", command=logout)
            sales_btn3.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
            sales_btn3.place(x=15, y=90)
            sales_btn3["state"] = "disabled"
            connectiondb = mysql.connect(host="localhost", user="root", password="", database="libingthings", port=3306)
            cursor = connectiondb.cursor()
            cursor.execute("select * from inventorysales ORDER BY p_id")
            tree3 = ttk.Treeview(framepro)
            tree3['show'] = 'headings'

            s = ttk.Style(framepro)
            s.theme_use("clam")
            s.configure(".", font=('Helvetica', 11))
            s.configure("Treeview.Heading", font=('Helvetica', 11, "bold"))

            # Define number of columns
            tree3["columns"] = ("Product ID", "Product Name", "Price", "Quantity", "Sales")
            # Ansign the width, minwidth and anchor to the respective columna
            tree3.column("Product ID", width=100, minwidth=100)
            tree3.column("Product Name", width=100, minwidth=150)
            tree3.column("Price", width=150, minwidth=100, anchor=CENTER)
            tree3.column("Quantity", width=100, minwidth=100, anchor=CENTER)
            tree3.column("Sales", width=100, minwidth=100, anchor=CENTER)

            # Assign the heading names to the respective columns
            tree3.heading("Product ID", text="PID", anchor=CENTER)
            tree3.heading("Product Name", text="Product Name", anchor=CENTER)
            tree3.heading("Price", text="Price", anchor=CENTER)
            tree3.heading("Quantity", text="Quantity", anchor=CENTER)
            tree3.heading("Sales", text="Sales", anchor=CENTER)
            tree3.configure(height=8)
            i = 0
            for row in cursor:
                tree3.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4]))
                i = i + 1
            tree3.place(x=110, y=250)

            def update(rows):
                tree3.delete(*tree3.get_children())
                for i in rows:
                    tree3.insert('', 'end', values=i)

            def search():
                cursor = connectiondb.cursor()
                tree3.delete(*tree3.get_children())
                q2 = search_ent.get()
                query = "SELECT p_id, p_name, p_price, p_qty, p_sales FROM inventorysales WHERE p_name LIKE '%" + q2 + "%'"
                cursor.execute(query)
                rows = cursor.fetchall()
                update(rows)

            def clear():
                cursor = connectiondb.cursor()
                query = "SELECT p_id, p_name, p_price, p_qty, p_sales FROM inventorysales"
                cursor.execute(query)
                rows = cursor.fetchall()
                search_ent.delete(0, END)
                update(rows)
            def back():
                framepro.destroy()
                framemenu12.destroy()
                controller.show_frame("salesmenu")
            global serc
            serc = StringVar()
            global search_ent
            search_ent = Entry(framepro, font=('arial', 18), width=24, textvariable=serc)
            search_ent.place(x=170, y=200)
            search_btn = Button(framepro, text="Search", font=('arial', 13, 'bold'), width=7, bg='gray', fg='white',
                                command=search)
            search_btn.place(x=500, y=200)
            search_clr = Button(framepro, text="Clear", font=('arial', 13, 'bold'), width=7, bg='gray', fg='white',
                                command=clear)
            search_clr.place(x=580, y=200)
            search_bck = Button(framepro, text="Back", font=('arial', 13, 'bold'), width=7, bg='gray', fg='white',
                                command=back)
            search_bck.place(x=630, y=20)

        sales_btn = Button(framemenu, text="Payment", command=None)
        sales_btn.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn.place(x=15, y=1)
        sales_btn2 = Button(framemenu, text="View Product List", command=productlist)
        sales_btn2.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn2.place(x=15, y=45)

        def logout():
            wayOut = tkinter.messagebox.askyesno("System Message",
                                                 "Do you want to log out?")
            if wayOut > 0:

                MessageBox.showinfo("Success", "Thank you!")
                product_id.set(0)
                product_qty.set(0)
                product_name.set(0)
                product_price.set(0)
                product_partot.set(0)
                product_qtydtb.set(0)
                product_qtydtb2.set(0)
                product_sales.set(0)
                product_fintot.set(0)
                serc.set("")
                bill_change.set(0)
                bill_pay.set(0)
                tree.delete(*tree.get_children())
                controller.show_frame("login")
                username_verification.set("")
                password_verification.set("")


        global sales_btn3
        sales_btn3 = Button(framemenu, text="Log-out", command=logout)
        sales_btn3.configure(font=('calibri', 14, 'bold'), width=15, bg='black', fg='white')
        sales_btn3.place(x=15, y=90)
        photo = PhotoImage(file="libingsalesbg.png")
        label = Label(framesl, image=photo)
        label.image = photo
        label.place(x=-50, y=0)
        global framebilling
        framebilling = Frame(self, width=100, highlightbackground='black', highlightthicknes=2 )
        framebilling.grid(row=0, column=0, padx=30, pady=100, ipadx=350, ipady=230)
        photo1 = PhotoImage(file="libingsalesviewproducts.png")
        label = Label(framebilling, image=photo1)
        label.image = photo1
        label.place(x=-50, y=-0)
        def GetRow(event):
            rowId = tree2.identify_row(event.y)
            item = tree2.item(tree2.focus())
            product_id.set(item['values'][0])
            product_name.set(item['values'][1])
            product_price.set(item['values'][2])
            product_qtydtb.set(item['values'][3])
            product_sales.set(item['values'][4])

        def GetRow2(event):
            rowId = tree.identify_row(event.y)
            item = tree.item(tree.focus())
            item1 = tree2.item(tree2.focus())
            product_delqty.set(item['values'][3])
            product_delqty1.set(item1['values'][3])
            product_delsales.set(item['values'][2])
            product_delsales1.set(item1['values'][4])

        def enter(event):
            total = int(product_fintot.get())
            pay = int(bill_pay.get())
            com = pay - total
            if pay < total:
                MessageBox.showerror("Error", "Payment is not enough.")
            else:
                bill_change.set(com)

        product_id = IntVar()
        # HIDDEN ENTRIES
        product_name = StringVar()
        product_price = IntVar()
        product_qty = IntVar()
        product_qtydtb = IntVar()
        product_qtydtb2 = IntVar()
        # COMPUTATIONS VARIABLES
        product_partot = IntVar()
        product_fintot = IntVar()
        product_sales = IntVar()
        bill_pay = IntVar()
        bill_change = IntVar()
        # DELETE FUNCTION
        product_delqty = IntVar()
        product_delqty1 = IntVar()
        product_delsales = IntVar()
        product_delsales1 = IntVar()

        connectiondb = mysql.connect(host="localhost", user="root", password="", database="libingthings", port=3306)
        cursor = connectiondb.cursor()
        cursor.execute("select * from inventorysales ORDER BY p_id")
        global tree
        tree = ttk.Treeview(framebilling)
        tree['show'] = 'headings'

        s = ttk.Style(framebilling)
        s.theme_use("clam")
        s.configure(".", font=('Helvetica', 10))
        s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

        # Define number of columns
        tree["columns"] = ("Product ID", "Product Name", "Price", "Quantity")
        # Ansign the width, minwidth and anchor to the respective column
        tree.column("Product ID", width=100, minwidth=100)
        tree.column("Product Name", width=80, minwidth=100)
        tree.column("Price", width=80, minwidth=90, anchor=CENTER)
        tree.column("Quantity", width=100, minwidth=70, anchor=CENTER)

        # Assign the heading names to the respective columns
        tree.heading("Product ID", text="Product ID", anchor=CENTER)
        tree.heading("Product Name", text="Product Name", anchor=CENTER)
        tree.heading("Price", text="Price", anchor=CENTER)
        tree.heading("Quantity", text="Qty", anchor=CENTER)
        tree.bind('<Double 1>', GetRow2)
        tree.configure(height=3)
        tree.place(x=400, y=180)

        tree2 = ttk.Treeview(framebilling)
        tree2['show'] = 'headings'

        tbl2 = ttk.Style(framebilling)
        tbl2.theme_use("clam")
        tbl2.configure(".", font=('Helvetica', 10))
        tbl2.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

        # Define number of columns
        tree2["columns"] = ("Product ID", "Product Name", "Price", "Qty", "Sales")
        # Ansign the width, minwidth and anchor to the respective column
        tree2.column("Product ID", width=100, minwidth=90)
        tree2.column("Product Name", width=80, minwidth=100)
        tree2.column("Price", width=80, minwidth=90, anchor=CENTER)
        tree2.column("Qty", width=100, minwidth=70, anchor=CENTER)
        tree2.column("Sales", width=0, minwidth=0)

        #Assign the heading names to the respective columns
        tree2.heading("Product ID", text="Product ID", anchor=CENTER)
        tree2.heading("Product Name", text="Product Name", anchor=CENTER)
        tree2.heading("Price", text="Price", anchor=CENTER)
        tree2.heading("Qty", text="Qty", anchor=CENTER)
        tree2.heading("Sales", text="Sales", anchor=CENTER)
        tree2.bind('<Double 1>', GetRow)
        tree2.configure(height=4)

        i = 0
        for row in cursor:
            tree2.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4]))
            i = i + 1
        tree2.place(x=400, y=300)

        #LABEL
        id_lbl = Label(framebilling, text="Product ID:", font=('century gothic', 12, 'bold'), width=10, bg="gray", fg="white")
        id_lbl.place(x=70, y=200)
        name_lbl = Label(framebilling, text="Quantity:", font=('century gothic', 12, 'bold'), width=10, bg="gray", fg="white")
        name_lbl.place(x=70, y=240)
        tlt = Label(framebilling, text="Total:", font=('century gothic', 12, 'bold'), bg="gray", width=10, fg="white")
        tlt.place(x=70, y=290)
        pymnt = Label(framebilling, text="Payment:", font=('century gothic', 12, 'bold'), bg="gray", width=10, fg="white")
        pymnt.place(x=70, y=340)
        chng = Label(framebilling, text="Change:", font=('century gothic', 12, 'bold'), bg="gray", width=10, fg="white")
        chng.place(x=70, y=390)



        #ENTRY
        entry_id = Entry(framebilling, font=('century gothic', 12), width=20, textvariable=product_id)
        entry_id.place(x=170, y=200)
        entry_qty = Entry(framebilling, font=('century gothic', 12), width=20, textvariable=product_qty)
        entry_qty.place(x=170, y=240)
        entry_tot = Entry(framebilling, font=('century gothic', 12, 'bold'), bg='black', fg='white', width=20, textvariable=product_fintot)
        entry_tot.place(x=170, y=290)
        entry_pay = Entry(framebilling, font=('century gothic', 12), width=20, textvariable=bill_pay)
        entry_pay.place(x=170, y=340)
        entry_chng = Entry(framebilling, font=('century gothic', 12, 'bold'), bg='black', fg='white', width=20, textvariable=bill_change)
        entry_chng.place(x=170, y=390)
        # HIDDEN ENTRIES
        Entry(framebilling, font=('arial', 20), width=20, textvariable=product_name).pack_forget()
        Entry(framebilling, font=('arial', 20), width=20, textvariable=product_price).pack_forget()
        Entry(framebilling, font=('arial', 20), width=20, textvariable=product_partot).pack_forget()
        Entry(framebilling, font=('arial', 20), width=20, textvariable=product_qtydtb).pack_forget()
        Entry(framebilling, font=('arial', 20), width=20, textvariable=product_qtydtb2).pack_forget()
        Entry(framebilling, font=('arial', 20), width=20, textvariable=product_sales).pack_forget()
        # DELETE HIDDEN ENTRIES
        Entry(framebilling, font=('arial', 20), width=20, textvariable=product_delqty).pack_forget()
        Entry(framebilling, font=('arial', 20), width=20, textvariable=product_delqty1).pack_forget()
        Entry(framebilling, font=('arial', 20), width=20, textvariable=product_delsales).pack_forget()
        Entry(framebilling, font=('arial', 20), width=20, textvariable=product_delsales1).pack_forget()

        entry_pay.bind('<Return>', enter)

        def buy(tree2):
            curItem = tree2.focus()
            values = tree2.item(curItem, "values")

            p2_id = int(product_id.get())
            p2_name = str(product_name.get())
            p2_price = int(product_price.get())
            p2_qty = int(product_qty.get())
            p2_dbqty = int(product_qtydtb.get())
            p2_tot = int(product_fintot.get())
            p2_sales = int(product_sales.get())
            # computations
            com = int(p2_qty * p2_price)  # specific total
            fsales = p2_sales + com
            fin = p2_tot + com
            qty = p2_dbqty - p2_qty
            # computations
            product_fintot.set(fin)
            product_qtydtb2.set(qty)
            pchangeqty = product_qtydtb2.get()
            tree2.item(curItem, values=(values[0], values[1], values[2], pchangeqty, fsales))
            tree.insert('', 'end', text="", values=(p2_id, p2_name, com, p2_qty))
            cursor.execute("UPDATE inventorysales SET  p_qty=%s, p_sales=%s WHERE p_id=%s", (pchangeqty, fsales, values[0]))
            connectiondb.commit()
            MessageBox.showinfo("Success", "Added to Cart")
            entry_id.delete(0, END)
            entry_qty.delete(0, END)
            sales_btn3["state"]="disabled"

        def done():
            wayOut = tkinter.messagebox.askyesno("System Message",
                                             "You cannot undo the changes you have done")
            if wayOut > 0:
                    MessageBox.showinfo("Success", "Thank you!")
                    product_id.set(0)
                    product_qty.set(0)
                    product_name.set(0)
                    product_price.set(0)
                    product_partot.set(0)
                    product_qtydtb.set(0)
                    product_qtydtb2.set(0)
                    product_sales.set(0)
                    serc.set("")
                    product_fintot.set(0)
                    bill_change.set(0)
                    bill_pay.set(0)
                    tree.delete(*tree.get_children())
                    sales_btn3["state"] = "normal"

                    controller.show_frame("salesmenu")
        def delete_item(tree2):

            curItem = tree2.focus(tree.get_children())
            values = tree2.item(curItem, "values")
            selected_item = tree.selection()[0]
            p2_delq = int(product_delqty.get())
            p2_delq1 = int(product_delqty1.get())
            p2_dels = int(product_delsales.get())
            p2_dels1 = int(product_delsales1.get())
            p2_tot = int(product_fintot.get())
            # COMPUTATION
            com1 = p2_delq + p2_delq1
            com2 = p2_dels1 - p2_dels
            com3 = p2_tot - p2_dels
            tree2.item(curItem, values=(values[0], values[1], values[2], com1, com2))
            cursor.execute("UPDATE inventorysales SET  p_qty=%s, p_sales=%s WHERE p_id=%s", (com1, com2, values[0]))
            connectiondb.commit()
            product_fintot.set(com3)
            tree.delete(selected_item)
            MessageBox.showinfo("Success", "Data Deleted")

        add_btn = Button(framebilling, text="Add", font=('century gothic', 8, 'bold'), width=8, bg='black', fg='white',command=lambda: buy(tree2))
        add_btn.place(x=640, y=420)
        done_btn = Button(framebilling, text="Done", font=('century gothic', 8, 'bold'), width=8, bg='black', fg='white', command=done)
        done_btn.place(x=700, y=420)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()