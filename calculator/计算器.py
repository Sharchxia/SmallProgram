from tkinter import *
import tkinter.ttk as tk
import math


# 计算器部分
def mov():
    e_0.config(state=NORMAL)
    if len(e_0.get()) > 0:
        e__.insert(INSERT, e_0.get())
    e_0.config(state=DISABLED)


def back():
    ll = len(e__.get())
    e__.delete(ll-1, END)


def cal_1(event):
    cal()


def cal():
    try:
        if len(e__.get()) > 0:
            res = e__.get()
            res = res.replace('e', 'math.e')
            res = res.replace('π', 'math.pi')
            res = res.replace('×', '*')
            res = res.replace('÷', '/')
            res = res.replace('（', '(')
            res = res.replace('）', ')')
            res = eval(res)
            e_0.config(state=NORMAL)
            e_0.delete(0, END)
            e_0.insert(INSERT, str(res))
            e_0.config(state=DISABLED)
            e_0.insert(INSERT, str(round(res, 5)))
            history.config(state=NORMAL)
            history.insert(INSERT, str(round(res, 5))+'\n')
        history.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.config(fg='#f0003f')
        t_1.delete('1.0', 'end')
        t_1.insert(INSERT, '错误：输入数据不合法（超出范围）')
        t_1.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0003f')
        t_1.insert(INSERT, '错误：算式不正确')
        t_1.config(state=DISABLED)


def clear():
    history.config(state=NORMAL)
    e_0.config(state=NORMAL)
    e__.delete(0, END)
    e_0.delete(0, END)
    e_0.config(state=DISABLED)
    e_1.delete(0, END)
    e_2.delete(0, END)
    e_3.delete(0, END)
    e_4.delete(0, END)
    e_5.delete(0, END)
    e_6.delete(0, END)
    e_7.delete(0, END)
    e_8.delete(0, END)
    e_9.delete(0, END)
    e_10.delete(0, END)
    e_11.delete(0, END)
    e_12.delete(0, END)
    e_13.delete(0, END)
    e_14.delete(0, END)
    e_15.delete(0, END)
    e_16.delete(0, END)
    e_17.delete(0, END)
    e_18.delete(0, END)
    e_19.delete(0, END)
    e_20.delete(0, END)
    e_21.delete(0, END)
    history.delete('1.0', 'end')
    history.config(state=DISABLED)
    t_1.config(state=NORMAL, fg='#f0000f')
    t_1.delete('1.0', END)
    t_1.insert(INSERT, '没有错误')
    t_1.config(state=DISABLED)


def clear_p():
    e__.delete(0, END)
    e_0.config(state=NORMAL)
    e_0.delete(0, END)
    e_0.config(state=DISABLED)


def clear_pp():
    e__.delete(0, END)


def inp_0():
    e__.insert(INSERT, '0')


def inp_1():
    e__.insert(INSERT, '1')


def inp_2():
    e__.insert(INSERT, '2')


def inp_3():
    e__.insert(INSERT, '3')


def inp_4():
    e__.insert(INSERT, '4')


def inp_5():
    e__.insert(INSERT, '5')


def inp_6():
    e__.insert(INSERT, '6')


def inp_7():
    e__.insert(INSERT, '7')


def inp_8():
    e__.insert(INSERT, '8')


def inp_9():
    e__.insert(INSERT, '9')


def inp_10():
    e__.insert(INSERT, '.')


def inp_11():
    e__.insert(INSERT, '+')


def inp_12():
    e__.insert(INSERT, '-')


def inp_13():
    e__.insert(INSERT, '×')


def inp_14():
    e__.insert(INSERT, '÷')


def inp_15():
    e__.insert(INSERT, '(')


def inp_16():
    e__.insert(INSERT, ')')


def inp_17():
    e__.insert(INSERT, '**')


def inp_18():
    e__.insert(INSERT, '//')


def inp_19():
    e__.insert(INSERT, '%')


def inp_20():
    history.config(state=NORMAL)
    e__.insert(INSERT, 'π')
    history.insert(INSERT, 'π= '+str(round(math.pi, 5))+'\n')
    history.config(state=DISABLED)


def inp_21():
    history.config(state=NORMAL)
    e__.insert(INSERT, 'e')
    history.insert(INSERT, 'e= '+str(round(math.e, 5))+'\n')
    history.config(state=DISABLED)


def factor():
    try:
        res = math.factorial(eval(e_1.get()))
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        history.insert(INSERT, e_1.get()+'!='+str(res)+'\n')
        e_1.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.config(fg='#f0006f')
        t_1.delete('1.0', 'end')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)


def factor__1(event):
    factor()


