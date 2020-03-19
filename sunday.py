from tkinter import *
from tkinter import messagebox
from random import *
from math import *
import time


def dc():
    def exit_calc1():
        root2.destroy()

    root2 = Toplevel()

    root2.geometry("350x350+1000+80")
    root2.title("THEORY")
    mycolor2 = "#EDA895"

    root2.configure(bg=mycolor2)
    label3 = Label(root2, text='A little bit about DC theory...', bg=mycolor2, fg='white', font=('Fixedsys', 15)).place(
        x=25, y=10)
    button_exit_calc1 = Button(root2, text='exit', bg=mycolor2, fg='white', font=('Fixedsys', 4),
                               command=exit_calc1).place(x=305, y=320)


def exit():
    root.destroy()


def references():
    root_ref = Toplevel()
    root_ref.title("REFERENCES")

    root_ref.mainloop()


def calc():
    def exit_calc():
        root1.destroy()

    def tick1():
        if var1.get() == 1:
            label_r1.place(x=150, y=80)
            entry_r1.place(x=190, y=80)
            var1.set(1)
        else:
            label_r1.place_forget()
            entry_r1.place_forget()
            var1.set(0)

    def tick2():
        if var2.get() == 1:
            label_r2.place(x=80, y=80)
            label_r2_1.place(x=180, y=80)

            entry_r2.place(x=120, y=80)
            entry_r2_1.place(x=220, y=80)

            var2.set(1)
        else:
            label_r2.place_forget()
            label_r2_1.place_forget()

            entry_r2.place_forget()
            entry_r2_1.place_forget()

            var2.set(0)

    def tick3():
        if var3.get() == 1:
            label_r3.place(x=50, y=80)
            label_r3_1.place(x=140, y=80)
            label_r3_2.place(x=230, y=80)

            entry_r3.place(x=90, y=80)
            entry_r3_1.place(x=180, y=80)
            entry_r3_2.place(x=270, y=80)

            var3.set(1)
        else:
            label_r3.place_forget()
            label_r3_1.place_forget()
            label_r3_2.place_forget()

            entry_r3.place_forget()
            entry_r3_1.place_forget()
            entry_r3_2.place_forget()

            var3.set(0)

    def tick4():
        if var4.get() == 1:
            label_r4.place(x=15, y=80)
            label_r4_1.place(x=100, y=80)
            label_r4_2.place(x=170, y=80)
            label_r4_3.place(x=250, y=80)

            entry_r4.place(x=65, y=80)
            entry_r4_1.place(x=140, y=80)
            entry_r4_2.place(x=220, y=80)
            entry_r4_3.place(x=300, y=80)

            var4.set(1)
        else:
            label_r4.place_forget()
            label_r4_1.place_forget()
            label_r4_2.place_forget()
            label_r4_3.place_forget()

            entry_r4.place_forget()
            entry_r4_1.place_forget()
            entry_r4_2.place_forget()
            entry_r4_3.place_forget()

            var4.set(0)

    def result():
        if 0.0 < float(entry2.get()) <= 10000.0:
            v1 = float(entry2.get())
            # for series
            if var_s.get() == 1 and var1.get() == 1 and var_p.get() == 0 or var_p.get() == 1 and var1.get() == 1:
                if float(entry2.get()) <= 10000.0:
                    r1 = float(entry_r1.get())
                    i1 = v1 / r1
                    i1 = round(i1, 3)
                    power = (v1 ** 2) / r1
                    power = round(power, 3)
                    messagebox.showinfo('RESULT', 'I(supply) = ' + str(i1) + '\n' + 'Total power = ' + str(power))

            elif var_s.get() == 1 and var2.get() == 1 and var_p.get() == 0:
                if float(entry2.get()) <= 10000.0:
                    r1_2 = float(entry_r2.get())
                    r2_2 = float(entry_r2_1.get())
                    rt = r1_2 + r2_2
                    i2 = v1 / rt
                    i2 = round(i2, 3)
                    vr1_2 = i2 * r1_2
                    vr2_2 = i2 * r2_2
                    power = (v1 ** 2) / rt
                    power = round(power, 3)
                    messagebox.showinfo('RESULT', str(
                        'R(total) = ' + str(rt) + '\n' + 'I(supply) = ' + str(i2) + '\n' + 'V(across R1) = ' + str(
                            vr1_2) + '\n' + 'V(across R2) = ' + str(
                            vr2_2) + '\n' + 'Total power = ' + str(power)))

            elif var_s.get() == 1 and var3.get() == 1 and var_p.get() == 0:
                if float(entry2.get()) <= 10000.0:
                    r1_3 = float(entry_r3.get())
                    r2_3 = float(entry_r3_1.get())
                    r3_3 = float(entry_r3_2.get())
                    rt = r1_3 + r2_3 + r3_3
                    i3 = v1 / rt
                    i3 = round(i3, 3)
                    vr1_3 = i3 * r1_3
                    vr2_3 = i3 * r2_3
                    vr3_3 = i3 * r3_3
                    power = (v1 ** 2) / rt
                    power = round(power, 3)
                    messagebox.showinfo('RESULT', str(
                        'R(total) = ' + str(rt) + '\n' + 'I(supply) = ' + str(i3) + '\n' + 'V(across R1) = ' + str(
                            vr1_3) + '\n' + 'V(across R2) = ' + str(
                            vr2_3) + '\n' + 'V(across R3) = ' + str(vr3_3) + '\n' + 'Total power = ' + str(power)))

            elif var_s.get() == 1 and var4.get() == 1 and var_p.get() == 0:
                if float(entry2.get()) <= 10000.0:
                    r1_4 = float(entry_r4.get())
                    r2_4 = float(entry_r4_1.get())
                    r3_4 = float(entry_r4_2.get())
                    r4_4 = float(entry_r4_3.get())
                    rt = r1_4 + r2_4 + r3_4 + r4_4
                    i4 = v1 / rt
                    i4 = round(i4, 3)
                    vr1_4 = i4 * r1_4
                    vr2_4 = i4 * r2_4
                    vr3_4 = i4 * r3_4
                    vr4_4 = i4 * r4_4
                    power = (v1 ** 2) / rt
                    power = round(power, 3)
                    messagebox.showinfo('RESULT', str(
                        'R(total) = ' + str(rt) + '\n' + 'I(supply) = ' + str(i4) + '\n' + 'V(across R1) = ' + str(
                            vr1_4) + '\n' + 'V(across R2) = ' + str(
                            vr2_4) + '\n' + 'V(across R3) = ' + str(vr3_4) + '\n' + 'V(across R4) = ' + str(
                            vr4_4) + '\n' + 'Total power = ' + str(power)))
            # for parallel
            elif var_p.get() == 1 and var2.get() == 1 and var_s.get() == 0:
                if float(entry2.get()) <= 10000.0:
                    r1 = float(entry_r2.get())
                    r1_1 = float(entry_r2_1.get())
                    rt = ((r1 * r1_1) / (r1 + r1_1))
                    rt = round(rt, 3)
                    ir1 = v1 / r1
                    ir2 = v1 / r1_1
                    power = (v1 ** 2) / rt
                    power = round(power, 3)
                    messagebox.showinfo('RESULT', str(
                        'R(total) = ' + str(rt) + '\n' + 'I(across R1) = ' + str(ir1) + '\n' + 'I(across R2) = ' + str(
                            ir2) + '\n' + 'Total power = ' + str(power)))

            elif var_p.get() == 1 and var3.get() == 1 and var_s.get() == 0:
                if float(entry2.get()) <= 10000.0:
                    r1 = float(entry_r3.get())
                    r1_1 = float(entry_r3_1.get())
                    r1_2 = float(entry_r3_2.get())
                    rt = (1 / r1 + 1 / r1_1 + 1 / r1_2) ** -1
                    rt = round(rt, 3)
                    ir1 = v1 / r1
                    ir2 = v1 / r1_1
                    ir3 = v1 / r1_2
                    power = (v1 ** 2) / rt
                    power = round(power, 3)
                    messagebox.showinfo('RESULT', str(
                        'R(total) = ' + str(rt) + '\n' + 'I(across R1) = ' + str(ir1) + '\n' + 'I(across R2) = ' + str(
                            ir2) + '\n' + 'I(across R3) = ' + str(ir3) + '\n' + 'Total power = ' + str(power)))

            elif var_p.get() == 1 and var4.get() == 1 and var_s.get() == 0:
                if float(entry2.get()) <= 10000.0:
                    r1 = float(entry_r4.get())
                    r1_1 = float(entry_r4_1.get())
                    r1_2 = float(entry_r4_2.get())
                    r1_3 = float(entry_r4_3.get())
                    rt = (1 / r1 + 1 / r1_1 + 1 / r1_2 + 1 / r1_3) ** -1
                    rt = round(rt, 3)
                    ir1 = v1 / r1
                    ir2 = v1 / r1_1
                    ir3 = v1 / r1_2
                    ir4 = v1 / r1_3
                    power = (v1 ** 2) / rt
                    power = round(power, 3)
                    messagebox.showinfo('RESULT', str(
                        'R(total) = ' + str(rt) + '\n' + 'I(across R1) = ' + str(ir1) + '\n' + 'I(across R2) = ' + str(
                            ir2) + '\n' + 'I(across R3) = ' + str(ir3) + '\n' + 'I(across R4) = ' + str(
                            ir4) + '\n' + 'Total power = ' + str(power)))

            elif var_p.get() == 1 and var_s.get() == 1:
                messagebox.showinfo('Error', 'We have not covered this topic yet, sorry :)')
        else:
            messagebox.showinfo('Error', 'Invalid data')

    root1 = Toplevel()
    root1.geometry("350x350+20+80")
    root1.title("CIRCUIT MAKER")
    mycolor1 = "#6C6C6C"

    root1.configure(bg=mycolor1)

    button_exit_calc = Button(root1, text='exit', bg="#6C6C6C", fg='white', font=('Fixedsys', 4),
                              command=exit_calc).place(x=305, y=320)

    label_entry = Label(root1, text='Number of resistors(Ohms):', bg=mycolor1, fg='white',
                        font=('Fixedsys', 10))
    label_entry.place(x=90, y=8)

    tick_r1 = Checkbutton(root1, text='1', bg=mycolor1, variable=var1, font=('Fixedsys', 1), command=tick1)
    tick_r1.place(x=40, y=35)
    label_r1 = Label(root1, text='R1 =', bg=mycolor1, fg='white', font=('Fixedsys', 1))
    entry_r1 = Entry(root1, width=3)

    tick_r2 = Checkbutton(root1, text='2', bg=mycolor1, variable=var2, font=('Fixedsys', 1), command=tick2)
    tick_r2.place(x=120, y=35)
    label_r2 = Label(root1, text='R1 =', bg=mycolor1, fg='white', font=('Fixedsys', 1))
    label_r2_1 = Label(root1, text='R2 =', bg=mycolor1, fg='white', font=('Fixedsys', 1))
    entry_r2 = Entry(root1, width=3)
    entry_r2_1 = Entry(root1, width=3)

    tick_r3 = Checkbutton(root1, text='3', bg=mycolor1, variable=var3, font=('Fixedsys', 1), command=tick3)
    tick_r3.place(x=200, y=35)
    label_r3 = Label(root1, text='R1 =', bg=mycolor1, fg='white', font=('Fixedsys', 1))
    label_r3_1 = Label(root1, text='R2 =', bg=mycolor1, fg='white', font=('Fixedsys', 1))
    label_r3_2 = Label(root1, text='R3 =', bg=mycolor1, fg='white', font=('Fixedsys', 1))
    entry_r3 = Entry(root1, width=3)
    entry_r3_1 = Entry(root1, width=3)
    entry_r3_2 = Entry(root1, width=3)

    tick_r4 = Checkbutton(root1, text='4', bg=mycolor1, variable=var4, font=('Fixedsys', 1), command=tick4)
    tick_r4.place(x=280, y=35)
    label_r4 = Label(root1, text='R1 =', bg=mycolor1, fg='white', font=('Fixedsys', 1))
    label_r4_1 = Label(root1, text='R2 =', bg=mycolor1, fg='white', font=('Fixedsys', 1))
    label_r4_2 = Label(root1, text='R3 =', bg=mycolor1, fg='white', font=('Fixedsys', 1))
    label_r4_3 = Label(root1, text='R4 =', bg=mycolor1, fg='white', font=('Fixedsys', 1))
    entry_r4 = Entry(root1, width=3)
    entry_r4_1 = Entry(root1, width=3)
    entry_r4_2 = Entry(root1, width=3)
    entry_r4_3 = Entry(root1, width=3)

    label_voltage = Label(root1, text='Input the supply voltage(Volts):', bg=mycolor1, fg='white',
                          font=('Fixedsys', 10)).place(x=20, y=150)
    entry2 = Entry(root1, width=6)
    entry2.place(x=280, y=150)

    # label_cai = Label(root1, text='Input the supply current(Amps):', bg=mycolor1, fg='white',
    # font=('Fixedsys', 10)).place(x=1, y=200)
    # entry3 = Entry(root1, width=6)
    # entry3.place(x=260, y=200)

    tick = Checkbutton(root1, text='Series', bg=mycolor1, variable=var_s)
    tick.place(x=50, y=240)

    tick1 = Checkbutton(root1, text='Parallel', bg=mycolor1, variable=var_p)
    tick1.place(x=200, y=240)

    button_go = Button(root1, text='CALCULATE!', bg="#6C6C6C", fg='white', font=('Fixedsys', 10), command=result).place(
        x=108,
        y=270)

    root1.mainloop()


