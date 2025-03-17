import sqlite3

# Функция для создания соединения с базой данных
def create_connection():
    connection = sqlite3.connect('demo.db')
    return connection

# Функция для создания таблиц
def create_tables():
    connection = create_connection()
    cursor = connection.cursor()

    # Таблица Partners (оставляем без изменений, если она вам нужна)
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

    # Таблица Departments
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Departments (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL) ''')

    # Таблица Devices (заменили Computers на Devices)
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Devices (
                        id INTEGER PRIMARY KEY,
                        department_id INTEGER,
                        device_type TEXT NOT NULL,  -- Тип устройства (ПК, ноутбук, ...)
                        model TEXT NOT NULL,
                        serial_number TEXT,
                        inventory_number TEXT,
                        cpu TEXT,            -- Процессор
                        memory TEXT,         -- Память
                        hard_drive TEXT,     -- Жесткий диск
                        video_card TEXT,     -- Видеокарта
                        status TEXT,
                        FOREIGN KEY (department_id) REFERENCES Departments (id) ON DELETE CASCADE) ''')

    connection.commit()
    connection.close()

# --- Функции для работы с отделами ---
def insert_department(name):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Departments (name) VALUES (?)", (name,))
    connection.commit()
    department_id = cursor.lastrowid # Возвращаем id вставленной строки
    connection.close()
    return department_id # Возвращаем ID

def get_departments():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Departments")
    rows = cursor.fetchall()
    connection.close()
    return rows

def update_department(id, name):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Departments SET name=? WHERE id=?", (name, id))
    connection.commit()
    connection.close()

def delete_department(id):
    connection = create_connection()
    cursor = connection.cursor()
    # Удаляем сначала связанные устройства (CASCADE будет работать из-за ON DELETE CASCADE)
    cursor.execute("DELETE FROM Devices WHERE department_id=?", (id,))
    # Затем удаляем отдел
    cursor.execute("DELETE FROM Departments WHERE id=?", (id,))
    connection.commit()
    connection.close()

# --- Функции для работы с устройствами ---
def insert_device(department_id, device_type, model, serial_number, inventory_number, cpu, memory, hard_drive, video_card, status):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Devices (department_id, device_type, model, serial_number, inventory_number, cpu, memory, hard_drive, video_card, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (department_id, device_type, model, serial_number, inventory_number, cpu, memory, hard_drive, video_card, status))
    connection.commit()
    device_id = cursor.lastrowid  # Получаем ID вставленной строки
    connection.close()
    return device_id  # Возвращаем ID

def get_devices(department_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Devices WHERE department_id=?", (department_id,))
    rows = cursor.fetchall()
    connection.close()
    return rows

def update_device(id, department_id, device_type, model, serial_number, inventory_number, cpu, memory, hard_drive, video_card, status):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Devices SET department_id=?, device_type=?, model=?, serial_number=?, inventory_number=?, cpu=?, memory=?, hard_drive=?, video_card=?, status=? WHERE id=?",
                   (department_id, device_type, model, serial_number, inventory_number, cpu, memory, hard_drive, video_card, status, id))
    connection.commit()
    connection.close()

def delete_device(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Devices WHERE id=?", (id,))
    connection.commit()
    connection.close()

# Оставляем ваши функции для Partners (если они вам нужны):
def insert_partner(type, companyname, address, inn, fiodirector, phone, email, logo, rating, marketpoint, history):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Partners (type, companyname, address, inn, fiodirector, phone, email, logo, rating, marketpoint, history) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (type, companyname, address, inn, fiodirector, phone, email, logo, rating, marketpoint, history))
    connection.commit()
    connection.close()

def update_partner(id, type, companyname, address, inn, fiodirector, phone, email, logo, rating, marketpoint, history):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Partners SET type=?, companyname=?, address=?, inn=?, fiodirector=?, phone=?, email=?, logo=?, rating=?, marketpoint=?, history=? WHERE id=?",
                    (type, companyname, address, inn, fiodirector, phone, email, logo, rating, marketpoint, history, id))
    connection.commit()
    connection.close()

def get_partners():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Partners")
    rows = cursor.fetchall()
    connection.close()
    return rows

def get_device(id):
    connection = sqlite3.connect('demo.db')  # Замените 'demo.db' на имя вашей базы данных
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Devices WHERE id=?", (id,))
    device = cursor.fetchone()
    connection.close()
    return device

if __name__ == '__main__':
    create_tables()