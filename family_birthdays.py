import random

birthdays = {
"Sherry Guzha":"05/20/1962",
"Shungu Guzha Magaya":"05/15/1979",
"Primrose Vimbai Guzha":"10/06/1982",
"Monica Guzha Gadaga":"01/11/1984",
"Shorayi Spencer Guzha":"07/03/1987",
"Tafadzwa Tevin Togo":"02/26/1995",
"Tariro Louisa Togo":"11/01/1997",
"Rudo Sabeka":"11/06/1987",
"Patrick Wiri Ndlovu":"01/15/1945"
}

print("")
print("Welcome to my family birthday dictionary. Here are our names: ")
for name in birthdays:
    print(name)

print("Whose birthday do you want to look up? ")
name = str(input())

# Birthday calculator
#import datetime module to manipulate dates

import datetime

def age_calculator(birthday):
    birthday = datetime.datetime.strptime(birthday, "%m/%d/%Y")
    date_today = datetime.datetime.now()

    if birthday.month > date_today.month:
        age = date_today.year - birthday.year
    else:
        age = date_today.year - birthday.year

    return age

# Current age = age_calculator(birthdays[name])
if name in birthdays:
    current_age = age_calculator(birthdays[name])
    print("{}'s birthday is {}.".format(name, birthdays[name]))
    print("{} is now {} years old".format(name, current_age))
else:
    print("Sadly, we do not have {}'s birthday.".format(name))
