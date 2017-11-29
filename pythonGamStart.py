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

print("Python v1.0")
print("Starting...")
result_test = os.popen("gam info user jswanton").read()

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
        gam_input = "gam create user "+NEWUSER+" firstname "+first_name+" lastname "+last_name+" password "+NEWDEFAULTPW+" changepassword off org '/Swanton-All/Swan Staff-All'"
        result_1 = os.popen(gam_input).read()
        print(result_1)

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
        gam_input = "gam create user "+NEWUSER+" firstname "+first_name+" lastname "+last_name+" password "+NEWDEFAULTPW+" changepassword off org '/Swanton-All/Swan Students-All/Swan Grade "+str(grade)+"-20"+str(grad_year)+"'"
        result_1 = os.popen(gam_input).read()
        print(result_1)

    print()
    print("Newly Created User Info:")
    print("Name: "+first_name+" "+last_name)
    print("User: "+NEWUSER)
    print("Email: "+NEWEMAIL)
    print("Password: "+NEWDEFAULTPW)
    print()

    gam_input = "gam info user "+NEWUSER
    result_1 = os.popen(gam_input).read()
    print(result_1)
    print()

##########################################################
##########################################################
##########################################################

question = "Do you wish to modify EXISTING USER?"
choice = query_yes_no(question, default="yes")
if choice:
    existing_user_name = input('Username? (just user - no email) ')
    existing_email = existing_user_name + "@fnwsu.org"
    print("Info:")
    print()
    gam_input = "gam info user "+existing_user_name
    result_1 = os.popen(gam_input).read()
    result_2 = result_1
    head = list(islice(result_1.splitlines(), 19))
    for x in head:
        print(x)

    ## Groups

    group_list= []
    group_dictionary= {}
    for x in result_1.splitlines():
        if "@" in x and "User" not in x:
            a = x.split('<',1)[-1]
            b = a.replace(">", "")
            group_list.append(b)

    for x in group_list:
        gam_input = "gam info group "+x
        result_1 = os.popen(gam_input).read()
        for y in result_1.splitlines():
            if existing_email in y:
                w = y.split(':',1)[0].strip()
                group_dictionary[x] = w
    print()
    print("Groups:")
    for x in group_dictionary:

        print(group_dictionary[x], x)

    #variable creation
    for x in result_2.splitlines():
        if "First Name:" in x:
            first_name = x.split(':',1)[-1].strip()
        if "Last Name:" in x:
            last_name = x.split(':',1)[-1].strip()
        if "Must Change Password:" in x:
            PW_Flag = x.split(':',1)[-1].strip()
        if "Account Suspended:" in x:
            account_suspended = x.split(':',1)[-1].strip()
    NEWFIRST_I_L = first_name[0].lower()
    NEWLAST_I_L = last_name[0].lower()
    DEFAULTPW = first_name[0].lower() + last_name[0].lower() + "3456789"

    if account_suspended == "True":
        print()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("WARNING: ACCOUNT IS SUSPENDED")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print()
    if PW_Flag == "True":
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("WARNING: PWFLAG IS SET TO TRUE")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    print("********************")

    question = str("Do you wish to reset password?")
    choice = query_yes_no(question, default="yes")
    if choice:
        question = "Default password for "+existing_user_name+"?"
        choice = query_yes_no(question, default="yes")
        if choice:
            new_password = DEFAULTPW
        else:
            custom_pw = input('Input custom password: ')
            new_password = custom_pw
        print("Password will be "+new_password)
        gam_input = "gam update user "+existing_user_name+" password '"+new_password+"' changepassword off"
        result = os.popen(gam_input).read()
        print(result)
    print("********************")

    question = str("Do you wish to remove user from ALL OF THEIR GROUPS?")
    choice = query_yes_no(question, default="yes")
    if choice:
        for key in group_dictionary:
            gam_input = "gam update group "+key+" remove user "+existing_email
            print(key)
            result = os.popen(gam_input).read()
            print(result)
        gam_input = "gam info user "+existing_user_name
        result_1 = os.popen(gam_input).read()
        print(result_1)

        question = "Do you wish to add "+existing_user_name+" back to ALL OF THEIR GROUPS?"
        choice = query_yes_no(question, default="yes")
        if choice:
            for key in group_dictionary:
                print(key)
                gam_input = "gam update group "+key+" add "+group_dictionary[key]+" user "+existing_email
                result_1 = os.popen(gam_input).read()
                print(result_1)
        else:
            print ("no group addback ")
    print("********************")

    question = str("Do you wish to add "+existing_user_name+" to groups manually?")
    choice = query_yes_no(question, default="yes")
    if choice:
        question = str("Do you wish to add "+existing_user_name+" to groups as REGULAR USER?")
        choice = query_yes_no(question, default="yes")
        if choice:
            question = str("Do you wish to add "+existing_user_name+" to SWANTON PROFESSIONAL GROUP as REGULAR USER?")
            choice = query_yes_no(question, default="yes")
            if choice:
                gam_input= "gam update group swantonprofessionalstaff@fnwsu.org add member user "+ existing_email
                result_1 = os.popen(gam_input).read()
                print(result_1)
            question = str("Add "+existing_user_name+" to SWANTON PARA PROFESSIONAL as REGULAR USER?")
            choice = query_yes_no(question, default="yes")
            if choice:
                gam_input= "gam update group swantonparaprofessionals@fnwsu.org add member user "+ existing_email
                result_1 = os.popen(gam_input).read()
                print(result_1)
            question = str("Add "+existing_user_name+" to CENTRAL BUILDING as REGULAR USER?")
            choice = query_yes_no(question, default="yes")
            if choice:
                gam_input= "gam update group centralstaff@fnwsu.org add member user "+ existing_email
                result_1 = os.popen(gam_input).read()
                print(result_1)
            question = str("Add "+existing_user_name+" to BABCOCK BUILDING as REGULAR USER?")
            choice = query_yes_no(question, default="yes")
            if choice:
                gam_input= "gam update group babcockstaff@fnwsu.org add member user "+ existing_email
                result_1 = os.popen(gam_input).read()
                print(result_1)

        question = str("Do you wish to add "+existing_user_name+" to groups as MANAGER?")
        choice = query_yes_no(question, default="yes")
        if choice:
            question = str("Do you wish to add "+existing_user_name+" to SWANTON PROFESSIONAL GROUP as MANAGER?")
            choice = query_yes_no(question, default="yes")
            if choice:
                gam_input= "gam update group swantonprofessionalstaff@fnwsu.org add manager user "+ existing_email
                result_1 = os.popen(gam_input).read()
                print(result_1)
            question = str("Add "+existing_user_name+" to SWANTON PARA PROFESSIONAL as MANAGER?")
            choice = query_yes_no(question, default="yes")
            if choice:
                gam_input= "gam update group swantonparaprofessionals@fnwsu.org add manager user "+ existing_email
                result_1 = os.popen(gam_input).read()
                print(result_1)
            question = str("Add "+existing_user_name+" to CENTRAL BUILDING as MANAGER?")
            choice = query_yes_no(question, default="yes")
            if choice:
                gam_input= "gam update group centralstaff@fnwsu.org add manager user "+ existing_email
                result_1 = os.popen(gam_input).read()
                print(result_1)
            question = str("Add "+existing_user_name+" to BABCOCK BUILDING as MANAGER?")
            choice = query_yes_no(question, default="yes")
            if choice:
                gam_input= "gam update group babcockstaff@fnwsu.org add manager user "+ existing_email
                result_1 = os.popen(gam_input).read()
                print(result_1)
    print("********************")

    question = str("Do you wish to move "+existing_user_name+" to a different ORGANIZATIONAL UNIT?")
    choice = query_yes_no(question, default="yes")
    if choice:
        question = str("ACTIVE staff member?")
        choice = query_yes_no(question, default="yes")
        if choice:
            gam_input= "gam update user "+existing_email+" org '/Swanton-All/Swan Staff-All'"
            result_1 = os.popen(gam_input).read()
            print(result_1)
        else:
            question = str("REMOVED staff member?")
            choice = query_yes_no(question, default="yes")
            if choice:
                gam_input= "gam update user "+existing_email+" org '/Swanton-All/Swan Staff-All/Swan Suspended-Staff'"
                result_1 = os.popen(gam_input).read()
                print(result_1)
            else:
                for key in grade_book:
                    question = str("Grade: "+str(key)+" Grad Year: "+str(grade_book[key])+" ?")
                    choice = query_yes_no(question, default="yes")
                    if choice:
                        gam_input= "gam update user "+existing_email+" org '/Swanton-All/Swan Students-All/Swan Grade "+str(key)+"-20"+str(grade_book[key])+"'"
                        result_1 = os.popen(gam_input).read()
                        print(result_1)
    print("********************")

    question = str("Do you wish to have "+existing_user_name+" SUSPENDED?")
    choice = query_yes_no(question, default="yes")
    if choice:
        gam_input= "gam update user "+existing_email+" suspended on"
        result_1 = os.popen(gam_input).read()
        print(result_1)
    else:
        gam_input= "gam update user "+existing_email+" suspended off"
        result_1 = os.popen(gam_input).read()
        print(result_1)