def factor_1():
    try:
        res = math.factorial(eval(e_1.get()))
        e__.insert(INSERT, str(res)+' ')
        history.config(state=NORMAL)
        history.insert(INSERT, e_1.get()+'!='+str(res)+'\n')
        e_1.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0009f')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0009f')
        t_1.insert(INSERT, '错误：输入数据不合法（超出范围）')
        t_1.config(state=DISABLED)


def factor_1_1(event):
    factor_1()


def comb():
    try:
        res = math.comb(eval(e_2.get()), eval(e_3.get()))
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        history.insert(INSERT, 'C('+e_2.get()+','+e_3.get()+')='+str(res)+'\n')
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f000cf')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f000cf')
        t_1.insert(INSERT, '错误：输入数据不合法（超出范围）')
        t_1.config(state=DISABLED)


def comb_1():
    try:
        res = math.comb(eval(e_2.get()), eval(e_3.get()))
        e__.insert(INSERT, str(res)+' ')
        history.config(state=NORMAL)
        history.insert(INSERT, 'C('+e_2.get()+','+e_3.get()+')='+str(res)+'\n')
        e_2.delete(0, END)
        e_3.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f000ff')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f000ff')
        t_1.insert(INSERT, '错误：输入数据不合法（超出范围）')
        t_1.config(state=DISABLED)


def comb__1(event):
    comb()


def comb_1_1(event):
    comb_1()


def gcd():
    try:
        res = math.gcd(eval(e_6.get()), eval(e_7.get()))
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        history.insert(INSERT, e_6.get()+'和'+e_7.get()+'的最大公约数= '+str(res)+'\n')
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0200f')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except TypeError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#a0e0af')
        t_1.insert(INSERT, '错误：输入数据不合法（小数）')
        t_1.config(state=DISABLED)


def gcd__1(event):
    gcd()


def perm():
    try:
        res = math.perm(eval(e_4.get()), eval(e_5.get()))
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        history.insert(INSERT, 'P('+e_4.get()+','+e_5.get()+')='+str(res)+'\n')
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0403f')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0403f')
        t_1.insert(INSERT, '错误：输入数据不合法（超出范围）')
        t_1.config(state=DISABLED)


def perm__1(event):
    perm()


def perm_1():
    try:
        res = math.perm(eval(e_4.get()), eval(e_5.get()))
        e__.insert(INSERT, str(res)+' ')
        history.config(state=NORMAL)
        history.insert(INSERT, 'P('+e_4.get()+','+e_5.get()+')='+str(res)+'\n')
        e_4.delete(0, END)
        e_5.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0603f')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0603f')
        t_1.insert(INSERT, '错误：输入数据不合法（超出范围）')
        t_1.config(state=DISABLED)


def perm_1_1(event):
    perm_1()


def log():
    try:
        if e_8.get() == '':
            res = math.log(eval(e_9.get()))
            res = round(res, 3)
            history.config(state=NORMAL)
            history.insert(INSERT, 'ln('+e_9.get()+')= '+str(res)+'\n')
        else:
            res = math.log(eval(e_9.get()), eval(e_8.get()))
            res = round(res, 3)
            history.config(state=NORMAL)
            history.insert(INSERT, 'log(' + e_8.get()+','+e_9.get() + ')= '+str(res)+'\n')
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0803f')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0803f')
        t_1.insert(INSERT, '错误：输入数据不合法（超出范围）')
        t_1.config(state=DISABLED)


def log__1(event):
    log()


def log_1():
    try:
        if e_8.get() == '':
            res = math.log(eval(e_9.get()))
            res = round(res, 3)
            e__.insert(INSERT, str(res)+' ')
            history.config(state=NORMAL)
            history.insert(INSERT, 'ln('+e_9.get()+')= '+str(res)+'\n')
            e_9.delete(0, END)
        else:
            res = math.log(eval(e_9.get()), eval(e_8.get()))
            res = round(res, 3)
            e__.insert(INSERT, str(res)+' ')
            history.config(state=NORMAL)
            history.insert(INSERT, 'log(' + e_8.get()+','+e_9.get() + ')= ' + str(res)+'\n')
            e_8.delete(0, END)
            e_9.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0a03f')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0a03f')
        t_1.insert(INSERT, '错误：输入数据不合法（超出范围）')
        t_1.config(state=DISABLED)


def log_1_1(event):
    log_1()


def sin():
    try:
        if e_10.get() != '':
            num = eval(e_10.get())
            num_1 = num*math.pi
        elif e_11.get() != '':
            num = eval(e_11.get())
            num_1 = num
        else:
            num = eval(e_12.get())
            num_1 = num*math.pi/180
        res = math.sin(num_1)
        res = round(res, 3)
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        if e_10.get():
            history.insert(INSERT, 'sin('+str(num)+'π)= '+str(res)+'\n')
        elif e_11.get():
            history.insert(INSERT, 'sin('+str(num)+'rad)= '+str(res)+'\n')
        else:
            history.insert(INSERT, 'sin('+str(num)+'°)= '+str(res)+'\n')
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0c03f')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)


