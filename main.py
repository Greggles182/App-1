from tkinter import *
from replit import db
import tkinter.messagebox as box
import matplotlib.pyplot as plt
import csv
from pickle import *
import time
import os
#db["Filename"] = "value"
var = db["Filename"]
main = Tk()
def Append():
	new_window2 = Toplevel(main)
	Text = Text(new_window2)
	def destroy():
		#start
		var1 = Text.get
		file = open( var , 'a' )
		print('opened file')
		file.write(var1)
		print('Dumped the data')
		print(input.get())
		file.close()
		print('closed')
		#end
		dialog()
		new_window2.destroy()
	
	#Window has no content  - Fix!
	new_window2.geometry('400x400')
	new_window2.title('Append')
	new_window2.resizable(False, False)
	btn4 = Button(new_window2, text = 'Exit and append', command = destroy,)
	btn4.pack()
	def dialog():
		box.showinfo('Done','The Data has been added to the end to the file')
		label = Label( new_window2 , text = 'Enter text here to add to end of file' )
  
	Text.pack(padx = 20, pady = 20)
	label.pack( padx = 200 , pady = 50 )
	#btn.place(y=22, x=1)
	#btn.grid(row=1,column=1)
	new_window2.mainloop()
def Plot():
	#The x and y Variable
  x = []
  y = []
  #open the file
  with open(var, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
      x.append(int(row[0]))
      y.append(int(row[1]))
  plt.plot(x,  y, marker='o')
  plt.title('Data from the CSV File: People and Expenses')
  plt.xlabel('Number of People')
  plt.ylabel('Expenses')
  #show the plot
  plt.show()



def dialog():
    box.showinfo(
        'FileInfo', 'The directory your .csv file should be in is ' +
        os.getcwd() + ' and the filename should be ' + db["Filename"])


def Name():
    def Name1():
        var = entry.get()
        db["Filename"] = var
        box.showinfo(
            'Success',
            'The Name the file should have has been changed to ' + var)
        new_window.destroy()
    def Reset():
        db["Filename"] = "example.csv"
        new_window.destroy()
    new_window = Toplevel(main)
    new_window.geometry('500x100')
    new_window.title(
        'Please enter a filename')
    new_window.resizable(False, False)
    label = Label(new_window, text='Enter a filename and click Done. If you want to reset to Deafault click Reset.')
    label.pack()
    entry = Entry(new_window)
    entry.pack()
    btn3 = Button(new_window, text='Done',
    command=Name1)
    btn4 = Button(new_window, text='Reset', command = Reset)
    btn4.pack()
    btn3.pack()
    var = entry.get()
    new_window.mainloop()


main.geometry('500x500')
main.title('Main Plotter Window')
btn = Button(main, text='Plot', command=Plot)
btn.pack(padx=20, pady=20)
btn2 = Button(main,text='What directory should my file be in and what should it be called?',
    command=dialog)
btn2.pack(padx=20, pady=20)
btn1 = Button(main, text='Change filename', command=Name)
btn1.pack(padx=20, pady=20)
btn_Append = Button(main, text='Add text to end of current file', command = Append)
btn_Append.pack()
main.mainloop()
from tkinter import *
from replit import db
import tkinter.messagebox as box
#import matplotlib.pyplot as plt
#import csv
from pickle import *
import time
import os
var = db["Filename"]
main = Tk()
def Append():
    def destroy():
      var1 = Text.get
      file = open( var , 'a' )
      print('opened file')
      file.write(var1)
      print('Dumped the data')
      print(input.get())
      file.close()
      print('closed')
      dialog()
      new_window2.destroy()
    new_window2 = Toplevel(main)
    new_window2.geometry('400x400')
    new_window2.title('Append')
    new_window2.resizable(False, False)
    btn4 = Button(new_window2, text = 'Exit and append', command = destroy,)
    btn4.pack()
    def dialog():
        box.showinfo('Done','The Data has been added to the end to the file')
    label = Label( new_window2 , text = 'Enter text here to add to end of file' )
    Text = Text(new_window2)
    Text.pack(padx = 20, pady = 20)
    label.pack( padx = 200 , pady = 50 )
    #btn.place(y=22, x=1)
    #btn.grid(row=1,column=1)
    
    new_window2.mainloop()



def Plot():
  x = []
  y = []
  #open the file
  with open('csvfile1.txt', 'r') as csvfile:
      plots = csv.reader(csvfile, delimiter=',')
      for row in plots:
          x.append(int(row[0]))
          y.append(int(row[1]))


  plt.plot(x,  y, marker='o')

  plt.title('Data from the CSV File: People and Expenses')

  plt.xlabel('Number of People')
  plt.ylabel('Expenses')

  plt.show()


def dialog():
    box.showinfo(
        'FileInfo', 'The directory your .csv file should be in is ' +
        os.getcwd() + ' and the filename should be ' + db["Filename"])


def Name():
    def Name1():
        var = entry.get()
        db["Filename"] = var
        box.showinfo(
            'Success',
            'The Name the file should have has been changed to ' + var)
        new_window.destroy()
    def Reset():
        db["Filename"] = "example.csv"
        new_window.destroy()
    new_window = Toplevel(main)
    new_window.geometry('500x100')
    new_window.title(
        'Please enter a filename')
    new_window.resizable(False, False)
    label = Label(new_window, text='Enter a filename and click Done. If you want to reset to Deafault click Reset.')
    label.pack()
    entry = Entry(new_window)
    entry.pack()
    btn3 = Button(new_window, text='Done',
    command=Name1)
    btn4 = Button(new_window, text='Reset', command = Reset)
    btn4.pack()
    btn3.pack()
    var = entry.get()
    new_window.mainloop()


main.geometry('500x500')
main.title('Main Plotter Window')
btn = Button(main, text='Plot', command=Plot)
btn.pack(padx=20, pady=20)
btn2 = Button(
    main,
    text='What directory should my file be in and what should it be called?',
    command=dialog)
btn2.pack(padx=20, pady=20)
btn1 = Button(main, text='Change filename', command=Name)
btn1.pack(padx=20, pady=20)
btn_Append = Button(main, text='Add text to end of current file', command = Append)
btn_Append.pack()
main.mainloop()