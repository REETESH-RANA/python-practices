students={
    'CS100':{"Name":"Arnab","Maths":67,"physics":90,"Chemistry":78},
    'CS101':{"Name":"Tony","Maths":47,"physics":56,"Chemistry":67},
    'CS102':{"Name":"Mohit","Maths":97,"physics":99,"Chemistry":88},
    'CS103':{"Name":"Riya","Maths":77,"physics":70,"Chemistry":79},
    'CS104':{"Name":"Ramit","Maths":92,"physics":40,"Chemistry":28},
    }
'''roll_no=input("enter the roll no of the student: ")

result=students.get(roll_no,"roll number not exist..")
if(isinstance(result,str)):
    print(result)
else:   
    total=result['Maths']+result['physics']+result['Chemistry']
    print('total',total)
    print("Name:",result['Name'])
    print("Maths:",result['Maths'])
    print("physics:",result['physics'])
    print("Chemistry:",result['Chemistry'])

    percentage=total/3
    print("percentage",percentage)'''


# now find the student name whose marks in math is above to 80
'''for std in students.values():
    if(std["Maths"]>=80):
        print(std['Name'])'''

'''for std in students.keys():
    if(students[std]["Maths"]>=80):
        print(std,students[std]['Name'])'''

''' for std in students.items():
    if(students[std[0]]["Maths"]>=80):
        print(std[0],std[1]['Name'])'''

# Again we have to add two rows dynamically in students dictionary program
'''for i in range(2):
    students.setdefault(input("enter rollno: "),{"Name":input("enter the name: "),"Maths":int(input("enter maths mark: ")),"physics":int(input("enter the physics mark: ")),"Chemistry":int(input("enter the chemistry mark: "))})
print(students)
'''
#PROGRAM FOR VOTING USING DICTIONARY
'''D=dict.fromkeys(['BJP','INC','SP','AAP','BSP'],0)
print(D)
i=0
while(i<10):
    v=input("enter the vote :")
    D[v]+=1
    i+=1
print(D)'''