def sin__1(event):
    sin()


def sin_1():
    try:
        if e_10.get() != '':
            num = eval(e_10.get())
            num_1 = num*math.pi
        elif e_11.get() != '':
            num = eval(e_11.get())
            num_1 = num
        else:
            num = eval(e_12.get())
            num_1 = num*math.pi/180
        res = math.sin(num_1)
        res = round(res, 3)
        e__.insert(INSERT, str(res)+' ')
        history.config(state=NORMAL)
        if e_10.get():
            history.insert(INSERT, 'sin('+str(num)+'π)= '+str(res)+'\n')
        elif e_11.get():
            history.insert(INSERT, 'sin('+str(num)+'rad)= '+str(res)+'\n')
        else:
            history.insert(INSERT, 'sin('+str(num)+'°)= '+str(res)+'\n')
        e_10.delete(0, END)
        e_11.delete(0, END)
        e_12.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0e03f')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)


def sin_1_1(event):
    sin_1()


def cos():
    try:
        if e_13.get() != '':
            num = eval(e_13.get())
            num_1 = num*math.pi
        elif e_14.get() != '':
            num = eval(e_14.get())
            num_1 = num
        else:
            num = eval(e_15.get())
            num_1 = num*math.pi/180
        res = math.cos(num_1)
        res = round(res, 3)
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        if e_13.get():
            history.insert(INSERT, 'cos('+str(num)+'π)= '+str(res)+'\n')
        elif e_14.get():
            history.insert(INSERT, 'cos('+str(num)+'rad)= '+str(res)+'\n')
        else:
            history.insert(INSERT, 'cos('+str(num)+'°)= '+str(res)+'\n')
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f020af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)


def cos__1(event):
    cos()


def cos_1():
    try:
        if e_13.get() != '':
            num = eval(e_13.get())
            num_1 = num*math.pi
        elif e_14.get() != '':
            num = eval(e_14.get())
            num_1 = num
        else:
            num = eval(e_15.get())
            num_1 = num*math.pi/180
        res = math.cos(num_1)
        res = round(res, 3)
        e__.insert(INSERT, str(res)+' ')
        history.config(state=NORMAL)
        if e_13.get():
            history.insert(INSERT, 'cos('+str(num)+'π)= '+str(res)+'\n')
        elif e_14.get():
            history.insert(INSERT, 'cos('+str(num)+'rad)= '+str(res)+'\n')
        else:
            history.insert(INSERT, 'cos('+str(num)+'°)= '+str(res)+'\n')
        e_13.delete(0, END)
        e_14.delete(0, END)
        e_15.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f040af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)


def cos_1_1(event):
    cos_1()


def tan():
    try:
        if e_16.get() != '':
            num = eval(e_16.get())
            num_1 = num*math.pi
        elif e_17.get() != '':
            num = eval(e_17.get())
            num_1 = num
        else:
            num = eval(e_18.get())
            num_1 = num*math.pi/180
        res = math.tan(num_1)
        res = round(res, 3)
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        if e_16.get():
            history.insert(INSERT, 'tan('+str(num)+'π)= '+str(res)+'\n')
        elif e_17.get():
            history.insert(INSERT, 'tan('+str(num)+'rad)= '+str(res)+'\n')
        else:
            history.insert(INSERT, 'tan('+str(num)+'°)= '+str(res)+'\n')
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f060af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)


def tan__1(event):
    tan()


def tan_1():
    try:
        if e_16.get() != '':
            num = eval(e_16.get())
            num_1 = num*math.pi
        elif e_17.get() != '':
            num = eval(e_17.get())
            num_1 = num
        else:
            num = eval(e_18.get())
            num_1 = num*math.pi/180
        res = math.tan(num_1)
        res = round(res, 3)
        e__.insert(INSERT, str(res)+' ')
        history.config(state=NORMAL)
        if e_16.get():
            history.insert(INSERT, 'tan('+str(num)+'π)= '+str(res)+'\n')
        elif e_17.get():
            history.insert(INSERT, 'tan('+str(num)+'rad)= '+str(res)+'\n')
        else:
            history.insert(INSERT, 'tan('+str(num)+'°)= '+str(res)+'\n')
        e_16.delete(0, END)
        e_17.delete(0, END)
        e_18.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f080af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)


def tan_1_1(event):
    tan_1()


