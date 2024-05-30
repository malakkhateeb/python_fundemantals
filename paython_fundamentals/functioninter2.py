x = [ [5,2,3], [10,8,9] ] 
students = [ {'first_name':  'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1.Update Values in Dictionaries and Lists
x[1][0]=15
print(x)

students[0]["last_name"] = 'Bryant'
print(students)

sports_directory['soccer'][0]= 'Andres'
print(sports_directory)

z[0]['y']=30
print(z)

# Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for students in some_list:
        lst=", ".join([f"{key} - {val}" for key, val in  students.items()])
        print(lst)
# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for students in some_list:
        print(students[key_name])

students = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]
iterateDictionary(students)
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, val in some_dict.items():
        print(f"{len(val)} {key.upper()}")
        for vals in val:
            print(vals)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

