#!/usr/bin/env python
# coding: utf-8

# # Basic Calulator

# ***Importing required liabraries***

# In[1]:


from tkinter import *


# ***Defining finctions***

# In[2]:


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


# In[3]:


def btnClearDisplay():
    global operator
    operator =""
    text_input.set("")


# In[4]:


def btnEqualsInput():
    global operator
    sumup =str(eval(operator))
    text_input.set(sumup)
    operator=""


# ***Creating Display & Title***

# In[5]:


cal = Tk()
cal.title("Calcuator")
operator=""
text_input=StringVar()


# In[6]:


txtDispay = Entry(cal, font = ('arial', 20, 'bold'), textvariable = text_input, bd = 30,
                 insertwidth = 4, bg = "powder blue", justify = 'right').grid(columnspan=4)


# ***Creating Buttons & Assigning Commands***

# In[7]:


btn7 = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "7", bg = "powder blue", command = lambda : btnClick(7)).grid(row = 1, column = 0)

btn8 = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "8", bg = "powder blue", command = lambda : btnClick(8)).grid(row = 1, column = 1)

btn9 = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "9", bg = "powder blue", command = lambda : btnClick(9)).grid(row = 1, column = 2)

Addition = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "+", bg = "powder blue", command = lambda : btnClick("+")).grid(row = 1, column = 3)


# In[8]:


btn4 = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "4", bg = "powder blue", command = lambda : btnClick(4)).grid(row = 2, column = 0)

btn5 = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "5", bg = "powder blue", command = lambda : btnClick(5)).grid(row = 2, column = 1)

btn6 = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "6", bg = "powder blue", command = lambda : btnClick(6)).grid(row = 2, column = 2)

Substraction = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "-", bg = "powder blue", command = lambda : btnClick("-")).grid(row = 2, column = 3)


# In[9]:


btn1 = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "1", bg = "powder blue", command = lambda : btnClick(1)).grid(row = 3, column = 0)

btn2 = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "2", bg = "powder blue", command = lambda : btnClick(2)).grid(row = 3, column = 1)

btn3 = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "3", bg = "powder blue", command = lambda : btnClick(3)).grid(row = 3, column = 2)

Multiply = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "*", bg = "powder blue", command = lambda : btnClick("*")).grid(row = 3, column = 3)


# In[10]:


btn0 = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "0", bg = "powder blue", command = lambda : btnClick(0)).grid(row = 4, column = 0)

btnClear = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "C", bg = "powder blue", command = btnClearDisplay).grid(row = 4, column = 1)

btnEquals = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "=", bg = "powder blue", command = btnEqualsInput).grid(row = 4, column = 2)

Division = Button (cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
              text = "/", bg = "powder blue", command = lambda : btnClick("/")).grid(row = 4, column = 3)


# In[11]:


cal.mainloop()

