from employeewage import Employee, Company
import pytest


@pytest.fixture
def emp():
    return Employee("Ronit", 50, 20, 100)


@pytest.fixture
def comp():
    return Company("TCS")


class TestEmployeeWage:
    def test_check_attendance(self, emp):
        exp = emp.check_attendance(0)
        assert exp == 8
        exp = emp.check_attendance(1)
        assert exp == 4
        exp = emp.check_attendance(2)
        assert exp == 0

    def test_calculating_wage(self, emp):
        total = emp.calculating_wage()
        assert isinstance(total, int)

    def test_as_dict(self, emp):
        actual = emp.as_dict()
        assert actual.get("Name") == "Ronit"

    def test_add_employee(self, emp, comp):
        assert len(comp.employee_dict) == 0
        comp.add_employee(emp)
        assert len(comp.employee_dict) == 1
        emp2 = Employee("KD", 20, 18, 100)
        comp.add_employee(emp2)
        assert len(comp.employee_dict) == 2

    def test_get_employee(self, emp, comp):
        comp.add_employee(emp)
        actual = comp.get_employee("Ronit")
        assert isinstance(actual, Employee)
        assert actual.name == "Ronit"

    def test_delete_employee(self, emp, comp):
        comp.add_employee(emp)
        assert len(comp.employee_dict) == 1
        comp.delete_employee("Ronit")
        assert len(comp.employee_dict) == 0

    def test_employee_details_view(self, comp):
        exp = 0
        actual = comp.employee_details_view()
        assert exp == len(actual)
