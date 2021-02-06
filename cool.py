from tkinter import *

root=Tk()

root.title("Fibonacci series")
root.geometry("400x400")

label_series = Label(root, text="Fibonacci Series")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
    num = 10
    
    first_num = 0
    second_num = 1
    sum = 1
    counter = 1
    
    while(counter <= num):
        
        label_series['text'] += str(sum) + ","
        counter = counter + 1
        first_num = second_num
        second_num = sum
        sum = first_num + second_num
        
        label_flower['text'] = "Flower is fully bloomed"
        label_spiral['text'] = "Spirals in the right direction are " + str(first_num) + "and spirals in the left dirction are " + str(second_num) + ".\n Total spirals are " + str(sum)
btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)

btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()

root.mainloop()
