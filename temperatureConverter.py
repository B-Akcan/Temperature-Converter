import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


def fh_to_cel(n):
    return (n-32)*5/9

def fh_to_kel(n):
    return (n-32.0)*5/9 + 273.15

def cel_to_fh(n):
    return n*9/5+32

def cel_to_kel(n):
    return n+273.15

def kel_to_cel(n):
    return n-273.15

def kel_to_fh(n):
    return (n-273.15)*9/5+32

def result1(n):
    res = round(fh_to_cel(entry1_var.get()), 2)
    showinfo(title="Result", message=f"The result is {res} celcius.")

def result2(n):
    res = round(fh_to_kel(entry2_var.get()), 2)
    if res >= 0:
        showinfo(title="Result", message=f"The result is {res} kelvin.")
    else:
        showinfo(title="Error", message="Please enter a valid value.")

def result3(n):
    res = round(cel_to_fh(entry3_var.get()), 2)
    showinfo(title="Result", message=f"The result is {res} fahrenheit.")

def result4(n):
    res = round(cel_to_kel(entry4_var.get()), 2)
    if res >= 0:
        showinfo(title="Result", message=f"The result is {res} kelvin.")
    else:
        showinfo(title="Error", message="Please enter a valid value.")

def result5(n):
    res = round(kel_to_cel(entry5_var.get()), 2)
    showinfo(title="Result", message=f"The result is {res} celcius.")

def result6(n):
    res = round(kel_to_fh(entry6_var.get()), 2)
    showinfo(title="Result", message=f"The result is {res} fahrenheit.")


root = tk.Tk()
root.geometry("450x300+50+50")
root.resizable(False, False)
root.title("Temperature Converter")
root.iconbitmap("termometer.ico")
root["bg"] = "black"

name = tk.Label(root, text="Temperature Converter - made by Batuhan Akçan", bg="black", fg="white", font=("Gabriola", 20))
name.place(x=5, y=5)

lbl1 = tk.Label(root, text="Fahrenheit to Celcius: ", bg="black", fg="white")
lbl1.place(x=5, y=60)

entry1_var = tk.DoubleVar()
entry1 = tk.Entry(root, textvariable=entry1_var, bg="white", bd=2, justify=tk.CENTER)
entry1.place(x=130, y=60)
entry1.bind("<Return>", result1)

bttn1 = ttk.Button(root, text="Enter", width=5, takefocus=False)
bttn1.place(x=260, y=57)
bttn1.bind("<Button>", result1)
style1 = ttk.Style()
style1.configure("style1", )

lbl2 = tk.Label(root, text="Fahrenheit to Kelvin: ", bg="black", fg="white")
lbl2.place(x=5, y=100)

entry2_var = tk.DoubleVar()
entry2 = tk.Entry(root, textvariable=entry2_var, bg="white", bd=2, justify=tk.CENTER)
entry2.place(x=130, y=100)
entry2.bind("<Return>", result2)

bttn2 = ttk.Button(root, text="Enter", width=5, takefocus=False)
bttn2.place(x=260, y=97)
bttn2.bind("<Button>", result2)

lbl3 = tk.Label(root, text="Celcius to Fahrenheit: ", bg="black", fg="white")
lbl3.place(x=5, y=140)

entry3_var = tk.DoubleVar()
entry3 = tk.Entry(root, textvariable=entry3_var, bg="white", bd=2, justify=tk.CENTER)
entry3.place(x=130, y=140)
entry3.bind("<Return>", result3)

bttn3 = ttk.Button(root, text="Enter", width=5, takefocus=False)
bttn3.place(x=260, y=137)
bttn3.bind("<Button>", result3)

lbl4 = tk.Label(root, text="Celcius to Kelvin: ", bg="black", fg="white")
lbl4.place(x=5, y=180)

entry4_var = tk.DoubleVar()
entry4 = tk.Entry(root, textvariable=entry4_var, bg="white", bd=2, justify=tk.CENTER)
entry4.place(x=130, y=180)
entry4.bind("<Return>", result4)

bttn4 = ttk.Button(root, text="Enter", width=5, takefocus=False)
bttn4.place(x=260, y=177)
bttn4.bind("<Button>", result4)

lbl5 = tk.Label(root, text="Kelvin to Celcius: ", bg="black", fg="white")
lbl5.place(x=5, y=220)

entry5_var = tk.DoubleVar()
entry5 = tk.Entry(root, textvariable=entry5_var, bg="white", bd=2, justify=tk.CENTER)
entry5.place(x=130, y=220)
entry5.bind("<Return>", result5)

bttn5 = ttk.Button(root, text="Enter", width=5, takefocus=False)
bttn5.place(x=260, y=217)
bttn5.bind("<Button>", result5)

lbl6 = tk.Label(root, text="Kelvin to Fahrenheit: ", bg="black", fg="white")
lbl6.place(x=5, y=260)

entry6_var = tk.DoubleVar()
entry6 = tk.Entry(root, textvariable=entry6_var, bg="white", bd=2, justify=tk.CENTER)
entry6.place(x=130, y=260)
entry6.bind("<Return>", result6)

bttn6 = ttk.Button(root, text="Enter", width=5, takefocus=False)
bttn6.place(x=260, y=257)
bttn6.bind("<Button>", result6)


root.mainloop()