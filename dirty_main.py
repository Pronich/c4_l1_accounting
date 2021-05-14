from application.salary import *
from application.db.people import *
from datetime import date

if __name__ == '__main__':
    print(date.today())
    get_employees()
    calculate_salary(10, 200)
