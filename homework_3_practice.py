#make a list of people who will graduate collge off of their final and seperate them from the ones who failed

def main():
   students_in_school = ["Alex", "Sam", "Bob", "Arjun", "Bianca", "Beth", "Stephanie", "Booker", "Goldie"]

   for student_in_school in students_in_school:

        result= passing_list(student_in_school)

        if result == True:
            return if_passed(student_in_school)

        elif result == False:
            return if_failed(student_in_school)





def passing_list(name):
    passed= ["Alex", "Sam", "Booker"]

    for student_that_passed in passed:
        if name == student_that_passed:
            return True
 
    return False

def if_passed(name):

    print(f"{name}, you may go to the next grade up! you've passed ")

def if_failed(name):
    print(f"{name}, sorry you've failed you cannot move forward")


if __name__ == "__main__": 
    main()


