from pprint import pprint
# dictionary  {}

def main():
    # run_club_example()
    # simple_phone_book_example()

    employees={
        "jake":{
            "favorite_food":"pizza", 
            "age":45,
            "money":3,
            "salary":145000,

        },
        "todd":{
            "favorite_food":"rice", 
            "age":40,
            "money":67,
            "salary":25000,


        },
        "peter":{
            "favorite_food":"jelly", 
            "age":37,
            "money":34,
            "salary":34000,
        },
        "forreal":{
            "favorite_food":"pickles", 
            "age":22,
            "money":0,
            "salary":37,

        },
    }

    hire_employee(employees, "bob", 37, "sushi", 10)
    hire_employee(employees, "sally,", 21, "eatting ass", 200)
    hire_employee(employees, "jim",30, "duck", 200000)

    pprint(employees) 

# goal if the empolyee is too young or eat ass then return false
# if they pass our requirements then we want them to pass a dictionary for our new empplyee
def build_employee_folder(name, age, favorite_food, salary):
    print(f"{name} is {age} years old and loves {favorite_food}")

    if age<25:
        return False

    elif favorite_food == "eating ass":
        return False

    else:
        return {
            "favorite_food": favorite_food, 
            "age": age,
            "money": 0,
            "salary": salary,
        }


def hire_employee(all_employees, name, age, favorite_food, salary):
    new_employee_folder = build_employee_folder(name, age, favorite_food, salary)

    if new_employee_folder == False:
        print(f"We cannot hire {name}.")
    else:
        all_employees[name] = new_employee_folder


def run_payroll(employees):
    pass






# ================= OLDER EXAMPLES =================
def simple_phone_book_example():
    phone_book={
        "sam":"1234567890",
        "zack":"0987654321",
        "sam":"5"
        
    }
    print(phone_book["sam"])
    phone_book["alex"]="9717089865"# doing this adds alex into the origninal phonebook
    print(phone_book)

    phone_book["sam"]="bootycheeks"
    print(phone_book)
    

def run_club_example():
    line_of_people_at_door = ["Gregory", "Gary", "Zack", "marley","jessica","kendal"]

    for person_at_door in line_of_people_at_door:
        answer=check_name_using_dictionary(person_at_door)

        if answer == True:
            enter_club(person_at_door)

        elif answer == False:
            kick_out_of_club(person_at_door)


def check_name_using_dictionary(name):
    # using a dictionary, checking if name is in black_list is EASY and IMMEDIATE even if there are 10,000 people
    black_list= {
        "marley": "becasue eating ass",
        "jessica": "because shot boyfriend",
        "kendal": "false advertising",
    }

    if name in black_list:
        return False

    else:
        return True


def check_name_using_list(name):
    # using a list / array, if we had 10,000 people we would have to check them one by one and it would be SLOW
    black_list = ["marley", "jessica", "kendal"]

    for banned_person in black_list:
        if name == banned_person:
            return False

    return True


 
def enter_club(name):# if you use enter clube you need () 
    print(f"{name}, you can go in. Have a good time.")


def kick_out_of_club(name):
    print(f"{name}, you're not on the list. Get the fuck out.")


if __name__ == "__main__": 
    main()