root = Tk()
root.geometry("450x550+470+200")
root.title("DC simulator")

var_s = IntVar()
var_p = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

mycolor = '#E3FFFD'

root.configure(bg=mycolor)

label_main_title = Label(root, text='Welcome to the DC Simulator!', bg='#E3FFFD', fg='#45A7A2', font=('Cambria', 18)) \
    .place(x=70, y=60)

label_theory = Label(root, text='Click here to learn about DC circuit theory!', bg='#E3FFFD', fg='#45A7A2',
                     font=('Cambria', 12)).place(x=65, y=215)

label_calc = Label(root, text='Stuck on a problem ?\nClick here to get some help!', bg='#E3FFFD', fg='#45A7A2',
                   font=('Cambria', 12)).place(x=130, y=345)

button_theory = Button(root, text='DC THEORY', bg='#85E8E1', fg='white', font=('Fixedsys', 15), command=dc).place(x=170,
                                                                                                                  y=248)
button_calc = Button(root, text='CALCULATOR', bg='#85E8E1', fg='white', font=('Fixedsys', 15), command=calc).place(
    x=170,
    y=400)

button_exit = Button(root, text='Exit', bg='#85E8E1', fg='white', font=('Fixedsys', 15), command=exit).place(x=400,
                                                                                                             y=520)
label_references = Label(root, text='Want to know more ?\nClick                to see our references!', bg='#E3FFFD',
                         fg='#45A7A2', font=('Cambria', 12)).place(x=10, y=495)

button_ref = Button(root, text='Here', bg='#85E8E1', fg='white', font=('Fixedsys', 1), command=references, padx=5,
                    pady=1).place(x=51, y=520)

root.mainloop()
