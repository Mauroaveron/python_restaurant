from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operator = ''
meal_prices = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drink_prices = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dessert_prices = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_button(number):
    global operator
    operator = operator + number
    calculator_visor.delete(0, END)
    calculator_visor.insert(END, operator)


def delete():
    global operator
    operator = ''
    calculator_visor.delete(0, END)


def get_result():
    global operator
    result = str(eval(operator))
    calculator_visor.delete(0, END)
    calculator_visor.insert(0, result)
    operator = ''


def check_checkbutton():
    x = 0
    for c in meal_boxes:
        if meal_variables[x].get() == 1:
            meal_boxes[x].config(state=NORMAL)
            if meal_boxes[x].get() == '0':
                meal_boxes[x].delete(0, END)
            meal_boxes[x].focus()
        else:
            meal_boxes[x].config(state=DISABLED)
            meal_text[x].set('0')
        x += 1

    x = 0
    for c in drink_boxes:
        if drink_variables[x].get() == 1:
            drink_boxes[x].config(state=NORMAL)
            if drink_boxes[x].get() == '0':
                drink_boxes[x].delete(0, END)
            drink_boxes[x].focus()
        else:
            drink_boxes[x].config(state=DISABLED)
            drink_text[x].set('0')
        x += 1

    x = 0
    for c in dessert_boxes:
        if dessert_variables[x].get() == 1:
            dessert_boxes[x].config(state=NORMAL)
            if dessert_boxes[x].get() == '0':
                dessert_boxes[x].delete(0, END)
            dessert_boxes[x].focus()
        else:
            dessert_boxes[x].config(state=DISABLED)
            dessert_text[x].set('0')
        x += 1


def total():
    meal_subtotal = 0
    p = 0
    for quantity in meal_text:
        meal_subtotal = meal_subtotal + (float(quantity.get()) * meal_prices[p])
        p += 1

    drink_subtotal = 0
    p = 0
    for quantity in drink_text:
        drink_subtotal = drink_subtotal + (float(quantity.get()) * drink_prices[p])
        p += 1

    dessert_subtotal = 0
    p = 0
    for quantity in dessert_text:
        dessert_subtotal = dessert_subtotal + (float(quantity.get()) * dessert_prices[p])
        p += 1

    subtotal = meal_subtotal + drink_subtotal + dessert_subtotal
    taxes = subtotal * 0.07
    total = subtotal + taxes

    meal_cost_var.set(f'${round(meal_subtotal, 2)}')
    drink_cost_var.set(f'${round(drink_subtotal, 2)}')
    dessert_cost_var.set(f'${round(dessert_subtotal, 2)}')
    subtotal_var.set(f'${round(subtotal, 2)}')
    taxes_var.set(f'${round(taxes, 2)}')
    total_var.set(f'${round(total, 2)}')


def receipt():
    receipt_text.delete(1.0, END)
    receipt_num = f'N# - {random.randint(1000, 9999)}'
    date = datetime.datetime.now()
    receipt_date = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}'
    receipt_text.insert(END, f'Info:\t{receipt_num}\t\t{receipt_date}\n')
    receipt_text.insert(END, f'*' * 61 + '\n')
    receipt_text.insert(END, 'Items\t\tQuantity\tItem Cost\n')
    receipt_text.insert(END, f'-' * 73 + '\n')

    x = 0
    for meal in meal_text:
        if meal.get() != '0':
            receipt_text.insert(END, f'{(meal_list[x]).capitalize()}\t\t{meal.get()}\t' 
                                     f'${int(meal.get()) * meal_prices[x]}\n')
        x += 1

    x = 0
    for drink in drink_text:
        if drink.get() != '0':
            receipt_text.insert(END, f'{(drink_list[x]).capitalize()}\t\t{drink.get()}\t' 
                                     f'${int(drink.get()) * drink_prices[x]}\n')
        x += 1

    x = 0
    for dessert in dessert_text:
        if dessert.get() != '0':
            receipt_text.insert(END, f'{(dessert_list[x]).capitalize()}\t\t{dessert.get()}\t' 
                                     f'${int(dessert.get()) * dessert_prices[x]}\n')
        x += 1

    receipt_text.insert(END, f'-' * 73 + '\n')
    receipt_text.insert(END, f'Cost of meals: \t\t\t{meal_cost_var.get()}\n')
    receipt_text.insert(END, f'Cost of drinks: \t\t\t{drink_cost_var.get()}\n')
    receipt_text.insert(END, f'Cost of desserts: \t\t\t{dessert_cost_var.get()}\n')
    receipt_text.insert(END, f'Subtotal: \t\t\t{subtotal_var.get()}\n')
    receipt_text.insert(END, f'Taxes: \t\t\t{taxes_var.get()}\n')
    receipt_text.insert(END, f'Total: \t\t\t{total_var.get()}\n')
    receipt_text.insert(END, f'*' * 61 + '\n')
    receipt_text.insert(END, 'Thanks, come back soon!')


