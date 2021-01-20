import tkinter as tk
from tkinter import messagebox as mgb
from tkinter import ttk
import sqlite3


class Sklad(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.create_widgets()
        self.db = db
        self.tr = tr
        self.tr.view_record_db()

    def create_widgets(self):
        self.entry_action = tk.Label(self, text='Выберите действие', justify=tk.LEFT)
        self.entry_action.grid(row=0, column=0)

        self.add_sklad = tk.Button(self, text='Добавить на склад', bd=5, justify=tk.CENTER, width=75, height=2,
                                   command=self.open_dialog_add)
        self.add_sklad.grid(row=0, column=3)

        self.remove_skald = tk.Button(self, text='Забрать со склада', bd=5, justify=tk.CENTER, width=75, height=2,
                                      command=self.remove_wh)

        self.remove_skald.grid(row=1, column=3)
        self.from_sklad = tk.Button(self, text='Проверить наличие на складе', bd=5, justify=tk.CENTER, width=75,
                                    height=2, command=self.check_nal)
        self.from_sklad.grid(row=2, column=3)
        self.table = tk.Button(self, text='Таблица', bd=5, justify=tk.CENTER, width=75, height=2,
                               command=self.in_table)
        self.table.grid(row=3, column=3)

    def record_db(self, name, model, serial, quantity, shelf, place):
        self.db.insert_data(name, model, serial, quantity, shelf, place)
        self.tr.view_record_db()

    @staticmethod
    def open_dialog_add():
        Add_sklad()

    @staticmethod
    def remove_wh():
        Remove_sklad()

    @staticmethod
    def check_nal():
        Chek()

    @staticmethod
    def in_table():
        Tree()


class Add_sklad(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Внести на склад')
        self.geometry('600x600')
        self.resizable(False, False)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place()

        self.grab_set()
        self.focus_set()

        self.entry_name = tk.Label(self, text="Наименование: ", justify=tk.LEFT)
        self.entryName = ttk.Entry(self, width=35)
        self.entryName.grid(row=0, column=1)
        self.entry_name.grid(row=0, column=0)

        self.entry_model = tk.Label(self, text='Модель: ', justify=tk.RIGHT)
        self.entryModel = ttk.Entry(self, width=35)
        self.entryModel.grid(row=1, column=1)
        self.entry_model.grid(row=1, column=0)

        self.entry_serial = tk.Label(self, justify=tk.LEFT, text='Серийный №: ')
        self.entrySerial = ttk.Entry(self, width=35)
        self.entrySerial.grid(row=2, column=1)
        self.entry_serial.grid(row=2, column=0)

        self.entry_quantity = tk.Label(self, justify=tk.LEFT, text='Количество: ')
        self.entryQantity = ttk.Entry(self, width=35)
        self.entryQantity.grid(row=3, column=1)
        self.entry_quantity.grid(row=3, column=0)

        self.entry_shelf = tk.Label(self, justify=tk.LEFT, text='Стеллаж №: ')
        self.entryShelf = ttk.Entry(self, width=35)
        self.entryShelf.grid(row=4, column=1)
        self.entry_shelf.grid(row=4, column=0)

        self.entry_longline = tk.Label(self, justify=tk.LEFT, text='Полка №: ')
        self.entryLongline = ttk.Entry(self, width=35)
        self.entryLongline.grid(row=5, column=1)
        self.entry_longline.grid(row=5, column=0)

        self.entry_place = tk.Label(self, justify=tk.LEFT, text='Ячейка №: ')
        self.entryPlace = ttk.Entry(self, width=35)
        self.entryPlace.grid(row=5, column=1)
        self.entry_place.grid(row=5, column=0)
        btn_ok = tk.Button(self, text='Внести')
        btn_ok.place(y=585, x=300, anchor=tk.S)
        btn_ok.bind('<Button-1>', lambda event: self.view.record_db(self.entryName.get(), self.entryModel.get(),
                                                                    self.entrySerial.get(), self.entryQantity.get(),
                                                                    self.entryShelf.get(), self.entryPlace.get()))


class Tree(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.tree()
        self.db = db

    def tree(self):
        self.tree1 = ttk.Treeview(self, columns=('name', 'model', 'serial', 'quantity', 'shelf', 'place'),
                                  height=15, show='headings')

        self.tree1.column('model', width=90, anchor=tk.CENTER)
        self.tree1.column('serial', width=90, anchor=tk.CENTER)
        self.tree1.column('quantity', width=90, anchor=tk.CENTER)
        self.tree1.column('shelf', width=90, anchor=tk.CENTER)
        self.tree1.column('place', width=90, anchor=tk.CENTER)

        self.tree1.heading('name', text='Наименование')
        self.tree1.heading('model', text='Модель')
        self.tree1.heading('serial', text='Серийный №')
        self.tree1.heading('quantity', text='Количество')
        self.tree1.heading('shelf', text='Стелаж №')
        self.tree1.heading('place', text='Место №')

        self.tree1.grid()

    def view_record_db(self):
        self.db.c.execute('''SELECT * FROM sklad''')
        [self.tree1.delete(i) for i in self.tree1.get_children()]
        [self.tree1.insert('', 'end', values=row) for row in self.db.c.fetchall()]


class Remove_sklad(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_remove()

    def init_remove(self):
        self.title('Забрать со склада')
        self.geometry('600x600')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        self.name_remove = tk.Label(self, justify=tk.LEFT, text='Наименование')
        self.entryRemove = tk.Entry(self, width=35)
        self.entryRemove.grid(row=0, column=1)
        self.name_remove.grid(row=0, column=0)

        self.entry_serial = tk.Label(self, justify=tk.LEFT, text='Серийный №: ')
        self.entrySerial = tk.Entry(self, width=35)
        self.entrySerial.grid(row=2, column=1)
        self.entry_serial.grid(row=2, column=0)

        self.entry_quantity = tk.Label(self, justify=tk.LEFT, text='Количество: ')
        self.entryQantity = tk.Entry(self, width=35)
        self.entryQantity.grid(row=4, column=1)
        self.entry_quantity.grid(row=4, column=0)

        self.sur_name = tk.Label(self, justify=tk.LEFT, text='Фамилия')
        self.surName = tk.Entry(self, width=35)
        self.sur_name.grid(row=3, column=0)
        self.surName.grid(row=3, column=1)

        btn_ok = tk.Button(self, text='Забрать')
        btn_ok.place(y=585, x=300, anchor=tk.S)


class Chek(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.check_wh()
        self.db = db
        self.tr = tr
        self.check_in()

    def check_wh(self):
        self.title('Проверить наличие')
        self.geometry('600x600')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        self.name_check = tk.Label(self, justify=tk.LEFT, text='Наименование')
        self.entryCheck = ttk.Entry(self, width=35)
        self.entryCheck.grid(row=0, column=1)
        self.name_check.grid(row=0, column=0)

        self.entry_serial = tk.Label(self, justify=tk.LEFT, text='Серийный №: ')
        self.entrySerial = ttk.Entry(self, width=35)
        self.entrySerial.grid(row=2, column=1)
        self.entry_serial.grid(row=2, column=0)

        btn_ok = tk.Button(self, text='Проверить', command=self.check_in)
        btn_ok.place(y=585, x=300, anchor=tk.S)

    def check_in(self):
        self.db.conn.row_factory = sqlite3.Row
        self.db.c.execute("SELECT * from sklad")
        self.check = self.db.c.fetchone()
        for number in self.check:

            if self.check(number[0]) != self.entryCheck and self.check(number[2]) != self.entrySerial:

                mgb.showerror(title='Ошибка', message='Данных не существует')
            else:
                self.tr.view_record_db()


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('db_sklad.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS sklad (id integer primary key, name text, model text, serial text, quantity int, shelf INT, place INT) ''')
        self.conn.commit()

    def insert_data(self, name, model, serial, quantity, shelf, place):
        self.c.execute("""INSERT INTO sklad (name, model, serial, quantity, shelf, place) VALUES (?, ?, ?, ?, ?, ?)""",
                       (name, model, serial, quantity, shelf, place))
        self.conn.commit()


if __name__ == '__main__':
    root = tk.Tk()
    db = DB()
    tr = Tree()
    app = Sklad(root)
    app.grid()

    root.title('Программа реализации склада')
    root.geometry('1200x800')
    root.resizable(False, False)

    root.mainloop()