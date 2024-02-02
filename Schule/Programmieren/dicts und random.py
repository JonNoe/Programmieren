from faker import Faker
import random as rd
fake = Faker()
students = []

for _ in range(10):
    student = {
        "name": fake.name(),
        "age": rd.randint(18,25),
        'major': rd.choice(['Computer Science', 'Mathematics', 'Physics']),
        'gpa': round(rd.uniform(2.0,4.0),2),
        'is_intentional': rd.choice([True,False])
        }
    
    students.append(student)
vornamen = []
for student in students:
    full_name = student['name']
    vorname = full_name.split()[0]
    nachname = full_name.split()[1]
    print(vorname,nachname)
    print('Age:', student['age'])


for student in students:
    vorname = full_name.split()[0]
    vornamen.append(vorname[0])
    
Anzahl_Duplikate = len(vornamen) - len(set(vornamen))
print(Anzahl_Duplikate)

duplicate_count = {name: vornamen.count(name)
                   for name in set(vornamen)
                        if vornamen.count(name) > 1}
print(duplicate_count)

ohne_Duplikate = list(set(vornamen))
print(ohne_Duplikate)
Duplikate = []
for name in vornamen:
    if name not in ohne_Duplikate:
        Duplikate.append(name)
print(Duplikate)
