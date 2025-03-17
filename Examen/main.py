import tkinter as tk
from tkinter import ttk, messagebox
from db import database
def submit_fields(data_type, entries):
    values = [entry.get() for entry in entries]
    
    if all(values):
        if data_type == "partners":
            database.insert_partner(*values)
        elif data_type == "employees":
            database.insert_employee(*values)
        elif data_type == "materials":
            database.insert_material(*values)
        
        messagebox.showinfo("Success", "Data inserted successfully")
        
        # Очистка полей ввода
        for entry in entries:
            entry.delete(0, tk.END)
        
        display_data(data_type)
    else:
        messagebox.showerror("Error", "Please fill all fields")

def edit_fields(data_type, id_entry, entries):
    values = [entry.get() for entry in entries]
    if id_entry.get() and all(values):
        if data_type == "partners":
            database.update_partner(id_entry.get(), *values)
        elif data_type == "employees":
            database.update_employee(id_entry.get(), *values)
        elif data_type == "materials":
            database.update_material(id_entry.get(), *values)
        
        messagebox.showinfo("Success", "Data updated successfully")
    else:
        messagebox.showerror("Error", "Please fill all fields")

def display_data(data_type):
    data_window = tk.Toplevel(root)
    data_window.title(f"Информация о {data_type}")
    data_window.focus_set()
    data_window.grab_set()

    data_text = tk.Text(data_window, width=60, height=15)
    data_text.pack()

    if data_type == "partners":
        rows = database.get_partners()
        labels = ["ID", "Тип организации", "Наименование компании", "Юр. адрес", "ИНН", "ФИО Директора", "Телефон", "Email", "Логотип", "Рейтинг", "Место продажи", "История реализации"]
    elif data_type == "employees":
        rows = database.get_employees()
        labels = ["ID", "ФИО", "Дата рождения", "Паспортные данные", "Банковские реквизиты", "Семейное положение", "Состояние здоровья"]
    elif data_type == "materials":
        rows = database.get_materials()
        labels = ["ID", "Тип материала", "Название", "Поставщик", "Количество в упаковке", "Единица измерения", "Описание", "Изображение", "Стоимость", "Количество на складе", "Минимальное количество", "История изменений"]

    for row in rows:
        data_text.insert(tk.END, f"ID: {row[0]}\n" + "\n".join([f"{label}: {value}" for label, value in zip(labels, row)]) + "\n\n")

def create_entry_frame(parent, labels):
    frame = ttk.Frame(parent)
    frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    entries = []
    for i, label in enumerate(labels):
        row = i // 4
        col = i % 4
        ttk.Label(frame, text=label, font=("Helvetica", 12)).grid(row=row*2, column=col, columnspan=4, padx=5, pady=(10, 0), sticky="nsew")
        entry = ttk.Entry(frame, font=("Helvetica", 12))
        entry.grid(row=row*2+1, column=col, padx=(5, 5), pady=(0, 10), sticky="ew")
        entries.append(entry)
    return entries

def create_buttons_frame(parent, commands):
    button_frame = ttk.Frame(parent)
    button_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

    for i, (text, command) in enumerate(commands):
        if text == "Редактировать\nзапись":
            button = ttk.Button(button_frame, text=text.replace("\n", " "), command=command, style="TButton")
            button.grid(row=0, column=i, padx=(10, 10), pady=10, sticky="ew", ipadx=20)
        else:
            button = ttk.Button(button_frame, text=text, command=command, style="TButton")
            button.grid(row=0, column=i, padx=(10, 10), pady=10, sticky="ew")

    return button_frame

def show_partners_tab():
    notebook.select(partners_tab)

def show_employees_tab():
    notebook.select(employees_tab)

def show_materials_tab():
    notebook.select(materials_tab)

