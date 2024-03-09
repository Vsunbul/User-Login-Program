

from datetime import datetime

import sqlite3

class Table():
    
    def __init__(self, user_name, password, name, surname, birth_date):
        
        """
        
        This function creates the basis person datas.
       
        return None
        
        """
        self.user_name = user_name
        self.password = password
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        

    def create_table(self):
        
        """
        
        This function creates information.db for  person informaitons.
        
        return None
    
        """
        
        con = sqlite3.connect("information.db")
        cursor = con.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS personal(user_name TEXT,
                       password TEXT,
                       name TEXT, 
                       surname TEXT, 
                       birth_date INT, 
                       age INT, 
                       current_salary INT,
                       increase_amount INT, 
                       desired_increase INT, 
                       pleasure_salary FLOAT, 
                       skill TEXT)""")
        con.commit()
        con.close()
        
  
    def calculate_age(self):
        
        """
        
        This function calculates the person age.
        
        return age -> Integer
        
        """
        return datetime.now().year - self.birth_date
    
    
    def enter_information(self, user_name, password, name, surname, birth_date,
                          current_salary, increase_amount, desired_increase, skill):
        
        
        """
        
        This function enters data into information.db
                
        return None
        
        """
        
        self.user_name = user_name
        self.password = password
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.current_salary = current_salary
        self.increase_amount = increase_amount
        self.desired_increase = desired_increase
        self.skill = skill
        
        
        #pleasure_salary shows the satisfaction rate of the staff according to the salary increase they receive.
        pleasure_salary = (self.increase_amount - self.desired_increase) / 100
        age = self.calculate_age()
        self.current_salary += self.increase_amount 
        
        con = sqlite3.connect("information.db")
        cursor=con.cursor()
        cursor.execute("INSERT INTO  personal  VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                       (self.user_name, 
                        self.password,
                        self.name,
                        self.surname, 
                        self.birth_date,
                        age,
                        self.current_salary,
                        self.increase_amount, 
                        self.desired_increase, 
                        pleasure_salary,
                        self.skill))
        con.commit()
        con.close()
        
        
    def show_information(self):
        
        """
        
        This fonctions shows all person informations using information.db
        
        return -> list
        
        """
        
        con = sqlite3.connect("information.db")
        cursor=con.cursor()
        cursor.execute("SELECT * FROM personal")
        data = cursor.fetchall()
        print(data)
        con.close()
        
    def input_values(self):
        
        """
        
        This function gets data for the new person record in the database.
        
        return None
    
        """
        
        self.user_name = input("Enter user name :")
        self.password = input("Enter password :")
        self.name = input("Enter name :")
        self.surname = input("Enter surname :")
        self.birth_date = int(input("Enter birth year : "))
        self.current_salary = int(input("Enter current salary : "))
        self.increase_amount = int(input(" Enter increase amount : "))
        self.desired_increase = int(input("Enter desired increase : "))
        self.skill = input("Enter skilss :")
        
        #Using enter_information for the new person record.
        self.enter_information(self.user_name, self.password, self.name, self.surname,
                               self.birth_date, self.current_salary, self.increase_amount,
                               self.desired_increase, self.skill)

    def total_input_values(self):
        
        """

        This function performs multiple data entry.

        return None
   
        """

        person_list =[["ahmetdemir","sifre123","ahmet", "demir", 1965, 50000, 10000, 5000, "HR", "MS OFFICE"],
              ["mehmetmeral","sifre142","mehmet", "meral", 1980, 100000, 20000, 5000, "IT", "Python"],
              ["kemalbirkis","sifre112","kemal", "birkis", 1999, 60000, 5000, 7000, "IT", "SECURITY"],
              ["sibelyorgun","sifre122","sibel", "yorgun", 1992, 50000, 10000, 7000, "HR", "Conversation"],
              ["mahmuttuncer","sifre162","mahmut", "tuncer", 1977, 0, 100000, 70000, "HR", "SONG"],
              ["ibrahimtatlıses","sifre152","ibrahim", "tatlıses", 1955, 7000, 70000, 60000, "QC", "Statistic"],
              ["tuncaysanli","sifre142","tuncay", "sanli", 1980, 50000, 15000, 8000, "QC", "Statistic"],
              ["ardaturan","sifre132","arda", "turan", 1986, 60000, 10000, 1000, "HR", " "]]


        for data in person_list:

            person = Table(data[0], data[1], data[2], data[3], data[4])
            person.enter_information(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])


    def get_loggin_data(self):

        """
        This function gets username and password data from information.db
        
        return -> list
        
        """
        
        con = sqlite3.connect("information.db")
        cursor=con.cursor()
        cursor.execute("SELECT user_name, password FROM personal")
        self.data = cursor.fetchall()
        print(self.data)
        con.close()
        
        
    def show_person_data(self):
        
        """
        This function retrieves the personnel information using user_name data.
        
        return None
    
        """
        self.user_name = self.logged_in_user
        con = sqlite3.connect("information.db")
        cursor=con.cursor()
        cursor.execute("SELECT * FROM personal WHERE user_name = ? ",(self.logged_in_user,))
        self.data = cursor.fetchall()
        #User information is shown here for testing.
        print(self.data)
        con.close()
        
        
    def change_password_db(self,new_password):
        
        """
        
        This function saves the new password to information.db
        
        return None
    
        
        """
        
        self.new_password = new_password
        con = sqlite3.connect("information.db")
        cursor = con.cursor()
        add_command = "UPDATE personal SET password = ? WHERE user_name = ?"
        cursor.execute(add_command, (self.new_password, self.logged_in_user))
        con.commit()
        con.close()
        
        
        

class App(Table):
    
        
    def get_main_menu_choice(self):
        
        """
        This function shows the main menu
        
        return None
    
        """
        
        return input("""
                     
