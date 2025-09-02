from product_manager import create_product, read_all, read_by_id
from product_manager import update, delete_by_id
from product import Product



def menu():
    message = '''



1 - Crate Product
2 - Read All Products
3 - Read By id
4 - Update 
5 - Delete 
6 - Exit/ Logout 
'''
    choice = int(input(message))
    if choice == 1:
        name = input('Name:')
        description = input('description:')
        category = input('category:')
        tags = input('tags')
        stock = int(input('stock:'))
        price = int(input('price:'))
        id= -1


        product = Product(id,name, description, category,tags, stock, price)


        create_product(product)
    elif choice == 2:
        result_salaries = read_all()
        print('salaries:')
        for salary in result_salaries:
            print(salary)
    elif choice == 3:
        salary = int(input('Search  Salary:'))
        index = read_by_id(salary)
        if salary == -1:
            print('Salary not found')
        else:
            print(f'Salary is at index {index}')
    elif choice == 4:
        old_salary = int(input(' Salary to update:'))
        new_salary = int(input('New Salary:'))
        update(salary, new_salary)




    elif choice == 5:
        salary = int(input('Salary to delete:'))
        delete_by_id(salary)
    return choice
def menus():
    print('Salary Mnaagement App')
    choice = menu()
    while choice != 6:
        choice = menu ()
    print('Thank You for using app')
menus()