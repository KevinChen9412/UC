"""python project: display the energy comsumption or share of
renewables in electricity production based on user selection"""
import csv
from matplotlib import pyplot as plt
from tkinter import *
from tkinter.ttk import *
import pandas as pd 
from PIL import ImageTk, Image #for display image
import seaborn as sns #for regession

def my_flat(l):
    """This is a helper fuction to prepare the data for regression line"""
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    return flat_list
        
def plot1():
    """plot a line chart of power consumption of  one country"""
    global country_combobox
    filename = 'total.csv'
    country = country_combobox.get() #user selected country
    data = pd.read_csv("total.csv",usecols=["Year",country]) #subset of data 
    x = data.iloc[1:,[0]] #select first column which contains time
    y = data.iloc[1:,[1]] #select second column which contains data
    plt.plot(x,y)
    plt.ylim(ymin=0)
    plt.title("Total Energy Consumption of {}".format(country))
    plt.xlabel("Year")
    plt.ylabel("Energy consumption (Mtoe)")
    plt.show()
    
def plot1_regression():
    """plot a line chart of power consumption of one country with regression line"""
    global country_combobox
    filename = 'total.csv'
    country = country_combobox.get()
    data = pd.read_csv("total.csv",usecols=["Year",country]) 
    x = data.iloc[1:,[0]]
    y = data.iloc[1:,[1]]
    plt.plot(x,y)
    plt.ylim(ymin=0)
    plt.title("Total Energy Consumption of {}".format(country))
    plt.xlabel("Year")
    plt.ylabel("Energy consumption (Mtoe)")
    #extract data from panda data.frame
    x_flat = my_flat(x.values.tolist())
    y_flat = my_flat(y.values.tolist())
    #regression line
    sns.regplot(x=x_flat,y=y_flat,data=data, fit_reg=True)
    plt.show()
    
def plot2():
    """plot a line chart of power consumption of  multiple countries"""
    global chkValue1, chkValue2, chkValue3, chkValue4
    selected = ["Year"]
    G7 = ["Canada", "France", "Germany", "Italy", "Japan", "UK", "USA"]
    BRICS = ["China", "India", "Russia", "South Africa", "Brazil"]
    #following section is used to generate a list of countries
    if chkValue1.get():
        selected = selected + G7
    if chkValue2.get():
        selected = selected + BRICS
    if chkValue3.get():
        selected.append("World")
    if chkValue4.get():
        selected.append("New Zealand")
        
    data = pd.read_csv("total.csv",usecols=selected) 
    x = data.iloc[1:,[0]]
    #one line for each country
    for i in range(1,len(selected)):
        y = data.iloc[1:,[i]]
        plt.plot(x,y, label=data.columns.values[i])
    plt.ylim(ymin=0)
    plt.title("Total Energy Consumption")
    plt.xlabel("Year")
    plt.ylabel("Energy consumption (Mtoe)")
    plt.legend(loc='upper left',prop={'size': 6})
    plt.show()

def plot3():
    """plot a line of renewable energy share of one contry"""
    global country_combobox
    filename = 'clean.csv'
    country = country_combobox.get()
    data = pd.read_csv("clean.csv",usecols=["Year",country]) 
    x = data.iloc[1:,[0]]
    y = data.iloc[1:,[1]]
    plt.plot(x,y)
    plt.ylim(ymin=0)
    plt.title("Share of renewables in electricity production of {}".format(country))
    plt.xlabel("Year")
    plt.ylabel("% in electricity production")
    plt.show()

def plot3_regression():
    """plot a line of renewable energy share of one contry with regression line"""
    global country_combobox
    filename = 'clean.csv'
    country = country_combobox.get()
    data = pd.read_csv("clean.csv",usecols=["Year",country]) 
    x = data.iloc[1:,[0]]
    y = data.iloc[1:,[1]]
    plt.plot(x,y)
    plt.ylim(ymin=0)
    plt.title("Share of renewables in electricity production of {}".format(country))
    plt.xlabel("Year")
    plt.ylabel("% in electricity production")
    x_flat = my_flat(x.values.tolist())
    y_flat = my_flat(y.values.tolist())
    sns.regplot(x=x_flat,y=y_flat,data=data, fit_reg=True)
    plt.show()

