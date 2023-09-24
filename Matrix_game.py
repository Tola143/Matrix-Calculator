from tkinter import *
import numpy as np
from tkinter import ttk
import webbrowser
import os

def convert_matrix(matrix_text,):
    msg = str(matrix_text.get("1.0", END))
    array = msg.split("\n")
    array.remove("")
    data = []
    for i in range(len(array)):
        ri = array[i].split(" ")
        rowi = []
        for j in ri:
            r = j.replace('[', '').replace(']', '')
            rowi.append(int(r))
        data.append(rowi)
    return data

def oper_matrix():
    window.title("The Matrix operation")
    frame1.pack_forget()
    frame2.pack()

def back():
    add_clear()
    sub_clear()
    multi_clear()
    div_clear()
    window.title("The Matrix")
    frame1.pack()
    frame2.pack_forget()

def next_add():
    dataA = convert_matrix(matrix_add_A)
    dataB = convert_matrix(matrix_add_B)
    A = np.array(dataA)
    B = np.array(dataB)
    sum = A + B
    result_text_add.insert("1.0", str(sum))
    window.update()
    frame2.pack_forget()
    frame3_add.pack()
    frame3_sub.pack_forget()
    frame3_multi.pack_forget()
    frame3_div.pack_forget()
    frame3.pack()

def next_sub():
    dataA = convert_matrix(matrix_sub_A)
    dataB = convert_matrix(matrix_sub_B)
    A = np.array(dataA)
    B = np.array(dataB)
    subtract = A - B
    result_text_sub.insert("1.0", str(subtract))
    window.update()
    frame2.pack_forget()
    frame3_sub.pack_forget()
    frame3_sub.pack()
    frame3_multi.pack_forget()
    frame3_div.pack_forget()
    frame3.pack()

def next_multi():
    dataA = convert_matrix(matrix_multi_A)
    dataB = convert_matrix(matrix_multi_B)
    A = np.array(dataA)
    B = np.array(dataB)
    product = np.matrix(A) * np.matrix(B)
    result_text_multi.insert("1.0", str(product))
    window.update()
    frame2.pack_forget()
    frame3_add.pack_forget()
    frame3_add.pack_forget()
    frame3_div.pack_forget()
    frame3_multi.pack()
    frame3.pack()

def next_div():
    dataA = convert_matrix(matrix_div_A)
    dataB = convert_matrix(matrix_div_B)
    A = np.array(dataA)
    B = np.array(dataB)
    divided = np.matrix(A) / np.matrix(B)
    result_text_div.insert("1.0", str(divided))
    window.update()
    frame2.pack_forget()
    frame3_add.pack_forget()
    frame3_add.pack_forget()
    frame3_multi.pack_forget()
    frame3_div.pack()
    frame3.pack()

def back_add_result():
    result_text_add.delete("1.0", END)
    frame3_add.pack_forget()
    frame2.pack()
    frame3.pack_forget()

def back_sub_result():
    result_text_sub.delete("1.0", END)
    frame3_sub.pack_forget()
    frame2.pack()
    frame3.pack_forget()

def back_multi_result():
    result_text_multi.delete("1.0", END)
    frame3_multi.pack_forget()
    frame2.pack()
    frame3.pack_forget()
    
def back_div_result():
    result_text_div.delete("1.0", END)
    frame3_div.pack_forget()
    frame2.pack()
    frame3.pack_forget()

def add_clear():
    matrix_add_A.delete("1.0", END)
    matrix_add_B.delete("1.0", END)

def sub_clear():
    matrix_sub_A.delete("1.0", END)
    matrix_sub_B.delete("1.0", END)

def multi_clear():
    matrix_multi_A.delete("1.0", END)
    matrix_multi_B.delete("1.0", END)

def div_clear():
    matrix_div_A.delete("1.0", END)
    matrix_div_B.delete("1.0", END)

# --------------------------------#
# Inverse function
def inv_matrix():
    window.title("Find inverse matrix")
    frame1.pack_forget()
    inv_frame.pack()

def inv_clear():
    matrix_inv_A.delete("1.0", END)
    matrix_inv_B.delete("1.0", END)

def inv_back():
    inv_clear()
    frame1.pack_forget()
    inv_frame.pack_forget()
    window.title("The Matrix")
    frame1.pack()

