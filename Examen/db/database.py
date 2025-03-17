import sqlite3

# Функция для создания соединения с базой данных
def create_connection():
    connection = sqlite3.connect('demo.db')
    return connection

# Функция для создания таблиц
def create_tables():
    connection = create_connection()
    cursor = connection.cursor()
    
    # Таблица Partners
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Partners(
                        id INTEGER PRIMARY KEY,
                        type TEXT NOT NULL,
                        companyname TEXT NOT NULL,
                        address TEXT NOT NULL,
                        inn INTEGER NOT NULL,
                        fiodirector TEXT NOT NULL,
                        phone INTEGER NOT NULL,
                        email TEXT NOT NULL,
                        logo BLOB NULL,
                        rating INTEGER NOT NULL,
                        marketpoint TEXT NOT NULL,
                        history INTEGER NOT NULL) ''')

    # Таблица Employees
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Employees(
                        id INTEGER PRIMARY KEY,
                        fullname TEXT NOT NULL,
                        birthdate TEXT NOT NULL,
                        passport_data TEXT NOT NULL,
                        bank_details TEXT NOT NULL,
                        has_family INTEGER NOT NULL, -- 1 (да) или 0 (нет)
                        health_status TEXT NOT NULL) ''')
    
    # Таблица Materials
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Materials(
                        id INTEGER PRIMARY KEY,
                        material_type TEXT NOT NULL,
                        name TEXT NOT NULL,
                        supplier TEXT NOT NULL,
                        quantity_per_package REAL NOT NULL,
                        unit_of_measurement TEXT NOT NULL,
                        description TEXT,
                        image BLOB,
                        cost REAL NOT NULL,
                        stock_quantity REAL NOT NULL,
                        minimum_stock_quantity REAL NOT NULL,
                        quantity_change_history TEXT) ''')
    
    # Таблица Orders
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Orders(
                        id INTEGER PRIMARY KEY,
                        partner_id INTEGER NOT NULL,
                        product_id INTEGER NOT NULL,
                        quantity INTEGER NOT NULL,
                        cost REAL NOT NULL,
                        production_date TEXT NOT NULL,
                        status TEXT NOT NULL, 
                        FOREIGN KEY (partner_id) REFERENCES Partners(id),
                        FOREIGN KEY (product_id) REFERENCES Products(id)) ''')
    
    # Таблица Products
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Products(
                        id INTEGER PRIMARY KEY,
                        article TEXT NOT NULL,
                        type TEXT NOT NULL,
                        name TEXT NOT NULL,
                        description TEXT,
                        image BLOB,
                        min_cost_for_partner REAL NOT NULL,
                        package_size TEXT NOT NULL,
                        weight_without_package REAL NOT NULL,
                        weight_with_package REAL NOT NULL,
                        quality_certificate BLOB,
                        standard_number TEXT NOT NULL,
                        min_cost_change_history TEXT,
                        production_time TEXT NOT NULL,
                        cost_price REAL NOT NULL,
                        workshop_number INTEGER NOT NULL,
                        production_people_count INTEGER NOT NULL,
                        required_materials TEXT NOT NULL) ''')
    
    # Таблица Suppliers
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Suppliers(
                        id INTEGER PRIMARY KEY,
                        type TEXT NOT NULL,
                        name TEXT NOT NULL,
                        inn INTEGER NOT NULL,
                        supply_history TEXT) ''')
    
    connection.commit()
    connection.close()

# Вставка данных в таблицу Partners
def insert_partner(type, companyname, address, inn, fiodirector, phone, email, logo, rating, marketpoint, history):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Partners (type, companyname, address, inn, fiodirector, phone, email, logo, rating, marketpoint, history) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (type, companyname, address, inn, fiodirector, phone, email, logo, rating, marketpoint, history))
    connection.commit()
    connection.close()

# Вставка данных в таблицу Employees
def insert_employee(fullname, birthdate, passport_data, bank_details, has_family, health_status):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Employees (fullname, birthdate, passport_data, bank_details, has_family, health_status) VALUES (?, ?, ?, ?, ?, ?)",
                   (fullname, birthdate, passport_data, bank_details, has_family, health_status))
    connection.commit()
    connection.close()

# Вставка данных в таблицу Materials
def insert_material(material_type, name, supplier, quantity_per_package, unit_of_measurement, description, image, cost, stock_quantity, minimum_stock_quantity, quantity_change_history):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO Materials (material_type, name, supplier, quantity_per_package, unit_of_measurement, description, image, cost, stock_quantity, minimum_stock_quantity, quantity_change_history)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (material_type, name, supplier, quantity_per_package, unit_of_measurement, description, image, cost, stock_quantity, minimum_stock_quantity, quantity_change_history))
    connection.commit()
    connection.close()

