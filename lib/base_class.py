#!/usr/bin/env python
# @Time    : 7/28/2017 10:06 AM
# @Author  : Wu Guo

from .lib import replace_text, create_item


class BaseClass(object):
    def __init__(self, name, employ_ratio, company_ratio, base_max, base_min, root, addition=0, hide=False):
        self.name = name
        self.employ_ratio = employ_ratio
        self.company_ratio = company_ratio
        self.base_max = base_max
        self.base_min = base_min
        self.addition = addition
        self.hide = hide
        if not hide:
            self.employ_entry = create_item(root, name + ' From Employ')
        self.company_entry = create_item(root, name + ' From Company')

    def calc(self, salary, ratio):
        return 0

    def get_employ(self, salary):
        return round(self.calc(salary, self.employ_ratio) + self.addition, 2)

    def get_company(self, salary):
        return round(self.calc(salary, self.company_ratio), 2)

    def fill_entry(self, base):
        if not self.hide:
            employ = self.get_employ(base)
            replace_text(self.employ_entry, employ)
        company = self.get_company(base)
        replace_text(self.company_entry, company)


class Insurance(BaseClass):
    def __init__(self, employ_ratio, company_ratio, base_max, base_min, root, name='', addition=0, hide=False):
        BaseClass.__init__(self, name, employ_ratio, company_ratio, base_max, base_min, root, addition, hide)

    def calc(self, salary, ratio):
        # salary = float(salary_str.replace(',', ''))
        if salary > self.base_max:
            value = self.base_max
        elif salary < self.base_min:
            value = self.base_min
        else:
            value = salary
        return round(value * ratio, 2)

    def get_min_employ(self):
        return round(self.base_min * self.employ_ratio, 2)

    def get_min_company(self):
        return round(self.base_min * self.company_ratio, 2)


class HouseFund(BaseClass):
    def __init__(self, employ_ratio, company_ratio, base_max, base_min, root, name=''):
        BaseClass.__init__(self, name, employ_ratio, company_ratio, base_max, base_min, root)

    def calc(self, salary, ratio):
        # salary = float(salary_str.replace(',', ''))
        if salary > self.base_max:
            value = self.base_max
        elif salary < self.base_min:
            value = self.base_min
        else:
            value = salary
        return int(value * ratio + 0.5)


class SalaryTax(object):
    def __init__(self, standard, tax_free):
        self.standard = standard
        self.tax_free = tax_free

    def get_tax(self, salary):
        tax_salary = salary - self.tax_free
        grade = [0, 0, 0]
        for i in self.standard:
            if tax_salary < i[0]:
                break
            grade = i
        if tax_salary < 0:
            tax_salary = 0
        return round(tax_salary * grade[1] - grade[2], 2)

    def get_net_salary(self, salary):
        return round(salary - self.get_tax(salary), 2)

    def beyond(self, salary, ratio):
        tax_salary = salary - self.tax_free
        grade = [0, 0, 0]
        for i in self.standard:
            if tax_salary < i[0]:
                break
            grade = i
        if grade[1] >= ratio:
            return True
        else:
            return False


class StockTax(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def get_tax(self, stock):
        return round(stock * self.ratio, 2)

    def get_net_stock(self, stock):
        return round(stock - self.get_tax(stock), 2)

    def get_stock(self, net_stock):
        return round(net_stock / (1 - self.ratio), 2)


class Bonus(object):
    def __init__(self, standard):
        self.standard = standard

    def get_tax(self, month_bonus):
        grade = [0, 0, 0]
        for i in self.standard:
            if month_bonus < i[0]:
                break
            grade = i
        annual_tax = month_bonus * 12 * grade[1] - grade[2]
        print(annual_tax)
        return round(annual_tax / 12, 2)


if __name__ == "__main__":
    from tkinter import Tk

    tk = Tk()

    house_fund = HouseFund(0.12, 0.12, 7706 * 3, 2148, tk, 'House')
    print(house_fund.get_company(29858.00))
    print(house_fund.get_employ(29858.00))

    retirement = Insurance(0.08, 0.19, 7706 * 3, int(77-6 * 0.4 + 0.5), tk, 'retirement')
    print(retirement.get_company(29858.00))
    print(retirement.get_employ(29858.00))

    tax_standard = \
        [
            [-80000, 0, 0],
            [0, 0.03, 0],
            [1500, 0.1, 105],
            [4500, 0.2, 555],
            [9000, 0.25, 1005],
            [35000, 0.3, 2755],
            [55000, 0.35, 5505],
            [80000, 0.45, 13505]
        ]

    tax = SalaryTax(tax_standard, 3500)
    print(tax.get_tax(21222.96 + 3500))