def create_widgets():
    global notebook, partners_tab, employees_tab, materials_tab, id_entry, type_entry, companyname_entry, address_entry, \
        inn_entry, fiodirector_entry, phone_entry, email_entry, \
        logo_entry, rating_entry, marketpoint_entry, history_entry, \
        id_entry_employees, fullname_entry_employees, birthdate_entry_employees, passport_data_entry_employees, \
        bank_details_entry_employees, has_family_entry_employees, health_status_entry_employees, \
        id_entry_materials, material_type_entry_materials, name_entry_materials, supplier_entry_materials, \
        quantity_per_package_entry_materials, unit_of_measurement_entry_materials, description_entry_materials, \
        image_entry_materials, cost_entry_materials, stock_quantity_entry_materials, \
        minimum_stock_quantity_entry_materials, quantity_change_history_entry_materials

    # Создаем вкладки
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)

    # Вкладка для партнеров
    partners_tab = ttk.Frame(notebook, style="TFrame")
    notebook.add(partners_tab, text="Партнеры")

    labels_partners = ["ID (for editing)", "Тип организации", "Наименование компании", "Юр. адрес", "ИНН", "ФИО Директора", "Телефон", "Email", "Логотип", "Рейтинг", "Место продажи", "История реализации"]
    id_entry, type_entry, companyname_entry, address_entry, \
    inn_entry, fiodirector_entry, phone_entry, email_entry, \
    logo_entry, rating_entry, marketpoint_entry, history_entry = create_entry_frame(partners_tab, labels_partners)

    commands_partners = [
        ("Внести данные\nо партнере", lambda: submit_fields("partners", [type_entry, companyname_entry, address_entry, inn_entry, fiodirector_entry, phone_entry, email_entry, logo_entry, rating_entry, marketpoint_entry, history_entry])),
        ("Редактировать\nзапись", lambda: edit_fields("partners", id_entry, [type_entry, companyname_entry, address_entry, inn_entry, fiodirector_entry, phone_entry, email_entry, logo_entry, rating_entry, marketpoint_entry, history_entry])),
        ("Просмотр информации\nо партнерах", lambda: display_data("partners")),
        ("Перейти к сотрудникам", show_employees_tab)
    ]
    create_buttons_frame(partners_tab, commands_partners)

    # Вкладка для сотрудников
    employees_tab = ttk.Frame(notebook, style="TFrame")
    notebook.add(employees_tab, text="Сотрудники")

    labels_employees = ["ID (for editing)", "ФИО", "Дата рождения", "Паспортные данные", "Банковские реквизиты", "Семейное положение", "Состояние здоровья"]
    id_entry_employees, fullname_entry_employees, birthdate_entry_employees, passport_data_entry_employees, \
    bank_details_entry_employees, has_family_entry_employees, health_status_entry_employees = create_entry_frame(employees_tab, labels_employees)

    commands_employees = [
        ("Внести данные\nо сотруднике", lambda: submit_fields("employees", [fullname_entry_employees, birthdate_entry_employees, passport_data_entry_employees, bank_details_entry_employees, has_family_entry_employees, health_status_entry_employees])),
        ("Редактировать\nзапись", lambda: edit_fields("employees", id_entry_employees, [fullname_entry_employees, birthdate_entry_employees, passport_data_entry_employees, bank_details_entry_employees, has_family_entry_employees, health_status_entry_employees])),
        ("Просмотр информации\nо сотрудниках", lambda: display_data("employees")),
        ("Перейти к материалам", show_materials_tab)
    ]
    create_buttons_frame(employees_tab, commands_employees)

    # Вкладка для материалов
    materials_tab = ttk.Frame(notebook, style="TFrame")
    notebook.add(materials_tab, text="Материалы")

    labels_materials = ["ID (for editing)", "Тип материала", "Название", "Поставщик", "Количество в упаковке", "Единица измерения", "Описание", "Изображение", "Стоимость", "Количество на складе", "Минимальное количество", "История изменений"]
    id_entry_materials, material_type_entry_materials, name_entry_materials, supplier_entry_materials, \
    quantity_per_package_entry_materials, unit_of_measurement_entry_materials, description_entry_materials, \
    image_entry_materials, cost_entry_materials, stock_quantity_entry_materials, \
    minimum_stock_quantity_entry_materials, quantity_change_history_entry_materials = create_entry_frame(materials_tab, labels_materials)

    commands_materials = [
        ("Внести данные\nо материале", lambda: submit_fields("materials", [material_type_entry_materials, name_entry_materials, supplier_entry_materials, quantity_per_package_entry_materials, unit_of_measurement_entry_materials, description_entry_materials, image_entry_materials, cost_entry_materials, stock_quantity_entry_materials, minimum_stock_quantity_entry_materials, quantity_change_history_entry_materials])),
        ("Редактировать\nзапись", lambda: edit_fields("materials", id_entry_materials, [material_type_entry_materials, name_entry_materials, supplier_entry_materials, quantity_per_package_entry_materials, unit_of_measurement_entry_materials, description_entry_materials, image_entry_materials, cost_entry_materials, stock_quantity_entry_materials, minimum_stock_quantity_entry_materials, quantity_change_history_entry_materials])),
        ("Просмотр информации\nо материалах", lambda: display_data("materials")),
        ("Перейти к партнерам", show_partners_tab)
    ]
    create_buttons_frame(materials_tab, commands_materials)

# Создаем соединение с базой данных
database.create_connection()
database.create_tables()

# Создаем главное окно
root = tk.Tk()
root.title("Учет и контроль состояния компьютерной техники")
root.geometry("1000x600")  # Увеличиваем ширину окна
root.configure(bg="white")

# Устанавливаем стиль для ttk
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', padding=6, relief="flat", background="#0078d7", foreground="white", font=("Helvetica", 12))
style.map('TButton', background=[('active', '#005a9e')])
style.configure('TLabel', background="white", foreground="#333333", font=("Helvetica", 12))
style.configure('TEntry', fieldbackground="white", foreground="#333333", font=("Helvetica", 12))
style.configure('TFrame', background="white")
style.configure('TNotebook.Tab', background="white", foreground="#0078d7", font=("Helvetica", 12))
style.map('TNotebook.Tab', background=[('selected', 'white')])
style.configure('TNotebook', background="#f0f0f0")  # Цвет фона заголовочной области блокнота

# Создаем виджеты
create_widgets()

# Запускаем главный цикл
root.mainloop()