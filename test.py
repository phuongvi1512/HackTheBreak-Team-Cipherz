from typing import NamedTuple, List
import numpy as np
import matplotlib as mpl
from pandas import read_csv
import pandas as pd

mpl.use('tkagg')
import matplotlib.pyplot as plt


def start_question():
    print("Hello User! You're about to move to a new country for work and you're interested to know about the unemployment rate in that country!")
    print("Your options are: 1. Canada 2. United States 3. Mexico")


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


def get_average_unemployment_rate(data, country):
    return data[country].mean()

def plot_unemployment(data, countries):
    country_names = ['Canada', 'United_States', 'Mexico']
    country_codes = [1, 2, 3]
    selected_countries = [country_names[c-1] for c in countries]
    unem = [get_average_unemployment_rate(data, country_names[c-1]) for c in countries]
    colors = ['red', 'blue', 'green']
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(selected_countries, unem, color=colors[:len(unem)], width=0.5)
    ax.set_xlabel("Countries")
    ax.set_ylabel("Unemployment rate")
    title = "Average Unemployment rate in " + ", ".join(selected_countries)
    ax.set_title(title)
    ax.set_ylim([0, max(unem)+1])
    for i, v in enumerate(unem):
        ax.text(i, v+0.2, str(round(v, 2)), ha='center', fontsize=10)
    plt.show()
    print("Thank you for using this program!")


start_question()
data = read_csv("data.csv")

while True:
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
            continue

        while True:
            repeat = input("Do you want to see the scatter diagram for another country? Enter 'yes' or 'no': ")
            if repeat.lower() == 'yes':
               break
            elif repeat.lower() == 'no':
               break
            else:
                print("Invalid answer. Please enter 'yes' or 'no'.")
                
                
    if repeat.lower() == 'no':
        break

detailed_analysis = input("Do you want to see a more detailed analysis between countries? Enter 'yes' or 'no': ")

if detailed_analysis.lower() == 'yes':
    num_countries = int(input("How many countries would you like to include in the analysis? Enter a number: "))
    countries = []

    if num_countries == 3:
        countries = [1, 2, 3]
    elif num_countries == 2:
        while len(countries) < num_countries:
            try:
                country_choice = int(input(f"Select country {len(countries)+1}: 1 for Canada, 2 for US, 3 for Mexico: "))
                if country_choice not in [1, 2, 3]:
                    print("Invalid choice. Please select 1, 2, or 3.")
                elif country_choice in countries:
                    print("Country already selected. Please select another country.")
                else:
                    countries.append(country_choice)
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif num_countries == 1:
        while len(countries) < num_countries:
            try:
                country_choice = int(input("Select a country: 1 for Canada, 2 for US, 3 for Mexico: "))
                if country_choice not in [1, 2, 3]:
                    print("Invalid choice. Please select 1, 2, or 3.")
                elif country_choice in countries:
                    print("Country already selected. Please select another country.")
                else:
                    countries.append(country_choice)
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("Invalid number of countries. Please select 1, 2, or 3.")
        exit()

    plot_unemployment(data, countries)

else:
    print("Thank you for using this program!")





