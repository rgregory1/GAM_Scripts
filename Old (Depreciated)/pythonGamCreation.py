import os
import sys
from itertools import islice

grade_book = {'6': 24, '5': 25, '4': 26, '3':27, '2':28, '1':29}

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        #choice = choice.strip()
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

print("Starting...")
#result_test = os.popen("gam info user jhavens").read()

question_1 = "Do you wish to create NEW USER?"
choice_1 = query_yes_no(question_1, default="yes")
if choice_1:

    question_2 = "Is this a Staff Member?"
    choice_2 = query_yes_no(question_2, default="yes")
    if choice_2:

        first_name = input('First Name: ')
        last_name = input('Last Name: ')

        NEWFIRST_I_L = first_name[0].lower()
        NEWLAST_I_L = last_name[0].lower()
        NEWUSER = NEWFIRST_I_L + last_name.lower()
        NEWEMAIL = NEWUSER + "@fnwsu.org"
        NEWDEFAULTPW = first_name[0].lower() + last_name[0].lower() + "3456789"
        input_1 = "gam create user "+NEWUSER+" firstname "+first_name+" lastname "+last_name+" password "+NEWDEFAULTPW+" changepassword off org '/Swanton-All/Swan Staff-All'"
        #result_1 = os.popen(input_1).read()
        #print(result_1)
    else:
        print ("no staff member")

        question_3 = "Is this a Student?"
        choice_3 = query_yes_no(question_3, default="yes")
        if choice_3:

            first_name = input('First Name: ')
            last_name = input('Last Name: ')
            grade = input('Grade: ')
            grad_year = grade_book[grade]

            NEWFIRST_I_L = first_name[0].lower()
            NEWLAST_I_L = last_name[0].lower()
            NEWUSER = str(grad_year) + last_name.lower() + NEWFIRST_I_L
            NEWEMAIL = NEWUSER + "@fnwsu.org"
            NEWDEFAULTPW = first_name[0].lower() + last_name[0].lower() + "3456789"
            input_1 = "gam create user "+NEWUSER+" firstname "+first_name+" lastname "+last_name+" password "+NEWDEFAULTPW+" changepassword off org '/Swanton-All/Swan Students-All/Swan Grade "+str(grade)+"-20"+str(grad_year)+"'"
            #result_1 = os.popen(input_1).read()
            #print(result_1)

        else:
            print ("no student")

    print("Newly Created User Info:")
    print("Name: "+first_name+" "+last_name)
    print("User: "+NEWUSER)
    print("Email: "+NEWEMAIL)
    print("Password: "+NEWDEFAULTPW)

else:
    print ("no NEW USER creation")
