staff = {
    "developer": "Ajay",
    "tester": "manisha",
    "dba": "jyoti",
    "devops": "sanjay"
}
print(staff["tester"])

#built in methods for dictionary. 

#dictionary.keys() - displays all the keys as a list
print(staff.keys())

#dictionary.values() - displays all the values as a list
print(staff.values())

#dictionary.items() - displays all the items as a tuple
print(staff.items())

# change a value

staff["tester"] = "manisha R"
print(staff["tester"])

#upadte a value. 
staff.update({"lead": "saikat"})
print(staff)

#delete value
del staff["dba"]
print(staff)

#delete last item
staff.popitem()
print(staff)

#delete all data in dict
staff.clear()
print(staff)

#copy a disctionary
staff2 = staff.copy()
print(staff2)