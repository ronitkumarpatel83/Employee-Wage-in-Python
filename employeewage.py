"""
    @Name = Ronit kumar Patel
    @Title = Employee Wage
"""
import logging
import random

print("********************************************************************************")
print("<<<<<<<<<<<<----- Welcome to Employee Wage Computation Program----->>>>>>>>>>>>> ")
print("********************************************************************************")

log = '%(lineno)d ** %(asctime)s ** %(message)s'
logging.basicConfig(filename='EmployeeWage.log', filemode='w', format=log, level=logging.DEBUG)


class Employee:
    def __init__(self, name, wage_per_hour, monthly_working_day, total_working_hour):
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.monthly_working_day = monthly_working_day
        self.total_working_hour = total_working_hour

    def check_attendance(self, rand):
        """
        This function is work for calculation employees wage
        :return:
        """
        try:
            if rand == 0:
                daily_work_hour = 8
                print(" Employee is present ")
            elif rand == 1:
                daily_work_hour = 4
                print(" Employee is present for part-time ")
            else:
                daily_work_hour = 0
                print(" Employee is absent ")
            return daily_work_hour
        except Exception as e:
            print(e)
            logging.exception("There is something occurs please re-check the code")

    def calculating_wage(self):
        """
        This function is work for employees attendance
        is there take attendance using random
        :return: nothing
        """
        logging.debug("Employee wage program is running perfectly.....")
        try:
            total_wage = 0
            no_of_working_days = 0
            working_hours = 0
            while no_of_working_days < self.monthly_working_day and working_hours <= self.total_working_hour:
                no_of_working_days += 1
                rand = random.randint(0, 2)
                daily_work_hour = self.check_attendance(rand)
                print(f" The working days is : {no_of_working_days}")
                working_hours += daily_work_hour
                print(f" The working hours is : {working_hours}")
                daily_wage = self.wage_per_hour * daily_work_hour
                print(f" The daily wage is : {daily_wage}")
                total_wage += daily_wage
                print("------------------------------------------------")
            print(f"The monthly wage is : {total_wage}")
            print("------------------------------------------------")
            return total_wage

        except Exception as e:
            print(e)
            logging.exception("There is something occurs please re-check the code")

    def as_dict(self):
        return {"Name": self.name }


class Company:
    def __init__(self, name):
        self.name = name
        self.employee_dict = {}

    def add_employee(self, employee_obj):
        self.employee_dict.update({self.name: employee_obj})

    def delete_employee(self):
        self.employee_dict.clear()

    def view(self):
        print(self.employee_dict)


if __name__ == "__main__":
    try:
        comp1 = Company("labz")
        comp2 = Company("tcs")

        company_dict = {comp1.name: comp1, comp2.name: comp2}

        emp1 = Employee("Ronit", 20, 20, 100)
        emp2 = Employee("Dibya", 18, 15, 80)
        comp1.employee_dict.update({emp1.name: emp1})
        comp1.employee_dict.update({emp2.name: emp2})

        comp_name = input("Enter company name : ")
        comp_obj = company_dict.get(comp_name)
        print(comp_obj.employee_dict)
        print(" <<<<<<<<<<<<<<----->>>>>>>>>>>>>>>>>>> ")
        employee_name = input("Enter employee name : ")
        emp_obj = comp_obj.employee_dict.get(employee_name)
        print(emp_obj.as_dict())
        print(" <<<<<<<<<<<<<<----->>>>>>>>>>>>>>>>>>> ")
    except Exception as e:
        print(e)
        logging.warning("Warning !!")
    else:
        print("      Employee Wage Calculation ! ")
    finally:
        print(" <<<<<<<<<<<<<<----->>>>>>>>>>>>>>>>>>> ")