# Вставка данных в таблицу Orders
def insert_order(partner_id, product_id, quantity, cost, production_date, status):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO Orders (partner_id, product_id, quantity, cost, production_date, status)
                      VALUES (?, ?, ?, ?, ?, ?)''',
                   (partner_id, product_id, quantity, cost, production_date, status))
    connection.commit()
    connection.close()

# Вставка данных в таблицу Products
def insert_product(article, type, name, description, image, min_cost_for_partner, package_size, weight_without_package, weight_with_package, quality_certificate, standard_number, min_cost_change_history, production_time, cost_price, workshop_number, production_people_count, required_materials):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO Products (article, type, name, description, image, min_cost_for_partner, package_size, weight_without_package, weight_with_package, quality_certificate, standard_number, min_cost_change_history, production_time, cost_price, workshop_number, production_people_count, required_materials)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (article, type, name, description, image, min_cost_for_partner, package_size, weight_without_package, weight_with_package, quality_certificate, standard_number, min_cost_change_history, production_time, cost_price, workshop_number, production_people_count, required_materials))
    connection.commit()
    connection.close()

# Вставка данных в таблицу Suppliers
def insert_supplier(type, name, inn, supply_history):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO Suppliers (type, name, inn, supply_history)
                      VALUES (?, ?, ?, ?)''',
                   (type, name, inn, supply_history))
    connection.commit()
    connection.close()

# Обновление данных в таблице Partners
def update_partner(id, type, companyname, address, inn, fiodirector, phone, email, logo, rating, marketpoint, history):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Partners SET type=?, companyname=?, address=?, inn=?, fiodirector=?, phone=?, email=?, logo=?, rating=?, marketpoint=?, history=? WHERE id=?",
                    (type, companyname, address, inn, fiodirector, phone, email, logo, rating, marketpoint, history, id))
    connection.commit()
    connection.close()

# Обновление данных в таблице Employees
def update_employee(id, fullname, birthdate, passport_data, bank_details, has_family, health_status):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''UPDATE Employees SET fullname=?, birthdate=?, passport_data=?, bank_details=?, has_family=?, health_status=? WHERE id=?''',
                   (fullname, birthdate, passport_data, bank_details, has_family, health_status, id))
    connection.commit()
    connection.close()

# Обновление данных в таблице Materials
def update_material(id, material_type, name, supplier, quantity_per_package, unit_of_measurement, description, image, cost, stock_quantity, minimum_stock_quantity, quantity_change_history):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''UPDATE Materials SET material_type=?, name=?, supplier=?, quantity_per_package=?, unit_of_measurement=?, description=?, image=?, cost=?, stock_quantity=?, minimum_stock_quantity=?, quantity_change_history=? WHERE id=?''',
                   (material_type, name, supplier, quantity_per_package, unit_of_measurement, description, image, cost, stock_quantity, minimum_stock_quantity, quantity_change_history, id))
    connection.commit()
    connection.close()

# Обновление данных в таблице Orders
def update_order(id, partner_id, product_id, quantity, cost, production_date, status):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''UPDATE Orders SET partner_id=?, product_id=?, quantity=?, cost=?, production_date=?, status=? WHERE id=?''',
                   (partner_id, product_id, quantity, cost, production_date, status, id))
    connection.commit()
    connection.close()

# Обновление данных в таблице Products
def update_product(id, article, type, name, description, image, min_cost_for_partner, package_size, weight_without_package, weight_with_package, quality_certificate, standard_number, min_cost_change_history, production_time, cost_price, workshop_number, production_people_count, required_materials):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''UPDATE Products SET article=?, type=?, name=?, description=?, image=?, min_cost_for_partner=?, package_size=?, weight_without_package=?, weight_with_package=?, quality_certificate=?, standard_number=?, min_cost_change_history=?, production_time=?, cost_price=?, workshop_number=?, production_people_count=?, required_materials=? WHERE id=?''',
                   (article, type, name, description, image, min_cost_for_partner, package_size, weight_without_package, weight_with_package, quality_certificate, standard_number, min_cost_change_history, production_time, cost_price, workshop_number, production_people_count, required_materials, id))
    connection.commit()
    connection.close()

# Обновление данных в таблице Suppliers
def update_supplier(id, type, name, inn, supply_history):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''UPDATE Suppliers SET type=?, name=?, inn=?, supply_history=? WHERE id=?''',
                   (type, name, inn, supply_history, id))
    connection.commit()
    connection.close()

# Получение всех данных из таблицы Partners
def get_partners():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Partners")
    rows = cursor.fetchall()
    connection.close()
    return rows

# Получение всех данных из таблицы Employees
def get_employees():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Employees")
    rows = cursor.fetchall()
    connection.close()
    return rows

# Получение всех данных из таблицы Materials
def get_materials():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Materials")
    rows = cursor.fetchall()
    connection.close()
    return rows

# Получение всех данных из таблицы Orders
def get_orders():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Orders")
    rows = cursor.fetchall()
    connection.close()
    return rows

# Получение всех данных из таблицы Products
def get_products():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    connection.close()
    return rows

# Получение всех данных из таблицы Suppliers
def get_suppliers():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Suppliers")
    rows = cursor.fetchall()
    connection.close()
    return rows

# Основной блок для создания таблиц
if __name__ == '__main__':
    create_tables()