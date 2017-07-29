#!/usr/bin/env python
# @Time    : 7/28/2017 10:06 AM
# @Author  : Wu Guo


# from Tkinter import *
# import tkMessageBox as message_box
from tkinter import *
import tkinter.messagebox as message_box

social_average_salary = 7706
tax_free = 3500
proxy_fee = 328.38

house_fund_base_max = social_average_salary * 3
retirement_insurance_base_max = social_average_salary * 3
medicine_insurance_base_max = social_average_salary * 3
unemployed_insurance_base_max = social_average_salary * 3
injure_insurance_base_max = social_average_salary * 3
born_insurance_base_max = social_average_salary * 3

house_fund_base_min = 2148
retirement_insurance_base_min = int(social_average_salary * 0.4 + 0.5)
medicine_insurance_base_min = int(social_average_salary * 0.6 + 0.5)
unemployed_insurance_base_min = int(social_average_salary * 0.4 + 0.5)
injure_insurance_base_min = int(social_average_salary * 0.4 + 0.5)
born_insurance_base_min = int(social_average_salary * 0.6 + 0.5)

house_fund_employ_ratio = 0.12
retirement_insurance_employ_ratio = 0.08
medicine_insurance_employ_ratio = 0.02
unemployed_insurance_employ_ratio = 0.002
injure_insurance_employ_ratio = 0
born_insurance_employ_ratio = 0
medicine_insurance_employ_addition = 3

stock_tax_employ_ratio = 0.2

house_fund_company_ratio = 0.12
retirement_insurance_company_ratio = 0.19
medicine_insurance_company_ratio = 0.1
unemployed_insurance_company_ratio = 0.008
injure_insurance_company_ratio = 0.005
born_insurance_company_ratio = 0.008

house_fund_employ = 0
house_fund_company = 0
retirement_insurance_employ = 0
retirement_insurance_company = 0
medicine_insurance_employ = 0
medicine_insurance_company = 0
unemployed_insurance_employ = 0
unemployed_insurance_company = 0
injure_insurance_employ = 0
injure_insurance_company = 0
born_insurance_employ = 0
born_insurance_company = 0
salary_tax_employ = 0
stock_tax_employ = 0

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


def calc_tax(salary):
    tax_salary = salary - tax_free
    grade = [0, 0, 0]
    for i in tax_standard:
        if tax_salary < i[0]:
            break
        grade = i
    return tax_salary * grade[1] - grade[2]


def reverse_bonus_tax(raw_salary):
    """
    Get bonus with tax from bonus without tax
    :param raw_salary:
    :return:
    """
    pre_tax_salary = 0
    for tax_salary in range(1, raw_salary * 100):
        tax_salary_per_month = tax_salary/12
        grade = [0, 0, 0]
        for i in tax_standard:
            if tax_salary_per_month < i[0]:
                break
            grade = i
        tax = tax_salary_per_month * grade[1] - grade[2]/12
        if tax_salary_per_month - tax > raw_salary/12:
            break
        pre_tax_salary = tax_salary
    return pre_tax_salary


def calc_insurance(salary, base_max, base_min, employ_ratio, company_ratio):
    # salary = float(salary_str.replace(',', ''))
    if salary > base_max:
        value = base_max
    elif salary < base_min:
        value = base_min
    else:
        value = salary
    return round(value * employ_ratio, 2), round(value * company_ratio, 2)


def calc_house_fund(salary, base_max, base_min, employ_ratio, company_ratio):
    # salary = float(salary_str.replace(',', ''))
    if salary > base_max:
        value = base_max
    elif salary < base_min:
        value = base_min
    else:
        value = salary
    return int(value * employ_ratio + 0.5), int(value * company_ratio + 0.5)


def replace_text(entry, value):
    entry.delete('0.0', END)
    entry.insert(INSERT, value)