def asin_0():
    try:
        res = math.asin(eval(e_19.get()))
        res = round(res, 3)
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        history.insert(INSERT, 'asin('+e_19.get()+')= '+str(res)+'= '+str(round(res/math.pi, 3))+'π'+'(rad)'+'\n')
        e_19.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0a0af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0a0af')
        t_1.insert(INSERT, '错误：输入数值不合法（超出范围）')
        t_1.config(state=DISABLED)


def asin_1():
    try:
        res = math.asin(eval(e_19.get()))
        res = math.degrees(res)
        res = round(res, 3)
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        history.insert(INSERT, 'asin('+e_19.get()+')= '+str(res)+'°'+'\n')
        e_19.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0c0af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0c0af')
        t_1.insert(INSERT, '错误：输入数值不合法（超出范围）')
        t_1.config(state=DISABLED)


def asin_2(event):
    try:
        res = math.asin(eval(e_19.get()))
        res_ = math.degrees(res)
        res = round(res, 3)
        res_ = round(res_, 3)
        history.config(state=NORMAL)
        history.insert(INSERT, 'asin(' + e_19.get() + ')= ' + str(res) + '= ' + str(round(res / math.pi, 3)) + 'π' + '(rad)' + '\n')
        history.insert(INSERT, 'asin(' + e_19.get() + ')= ' + str(res_) + '°' + '\n')
        e_19.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0e0af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#f0e0af')
        t_1.insert(INSERT, '错误：输入数值不合法（超出范围）')
        t_1.config(state=DISABLED)


def acos_0():
    try:
        res = math.acos(eval(e_20.get()))
        res = round(res, 3)
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        history.insert(INSERT, 'acos('+e_20.get()+')= '+str(res)+'= '+str(round(res/math.pi, 3))+'π'+'(rad)'+'\n')
        history.config(state=DISABLED)
        e_20.delete(0, END)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#d0e0af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#d0e0af')
        t_1.insert(INSERT, '错误：输入数值不合法（超出范围）')
        t_1.config(state=DISABLED)


def acos_1():
    try:
        res = math.acos(eval(e_20.get()))
        res = math.degrees(res)
        res = round(res, 3)
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        history.insert(INSERT, 'acos('+e_20.get()+')= '+str(res)+'°'+'\n')
        history.config(state=DISABLED)
        e_20.delete(0, END)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#b0e0af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#b0e0af')
        t_1.insert(INSERT, '错误：输入数值不合法（超出范围）')
        t_1.config(state=DISABLED)


def acos_2(event):
    try:
        res = math.acos(eval(e_20.get()))
        res_ = math.degrees(res)
        res = round(res, 3)
        res_ = round(res_, 3)
        history.config(state=NORMAL)
        history.insert(INSERT, 'acos(' + e_20.get() + ')= ' + str(res) + '= ' + str(round(res / math.pi, 3)) + 'π' + '(rad)' + '\n')
        history.insert(INSERT, 'acos(' + e_20.get() + ')= ' + str(res_) + '°' + '\n')
        e_20.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#90e0af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)
    except ValueError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#90e0af')
        t_1.insert(INSERT, '错误：输入数值不合法（超出范围）')
        t_1.config(state=DISABLED)


def atan_0():
    try:
        res = math.atan(eval(e_21.get()))
        res = round(res, 3)
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        history.insert(INSERT, 'atan('+e_21.get()+')= '+str(res)+'= '+str(round(res/math.pi, 3))+'π'+'(rad)'+'\n')
        history.config(state=DISABLED)
        e_21.delete(0, END)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#70e0af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)


def atan_1():
    try:
        res = math.atan(eval(e_21.get()))
        res = math.degrees(res)
        res = round(res, 3)
        e_0.config(state=NORMAL)
        e_0.delete(0, END)
        e_0.insert(INSERT, str(res))
        e_0.config(state=DISABLED)
        history.config(state=NORMAL)
        history.insert(INSERT, 'atan('+e_21.get()+')= '+str(res)+'°'+'\n')
        history.config(state=DISABLED)
        e_21.delete(0, END)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#50e0af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)


def atan_2(event):
    try:
        res = math.atan(eval(e_21.get()))
        res_ = math.degrees(res)
        res = round(res, 3)
        res_ = round(res_, 3)
        history.config(state=NORMAL)
        history.insert(INSERT, 'atan(' + e_21.get() + ')= ' + str(res) + '= ' + str(round(res / math.pi, 3)) + 'π' + '(rad)' + '\n')
        history.insert(INSERT, 'atan(' + e_21.get() + ')= ' + str(res_) + '°' + '\n')
        e_21.delete(0, END)
        history.config(state=DISABLED)
    except SyntaxError:
        t_1.config(state=NORMAL)
        t_1.delete('1.0', 'end')
        t_1.config(fg='#30e0af')
        t_1.insert(INSERT, '错误：未在有效位置输入数据')
        t_1.config(state=DISABLED)


