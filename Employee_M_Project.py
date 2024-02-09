import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Employee_Management"
)
mycursor = mydb.cursor()

def showMenu():
    print("Choose an option:\n1)Add_employee\n2)Edit_employee\n3)Delete_employee\n4)Show_employees")
    print("5)Search_by_name\n6)Exit")
    choice = int(input("Enter your choice: "))
    return choice

lstNames = [] 
ch = 0
while(ch != 6):
    ch = showMenu()
    if ch == 1:
       employee_id = int(input("Enter Employee ID: "))
       employee_name = input("Enter Employee Name: ")
       employee_department = input("Enter Employee Department: ")
       employee_address = input("Enter Employee Address: ")

       sql = "Insert into Employee (Employee_ID, Employee_Name, Employee_Department, Employee_Add)VALUES (%s, %s, %s, %s)"
       val = (employee_id, employee_name, employee_department, employee_address)

       mycursor.execute(sql, val)
       mydb.commit()
       print("Employee added successfully!")
    elif ch == 2:
         employee_id = int(input("Enter Employee ID to edit: "))
         column_to_edit = input("Enter column to edit (Employee_Name/Employee_Department/Employee_Add): ").capitalize()
         new_value = input(f"Enter new {column_to_edit}: ")

         sql =sql = f"UPDATE Employee SET {column_to_edit} = %s WHERE Employee_ID = %s"
         val = (new_value, employee_id)

         mycursor.execute(sql, val)
         mydb.commit()
         print("Employee details updated!")
    elif ch == 3:
         employee_id = int(input("Enter Employee ID to delete: "))

         sql = "DELETE FROM Employee WHERE Employee_ID = %s"
         val = (employee_id,)

         mycursor.execute(sql, val)
         mydb.commit()
         print("Employee deleted successfully!")
    elif ch == 4:
         mycursor.execute("SELECT * FROM Employee")
         employees = mycursor.fetchall()

         if not employees:
             print("No employees found.")
         else:
             for employee in employees:
                 print(employee)
    elif ch == 5:
         employee_name = input("Enter Employee Name to search: ")

         sql = "SELECT * FROM Employee WHERE Employee_Name = %s"
         val = (employee_name,)

         mycursor.execute(sql, val)
         employees = mycursor.fetchall()
    
         if not employees:
             print("No matching employee found.")
         else:
             for employee in employees:
                 print(employee)
    elif ch == 6:
         print("Exiting the Program, Thank You!")
         break
        
    else:
        print("Invalid option")