def inv_convt():
    try:
        dataA = convert_matrix(matrix_inv_A)
        A = np.array(dataA)
        B = np.linalg.inv(A)
        matrix_inv_B.delete("1.0", END)
        matrix_inv_B.insert("1.0", str(B))
    except:
        matrix_inv_B.delete("1.0", END)
        msg = """This Matrix have no inverse.\n\nRule:    
        1, The array must be square.
        2, Array must be at least 2D.\n\nSometimes:
        3, This matrix is Singular matrix.\n\nWarning
        4, Don't insert letter or empty array.
        """
        matrix_inv_B.delete("1.0", END)
        matrix_inv_B.insert("1.0", str(msg))

def sol_linear():
    window.title("Solve system linear equation")
    frame1.pack_forget()
    linear_frame.pack()

def linear_back():
    linear_clear()
    frame1.pack()
    window.title("The Matrix")
    linear_frame.pack_forget()

def linear_clear():
    matrix_linear_solution.delete("1.0", END)
    matrix_linear_A.delete("1.0", END)
    matrix_linear_B.delete("1.0", END)

def linear_convt():
    try:
        dataA = convert_matrix(matrix_linear_A)
        dataB = convert_matrix(matrix_linear_B)
        A = np.array(dataA)
        B = np.array(dataB)
        inv_A = np.linalg.inv(A)
        matrix_linear_solution.delete("1.0", END)
        solution = np.matrix(inv_A) * np.matrix(B)
        matrix_linear_solution.insert("1.0", str(solution))
    except:
        matrix_linear_solution.delete("1.0", END)
        msg = """You did somethings wrong,\nplease check below:\n\nRule:    
1, The array must be square.
2, Array must be at least 2D.
3, The matrix A and B must be
   in the same Dimension.\n\nWarning
4, Don't insert letter or 
   empty array\n"""
        matrix_linear_solution.insert("1.0", str(msg))

def about():
    window.title("About the matrix")
    frame1.pack_forget()
    about_frame.pack()
    filename = os.path.join(os.path.dirname(__file__), "about_the_matrix.txt")
    try:
        with open(filename, 'r') as file:
            text = file.read()
            about_text.insert("1.0", str(text))
    except:
        text = '\t\tTo read instruction:\n\nPlease, put the txt file \"about_the_matrix.txt\" in the same source \ncode directory.'
        about_text.insert("1.0", str(text))

def about_back():
    about_text.delete("1.0", END)
    frame1.pack()
    window.title("The Matrix")
    about_frame.pack_forget()

def contact():
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open_new_tab(url)

# Background color variables
window_bg = "lightyellow"
add_bg = "#b9faf9"
sub_bg = "#f7fad2"
multi_bg = "#fce3d2"
div_bg = "#fcd2f1"

# URL
url = 'https://www.facebook.com/litayong.kantola/'

window = Tk()
window.geometry('800x500')
window.title('The Matrix')
window.config(bg=window_bg)
window.resizable(width=False, height=False)

# part one
frame1 = Frame(window, height=500, width=500, bg=window_bg)
lable = Label(frame1, text='Welcome To The Matrix',  width=50, pady=15, bg='red', fg='white', font=('Arial', 30,'bold'))
button1 = Button(frame1, text='Operation Of Matrix', bg="#f0ae1f", fg='white', width=40, pady=10, command=oper_matrix, font=('Arial', 20,'bold'))
button2 = Button(frame1, text='Find Inverse Matrix', bg="#0acc6e", fg='white', width=40, pady=10, command=inv_matrix, font=('Arial', 20,'bold'))
button3 = Button(frame1, text='Solve system linear equation', bg="#de0d8a", fg='white', width=40, pady=10, command=sol_linear, font=('Arial', 20,'bold'))
button4 = Button(frame1, text='About !', bg="#42aaf5", fg='white', width=40, pady=10, command=about, font=('Arial', 20,'bold'))

lable.pack(pady=10)
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)

frame1.pack()

# -----------------------------------------------------#
# part 2 Operation Matrix
frame2 = Frame(window, height=500, width=800, bg=window_bg)
notebooks = ttk.Notebook(frame2, height=500, width=800)
add_frame = Frame(notebooks, bg=add_bg, padx=10)
sub_frame = Frame(notebooks, bg=sub_bg, padx=10)
multi_frame = Frame(notebooks, bg=multi_bg, padx=10)
div_frame = Frame(notebooks, bg=div_bg, padx=10)