def get_0():
    e_0.config(state=NORMAL)
    e_19.delete(0, END)
    e_19.insert(INSERT, e_0.get())
    e_0.config(state=DISABLED)


def get_0_1(event):
    get_0()


def get_1():
    e_0.config(state=NORMAL)
    e_20.delete(0, END)
    e_20.insert(INSERT, e_0.get())
    e_0.config(state=DISABLED)


def get_1_1(event):
    get_1()


def get_2():
    e_0.config(state=NORMAL)
    e_21.delete(0, END)
    e_21.insert(INSERT, e_0.get())
    e_0.config(state=DISABLED)


def get_2_1(event):
    get_2()


def switchover(event):
    global i
    if event.keycode == 37:
        if i == 0:
            i = 2
        else:
            i -= 1
    else:
        if i == 2:
            i = 0
        else:
            i += 1
    note.select(frames[i])


def top(event):
    global check
    check = not check
    win.attributes('-topmost', check)


win = Tk()
check = False
win.attributes('-topmost', check)
win.bind('<Escape>', top)
win.bind('<Left>', switchover)
win.bind('<Right>', switchover)
w, h = win.winfo_screenwidth(), win.winfo_screenheight()
# win.iconphoto(False, PhotoImage(file='D:\\25316\\Code\\soft\\bb.gif'))
win.geometry('%dx%d+%d+%d' % (w*0.3, h*0.7, w*0.1, h*0.15))
win.title('基于Python tkinter的计算器')
win.minsize(int(w*0.3), int(h*0.7))
note = tk.Notebook(win)
frame_1 = Frame()
e__ = Entry(frame_1, fg='#ff00ff')
Label(frame_1, text='算式:', font=17).place(relwidth=0.1, relheight=0.05, relx=0, rely=0)
e__.bind('<Return>', cal_1)
e__.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0)
Button(frame_1, text='后退', command=back).place(relwidth=0.1, relheight=0.05, relx=0.9, rely=0)
e_0 = Entry(frame_1, state=DISABLED, fg='#12da90')
e_0.place(relwidth=0.45, relheight=0.05, relx=0.1, rely=0.05)
Label(frame_1, text='结果:', font=17).place(relwidth=0.1, relheight=0.05, relx=0, rely=0.05)
Button(frame_1, text='计算', command=cal).place(relwidth=0.1, relheight=0.05, relx=0.55, rely=0.05)
Button(frame_1, text='全部清除', command=clear, fg='#422210').place(relwidth=0.15, relheight=0.05, relx=0.65, rely=0.05)
Button(frame_1, text='结果算式清除', command=clear_p).place(relwidth=0.2, relheight=0.05, relx=0.6, rely=0.1)
Button(frame_1, text='结果移入算式', command=mov, fg='#ff0000').place(relwidth=0.2, relheight=0.05, relx=0.8, rely=0.05)
Button(frame_1, text='算式内容清除', command=clear_pp).place(relwidth=0.2, relheight=0.05, relx=0.8, rely=0.1)
Button(frame_1, text='9', font=18, command=inp_9).place(relwidth=0.1, relheight=0.05, relx=0.2, rely=0.1)
Button(frame_1, text='8', font=18, command=inp_8).place(relwidth=0.1, relheight=0.05, relx=0.1, rely=0.1)
Button(frame_1, text='7', font=18, command=inp_7).place(relwidth=0.1, relheight=0.05, relx=0, rely=0.1)
Button(frame_1, text='6', font=18, command=inp_6).place(relwidth=0.1, relheight=0.05, relx=0.2, rely=0.15)
Button(frame_1, text='5', font=18, command=inp_5).place(relwidth=0.1, relheight=0.05, relx=0.1, rely=0.15)
Button(frame_1, text='4', font=18, command=inp_4).place(relwidth=0.1, relheight=0.05, relx=0, rely=0.15)
Button(frame_1, text='3', font=18, command=inp_3).place(relwidth=0.1, relheight=0.05, relx=0.2, rely=0.2)
Button(frame_1, text='2', font=18, command=inp_2).place(relwidth=0.1, relheight=0.05, relx=0.1, rely=0.2)
Button(frame_1, text='1', font=18, command=inp_1).place(relwidth=0.1, relheight=0.05, relx=0, rely=0.2)
Button(frame_1, text='.', font=18, command=inp_10).place(relwidth=0.1, relheight=0.05, relx=0.2, rely=0.25)
Button(frame_1, text='0', font=18, command=inp_0).place(relwidth=0.1, relheight=0.05, relx=0.1, rely=0.25)
Button(frame_1, text='=', font=18, command=cal).place(relwidth=0.1, relheight=0.05, relx=0, rely=0.25)
Button(frame_1, text='+', font=18, command=inp_11).place(relwidth=0.1, relheight=0.05, relx=0.3, rely=0.1)
Button(frame_1, text='-', font=18, command=inp_12).place(relwidth=0.1, relheight=0.05, relx=0.3, rely=0.15)
Button(frame_1, text='×', font=18, command=inp_13).place(relwidth=0.1, relheight=0.05, relx=0.3, rely=0.2)
Button(frame_1, text='÷', font=18, command=inp_14).place(relwidth=0.1, relheight=0.05, relx=0.3, rely=0.25)
Button(frame_1, text='(', font=18, command=inp_15).place(relwidth=0.1, relheight=0.05, relx=0.4, rely=0.1)
Button(frame_1, text=')', font=18, command=inp_16).place(relwidth=0.1, relheight=0.05, relx=0.5, rely=0.1)
Button(frame_1, text='**(乘方)', font=18, command=inp_17).place(relwidth=0.2, relheight=0.05, relx=0.4, rely=0.15)
Button(frame_1, text='π', font=18, command=inp_20).place(relwidth=0.1, relheight=0.05, relx=0.6, rely=0.15)
Button(frame_1, text='e', font=18, command=inp_21).place(relwidth=0.1, relheight=0.05, relx=0.7, rely=0.15)
Label(frame_1, text='历史记录：').place(relwidth=0.2, relheight=0.05, relx=0.8, rely=0.15)
sr = Scrollbar(frame_1)
history = Text(frame_1, font=15, yscrollcommand=sr.set, state=DISABLED)
sr.config(command=history.yview)
history.place(relwidth=0.35, relheight=0.5, relx=0.6, rely=0.2)
sr.place(relwidth=0.05, relheight=0.5, rely=0.2, relx=0.95)
Button(frame_1, text='//(整除)', font=18, command=inp_18).place(relwidth=0.2, relheight=0.05, relx=0.4, rely=0.2)
Button(frame_1, text='%(取余）', font=18, command=inp_19).place(relwidth=0.2, relheight=0.05, relx=0.4, rely=0.25)
label_1 = Label(frame_1, text='以下为特殊运算', fg='#ffff00', font='bold 17', bg='#000000')
label_1.place(relwidth=0.6, relheight=0.05, relx=0, rely=0.3)
Label(frame_1, text='阶乘', font='bold 16').place(relwidth=0.1, relheight=0.05, relx=0, rely=0.35)
e_1 = Entry(frame_1)
e_1.bind('<Return>', factor__1)
e_1.bind('<Key-Up>', factor_1_1)
e_1.place(relwidth=0.15, relheight=0.05, relx=0.1, rely=0.35)
Button(frame_1, text='! =', command=factor, font=18).place(relwidth=0.1, relheight=0.05, relx=0.25, rely=0.35)
Button(frame_1, text='计算并上移结果', command=factor_1).place(relwidth=0.225, relheight=0.05, relx=0.375, rely=0.35)
Label(frame_1, text='组合', font='bold 16').place(relwidth=0.1, relheight=0.05, relx=0, rely=0.4)
e_2 = Entry(frame_1)
e_2.bind('<Return>', comb__1)
e_2.bind('<Up>', comb_1_1)
e_2.place(relwidth=0.075, relheight=0.05, relx=0.1, rely=0.4)
e_3 = Entry(frame_1)
e_3.bind('<Return>', comb__1)
e_3.bind('<Up>', comb_1_1)
e_3.place(relwidth=0.075, relheight=0.05, relx=0.175, rely=0.4)
Button(frame_1, text='C =', command=comb, font=18).place(relwidth=0.1, relheight=0.05, relx=0.25, rely=0.4)
Button(frame_1, text='计算并上移结果', command=comb_1).place(relwidth=0.225, relheight=0.05, relx=0.375, rely=0.4)
Label(frame_1, text='排列', font='bold 16').place(relwidth=0.1, relheight=0.05, relx=0, rely=0.45)
e_4 = Entry(frame_1)
e_4.bind('<Return>', perm__1)
e_4.bind('<Up>', perm_1_1)
e_4.place(relwidth=0.075, relheight=0.05, relx=0.1, rely=0.45)
e_5 = Entry(frame_1)
e_5.place(relwidth=0.075, relheight=0.05, relx=0.175, rely=0.45)
Button(frame_1, text='P =', command=perm, font=18).place(relwidth=0.1, relheight=0.05, relx=0.25, rely=0.45)
Button(frame_1, text='计算并上移结果', command=perm_1).place(relwidth=0.225, relheight=0.05, relx=0.375, rely=0.45)
Label(frame_1, text='最大公约数', font='bold 16').place(relwidth=0.25, relheight=0.05, relx=0, rely=0.5)
e_6 = Entry(frame_1)
e_6.place(relwidth=0.075, relheight=0.05, relx=0.25, rely=0.5)
e_7 = Entry(frame_1)
e_7.place(relwidth=0.075, relheight=0.05, relx=0.325, rely=0.5)
e_6.bind('<Return>', gcd__1)
e_7.bind('<Return>', gcd__1)
Button(frame_1, text='公约 =', command=gcd, font=18).place(relwidth=0.2, relheight=0.05, relx=0.4, rely=0.5)
Label(frame_1, text='对数', font='bold 16').place(relwidth=0.1, relheight=0.05, relx=0, rely=0.55)
e_8 = Entry(frame_1)
e_8.place(relwidth=0.075, relheight=0.05, relx=0.1, rely=0.55)
e_9 = Entry(frame_1)
e_9.place(relwidth=0.075, relheight=0.05, relx=0.175, rely=0.55)
e_8.bind('<Return>', log__1)
e_8.bind('<Up>', log_1_1)
e_9.bind('<Return>', log__1)
e_9.bind('<Up>', log_1_1)
Button(frame_1, text='log=', command=log, font=18).place(relwidth=0.1, relheight=0.05, relx=0.25, rely=0.55)
Button(frame_1, text='计算并上移结果', command=log_1).place(relwidth=0.225, relheight=0.05, relx=0.375, rely=0.55)
label_2 = Label(frame_1, text='三角函数', fg='#ffff00', font='bold 17', bg='#000000')
label_2.place(relwidth=0.6, relheight=0.1, relx=0, rely=0.6)
Label(frame_1, text='sin', font='bold 18').place(relwidth=0.1, relheight=0.05, relx=0, rely=0.7)
e_10 = Entry(frame_1)
e_10.place(relwidth=0.075, relheight=0.05, relx=0.1, rely=0.7)
Label(frame_1, text='π', font='bold 18').place(relwidth=0.075, relheight=0.05, relx=0.175, rely=0.7)
e_11 = Entry(frame_1)
e_11.place(relwidth=0.1, relheight=0.05, relx=0.25, rely=0.7)
Label(frame_1, text='rad', font='bold 16').place(relwidth=0.075, relheight=0.05, relx=0.35, rely=0.7)
e_12 = Entry(frame_1)
e_12.place(relwidth=0.1, relheight=0.05, relx=0.425, rely=0.7)
e_10.bind('<Return>', sin__1)
e_11.bind('<Return>', sin__1)
e_12.bind('<Return>', sin__1)
e_10.bind('<Up>', sin_1_1)
e_11.bind('<Up>', sin_1_1)
e_12.bind('<Up>', sin_1_1)
Label(frame_1, text='°', font='bold 18').place(relwidth=0.075, relheight=0.05, relx=0.525, rely=0.7)
Button(frame_1, text='=', command=sin, font=18).place(relwidth=0.1, relheight=0.05, relx=0.6, rely=0.7)
Button(frame_1, text='计算并上移结果', command=sin_1).place(relwidth=0.225, relheight=0.05, relx=0.72, rely=0.7)
Label(frame_1, text='cos', font='bold 18').place(relwidth=0.1, relheight=0.05, relx=0, rely=0.75)
e_13 = Entry(frame_1)
e_13.place(relwidth=0.075, relheight=0.05, relx=0.1, rely=0.75)
Label(frame_1, text='π', font='bold 18').place(relwidth=0.075, relheight=0.05, relx=0.175, rely=0.75)
e_14 = Entry(frame_1)
e_14.place(relwidth=0.1, relheight=0.05, relx=0.25, rely=0.75)
Label(frame_1, text='rad', font='bold 16').place(relwidth=0.075, relheight=0.05, relx=0.35, rely=0.75)
e_15 = Entry(frame_1)
e_15.place(relwidth=0.1, relheight=0.05, relx=0.425, rely=0.75)
e_13.bind('<Return>', cos__1)
e_14.bind('<Return>', cos__1)
e_15.bind('<Return>', cos__1)
e_13.bind('<Up>', cos_1_1)
e_14.bind('<Up>', cos_1_1)
e_15.bind('<Up>', cos_1_1)
Label(frame_1, text='°', font='bold 18').place(relwidth=0.075, relheight=0.05, relx=0.525, rely=0.75)
Button(frame_1, text='=', command=cos, font=18).place(relwidth=0.1, relheight=0.05, relx=0.6, rely=0.75)
Button(frame_1, text='计算并上移结果', command=cos_1).place(relwidth=0.225, relheight=0.05, relx=0.72, rely=0.75)
Label(frame_1, text='tan', font='bold 18').place(relwidth=0.1, relheight=0.05, relx=0, rely=0.8)
e_16 = Entry(frame_1)
e_16.place(relwidth=0.075, relheight=0.05, relx=0.1, rely=0.8)
Label(frame_1, text='π', font='bold 18').place(relwidth=0.075, relheight=0.05, relx=0.175, rely=0.8)
e_17 = Entry(frame_1)
e_17.place(relwidth=0.1, relheight=0.05, relx=0.25, rely=0.8)
Label(frame_1, text='rad', font='bold 16').place(relwidth=0.075, relheight=0.05, relx=0.35, rely=0.8)
e_18 = Entry(frame_1)
e_18.place(relwidth=0.1, relheight=0.05, relx=0.425, rely=0.8)
e_16.bind('<Return>', tan__1)
e_17.bind('<Return>', tan__1)
e_18.bind('<Return>', tan__1)
e_16.bind('<Up>', tan_1_1)
e_17.bind('<Up>', tan_1_1)
e_18.bind('<Up>', tan_1_1)
Label(frame_1, text='°', font='bold 18').place(relwidth=0.075, relheight=0.05, relx=0.525, rely=0.8)
Button(frame_1, text='=', command=tan, font=18).place(relwidth=0.1, relheight=0.05, relx=0.6, rely=0.8)
Button(frame_1, text='计算并上移结果', command=tan_1).place(relwidth=0.225, relheight=0.05, relx=0.72, rely=0.8)
Label(frame_1, text='错\n误：', justify=LEFT).place(relwidth=0.055, relheight=0.15, relx=0.945, rely=0.7)
Label(frame_1, text='asin', font='bold 13').place(relwidth=0.1, relheight=0.05, relx=0, rely=0.85)
e_19 = Entry(frame_1)
e_19.place(relwidth=0.1, relheight=0.05, relx=0.1, rely=0.85)
e_19.bind('<Return>', asin_2)
e_19.bind('<Down>', get_0_1)
Button(frame_1, text='=(rad)', font=18, command=asin_0).place(relwidth=0.12, relheight=0.05, relx=0.2, rely=0.85)
Button(frame_1, text='=(°)', font=18, command=asin_1).place(relwidth=0.11, relheight=0.05, relx=0.33, rely=0.85)
Button(frame_1, text='获得上面结果', command=get_0, font=18).place(relwidth=0.25, relheight=0.05, relx=0.45, rely=0.85)
Label(frame_1, text='acos', font='bold 13').place(relwidth=0.1, relheight=0.05, relx=0, rely=0.9)
e_20 = Entry(frame_1)
e_20.place(relwidth=0.1, relheight=0.05, relx=0.1, rely=0.9)
e_20.bind('<Return>', acos_2)
e_20.bind('<Down>', get_1_1)
Button(frame_1, text='=(rad)', font=18, command=acos_0).place(relwidth=0.12, relheight=0.05, relx=0.2, rely=0.9)
Button(frame_1, text='=(°)', font=18, command=acos_1).place(relwidth=0.11, relheight=0.05, relx=0.33, rely=0.9)
Button(frame_1, text='获得上面结果', command=get_1, font=18).place(relwidth=0.25, relheight=0.05, relx=0.45, rely=0.9)
Label(frame_1, text='atan', font='bold 13').place(relwidth=0.1, relheight=0.05, relx=0, rely=0.95)
e_21 = Entry(frame_1)
e_21.place(relwidth=0.1, relheight=0.05, relx=0.1, rely=0.95)
e_21.bind('<Return>', atan_2)
e_21.bind('<Down>', get_2_1)
Button(frame_1, text='=(rad)', font=18, command=atan_0).place(relwidth=0.12, relheight=0.05, relx=0.2, rely=0.95)
Button(frame_1, text='=(°)', font=18, command=atan_1).place(relwidth=0.11, relheight=0.05, relx=0.33, rely=0.95)
Button(frame_1, text='获得上面结果', command=get_2, font=18).place(relwidth=0.25, relheight=0.05, relx=0.45, rely=0.95)
note.add(frame_1, text='计算器')
t_1 = Text(frame_1, font=20, fg='#f0000f')
t_1.insert(INSERT, '没有错误')
t_1.config(state=DISABLED)
t_1.place(relwidth=0.24, relx=0.72, rely=0.875, relheight=0.1)
# 计算器部分
# 积分表部分
frame_2 = Frame()
note.add(frame_2, text='积分表')
label_3 = Label(frame_2, justify=LEFT)
content = ''
# 积分表部分
# 导数表部分

frame_3 = Frame()
note.add(frame_3, text='导数表')

# 导数表部分
frames = [frame_1, frame_2, frame_3]
i = 0
note.select(frames[i])
note.place(relwidth=1, relheight=1)
win.mainloop()
