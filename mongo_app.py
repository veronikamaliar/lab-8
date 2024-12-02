import pymongo

# Підключення до сервера MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Створення бази даних
db = client["mydatabase"]

# Створення колекції (еквівалент таблиці в реляційних базах даних)
expense_categories = db['Expense_Categories']
expenses = db['Expenses']
income_sources = db['Income_Sources']
incomes = db['Incomes']
users = db['Users']

def insert_if_not_exists(collection, query, data):
    existing_document = collection.find_one(query)
    if existing_document is None:
        collection.insert_one(data)
        print(f"Додано новий документ: {data}")
    else:
        print(f"Документ уже існує: {existing_document}")

# Вставка категорій витрат
category_1 = {
    "category_name": "Food",
    "description": "Food for week"
}
insert_if_not_exists(expense_categories, {"category_name": "Food"}, category_1)

category_2 = {
    "category_name": "Transport",
    "description": "Expenses for public transport and fuel"
}
insert_if_not_exists(expense_categories, {"category_name": "Transport"}, category_2)

# Вставка витрат
expense_1 = {
    "user_id": 1,
    "category_id": 1,
    "amount": 150.50,
    "date_incurred": "2024-12-01"
}
insert_if_not_exists(expenses, {"user_id": 1, "category_id": 1, "date_incurred": "2024-12-01"}, expense_1)

expense_2 = {
    "user_id": 2,
    "category_id": 2,
    "amount": 50.00,
    "date_incurred": "2024-12-02"
}
insert_if_not_exists(expenses, {"user_id": 2, "category_id": 2, "date_incurred": "2024-12-02"}, expense_2)

# Вставка джерел доходу
income_source_1 = {
    "source_name": "Salary",
    "description": "Monthly salary from job"
}
insert_if_not_exists(income_sources, {"source_name": "Salary"}, income_source_1)

income_source_2 = {
    "source_name": "Freelance",
    "description": "Income from freelance work"
}
insert_if_not_exists(income_sources, {"source_name": "Freelance"}, income_source_2)

# Вставка доходів
income_1 = {
    "user_id": 1,
    "income_source_id": 1,
    "amount": 2000.00,
    "date_received": "2024-12-01"
}
insert_if_not_exists(incomes, {"user_id": 1, "income_source_id": 1, "date_received": "2024-12-01"}, income_1)

income_2 = {
    "user_id": 2,
    "income_source_id": 2,
    "amount": 1500.00,
    "date_received": "2024-12-02"
}
insert_if_not_exists(incomes, {"user_id": 2, "income_source_id": 2, "date_received": "2024-12-02"}, income_2)

# Вставка користувачів
user_1 = {
    "first_name": "Viktoria",
    "last_name": "Litvin",
    "email": "viktoria@gmail.com",
    "password": "1234567"
}
insert_if_not_exists(users, {"email": "veronika@gmail.com"}, user_1)

user_2 = {
    "first_name": "Maria",
    "last_name": "Melnyk",
    "email": "maria@gmail.com",
    "password": "7654321"
}
insert_if_not_exists(users, {"email": "maria@gmail.com"}, user_2)

# Зчитування документів
print("Expense Categories:")
for document in expense_categories.find():
    print(document)
print("Expenses:")
for document in expenses.find():
    print(document)
print("Income Sources:")
for document in income_sources.find():
    print(document)
print("Incomes:")
for document in incomes.find():
    print(document)
print("Users:")
for document in users.find():
    print(document)

# Пошук
category = expense_categories.find_one({"category_name": "Food"})
print(category)
user_expenses = expenses.find({"user_id": 1})
for expense in user_expenses:
    print(expense)
category = income_sources.find_one({"source_name": "Salary"})
print(category)
user_incomes = incomes.find({"user_id": 1})
for income in user_incomes:
    print(income)
user = users.find_one({"email": "veronika@gmail.com"})
print(user)



# Оновлення категорії витрат
query_category = {"category_name": "Food"} 
new_data_category = {"$set": {"description": "Food for mounth"}}
expense_categories.update_one(query_category, new_data_category)
# Оновлення витрат для користувача з ID 1
query_expense = {"category_id": 1} 
new_data_expense = {"$set": {"amount": 200.00, "date_incurred": "2024-12-02"}}
expenses.update_one(query_expense, new_data_expense)
# Оновлення джерела доходу
query_income_source = {"source_name": "Freelance"}  
new_data_income_source = {"$set": {"description": "Freelance income"}}
income_sources.update_one(query_income_source, new_data_income_source)
# Оновлення доходу для користувача з ID 1
query_income = {"income_source_id": 1}  
new_data_income = {"$set": {"amount": 2500.00, "date_received": "2024-12-05"}}
incomes.update_one(query_income, new_data_income)
# Оновлення користувача
query_users = {"first_name": "Maria"}  
new_data_users = {"$set": {"email": "mariaaaa@gmail.com"}}
users.update_one(query_users, new_data_users)



# Видалення категорії витрат
delete_query_category = {"category_name": "Food"}
expense_categories.delete_one(delete_query_category)

# Видалення витрат
delete_query_expense = {"category_id": 2}
expenses.delete_one(delete_query_expense)

# Видалення джерела доходу
delete_query_income_source = {"source_name": "Salary"}
income_sources.delete_one(delete_query_income_source)

# Видалення доходу
delete_query_income = {"income_source_id": 2}
incomes.delete_one(delete_query_income)

# Видалення користувача
delete_query_user = {"first_name": "Viktoria"}
users.delete_one(delete_query_user)

# Зчитування документів після оновлення та видалення
print("Після оновлення та видалення:")

print("Expense Categories:")
for category in expense_categories.find():
    print(category)

print("Expenses:")
for expense in expenses.find():
    print(expense)

print("Income Sources:")
for income_source in income_sources.find():
    print(income_source)

print("Incomes:")
for income in incomes.find():
    print(income)

print("Users:")
for users in users.find():
    print(users)

# Закриття підключення
client.close()