notebooks.add(add_frame,text=' Addition (+) ')
notebooks.add(sub_frame,text=' Subtraction (-) ')
notebooks.add(multi_frame,text=' Multiplication (x) ')
notebooks.add(div_frame,text=' Dividation (/) ')
notebooks.pack(expand=True, fill='both')

# addition
label_add_matrix_A = Label(add_frame, text='Matrix A:', width=10, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
label_add_matrix_B = Label(add_frame, text='Matrix B:', width=10, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
matrix_add_A = Text(add_frame, width=25, height=8, pady=10, font=('Arial', 20, 'bold'))
matrix_add_B = Text(add_frame, width=25, height=8, pady=10, font=('Arial', 20, 'bold'))

label_add_matrix_A.grid(row=0, column=0, padx=5, pady=10)
label_add_matrix_B.grid(row=0, column=1, padx=5, pady=10)
matrix_add_A.grid(row=1, column=0, padx=5, pady=10)
matrix_add_B.grid(row=1, column=1, padx=5, pady=10)

add_frame_1 = Frame(add_frame, bg=add_bg)
add_frame_1.grid(row=2, columnspan=2, padx=5, pady=10)

back_add = Button(add_frame_1, text='<<Back', width=8, pady=5, bg="lightblue", font=('Arial', 15, 'bold'), command=back)
clear_add = Button(add_frame_1, text='Clear', width=8, pady=5, bg="orange", font=('Arial', 15, 'bold'), command=add_clear)
next_add = Button(add_frame_1, text='Next>>', width=8, pady=5, bg="lightgreen", font=('Arial', 15, 'bold'), command=next_add)

back_add.grid(row=0, column=0, ipadx=0, pady=5)
clear_add.grid(row=0, column=1, padx=200, pady=5)
next_add.grid(row=0, column=2, ipadx=0, pady=5)

# subtraction
label_sub_matrix_A = Label(sub_frame, text='Matrix A:', width=10, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
label_sub_matrix_B = Label(sub_frame, text='Matrix B:', width=10, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
matrix_sub_A = Text(sub_frame, width=25, height=8, pady=10, font=('Arial', 20, 'bold'))
matrix_sub_B = Text(sub_frame, width=25, height=8, pady=10, font=('Arial', 20, 'bold'))

label_sub_matrix_A.grid(row=0, column=0, padx=5, pady=10)
label_sub_matrix_B.grid(row=0, column=1, padx=5, pady=10)
matrix_sub_A.grid(row=1, column=0, padx=5, pady=10)
matrix_sub_B.grid(row=1, column=1, padx=5, pady=10)

sub_frame_1 = Frame(sub_frame, bg=sub_bg)
sub_frame_1.grid(row=2, columnspan=2, padx=5, pady=10)

back_sub = Button(sub_frame_1, text='<<Back', width=8, pady=5, bg="lightblue", font=('Arial', 15, 'bold'), command=back)
clear_sub = Button(sub_frame_1, text='Clear', width=8, pady=5, bg="orange", font=('Arial', 15, 'bold'), command=sub_clear)
next_sub = Button(sub_frame_1, text='Next>>', width=8, pady=5, bg="lightgreen", font=('Arial', 15, 'bold'), command=next_sub)

back_sub.grid(row=0, column=0, ipadx=0, pady=5)
clear_sub.grid(row=0, column=1, padx=200, pady=5)
next_sub.grid(row=0, column=2, ipadx=0, pady=5)

# multiplication
label_multi_matrix_A = Label(multi_frame, text='Matrix A:', width=10, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
label_multi_matrix_B = Label(multi_frame, text='Matrix B:', width=10, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
matrix_multi_A = Text(multi_frame, width=25, height=8, pady=10, font=('Arial', 20, 'bold'))
matrix_multi_B = Text(multi_frame, width=25, height=8, pady=10, font=('Arial', 20, 'bold'))

label_multi_matrix_A.grid(row=0, column=0, padx=5, pady=10)
label_multi_matrix_B.grid(row=0, column=1, padx=5, pady=10)
matrix_multi_A.grid(row=1, column=0, padx=5, pady=10)
matrix_multi_B.grid(row=1, column=1, padx=5, pady=10)

multi_frame_1 = Frame(multi_frame, bg=multi_bg)
multi_frame_1.grid(row=2, columnspan=2, padx=5, pady=10)

back_multi = Button(multi_frame_1, text='<<Back', width=8, pady=5, bg="lightblue", font=('Arial', 15, 'bold'), command=back)
clear_multi = Button(multi_frame_1, text='Clear', width=8, pady=5, bg="orange", font=('Arial', 15, 'bold'), command=multi_clear)
next_multi = Button(multi_frame_1, text='Next>>', width=8, pady=5, bg="lightgreen", font=('Arial', 15, 'bold'), command=next_multi)

back_multi.grid(row=0, column=0, ipadx=0, pady=5)
clear_multi.grid(row=0, column=1, padx=200, pady=5)
next_multi.grid(row=0, column=2, ipadx=0, pady=5)

# Dividation
label_div_matrix_A = Label(div_frame, text='Matrix A:', width=10, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
label_div_matrix_B = Label(div_frame, text='Matrix B:', width=10, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
matrix_div_A = Text(div_frame, width=25, height=8, pady=10, font=('Arial', 20, 'bold'))
matrix_div_B = Text(div_frame, width=25, height=8, pady=10, font=('Arial', 20, 'bold'))

label_div_matrix_A.grid(row=0, column=0, padx=5, pady=10)
label_div_matrix_B.grid(row=0, column=1, padx=5, pady=10)
matrix_div_A.grid(row=1, column=0, padx=5, pady=10)
matrix_div_B.grid(row=1, column=1, padx=5, pady=10)

div_frame_1 = Frame(div_frame, bg=div_bg)
div_frame_1.grid(row=2, columnspan=2, padx=5, pady=10)

back_div = Button(div_frame_1, text='<<Back', width=8, pady=5, bg="lightblue", font=('Arial', 15, 'bold'), command=back)
clear_div = Button(div_frame_1, text='Clear', width=8, pady=5, bg="orange", font=('Arial', 15, 'bold'), command=div_clear)
next_div = Button(div_frame_1, text='Next>>', width=8, pady=5, bg="lightgreen", font=('Arial', 15, 'bold'), command=next_div)

back_div.grid(row=0, column=0, ipadx=0, pady=5)
clear_div.grid(row=0, column=1, padx=200, pady=5)
next_div.grid(row=0, column=2, ipadx=0, pady=5)

# Part3 Operation Matrix
frame3 = Frame(window, height=500, width=800, bg=window_bg)

# addition
frame3_add = Frame(window, height=500, width=800, bg=add_bg)
info_label_add = Label(frame3_add, text='Addition of Matrix A + B', width=25, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
result_text_add = Text(frame3_add, width=45, height=8, pady=15, bg='white', fg='black', font=('Arial', 20, 'bold'), relief=RAISED, bd=2, )

frame3_1_add = Frame(frame3_add, bg=add_bg)
back_add_frame3 = Button(frame3_1_add, text='<<Back', width=8, pady=10, bg="lightblue", font=('Arial', 15, 'bold'), command=back_add_result)
exit_add = Button(frame3_1_add, text='Exit', width=8, pady=10, font=('Arial', 15, 'bold'), bg='red', fg="white", command=exit)

info_label_add.pack(pady=10)
result_text_add.pack(pady=10)
back_add_frame3.grid(row=0, column=0, padx=55, pady=5)
exit_add.grid(row=0, column=2, padx=420, pady=5)
frame3_1_add.pack(pady=10)

# subtraction
frame3_sub = Frame(window, height=500, width=800, bg=sub_bg)
info_label_sub = Label(frame3_sub, text='Subtraction of Matrix A - B', width=25, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
result_text_sub = Text(frame3_sub, width=45, height=8, pady=15, bg='white', fg='black', font=('Arial', 20, 'bold'), relief=RAISED, bd=2, )

frame3_1_sub = Frame(frame3_sub, bg=sub_bg)
back_sub_frame3 = Button(frame3_1_sub, text='<<Back', width=8, pady=10, bg="lightblue", font=('Arial', 15, 'bold'), command=back_sub_result)
exit_sub = Button(frame3_1_sub, text='Exit', width=8, pady=10, font=('Arial', 15, 'bold'), bg='red', fg="white", command=exit)

info_label_sub.pack(pady=10)
result_text_sub.pack(pady=10)
back_sub_frame3.grid(row=0, column=0, padx=55, pady=5)
exit_sub.grid(row=0, column=2, padx=420, pady=5)
frame3_1_sub.pack(pady=10)

# Multiplication
frame3_multi = Frame(window, height=500, width=800, bg=multi_bg)
info_label_multi = Label(frame3_multi, text='Multiplication of Matrix A x B', width=25, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
result_text_multi = Text(frame3_multi, width=45, height=8, pady=15, bg='white', fg='black', font=('Arial', 20, 'bold'), relief=RAISED, bd=2, )

frame3_1_multi = Frame(frame3_multi, bg=multi_bg)
back_multi_frame3 = Button(frame3_1_multi, text='<<Back', width=8, pady=10, bg="lightblue", font=('Arial', 15, 'bold'), command=back_multi_result)
exit_multi = Button(frame3_1_multi, text='Exit', width=8, pady=10, font=('Arial', 15, 'bold'), bg='red', fg="white", command=exit)

info_label_multi.pack(pady=10)
result_text_multi.pack(pady=10)
back_multi_frame3.grid(row=0, column=0, padx=55, pady=5)
exit_multi.grid(row=0, column=2, padx=420, pady=5)
frame3_1_multi.pack(pady=10)

# Dividation
frame3_div = Frame(window, height=500, width=800, bg=div_bg)
info_label_div = Label(frame3_div, text='Dividation of Matrix A / B', width=25, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
result_text_div = Text(frame3_div, width=45, height=8, pady=15, bg='white', fg='black', font=('Arial', 20, 'bold'), relief=RAISED, bd=2, )

frame3_1_div = Frame(frame3_div, bg=div_bg)
back_div_frame3 = Button(frame3_1_div, text='<<Back', width=8, pady=10, bg="lightblue", font=('Arial', 15, 'bold'), command=back_div_result)
exit_div = Button(frame3_1_div, text='Exit', width=8, pady=10, font=('Arial', 15, 'bold'), bg='red', fg="white", command=exit)

info_label_div.pack(pady=10)
result_text_div.pack(pady=10)
back_div_frame3.grid(row=0, column=0, padx=55, pady=5)
exit_div.grid(row=0, column=2, padx=420, pady=5)
frame3_1_div.pack(pady=10)

# -----------------------------------------------------#
# Part 2 Inverse Matrix
inv_frame = Frame(window, height=500, width=800, bg=window_bg)
label_inv_matrix = Label(inv_frame, text='Inverse Matrix A', width=20, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
label_inv_matrix_A = Label(inv_frame, text='Matrix A:', width=10, pady=10, bg='lightgreen', fg='black', font=('Arial', 15, 'bold'))
label_inv_matrix_B = Label(inv_frame, text='Inverse A:', width=10, pady=10, bg='lightblue', fg='black', font=('Arial', 15, 'bold'))
matrix_inv_A = Text(inv_frame, width=33, height=11, pady=10, font=('Arial', 14, 'bold'))
matrix_inv_B = Text(inv_frame, width=33, height=11, pady=10, font=('Arial', 14, 'bold'))

label_inv_matrix.grid(row=0, columnspan=2, padx=5, pady=10)
label_inv_matrix_A.grid(row=1, column=0, padx=5, pady=0)
label_inv_matrix_B.grid(row=1, column=1, padx=5, pady=0)
matrix_inv_A.grid(row=2, column=0, padx=5, pady=0)
matrix_inv_B.grid(row=2, column=1, padx=5, pady=0)

inv_frame_1 = Frame(inv_frame, bg=window_bg)
inv_frame_1.grid(row=3, columnspan=2, padx=5, pady=10)

back_inv = Button(inv_frame_1, text='<<Back', width=8, pady=5, bg="lightblue", font=('Arial', 15, 'bold'), command=inv_back)
clear_inv = Button(inv_frame_1, text='Clear', width=8, pady=5, bg="orange", font=('Arial', 15, 'bold'), command=inv_clear)
convt_inv = Button(inv_frame_1, text='Convert>>', width=8, pady=5, bg='lightgreen', fg='black', font=('Arial', 15, 'bold'), command=inv_convt)
exit_inv = Button(inv_frame_1, text='Exit', width=8, pady=5, bg='red', fg='white', font=('Arial', 15, 'bold'), command=exit)

back_inv.grid(row=0, column=0, ipadx=5, pady=5)
clear_inv.grid(row=0, column=1, padx=80, pady=5)
convt_inv.grid(row=0, column=2, padx=80, pady=5)
exit_inv.grid(row=0, column=3, ipadx=5, pady=5)

# -----------------------------------------------------#
# Part 2 Solve linear equation
linear_frame = Frame(window, height=500, width=800, bg=window_bg)
label_linear_matrix = Label(linear_frame, text='Solve linear equation', width=20, pady=15, bg='red', fg='white', font=('Arial', 20, 'bold'))
label_linear_matrix_A = Label(linear_frame, text='Matrix A:', width=10, pady=10, bg='lightgreen', fg='black', font=('Arial', 15, 'bold'))
label_linear_matrix_B = Label(linear_frame, text='Matrix B:', width=10, pady=10, bg='orange', fg='black', font=('Arial', 15, 'bold'))
label_linear_solution = Label(linear_frame, text='Solution', width=10, pady=10, bg='lightblue', fg='black', font=('Arial', 15, 'bold'))
matrix_linear_A = Text(linear_frame, width=22, height=11, pady=10, font=('Arial', 14, 'bold'))
matrix_linear_B = Text(linear_frame, width=22, height=11, pady=10, font=('Arial', 14, 'bold'))
matrix_linear_solution = Text(linear_frame, width=26, height=13, pady=10, font=('Arial', 12, 'bold'))

label_linear_matrix.grid(row=0, columnspan=3, padx=5, pady=10)
label_linear_matrix_A.grid(row=1, column=0, padx=5, pady=0)
label_linear_matrix_B.grid(row=1, column=1, padx=5, pady=0)
label_linear_solution.grid(row=1, column=2, padx=5, pady=0)
matrix_linear_A.grid(row=2, column=0, padx=5, pady=0)
matrix_linear_B.grid(row=2, column=1, padx=5, pady=0)
matrix_linear_solution.grid(row=2, column=2, padx=5, pady=0)

linear_frame_1 = Frame(linear_frame, bg=window_bg)
linear_frame_1.grid(row=3, columnspan=3, padx=5, pady=10)

back_linear = Button(linear_frame_1, text='<<Back', width=8, pady=5, bg="lightblue", font=('Arial', 15, 'bold'), command=linear_back)
clear_linear = Button(linear_frame_1, text='Clear', width=8, pady=5, bg="orange", font=('Arial', 15, 'bold'), command=linear_clear)
convt_linear = Button(linear_frame_1, text='Convert>>', width=8, pady=5, bg='lightgreen', fg='black', font=('Arial', 15, 'bold'), command=linear_convt)
exit_linear = Button(linear_frame_1, text='Exit', width=8, pady=5, bg='red', fg='white', font=('Arial', 15, 'bold'), command=exit)

back_linear.grid(row=0, column=0, ipadx=5, pady=5)
clear_linear.grid(row=0, column=1, padx=80, pady=5)
convt_linear.grid(row=0, column=2, padx=80, pady=5)
exit_linear.grid(row=0, column=3, ipadx=5, pady=5)

# -----------------------------------------------------#
# Part 2 About !
about_frame = Frame(window, height=500, width=800, bg=window_bg)
about_text = Text(about_frame, bg='white', width=60, height=20, pady=10, font=('Arial', 12, 'bold'))

about_frame_1 = Frame(about_frame, height=100, width=800, bg=window_bg)

about_text.pack(pady=10)
about_frame_1.pack()

back_about = Button(about_frame_1, text='<<Back', width=10, pady=5, bg="lightblue", font=('Arial', 15, 'bold'), command=about_back)
contact = Button(about_frame_1, text='Contact Me>>', width=15, pady=5, bg="lightgreen", font=('Arial', 15, 'bold'), command=contact)

back_about.grid(row=0, column=0, padx=100, pady=5)
contact.grid(row=0, column=1, padx=100, pady=5)

window.mainloop()