********************************************                     
                     
    Please Enter A Choice:
        
            MENU
            1.LOGIN
            2.SIGN UP
            3.EXIT APP    
                   :  
                   
********************************************  

                    """)
    
    def get_login_information(self):
        
        """
        This function inputs username and password values 
        
        return self.user_name ->Str
                self.password ->Str
        """
        
        self.user_name = input("Enter User Name :")
        self.password = input("Enter Password :")
        return self.user_name, self.password
        

    def sing_up(self):
        
        """
        This function does enter data to the information.db
        return None
        """
        self.input_values()
        print("sing up Worked!")
    
    
    def logged_in_menu_choice(self):
         return input("""
                      
          ###############################################            
                      
                     PLease Choice Operation
                     
                     1.Show Informations
                     2.Change Password
                     3.logout
                     
                     
          ###############################################           
                      
                      """)
                                 

    def authanticate(self):
        
        """
        This function checks user name, password and directs logged in menu choice.
        
        return None
        
        """
        
        self.data = []
        self.logged_in_user = ""
        self.is_user_logged_in = False
        
        #The username and password are taken from the db and added to the data list.
        self.data.append(self.get_loggin_data())
        
        password_try = 3
        
        while True:
            
            
            #The number of attempts is checked.
            print("Username or Password is not True! Try Rights :", password_try)
            password_try -= 1
            
            
            if password_try == 0:
                print("You have run out of trial rights.")
                
                break
        
            self.get_login_information()
            
            for item in self.data:
                
                if item == (self.user_name, self.password):
                    
                    self.logged_in_user = self.user_name
            
                    choice = self.logged_in_menu_choice()
                    
                    if choice == "1":
                        #Shows person informations.
                        self.show_person_data()
                        return self.get_main_menu_choice()
                    
                    elif choice == "2":
                        #Changes password.
                        self.change_password()
                        return self.get_main_menu_choice()
                    
                    elif choice == "3":
                        print("exited program")
                        return None
                        break 

    def change_password(self):
        
        """
        This fonction changes password and send new password to the information.db.
        
        return None
        """
        
    
        while True: 
            #Entering login informations.
            self.get_login_information()
                
            for item in self.data:
                    
                if item == (self.user_name, self.password):
                        
                    self.logged_in_user = self.user_name
                    
                    #Entering new password.
                    new_password = input("Enter New Password :")
                    
                    #Checking new password.
                    new_password_again = input("Enter New Password Again:")  
                        
                    if new_password == new_password_again:
                        #New pasword changes at the database. 
                        self.change_password_db(new_password)
                        print("Your Password Was Changed")
                        return None
                    
                    else:
                        print("New Passwords Is Not Same.")
                        
                print("Please enter correct values!")
                break
        
    def get_choice(self):
        
        """
        This function makes selection from the main menu.
        
        
        return None
                
        """
        
        while True:
            
            number = self.get_main_menu_choice()
            
            if number == "1":
                self.authanticate()
                break
            
            elif number == "2":
                self.sing_up()
                return self.get_main_menu_choice()
            
            elif number == "3":
                print("Exited Program")
                break
            
        return None        
    
    
    def __del__(self):
        
        """
        
        This function is destructor.
        
        
        """
        
        print("destructor function worked")
        

    
app = App("alidemir","sifre123","ahmet", "demir", 1965)


app.get_choice()
#app.show_information()
