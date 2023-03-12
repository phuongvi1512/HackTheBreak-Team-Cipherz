from typing import NamedTuple, List 
import numpy as np
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
from pandas import *

def start_question():
    print("Hello User! You're about to move to a new country for work and you're interested to know about the unemployment rate in that country!")
    print("Your options are: 1. Canada  2. United States  3. Mexico")

    choice = 0

    while choice not in [1, 2, 3]:
        try:
            choice = int(input("Which country are you interested in examining? Please select 1, 2, or 3\n"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            countryName('Canada')
        elif choice == 2:
            countryName('United_States')
        elif choice == 3:
            countryName('Mexico')
        else:
            print("Invalid choice, please try again")

def countryName(s):
    data = read_csv("data.csv")

    years = data['Year'].tolist()
    unem = data[s].tolist()

    plt.scatter(years, unem)

    plt.xlabel("Years")

    plt.ylabel("Unemployment rate")

    name = "Unemployment rate Over the Years in " + s
    plt.title(name)

    plt.show()

start_question()
