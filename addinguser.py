import pyodbc as py
server = 'd2mtrainingdb.database.windows.net'
db = 'd2manalysistraining'
user = 'dbtuser'
pwd = 'Disys@2022'
conn = py.connect('DRIVER={SQL Server}'';SERVER=' + server +
';DATABASE=' + db +
'; UID=' + user +
'; PWD=' + pwd +
';Trusted_Connection=no')
cursor = conn.cursor()

#inserting
print("Enter Student ID")    
student_id=int(input())

print("Enter Student Name")    
student_name=input()

print("Enter Gender")    
sex=input()

print("Enter DOB")    
date_of_birth=input()

print("Enter Borrower ID")    
borrower_id=int(input())

print("Enter Department")    
department=input()

cursor = conn.cursor()
print(cursor)

SQLCommand = ("INSERT INTO gp_student_details(student_id, student_name, sex, date_of_birth, borrower_id, department) VALUES (?,?,?,?,?,?)")    
Values = [student_id, student_name, sex, date_of_birth, borrower_id, department]  

#Processing Query    
cursor.execute(SQLCommand,Values)     

#Commiting any pending transaction to the database.    
conn.commit()    

#closing connection    
print("Data Successfully Inserted")   
conn.close() 