def save():
    receipt_info = receipt_text.get(1.0, END)
    file = filedialog.asksaveasfile(mode='w',
                                    defaultextension='.txt')
    file.write(receipt_info)
    file.close()
    messagebox.showinfo('Information', 'Your receipt has been saved')


def reset():
    receipt_text.delete(0.1, END)

    for text in meal_text:
        text.set('0')
    for text in drink_text:
        text.set('0')
    for text in dessert_text:
        text.set('0')

    for box in meal_boxes:
        box.config(state=DISABLED)
    for box in drink_boxes:
        box.config(state=DISABLED)
    for box in dessert_boxes:
        box.config(state=DISABLED)

    for v in meal_variables:
        v.set(0)
    for v in drink_variables:
        v.set(0)
    for v in dessert_variables:
        v.set(0)

    meal_cost_var.set('')
    drink_cost_var.set('')
    dessert_cost_var.set('')
    subtotal_var.set('')
    taxes_var.set('')
    total_var.set('')


# Start TKinter
app = Tk()

# Window size
app.geometry('1020x630+0+0')

# Avoid maximizing window
app.resizable(0, 0)

# Window background colour
app.config(bg='burlywood')

# Window title
app.title('My restaurant - Facturation System')

# Top panel
top_panel = Frame(app, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

# Title label
title_label = Label(top_panel, text='Facturation System', fg='azure4', font=('Dosis', 48), bg='burlywood', width=27)
title_label.grid(row=0, column=0)

# Left panel
left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# Cost panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg='azure4', padx=50)
cost_panel.pack(side=BOTTOM)

# Meal panel
meal_panel = LabelFrame(left_panel, text='Meal', font=('Dosis', 15, 'bold'), bd=1, relief=FLAT, fg='azure4')
meal_panel.pack(side=LEFT)

# Drink panel
drink_panel = LabelFrame(left_panel, text='Drink', font=('Dosis', 15, 'bold'), bd=1, relief=FLAT, fg='azure4')
drink_panel.pack(side=LEFT)

# Dessert panel
dessert_panel = LabelFrame(left_panel, text='Dessert', font=('Dosis', 15, 'bold'), bd=1, relief=FLAT, fg='azure4')
dessert_panel.pack(side=LEFT)

# Right panel
right_panel = Frame(app, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# Calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
calculator_panel.pack()

# Receipt panel
receipt_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
receipt_panel.pack()

# Button panel
button_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
button_panel.pack()

# Product list
meal_list = ['chicken', 'lamb', 'salmon', 'hake', 'kebab', 'pizza 1', 'pizza 2', 'pizza 3']
drink_list = ['water', 'soda', 'juice', 'cola', 'wine 1', 'wine 2', 'beer 1', 'beer 2']
dessert_list = ['ice cream', 'fruit', 'brownies', 'custard', 'mousse', 'cake 1', 'cake 2', 'cake 3']

# Generate meal items
meal_variables = []
meal_boxes = []
meal_text = []
counter = 0
for meal in meal_list:

    # Create checkbutton
    meal_variables.append('')
    meal_variables[counter] = IntVar()
    meal = Checkbutton(meal_panel,
                       text=meal.title(),
                       font=('Dosis', 15, 'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable=meal_variables[counter],
                       command=check_checkbutton)
    meal.grid(row=counter,
              column=0,
              sticky=W)

    # Create entry boxes
    meal_boxes.append('')
    meal_text.append('')
    meal_text[counter] = StringVar()
    meal_text[counter].set('0')
    meal_boxes[counter] = Entry(meal_panel,
                                font=('Dosis', 15, 'bold'),
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=meal_text[counter])
    meal_boxes[counter].grid(row=counter,
                             column=1)

    counter += 1

# Generate drink items
drink_variables = []
drink_boxes = []
drink_text = []
counter = 0
for drink in drink_list:

    # Create checkbutton
    drink_variables.append('')
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drink_panel,
                        text=drink.title(),
                        font=('Dosis', 15, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=drink_variables[counter],
                        command=check_checkbutton)
    drink.grid(row=counter,
               column=0,
               sticky=W)

    # Create entry boxes
    drink_boxes.append('')
    drink_text.append('')
    drink_text[counter] = StringVar()
    drink_text[counter].set('0')
    drink_boxes[counter] = Entry(drink_panel,
                                 font=('Dosis', 15, 'bold'),
                                 bd=1,
                                 width=6,
                                 state=DISABLED,
                                 textvariable=drink_text[counter])
    drink_boxes[counter].grid(row=counter,
                              column=1)

    counter += 1

# Generate dessert items
dessert_variables = []
dessert_boxes = []
dessert_text = []
counter = 0
for dessert in dessert_list:

    # Create checkbutton
    dessert_variables.append('')
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_panel,
                          text=dessert.title(),
                          font=('Dosis', 15, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=dessert_variables[counter],
                          command=check_checkbutton)
    dessert.grid(row=counter,
                 column=0,
                 sticky=W)

    # Create entry boxes
    dessert_boxes.append('')
    dessert_text.append('')
    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')
    dessert_boxes[counter] = Entry(dessert_panel,
                                   font=('Dosis', 15, 'bold'),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable=dessert_text[counter])
    dessert_boxes[counter].grid(row=counter,
                                column=1)

    counter += 1

# Variables
meal_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_var = StringVar()
taxes_var = StringVar()
total_var = StringVar()

# Cost labels and entry boxes
meal_cost_label = Label(cost_panel,
                        text='Meal Cost',
                        font=('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white')
meal_cost_label.grid(row=0, column=0)

meal_cost_text = Entry(cost_panel,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=meal_cost_var)
meal_cost_text.grid(row=0, column=1, padx=41)

drink_cost_label = Label(cost_panel,
                         text='Drink Cost',
                         font=('Dosis', 12, 'bold'),
                         bg='azure4',
                         fg='white')
drink_cost_label.grid(row=1, column=0)

drink_cost_text = Entry(cost_panel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=drink_cost_var)
drink_cost_text.grid(row=1, column=1, padx=41)

dessert_cost_label = Label(cost_panel,
                           text='Dessert Cost',
                           font=('Dosis', 12, 'bold'),
                           bg='azure4',
                           fg='white')
dessert_cost_label.grid(row=2, column=0)

dessert_cost_text = Entry(cost_panel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=dessert_cost_var)
dessert_cost_text.grid(row=2, column=1, padx=41)

subtotal_label = Label(cost_panel,
                       text='Subtotal',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')
subtotal_label.grid(row=0, column=3)

subtotal_text = Entry(cost_panel,
                      font=('Dosis', 12, 'bold'),
                      bd=1,
                      width=10,
                      state='readonly',
                      textvariable=subtotal_var)
subtotal_text.grid(row=0, column=4, padx=41)

taxes_label = Label(cost_panel,
                    text='Impuestos',
                    font=('Dosis', 12, 'bold'),
                    bg='azure4',
                    fg='white')
taxes_label.grid(row=1, column=3)

taxes_text = Entry(cost_panel,
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=taxes_var)
taxes_text.grid(row=1, column=4, padx=41)

total_label = Label(cost_panel,
                    text='Total',
                    font=('Dosis', 12, 'bold'),
                    bg='azure4',
                    fg='white')
total_label.grid(row=2, column=3)

total_text = Entry(cost_panel,
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=total_var)
total_text.grid(row=2, column=4, padx=41)

# Buttons
buttons = ['total', 'receipt', 'save', 'reset']
created_buttons = []
columns = 0
for button in buttons:
    button = Button(button_panel,
                    text=button.title(),
                    font=('Dosis', 13, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=3,
                    width=8)

    created_buttons.append(button)

    button.grid(row=0,
                column=columns)
    columns += 1

created_buttons[0].config(command=total)
created_buttons[1].config(command=receipt)
created_buttons[2].config(command=save)
created_buttons[3].config(command=reset)

# Receipt area
receipt_text = Text(receipt_panel,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=41,
                    height=10)
receipt_text.grid(row=0,
                  column=0,
                  columnspan=4)

# Calculator
calculator_visor = Entry(calculator_panel,
                         font=('Dosis', 16, 'bold'),
                         width=33,
                         bd=1)
calculator_visor.grid(row=0,
                      column=0,
                      columnspan=4)

calculator_buttons = ['7', '8', '9', '+', '4', '5', '6', '-',
                      '1', '2', '3', 'x', '=', 'Del', '0', '/']
saved_buttons = []

row = 1
column = 0
for button in calculator_buttons:
    button = Button(calculator_panel,
                    text=button.title(),
                    font=('Dosis', 12, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=2,
                    width=9)

    saved_buttons.append(button)

    button.grid(row=row,
                column=column)

    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0

saved_buttons[0].config(command=lambda: click_button('7'))
saved_buttons[1].config(command=lambda: click_button('8'))
saved_buttons[2].config(command=lambda: click_button('9'))
saved_buttons[3].config(command=lambda: click_button('+'))
saved_buttons[4].config(command=lambda: click_button('4'))
saved_buttons[5].config(command=lambda: click_button('5'))
saved_buttons[6].config(command=lambda: click_button('6'))
saved_buttons[7].config(command=lambda: click_button('-'))
saved_buttons[8].config(command=lambda: click_button('1'))
saved_buttons[9].config(command=lambda: click_button('2'))
saved_buttons[10].config(command=lambda: click_button('3'))
saved_buttons[11].config(command=lambda: click_button('*'))
saved_buttons[12].config(command=get_result)
saved_buttons[13].config(command=delete)
saved_buttons[14].config(command=lambda: click_button('0'))
saved_buttons[15].config(command=lambda: click_button('/'))

# Prevent screen from closing
app.mainloop()
