#!/usr/bin/env python
# @Time    : 7/28/2017 10:06 AM
# @Author  : Wu Guo


# from Tkinter import *
from tkinter import *

social_average_salary = 7706
tax_free = 3500
proxy_fee = 328.38

house_fund_base_max = social_average_salary * 3
endowment_insurance_base_max = social_average_salary * 3
medical_insurance_base_max = social_average_salary * 3
unemployment_insurance_base_max = social_average_salary * 3
injure_insurance_base_max = social_average_salary * 3
childbirth_insurance_base_max = social_average_salary * 3

house_fund_base_min = 2148
endowment_insurance_base_min = int(social_average_salary * 0.4 + 0.5)
medical_insurance_base_min = int(social_average_salary * 0.6 + 0.5)
unemployment_insurance_base_min = int(social_average_salary * 0.4 + 0.5)
injure_insurance_base_min = int(social_average_salary * 0.4 + 0.5)
childbirth_insurance_base_min = int(social_average_salary * 0.6 + 0.5)

house_fund_employ_ratio = 0.12
endowment_insurance_employ_ratio = 0.08
medical_insurance_employ_ratio = 0.02
unemployment_insurance_employ_ratio = 0.002
injure_insurance_employ_ratio = 0
childbirth_insurance_employ_ratio = 0
medical_insurance_employ_addition = 3

stock_tax_employ_ratio = 0.2

house_fund_company_ratio = 0.12
endowment_insurance_company_ratio = 0.19
medical_insurance_company_ratio = 0.1
unemployment_insurance_company_ratio = 0.008
injure_insurance_company_ratio = 0.005
childbirth_insurance_company_ratio = 0.008

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


def replace_text(entry, value):
    entry.delete('0.0', END)
    entry.insert(INSERT, value)


def create_item(root, label_name):
    var = StringVar()
    label = Label(root, textvariable=var, relief=RAISED)
    var.set(label_name)
    label.pack()
    entry = Text(root, height=1, bg='green')
    entry.pack()
    return entry

