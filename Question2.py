dog = {}
#updating dog values to the dictionary
dog.update({'name' : 'Jackie','color' : 'White','breed' : 'labrador','legs' : '4','age' : '7'})
#updating student values to dictionary 
student = {'first_name' : 'Nithisha','last_name' : 'Majety','gender' : 'Female','age' : '22','marital_status' : 'Unmarried','skills' : ["C","C++","Java","Python"],'country' : 'India','city' : 'Rajahmundry','address' : 'Aryapuram, Rajahmundry'}
#finding length of student dictionary
print("Length of student dictionary is :", len(student))
#Finding skills of student and data type of skills
print("Skills of student are :", student['skills'])
print("Datatype of skills is :", type(student['skills']))
#modifying skills value by adding 2 more attributes to the skills list
student['skills'].extend(["SQL", "Azure_IaaS"])
print("Modified skills list in the student dictionary are :", student['skills'])
#keys and values as a list for student dictionary
print("Keys as a list in the student dictionary are :", list(student.keys()))
print("Values as a list in the student dictionary are :", list(student.values()))