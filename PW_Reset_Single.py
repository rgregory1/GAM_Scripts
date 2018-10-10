import os
import sys
from itertools import islice

grade_book = {'12': 19, '11': 20, '10': 21, '9': 22, '8': 23,'7': 24, \
    '6': 25, '5': 26, '4': 27, '3':28, '2':29, '1':30}

def query_yes_no(question, default="yes"):

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


existing_user_name = input('Username? (just user - no email) ')
existing_email = existing_user_name + "@mymtsd-vt.org"
print("Info:")
print()
gam_input = "~/bin/gam/gam info user "+existing_user_name
result_1 = os.popen(gam_input).read()
if not result_1:
    #User has not been found
    exit()
result_2 = result_1
head = list(islice(result_1.splitlines(), 19))

for x in head:
    print(x)

## Groups
group_list= []
group_dictionary= {}
for x in result_1.splitlines():
    if "@" in x and "User" not in x and existing_user_name not in x: #filter out results that aren't actual groups
        a = x.split('<',1)[-1]
        b = a.replace(">", "")
        group_list.append(b)

for x in group_list:
    gam_input = "~/bin/gam/gam info group "+x
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
#NEWFIRST_I_L = first_name[0].lower()
#NEWLAST_I_L = last_name[0].lower()
#DEFAULTPW = first_name[0].lower() + last_name[0].lower() + "3456789"
#NEWFIRST_I_L = first_name[:3].lower()
#NEWLAST_I_L = last_name[0].lower()
#DEFAULTPW = NEWFIRST_I_L + last_name.lower() + "123"

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

#question = str("Do you wish to reset password?")
#choice = query_yes_no(question, default="yes")
#if choice:
question = "Default password for "+existing_user_name+"?"
choice = query_yes_no(question, default="yes")
if choice:
    question = "Is "+existing_user_name+" a STUDENT?"
    choice = query_yes_no(question, default="yes")
    if choice:
        new_password = first_name[:3].lower() + last_name.lower() + "123"
    else:
        print("Creating Teacher Password...")
        #question = "Is "+existing_user_name+" a TEACHER?"
        #choice = query_yes_no(question, default="yes")
        #if choice:
        new_password = first_name[0].lower() + last_name.lower() + "123"
else:
    custom_pw = input('Input custom password: ')
    new_password = custom_pw
print()
print("Password will be: "+new_password)
gam_input = "~/bin/gam/gam update user "+existing_user_name+" password '"+new_password+"' changepassword off"
result = os.popen(gam_input).read()
print()
print(result)
print("********************")