def plot4():
    """plot a line of renewable energy share of multiple contries"""
    global chkValue1, chkValue2, chkValue3, chkValue4
    selected = ["Year"]
    G7 = ["Canada", "France", "Germany", "Italy", "Japan", "UK", "USA"]
    BRICS = ["China", "India", "Russia", "South Africa", "Brazil"]
    if chkValue1.get():
        selected = selected + G7
    if chkValue2.get():
        selected = selected + BRICS
    if chkValue3.get():
        selected.append("World")
    if chkValue4.get():
        selected.append("New Zealand")
        
    data = pd.read_csv("clean.csv",usecols=selected) 
    x = data.iloc[1:,[0]]
    for i in range(1,len(selected)):
        y = data.iloc[1:,[i]]
        plt.plot(x,y, label=data.columns.values[i])
    plt.ylim(ymin=0)
    plt.title("Share of renewables in electricity production")
    plt.xlabel("Year")
    plt.ylabel("% in electricity production)")
    plt.legend(loc='upper left',prop={'size': 6})
    plt.show()
    
def single_display():
    """decide which function to recall when Display Single button is clicked"""
    global topic_combobox, chkreg
    if topic_combobox.get() == "Total energy consumption":
        if chkreg.get():
            plot1_regression()
        if chkreg.get() == False:
            plot1()
    if topic_combobox.get() == "Share of renewables in electricity production":
        if chkreg.get():
            plot3_regression()
        if chkreg.get() == False:
            plot3()
            
def multi_display():
    """decide which function to recall when Display Multiple button is clicked"""
    global topic_combobox
    if topic_combobox.get() == "Total energy consumption":
        plot2()
    if topic_combobox.get() == "Share of renewables in electricity production":
        plot4() 
    
    
def main():
    """Set up the GUI"""
    global country_combobox, topic_combobox, chkValue1, chkValue2, chkValue3, chkValue4, chkreg
    window = Tk()
    window.geometry('300x650')
    window.title("World Energy")
    
    topic_label = Label(window, text = 'Select a Topic')
    topic_label.grid(row=0, column=0)
    
    topic_choices =["Total energy consumption", "Share of renewables in electricity production"]
    topic_combobox = Combobox(window, values=topic_choices,width=35)
    topic_combobox.set("Total energy consumption")
    topic_combobox.grid(row=1, column=0, padx=20, pady=30)
    
    country_label = Label(window, text='Select a country')
    country_label.grid(row=2, column=0)
    
    country_choices = ["Canada", "China", "France", "Germany", "India", "Italy",
    "Japan", "New Zealand", "Russia", "South Africa", "UK", "USA", "World"]
    country_combobox = Combobox(window,
                              values=country_choices,
                              font=("Arial", 10))
    country_combobox.set('World')
    country_combobox.grid(row=3, column=0, padx=20, pady=30)
    
    chkreg = BooleanVar()
    chkreg.set(False)
    check0 = Checkbutton(window, text ="Add Linear Regression", variable=chkreg)
    check0.grid(row=4, column=0)
    
    chkValue1 = BooleanVar()
    chkValue1.set(False)
    check1 = Checkbutton(window, text ="G7", variable=chkValue1)
    check1.grid(row=6, column=0)
    
    chkValue2 = BooleanVar()
    chkValue2.set(True)
    check2 = Checkbutton(window, text ="BRICS", variable=chkValue2)
    check2.grid(row=7, column=0)
    
    chkValue3 = BooleanVar()
    chkValue3.set(False)
    check3 = Checkbutton(window, text ="World", variable=chkValue3)
    check3.grid(row=9, column=0)
    
    chkValue4 = BooleanVar()
    chkValue4.set(False)
    check4 = Checkbutton(window, text ="New Zealand", variable=chkValue4)
    check4.grid(row=8, column=0)
    
    display_button = Button(window, text="Display Single", command=single_display)
    display_button.grid(row=5, column=0,pady=10)
    display_button2 = Button(window, text="Display Multiple", command=multi_display)
    display_button2.grid(row=10, column=0,pady=10)
    #exit button
    exit_button = Button(window, text="Exit", command=window.destroy)
    exit_button.grid(row=11, column=0,pady=10)
    
    source_label = Label(window, text = 'Data source')
    source_label.grid(row=12, column=0)
    #display a image
    img = ImageTk.PhotoImage(Image.open("logo.png"))
    picture = Label(window, image = img)
    picture.grid(row=13, column=0,pady=10)
    
    window.mainloop()

main()
