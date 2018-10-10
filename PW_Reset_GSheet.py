import pygsheets
from pprint import pprint
import os
import sys

#Works with google sheets instead of a copy/paste text file like previous verisons
gc = pygsheets.authorize()

# Open spreadsheet and then workseet
sh = gc.open('18/19 Student List')
wks = sh.worksheet_by_title("PWReset")

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

#####
exclude_header = True
#force_pw_change = True

question = "Force Password Change at Logon?"
choice = query_yes_no(question, default="yes")
if choice:
    change = "on"
else:
    change= "off"
#####

if exclude_header:
    row = 2
else:
    row = 1

# if force_pw_change:
#     change = "on"
# else:
#     change= "off"
####

column = 7 #Username
val_1 = wks.get_values(start=(row,column), end=(9999,column), returnas='matrix') #8 is how many over

column = 8 #default password
val_2 = wks.get_values(start=(row,column), end=(9999,column), returnas='matrix') #8 is how many over

for id,pw in zip(val_1,val_2):
    print("User: "+str(id[0])+" Password: "+str(pw[0]))
    gam_input = "~/bin/gam/gam update user "+id[0]+" password '"+pw[0]+"' changepassword " + change
    result_1 = os.popen(gam_input).read()
    print(result_1)
    print()
