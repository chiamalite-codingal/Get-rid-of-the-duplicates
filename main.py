student_data ={
'stu1':{'name':['Heritage'], 'class':[9], 'age':[12], 'subject':["Eng"]},
'stu2':{'name':['David'], 'class':[12], 'age':[14], 'subject':["Eng"]},
'stu3':{'name':['Esther'], 'class':[8], 'age':[11], 'subject':["Eng"]},
'stu4':{'name':['Heritage'], 'class':[14], 'age':[16], 'subject':["Eng"]},
}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)