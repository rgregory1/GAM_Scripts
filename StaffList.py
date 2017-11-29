#Python used to create list of staff in pro and para lists
import os

result1 = os.popen("gam info group swantonprofessionalstaff@fnwsu.org").read()
#result2 = os.popen("gam info group swantonparaprofessionals@fnwsu.org").read()
#print(result)
#result1 = result.splitlines()
#result2 = []
#print(result1)
def clean(result):
    result2 = []
    result1 = result.splitlines()
    for x in result1:
        if "@" in x and "email" not in x:
            a = x.strip()
            b = a.replace(" (user)", "")
            if "owner: " in b:
                d = b.replace("owner: ", "")
            if "manager: " in b:
                d = b.replace("manager: ", "")
            if "member: " in b:
                d = b.replace("member: ", "")
            result2.append(d)
    return result2
list2 = []
#list1 = clean(result1)
list1 = clean(result1)

final_list = list(set(list1 + list2))
print("Count: " + str(len(final_list)))
for x in sorted(final_list):
    print(x)
