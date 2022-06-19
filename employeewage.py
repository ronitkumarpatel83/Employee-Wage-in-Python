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


class EmployeeWage:
    def employee(self):
        """
        This function is work for employees attendance
        is there take attendance using random
        :return: nothing
        """
        logging.debug("Employee wage program is running perfectly.....")
        try:
            wage_per_hour = 20
            daily_work_hour = 8
            rand = random.randint(0, 1)
            if rand == 0:
                daily_wage = daily_work_hour * wage_per_hour
                print(f"Employee is present daily wage is : {daily_wage}")

            else:
                print("Employee is absent ")

        except Exception as e:
            print(e)
            logging.exception("There is something occurs please re-check the code")


if __name__ == "__main__":
    try:
        obj = EmployeeWage()
        obj.employee()
    except Exception as e:
        print(e)
        logging.warning("Warning !!")
    else:
        print("Employee attendance ! ")
    finally:
        print("Thanks for checking your attendance ")