def flush_insurance(insurance_base, house_fund_base):
    global house_fund_employ, house_fund_company, retirement_insurance_employ, retirement_insurance_company, \
        medicine_insurance_employ, medicine_insurance_company, unemployed_insurance_employ, \
        unemployed_insurance_company, salary_tax_employ, \
        injure_insurance_employ, injure_insurance_company, born_insurance_employ, born_insurance_company

    house_fund_employ, house_fund_company = calc_house_fund(house_fund_base, house_fund_base_max, house_fund_base_min,
                                                           house_fund_employ_ratio, house_fund_company_ratio)

    retirement_insurance_employ, retirement_insurance_company = calc_insurance(insurance_base, retirement_insurance_base_max,
                                                                               retirement_insurance_base_min,
                                                                               retirement_insurance_employ_ratio,
                                                                               retirement_insurance_company_ratio)

    medicine_insurance_employ, medicine_insurance_company = calc_insurance(insurance_base, medicine_insurance_base_max,
                                                                           medicine_insurance_base_min,
                                                                           medicine_insurance_employ_ratio,
                                                                           medicine_insurance_company_ratio)
    medicine_insurance_employ += medicine_insurance_employ_addition

    unemployed_insurance_employ, unemployed_insurance_company = calc_insurance(insurance_base, unemployed_insurance_base_max,
                                                                               unemployed_insurance_base_min,
                                                                               unemployed_insurance_employ_ratio,
                                                                               unemployed_insurance_company_ratio)

    injure_insurance_employ, injure_insurance_company = calc_insurance(insurance_base, injure_insurance_base_max,
                                                                       injure_insurance_base_min,
                                                                       injure_insurance_employ_ratio,
                                                                       injure_insurance_company_ratio)

    born_insurance_employ, born_insurance_company = calc_insurance(insurance_base, born_insurance_base_max,
                                                                   born_insurance_base_min,
                                                                   born_insurance_employ_ratio,
                                                                   born_insurance_company_ratio)


def get_employ_insurances():
    insurances = retirement_insurance_employ + medicine_insurance_employ + unemployed_insurance_employ \
                 + injure_insurance_employ + born_insurance_employ + house_fund_employ
    return insurances


def get_company_insurances():
    insurances = retirement_insurance_company + medicine_insurance_company + unemployed_insurance_company \
                 + injure_insurance_company + born_insurance_company + house_fund_company
    return insurances


def flush_tax(salary_with_tax, stock):
    global salary_tax_employ, stock_tax_employ
    stock_tax_employ = round(stock * stock_tax_employ_ratio, 2)
    salary_tax_employ = round(calc_tax(salary_with_tax - get_employ_insurances()), 2)


def get_net_salary_bonus(salary_with_tax, stock):
    return get_net_salary(salary_with_tax) + get_net_stock(stock)


def get_net_salary(salary_with_tax):
    net_salary = salary_with_tax - get_employ_insurances() - salary_tax_employ
    return net_salary


def get_net_stock(stock):
    net_stock = stock - stock_tax_employ
    return net_stock


def fill_insurance():
    replace_text(house_fund_employ_entry, house_fund_employ)
    replace_text(house_fund_company_entry, house_fund_company)

    replace_text(retirement_insurance_employ_entry, str(retirement_insurance_employ))
    replace_text(retirement_insurance_company_entry, str(retirement_insurance_company))

    replace_text(medicine_insurance_employ_entry, str(medicine_insurance_employ))
    replace_text(medicine_insurance_company_entry, str(medicine_insurance_company))

    replace_text(unemployed_insurance_employ_entry, str(unemployed_insurance_employ))
    replace_text(unemployed_insurance_company_entry, str(unemployed_insurance_company))

    # replace_text(injure_insurance_employ_entry, str(injure_insurance_employ))
    replace_text(injure_insurance_company_entry, str(injure_insurance_company))

    # replace_text(born_insurance_employ_entry, str(born_insurance_employ))
    replace_text(born_insurance_company_entry, str(born_insurance_company))


def fill_tax():
    replace_text(tax_employ_entry, str(round(salary_tax_employ + stock_tax_employ, 2)))


def fill_net_salary(net_salary):
    replace_text(pay_after_tax_entry, str(round(net_salary, 2)))


