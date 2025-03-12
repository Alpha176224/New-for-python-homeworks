n=0
with open("employees.txt", "a") as txt:
    txt.write("")
try:
    with open("employees.txt", "r") as txt:
        lines = txt.readlines()
        if lines:
            id_list = [int(line.split(", ")[0]) for line in lines]
            id = max(id_list) + 1
        else:
            id = 1001
except FileNotFoundError:
    id = 1001

while n!=6:
    n=int(input("Choose one option:\n1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit\nEnter a number from 1 until 6: "))
    if n==1:
        new_employee_record=input("Enter new employee records by this order:\nName, Position, Salary\n: ")
        with open("employees.txt", "r") as txt:
            is_empty = not txt.read().strip()
        with open("employees.txt", "a") as txt:
            if is_empty:
                txt.write(f"{id}, {new_employee_record}")
            else:
                txt.write(f"\n{id}, {new_employee_record}")
            id+=1
            
    elif n==2:
        with open("employees.txt","r") as txt:
            data=txt.read()
        if not data.strip():
            print('There is no data!!!')
        else:
            print(data)

    elif n==3:
        try:
            search_id=int(input("Enter an ID number of the employee: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        with open("employees.txt") as txt:
            lines=txt.readlines()
        s=0
        for line in lines:
            list_line=line.split(", ")
            if list_line[0]==f'{search_id:}':
                print(line[:len(line)])
                s+=1
        if s==0:
            print("There is no employee with such ID number!")
            
    elif n==4:
        try:
            search_for_update_id=int(input("Enter an ID number of the employee: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        with open("employees.txt") as txt:
            lines=txt.readlines()
        new_lines=[]
        s=0
        for line in lines:
            if line.split(", ")[0]==f'{search_for_update_id}':
                s+=1
                option_4=int(input(f'Info: {line}Choose one option to update\n1.Name\n2.Position\n3.Salary\nEnter a number from 1 until 3: '))
                line=line.split(", ")
                if option_4==1:
                    name_update=str(input('Enter new name to update: '))
                    line[1]=name_update
                elif option_4==2:
                    position_update=str(input('Enter new position to update: '))
                    line[2]=position_update
                elif option_4==3:
                    salary_update=int(input('Enter new salary to update: '))
                    line[3]=str(salary_update)
                else:
                    print('wrong command!')
                line=f'{line[0]}, {line[1]}, {line[2]}, {line[3]}'
            new_lines.append(line)
        with open("employees.txt","w") as txt:
            txt.writelines(new_lines)
        if s==0:
            print("There is no employee with such ID number!")

    elif n==5:
        try:
            search_for_delete_id=int(input("Enter an ID number of the employee: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        s=0
        with open("employees.txt") as txt:
            lines=txt.readlines()
        new_lines=[]
        for line in lines:
            if line.split(", ")[0]==f'{search_for_delete_id}':
                s+=1
            else:
                new_lines.append(line)
        with open("employees.txt","w") as txt:
            txt.writelines(new_lines)
        if s==0:
            print("There is no employee with such ID number!")
            
    elif n==6:
        break
    else:
        print('Wrong command!')


    
    
    

