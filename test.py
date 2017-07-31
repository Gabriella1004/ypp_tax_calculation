#!/usr/bin/env python
# @Time    : 7/28/2017 10:06 AM
# @Author  : Wu Guo


# from Tkinter import *
# import tkMessageBox as message_box
from tkinter import *
import tkinter.messagebox as message_box
from lib.lib import *
from lib.base_class import *


def submit_button():
    insurance_base_str = bonus_entry.get('0.0', END)
    if len(insurance_base_str) == 1:
        message_box.showinfo("Error", "Please input Monthly Bonus")
        return
    month_bonus = float(insurance_base_str.replace(',', '').replace(' ', ''))
    bonus_ob = Bonus(tax_standard)
    bonus_tax = bonus_ob.get_tax(month_bonus)

    replace_text(bonus_tax_entry, bonus_tax)


if __name__ == "__main__":
    endowment_name = 'Endowment Insurance'
    medical_name = 'Medical Insurance'
    unemployment_name = 'Unemployment Insurance'
    injure_name = 'Work-related Injury Insurance'
    childbirth_name = 'Childbirth Insurance'
    house_name = 'Housing Funds'

    root = Tk()
    root.wm_title('Salary Calculator on Net Salary')

    bonus_entry = create_item(root, 'Monthly Bonus')
    bonus_tax_entry = create_item(root, 'Monthly Bonus Tax')


    # for text
    replace_text(bonus_entry, '1000')

    root.mainloop()
