import datetime
from application.db.people import get_employees
from application.salary import calculate_salary

date = datetime.date.today()

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(date)