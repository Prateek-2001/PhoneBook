from collections import defaultdict
def add(dict):
    name = input('Name: ')
    phone = input('Phone Number: ')
    age = input('Age: ')
    locality = input('Locality: ')
    dict = defaultdict(list)
    dict[name].append(phone)
    dict[name].append(age)
    dict[name].append(locality)
    print(dict)

def search(dict):
    entry = input(
        "Write the name of the person whose age you'd like to know, or write 'ALL' to see all names and ages:\n ")
    if entry == "ALL":
        for key, value in dict.items():
            print("Name: " + key)
            print("Age: " + str(value) + "\n")
    elif entry in dict:
        print('Name: '+ entry)
        print(dict[entry])
    return dict
def delete(dict):
    deletion = input('Which contact would you like to remove?\n')
    dict.pop(deletion)
    print(dict)

dict = {'Shubhu':[123456789, 19, 'Japan'], 'Ishaan':[987654321, 19, 'Aussie'],'Prateek':[135792468, 19, 'India']}
print('1. Add Contact')
print('2. Search Contact')
print('3. Delete contact')
n = int(input('What do you want to do? Press number accordingly\n'))
if n==1:
    add(dict)
elif n==2:
    search(dict)
elif n==3:
    delete(dict)
