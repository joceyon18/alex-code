#          Homework for session 3:
#
#     CONTEXT:
#           You're a security guard at a club. There's a private party going on tonight, members only. When someone
#           comes to the door, ask them for their name and check it against your list. If they're on the list, let
#           them in. If they're not on the list, kick them out.



def main():
    line_of_people_at_door = ["Bob", "Jimbo", "Todd", "Frank", "Sam", "Rachel", "Gregory", "Gary", "Zack"]

    for person_at_door in line_of_people_at_door: #instead of print you can do anything with person sooooo check
       
        answer=check_name(person_at_door)#answer is the result of check_name if they're on the list or not. 
        # you only use answer(as a variable) = if you want the result of the anwer returned back to you 

        if answer == True:
            enter_club(person_at_door)#putting person here gives one variable because on line 40 we have name there

        elif answer == False:
            kick_out_of_club(person_at_door)



    # TODO: 1. for each person in the list above, call check_name and see if they can enter the club
    # TODO: 2. if check_name returns True, let them in to the club by calling the enter_club function
    # TODO: 3. if check_name returns False, kick them out of the club by calling kick_out_of_club function


def check_name(name):
    whitelist = ["Alex", "Sam", "Zack", "Panda", "H", "Hassan", "Rachel"]

    for person_on_whitelist in whitelist:
        if name == person_on_whitelist:
            return True
        # this didn't work because when running the main list compared to the whitelist
        # it would compare the first name on the whitelist first and then exiting because Alex in the whitelist
        # nowhere in the main list so it continued to be false 
        # else:
        #     return False

    # TODO: 1a. ask the user for their name and check it against the whitelist
    # TODO 1b. return True if they can come in and False if they can't
    return False



 
def enter_club(name):# if you use enter clube you need () 
    print(f"{name}, you can go in. Have a good time.")


def kick_out_of_club(name):
    print(f"{name}, you're not on the list. Get the fuck out.")


if __name__ == "__main__": 
    main()
uhuhuhuh