def create_item(root, label_name):
    var = StringVar()
    label = Label(root, textvariable=var, relief=RAISED)
    var.set(label_name)
    label.pack()
    entry = Text(root, height=1, bg='green')
    entry.pack()
    return label, entry


def submit_button():
    pay_before_tax_str = pay_before_tax_entry.get('0.0', END)
    if len(pay_before_tax_str) == 1:
        message_box.showinfo("Error", "Please input Salary")
        return
    month_salary = float(pay_before_tax_str.replace(',', '').replace(' ', ''))

    insurance_base_str = insurance_base_entry.get('0.0', END)
    if len(insurance_base_str) == 1:
        message_box.showinfo("Error", "Please input Insurance Base")
        return
    insurance_base = float(insurance_base_str.replace(',', '').replace(' ', ''))

    house_fund_base_str = house_fund_base_entry.get('0.0', END)
    if len(house_fund_base_str) == 1:
        message_box.showinfo("Error", "Please input House Fund Base")
        return
    house_fund_base = float(house_fund_base_str.replace(',', '').replace(' ', ''))

    stock_str = stock_entry.get('0.0', END)
    if len(stock_str) == 1:
        message_box.showinfo("Error", "Please input House Fund Base")
        return
    stock = float(stock_str.replace(',', '').replace(' ', ''))

    flush_insurance(insurance_base, house_fund_base)
    flush_tax(month_salary, stock)

    net_income = get_net_salary_bonus(month_salary, stock)
    fill_insurance()
    fill_tax()
    fill_net_salary(net_income)


if __name__ == "__main__":
    tk = Tk()

    pay_before_tax_label, pay_before_tax_entry = create_item(tk, 'Salary')
    insurance_base_label, insurance_base_entry = create_item(tk, 'Insurance Base')
    house_fund_base_label, house_fund_base_entry = create_item(tk, 'House Fund Base')
    # bonus_label, bonus_entry = create_item(tk, 'Bonus')
    stock_label, stock_entry = create_item(tk, 'Stock')
    pay_after_tax_label, pay_after_tax_entry = create_item(tk, "Net Salary")

    # Employ
    tax_employ_label, tax_employ_entry = create_item(tk, 'Tax of Employ')
    house_fund_employ_label, house_fund_employ_entry = create_item(tk, 'House Fund of Employ')
    retirement_insurance_employ_label, retirement_insurance_employ_entry = create_item(tk, 'Retirement Insurance of '
                                                                                           'Employ')
    medicine_insurance_employ_label, medicine_insurance_employ_entry = create_item(tk, 'Medicine Insurance of Employ')
    unemployed_insurance_employ_label, unemployed_insurance_employ_entry = create_item(tk, 'Unemployed Insurance of '
                                                                                           'Employ')
    # injure_insurance_employ_label, injure_insurance_employ_entry = create_item(tk, 'Injure Insurance of Employ')
    # born_insurance_employ_label, born_insurance_employ_entry = create_item(tk, 'Born Insurance of Employ')

    # Company
    house_fund_company_label, house_fund_company_entry = create_item(tk, 'Housing Funds of Company')
    retirement_insurance_company_label, retirement_insurance_company_entry = create_item(tk, 'Endowment Insurance of '
                                                                                             'Company')
    medicine_insurance_company_label, medicine_insurance_company_entry = create_item(tk, 'Medical Insurance of '
                                                                                         'Company')
    unemployed_insurance_company_label, unemployed_insurance_company_entry = create_item(tk,
                                                                                         'Unemployment Insurance of '
                                                                                         'Company')
    injure_insurance_company_label, injure_insurance_company_entry = create_item(tk, 'Work-related Injury '
                                                                                     'Insurance of Company')
    born_insurance_company_label, born_insurance_company_entry = create_item(tk, 'Childbirth Insurance of Company')

    submit = Button(tk, text='Submit', command=submit_button)
    submit.pack()

    # for text
    replace_text(pay_before_tax_entry, '29,858.00')
    replace_text(stock_entry, '0')
    replace_text(insurance_base_entry, '7706')
    replace_text(house_fund_base_entry, '4000')
    tk.mainloop()
