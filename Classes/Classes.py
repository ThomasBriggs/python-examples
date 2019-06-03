class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@comapny.com"

        self.raise_ammount = 4

    def __add__(self, other):
        return self.pay + other.pay

    def __contains__(self, item):
        return self.first.contains(item) or self.last.contains(item)

    def apply_raise(self, different_amount=int(0)):
        if different_amount == 0:
            self.pay *= self.raise_ammount
        else:
            self.pay *= different_amount

    def print_details(self):
        print("Fullname: %s %s"
              "\nPay: %s"
              "\nEmail: %s"
              % (self.first, self.last, self.pay, self.email))

    @staticmethod
    def print_employee(instance):
        print("Fullname: %s %s"
              "\nPay: %s"
              "\nEmail: %s"
              % (instance.first, instance.last, instance.pay, instance.email))


class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

    def print_details(self):
        Employee.print_details(self)
        print("Programming Language: %s" % (self.prog_lang))


def search_array(input_array, search_item):
    return search_item in input_array

dev_1 = Developer("Thomas", "Briggs", 500000, "Python")
dev_1.print_details()

# emp_1 = Employee("Thomas", "Briggs", 111)
# emp_1.print_details()
# Employee.print_details(emp_1)

array = [1, 6, 8, 3, 7, 5, 2, 6]
print(search_array(array, 99))