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
print("Enter book_id")    
book_id=input()


print("Enter a book_name")    
book_name=input()

print("Enter a author")    
author=input()

print("Enter a binding_id")    
binding_id=int(input())

print("Enter a no_of_actualcopies")    
no_of_actualcopies=int(input())

print("Enter a no_of_booksborrowed")    
no_of_booksborrowed=int(input())

print("Enter a category")    
category=input()

print("Enter a publication_year")    
publication_year=int(input())

print("Enter a reviews")    
reviews=input()

cursor = conn.cursor()
print(cursor)

SQLCommand = ("INSERT INTO gp_book_details(book_id, book_name, author, binding_id, no_of_actualcopies, no_of_booksborrowed, category, publication_year, reviews) VALUES (?,?,?,?,?,?,?,?,?)")    
Values = [book_id, book_name, author, binding_id, no_of_actualcopies, no_of_booksborrowed, category, publication_year, reviews]  

#Processing Query    
cursor.execute(SQLCommand,Values)     

#Commiting any pending transaction to the database.    
conn.commit()    

#closing connection    
print("Data Successfully Inserted")   
conn.close() 


