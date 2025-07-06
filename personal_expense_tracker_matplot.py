# first this will take input for profile 
#expense_tracker/
#├── main.py                # entry point
#├── profile.json           # stores user profile
#├── expenses.csv           # stores expense logs
#├── data_analysis.py       # functions to analyze
#├── visualizer.py          # charts
#├── utils.py               # load/save helpers

import json
import os 
import matplotlib.pyplot as plt
import numpy
import datetime
import pandas as pd
import numpy as np

Fileprofile = "profile.json"
now = datetime.datetime.now()

class Profile():
    def __init__(self, name=None, phone=None, age=None, monthly=None, budget=None):

        self.__name = name
        self.__phone = phone
        self.__age = age
        self.__monthly = monthly
        self.__budget = budget
    
    def store_profile(self):
        return {
            "name": self.__name,
            "phone": self.__phone,
            "age": self.__age,
            "monthly": self.__monthly,
            "budget": self.__budget
        }
    
    def profile_load(self):
        if os.path.exists(Fileprofile):
            try:
                with open(Fileprofile, "r") as file:
                    data = json.load(file)
                    return data
            except:
                return []
        return []
    
    def profile_save(self, name, phone, age, monthly, budget):
        user = Profile(name, phone, age, monthly, budget)
        data = self.profile_load()
        store = user.store_profile()
        data.append(store)
        with open(Fileprofile, "w") as file:
            json.dump(data, file, indent=5)
    
    
    
File = "expenses.json"
class Expense(Profile):
    def __init__(self, name=None, date=None, category=None, amount=None,description=None, payment_mode=None):
        self.__name = name
        self.__date = date
        self.__category = category
        self.__amount = amount
        self.__description = description 
        self.__payment_mode = payment_mode
        
    def store_expense(self):
        return {
                "name": self.__name,
                "date": self.__date,
                "category": self.__category,
                "amount": self.__amount,
                "description": self.__description,
                "payment_mode": self.__payment_mode
            
        }

    def expense_load(self):
        if os.path.exists(File):
            try:
                with open(File, "r") as file:
                    data = json.load(file)
                    return data
            except:
                return []
        return []
    
    def store_save(self,name, date, category, amount,description, payment_mode):
        expense = Expense(name, date, category, amount,description, payment_mode)
        data = self.expense_load()
        store = expense.store_expense()
        data.append(store)
        with open(File,"w") as file:
            json.dump(data,file,indent=6)

    def save(self,data):
        with open(File, "w") as file:
            json.dump(data,file,indent=5)


    def save_all_profiles(self, data):
        with open(Fileprofile, "w") as file:
            json.dump(data, file, indent=5)

    @staticmethod
    def check_name_exists(name):
        expense = Expense()
        data = expense.expense_load()
        for p in data:
            if p["name"].lower() == name.lower():
                return True
        return False


    
    
def menu():
    
    print("\n-|________________| WELCOME | TO | EXPENSE | TRACKER |________________|-")

    print("\nChoose an option:-")
    print("-----------------------------------------")
    print("\n0. Add Profile")
    print("1. Update Profile")
    print("2. View Profile")
    print("3. Add New Expense")
    print("4. View All Expenses")
    print("5. Search Expenses (by date/category)")
    print("6. Basic and Graph Expenses Analyser")
    print("7. Detailed Analysis of Months")
    print("8. Analysis By Rank")
    print("9. Exit")
    print("-----------------------------------------")

while True:
    menu()
    try:
        
        user = int(input("Enter your choice: "))

        if user == 0: # add profile

            while True:
                try:
                    name = input("1. Enter your Name: ")
                    if name.strip().isdigit() or len(name.strip()) < 2:
                        print("❌ Name must be alphabetic and at least 2 characters.")
                        continue
                    break
                except ValueError:
                    print("❌ Please enter a valid name.")

            while True:
                try:
                    phone = int(input("2. Enter your 10-digit Phone Number: "))
                    if len(str(phone)) != 10:
                        print("❌ Phone number must be exactly 10 digits.")
                        continue
                    break
                except ValueError:
                    print("❌ Please enter a valid phone number.")

            while True:
                try:
                    age = int(input("3. Enter your Age: "))
                    if age < 12 or age > 100:
                        print("❌ Age must be between 12 and 100.")
                        continue
                    break
                except ValueError:
                    print("❌ Please enter a valid age.")

            while True:
                try:
                    income = float(input("4. Enter your Monthly Income: ₹"))
                    if income <= 0:
                        print("❌ Income must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("❌ Enter a valid income amount.")

            while True:
                try:
                    budget = float(input("5. Enter your Monthly Budget: ₹"))
                    if budget <= 0 or budget > income:
                        print("❌ Budget must be > 0 and less than or equal to income.")
                        continue
                    break
                except ValueError:
                    print("❌ Enter a valid budget amount.")

            profile = Profile(
                name,
                phone,
                age,
                income,
                budget
            )
            store = profile.profile_save(
                name,
                phone,
                age,
                income,
                budget
            )

            print("\nAdding Your Profile...")
            print("- Your Profile Successfully Added!")


        elif user == 1:
        
            while True:
                try:
                    check_name = input("Enter your Name: ").lower()
                    if not check_name.isalpha() or len(check_name.strip()) < 2:
                        print("❌ Name must be alphabetic and at least 2 characters.")
                        continue
                    break
                except ValueError:
                    print("❌ Please enter a valid name.")
            
            profile = Profile()
            data = profile.profile_load()
            found = False
            for details in data:
                if details["name"].lower() == check_name:
                    found = True
                    print("\n1. Name")
                    print("2. Phone Number")
                    print("3. Age")
                    print("4. Monthly")
                    print("5. Budget")
                    print("\nFor Updating Your Profile.")
                   

                    while True:
                        try:
                            choice = int(input("Enter Your Choice to Update: "))
                            if choice < 0 or choice > 5:
                                print("Choice Invalid")
                                continue
                            break
                        except ValueError:
                            print("Enter a Valid Choice")
                    
                    if choice == 1:
                        while True:
                            try:
                                updated_name = input("1. Enter your Name: ")
                                if not updated_name.isalpha() or len(updated_name) < 2:
                                    print("❌ Name must be alphabetic and at least 2 characters.")
                                    continue
                                details["name"] = updated_name
                                break
                            except ValueError:
                                print("❌ Please enter a valid name.")
                       
                    
                    
                    elif choice == 2:
                        while True:
                            try:
                                updated_phone = int(input("2. Enter your 10-digit Phone Number: "))
                                if len(str(updated_phone)) != 10:
                                    print("❌ Phone number must be exactly 10 digits.")
                                    continue
                                details["phone"] = updated_phone
                                break
                            except ValueError:
                                print("❌ Please enter a valid phone number.")
                        

                    elif choice == 3:
                        while True:
                            try:
                                updated_age = int(input("3. Enter your Age: "))
                                if updated_age < 12 or updated_age > 100:
                                    print("❌ Age must be between 12 and 100.")
                                    continue
                                details["age"] = updated_age
                                break
                            except ValueError:
                                print("❌ Please enter a valid age.")
                        
                        

                    elif choice == 4:
                        while True:
                            try:
                                updated_income = float(input("4. Enter your Monthly Income: ₹"))
                                if updated_income <= 0:
                                    print("❌ Income must be greater than 0.")
                                    continue
                                details["monthly"] = updated_income
                                break
                            except ValueError:
                                print("❌ Enter a valid income amount.")
                        

                    elif choice == 5:
                        while True:
                            try:
                                updated_budget = float(input("5. Enter your Monthly Budget: ₹"))
                                if updated_budget <= 0 or updated_budget > updated_income:
                                    print("❌ Budget must be > 0 and less than or equal to income.")
                                    continue
                                details["budget"] = updated_budget
                                break
                            except ValueError:
                                print("❌ Enter a valid budget amount.")
                        
                    profile.save_all_profiles(data)
                    print("✅ Profile updated.")
                    break


            if not found:
                print("❌ No profile found with that name.")
        
        elif user == 2:
            while True:
                try:
                    check_name = input("\nEnter your Name: ").lower()
                    if check_name.strip().isdigit() or len(check_name.strip()) < 2:
                        print("❌ Name must be alphabetic and at least 2 characters.")
                        continue
                    break
                except ValueError:
                    print("❌ Please enter a valid name.")
            profile = Profile()
            data = profile.profile_load()
            
            found = False
            for details in data:
                if details['name'].lower() == check_name:
                    found = True
                    print("\nYour Profile:-")
                    print(f"1. Name: {details['name']}")
                    print(f"2. Phone Number: {details['phone']}")
                    print(f"3. Age: {details['age']}")
                    print(f"4. Monthly Income: ₹{details['monthly']}")
                    print(f"5. Budget: ₹{details['budget']}")
                    

            if not found:
                print("Name Not Found!")

        elif user == 3:
            
            while True:
                try:
                    check_name = input("\nEnter your Name: ").lower()
                    if not check_name.isalpha() or len(check_name.strip()) < 2:
                        print("❌ Name must be alphabetic and at least 2 characters.")
                        continue
                    break
                except ValueError:
                    print("❌ Please enter a valid name.")
            
            profile = Profile()
            data = profile.profile_load()
            found = False
            for details in data:
                if details["name"].lower() == check_name:
                    found = True
                    name = check_name

                    print("\nDate Entering Instructions:-")
                    print("\n1. For Automatic Date Entering(this will enter today's date)")
                    print("2. For Entering Date Manually")
                    
                    while True:
                        try:
                            choice = int(input("\nEnter Your Choice (1 or 2): "))
                            if choice not in [1, 2]:
                                print("❌ Invalid choice! Please enter 1 or 2.")
                                continue
                            if choice == 1:
                                formatted = now.strftime("%d-%m-%Y")
                                date = formatted

                            
                            elif choice == 2:
                                while True:
                                    try:
                                        date_input = input("\nEnter the date (DD-MM-YYYY): ").strip()
                                        if date_input[2] != '-' or date_input[5] != '-' or len(date_input) != 10:
                                            print("Incorrect or Invalid Format")
                                            continue
                                        parsed_date = datetime.datetime.strptime(date_input, "%d-%m-%Y").date()
                                        date = parsed_date.strftime("%d-%m-%Y")  # Store it in correct string format
                                        print(f"✅ Date entered: {date}")
                                        break
                                    except ValueError as e:
                                        print("❌ Error:", str(e))
                                        print("Please enter the date in correct format (DD-MM-YYYY) and ensure it's valid.")
                            break
                                
                        except ValueError:
                            print("❌ Please enter a valid number (1 or 2).")

                    
                    print("\nSelect Category From this All:-")

                    print("\n1. Rent / Mortgage")
                    print("2. Electricity Bill")
                    print("3. Water Bill")
                    print("4. Internet & Wifi")
                    print("5. Gas / Heating")
                    print("6. Groceries")
                    print("7. Household Supplies")
                    print("8. Restaurant / Eating Out")
                    print("9. Cafes / Tea / Coffee")
                    print("10. Food Delivery")
                    print("11. Fuel / Petrol / Diesel")
                    print("12. Public Transport")
                    print("13. Taxi / Ride-Sharing")
                    print("14. Medcine / Pharmacy")
                    print("15. Doctor / Hospital Visits")
                    print("16. Personal Care")
                    print("17. Mobile Recharge")
                    print("18. Streaming Services")
                    print("19. Shopping")
                    print("20. Entertainment / Movies / Events")
                    print("21. Others")
                    
                    
                    while True:
                        try:
                            category_n = int(input("\nEnter Your Category: "))
                            if category_n < 0 or category_n > 21:
                                print("Invalid Choice")
                                continue
                            if category_n == 1:
                                category = "Rent / Mortgage" 
                            elif category_n == 2:
                                category = "Electricity Bill"
                            elif category_n == 3:
                                category = "Water Bill"
                            elif category_n == 4:
                                category = "Internet & Wifi"
                            elif category_n == 5:
                                category = "Gas / Heating"
                            elif category_n == 6:
                                category = "Groceries"
                            elif category_n == 7:
                                category = "Household Supplies"
                            elif category_n == 8:
                                category = "Restaurant / Eating Out"
                            elif category_n == 9:
                                category = "Cafes / Tea / Coffee"
                            elif category_n == 10:
                                category = "Food Delivery"
                            elif category_n == 11:
                                category = "Fuel / Petrol / Diesel"
                            elif category_n == 12:
                                category = "Public Transport"
                            elif category_n == 13:
                                category = "Taxi / Ride-Sharing"
                            elif category_n == 14:
                                category = "Medcine / Pharmacy"
                            elif category_n == 15:
                                category = "Doctor / Hospital Visits"
                            elif category_n == 16:
                                category = "Personal Care"
                            elif category_n == 17:
                                category = "Mobile Recharge"
                            elif category_n == 18:
                                category = "Streaming Services"
                            elif category_n == 19:
                                category = "Shopping"
                            elif category_n == 20:
                                category = "Entertainment / Movies / Events"
                            elif category_n == 21:
                                while True:
                                    try:
                                        other = input("Enter Your Other Reason: ")
                                        if other.strip().isdigit() or len(other.strip()) < 2:
                                            print("❌ Reason must be alphabetic and at least 2 characters.")
                                            continue
                                        category = other
                                        break
                                    except ValueError:
                                        print("Enter a Valid Input")
                            else:
                                print("Invalid Input")

                            break
                        except ValueError:
                            print("Enter a Valid Input")

                    while True:
                        try:
                            amount = int(input("\nEnter the Amount of Your Expenses: "))
                            if amount <= 0:
                                print("❌ Amount must be greater than 0.")
                                continue
                            break
                        except ValueError:
                            print("Enter a Valid Amount")

                    print("\nAre you wants to add Description")
                    print("\n1. Yes")
                    print("2. No")
                    while True:
                        try:
                            description_choice = int(input("\nEnter Your Choice: "))
                            if description_choice == 1:
                                description = input("\nEnter the Description: ")
                                break
                            elif description_choice == 2:
                                description = ""
                                break
                        except ValueError:
                            print("Enter a Valid Input")

                    print("\nPayment Mode:-")
                    print("\n1. UPI / Online Payment")
                    print("2. Cash")
                    print("3. Credit / Debit or any card")
                    

                    try:
                        pay_choice = int(input('\nEnter the Payment Mode: '))
                        if pay_choice == 1:
                            payment_mode = "UPI / Online Payment"
                        elif pay_choice == 2:
                            payment_mode = "Cash"
                        elif pay_choice == 3:
                            payment_mode = "Credit / Debit / Card"
                        else:
                            print("Invalid Choice")
                    
                    except ValueError:
                        print("Enter a Valid Input")

                    
                    expenses = Expense(
                        name,
                        date,
                        category,
                        amount,
                        description,
                        payment_mode
                    )

                    expenses.store_save(
                        name,
                        date,
                        category,
                        amount,
                        description,
                        payment_mode
                    )

                    print("\n-Your Expenses Saved Successfully...")

            if not found:
                print("Your Name Not Found")
                print("Please enter correct name or make a new profile")
       
        
        elif user == 4:
            while True:
                try:
                    check_name = input("\nEnter your Name: ").lower()
                    if check_name.strip().isdigit() or len(check_name.strip()) < 2:
                        print("❌ Name must be alphabetic and at least 2 characters.")
                        continue

                    break
                except ValueError:
                    print("❌ Please enter a valid name.")
            expense = Expense()
            data = expense.expense_load()
            print("\nYour All Expenses:-")
            found = False
            for i,details in enumerate(data,start=1):
                if details['name'] == check_name:
                    found = True

                    print(f"\nExpense No. {i}:-")
                    print(f"\n1. Date: {details['date']}")
                    print(f"2. Expense Category: {details['category']}")
                    print(f"3. Expense's Amount: {details['amount']}")
                    print(f"4. Expense Payment Mode: {details['payment_mode']}")
                    print(f"5. Description: {details['description']}")
                    

            if not found:
                print("\nYour Name Not Found")

        elif user == 5:
            
            while True:
                try:
                    name = input("\nEnter Your Name: ")
                    if not name.isalpha() or len(name.strip()) < 2:
                        print("❌ Name must be alphabetic and at least 2 characters.")
                        continue

                    expense = Expense()
                    check = expense.check_name_exists(name)

                    break
                except ValueError:
                    print("❌ Please enter a valid name.")
            
            expense = Expense()
            data = expense.expense_load()
           
            if check == True:
                print("\n- How Do You Want to Search:-")
                print("\n1. Search By Date")
                print("2. Search By Category")
                
                choice = int(input("Enter Your Choice: "))

                if choice == 1:
                    while True:
                        try:
                            date_input = input("\nEnter the date (DD-MM-YYYY): ").strip()
                            if date_input[2] != '-' or date_input[5] != '-' or len(date_input) != 10:
                                print("Incorrect or Invalid Format")
                                continue

                            parsed_date = datetime.datetime.strptime(date_input, "%d-%m-%Y").date()
                            date = parsed_date.strftime("%d-%m-%Y")  # Store it in correct string format
                            break
                        except ValueError as e:
                            print("❌ Error:", str(e))
                            print("Please enter the date in correct format (DD-MM-YYYY) and ensure it's valid.")
                    
                    expense = Expense()
                    datas = expense.expense_load()
                    found = False
                    for i, data in enumerate(datas,start=1):
                        if data['date'] == date:
                            found = True

                            print(f"\nExpense {i}:-")
                            print(f"1. Date: {data['date']}")
                            print(f"2. Category: {data['category']}")
                            print(f"3. Amount: ₹{data['amount']}")
                            print(f"4. Payment Mode: {data['payment_mode']}")
                            print(f"5. Description: {data['description'] if data['description'] else 'N/A'}")

                    if not found:
                        print("Not Found")

                elif choice == 2:
                    try:
                        expense = Expense()
                        datas = expense.expense_load()
                        found = False
                        for i, data in enumerate(datas,start=1):
                            if data['category'] == category:
                                found = True
                                print(f"\nExpense {i}:-")
                                print(f"1. Date: {data['date']}")
                                print(f"2. Category: {data['category']}")
                                print(f"3. Amount: ₹{data['amount']}")
                                print(f"4. Payment Mode: {data['payment_mode']}")
                                print(f"5. Description: {data['description'] if data['description'] else 'N/A'}")
                        
                        if not found:
                            print("Not Found")

                    except:
                        pass

            else:
                print("Name Not Found")


        elif user == 6:
            while True:
                try:
                    name = input("\nEnter Your Name For Analysis: ").strip().lower()
                    if not name.isalpha() or len(name) < 2:
                        print("Name must be alphabetic and at least 2 characters.")
                        continue

                    expense = Expense()
                    check = expense.check_name_exists(name)
                    if not check:
                        print("Name Not Found")
                        break
                    break
                except ValueError:
                    pass
            
            
            if check:
                expense = Expense()
                data = expense.expense_load()

                def filter(to_filter,name): 
                    filter = [e[to_filter] for e in data if e['name'].lower() == name]
                    return filter
                
                category = filter("category",name)
                payment_mode = filter("payment_mode", name)
                amount = filter("amount", name)
                date = filter("date",name)
                dict = {
                    "Category": category,
                    "Payment_mode": payment_mode,
                    "Amount": amount,
                    "Date": date
                }
                if len(dict['Category']) > 2:

                    df = pd.DataFrame(dict, columns=["Category","Payment_Mode","Amount","Date"])

                    max_expense = df['Amount'].max()
                    max_spender = df[df['Amount'] == max_expense]
                    print(f"\n💰 Highest Expense Amount: ₹{max_expense}")
                    print(f"📦 Category of Max Expense: {max_spender['Category'].values[0]}")
                    print(f"📅 Date: {max_spender['Date'].values[0]}")

                    min_expense = df['Amount'].min()
                    min_spender = df[df['Amount'] == min_expense]
                    print(f"\nLowest Expense Amount: ₹{min_expense}")
                    print(f"Category of Min Expense: {min_spender['Category'].values[0]}")
                    print(f"📅 Date: {min_spender['Date'].values[0]}")
                    
                    most_used = df['Category'].value_counts().idxmax()
                    print(f"\n📌 Most Frequent Category: {most_used}")

                    cat_total = df.groupby('Category')['Amount'].sum()
                    max_spent_cat = cat_total.idxmax()
                    print(f"\n💸 Highest Spending Category: {max_spent_cat}")
                    
                    df['date'] = pd.to_datetime(df['Date'], dayfirst=True)
                    most_active_day = df['Date'].value_counts().idxmax()
                    print(f"\n📆 Most Active Spending Day: {most_active_day}")

                    print("\n📊 Summary:")
                    print(f"\nTotal Spent: ₹{df['Amount'].sum()}")
                    print(f"Average Expense: ₹{df['Amount'].mean():.2f}")
                    print(f"Number of Expenses: {df.shape[0]}")

                    print("\n- Want to See the Analysis In Graph")
                    print("\n1. Yes")
                    print("2. No")

                    try:
                        choice = int(input("Enter Your Choice: "))
                        if choice not in [1,2]:
                            print("Invalid Input")
                            continue
                        break
                    except ValueError:
                        pass

                    if choice == 1:
                        
                        category_counts = pd.Series(dict['Category']).value_counts()
                        plt.pie(category_counts.values, labels=category_counts.index, autopct="%1.1f%%", startangle=130)
                        plt.title("Monthly Expenses by Category")
                        plt.xlabel("Categories")
                        plt.show()
                        
                        plt.pie(dict['Payment_mode'],autopct="%1.1f%%", startangle=130)
                        plt.title("Monthly Expenses by Payment Mode")
                        plt.xlabel("Modes")
                        plt.show()

                        plt.boxplot(dict['Amount'])
                        plt.xlabel("Amount")
                        plt.title("Distribution of Amount by Boxplot")
                        plt.show()
                        
                        # Group by Category and sum the Amounts
                        head_amount = df.groupby('Category')['Amount'].sum()

                        # Plotting the bar chart
                        plt.figure(figsize=(10,6))
                        head_amount.plot(kind='bar', color="purple")
                        plt.title("💰 Total Expenses per Category")
                        plt.xlabel("Expense Category")
                        plt.ylabel("Total Amount (₹)")
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.show()
                        

                        count_amount = df['Category'].value_counts()

                        plt.figure(figsize=(10,6))
                        count_amount.plot(kind='bar', color="purple")
                        plt.title("📊 Number of Expenses per Category")
                        plt.xlabel("Expense Category")
                        plt.ylabel("Count of Expenses")
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.show()

                        plt.figure(figsize=(10,6))
                        plt.hist(df['Amount'], bins=10, color='skyblue', edgecolor='black')
                        plt.title("💵 Distribution of Expense Amounts")
                        plt.xlabel("Expense Amount (₹)")
                        plt.ylabel("Number of Expenses")
                        plt.grid(True, linestyle='--', alpha=0.5)
                        plt.tight_layout()
                        plt.show()
                    
                    elif choice == 2:
                        break

                elif len(dict['Category']) < 2:
                    print("You have not enough expenses for analysis")
                    print("\nPlease Add More Expenses for Analysis")

                elif len(dict['Category']) == 0:
                    print("\nNo Expenses Found for Analysis")
                    print("Please Add New Expenses For Analysis")

                else:
                    pass

        elif user == 7:
            
            while True:
                try:
                    name = input("\nEnter Your Name For Analysis: ").strip().lower()
                    if not name.isalpha() or len(name) < 2:
                        print("Name must be alphabetic and at least 2 characters.")
                        continue

                    expense = Expense()
                    check = expense.check_name_exists(name)
                    if not check:
                        print("Name Not Found")
                        break
                    break
            
                except ValueError:
                    pass
            
            if check: #if the check == True: 

                expense = Expense()
                data = expense.expense_load()

                def filter(to_filter, name):
                    return [e[to_filter] for e in data if e['name'].lower() == name]

                category = filter("category", name)
                payment_mode = filter("payment_mode", name)
                amount = filter("amount", name)
                date = filter("date", name)

                dict_exp = {
                    "Category": category,
                    "Payment_mode": payment_mode,
                    "Amount": amount,
                    "Date": date
                }

                df = pd.DataFrame(dict_exp)
                df["Date"] = pd.to_datetime(df["Date"], format='%d-%m-%Y')
                df["Month"] = df["Date"].dt.month
                df["Month_Name"] = df["Date"].dt.strftime("%B")
                df["Year"] = df["Date"].dt.year

                while True:
                    print("\nMonthly Analysis:- ")
                    print("------------------------------")
                    print("\nChoose how you want to analyze:")
                    print("\n1. Analyze Last Month Automatically")
                    print("2. Choose Month & Year Manually")
                    print("3. Back to Main Menu")

                    while True:
                        try:
                            choice = int(input("Enter Your Choice: "))
                            if choice not in [1,2,3]:
                                print("Invalid Input")
                                continue
                            break
                        except ValueError:
                            pass
                    
                    if choice == 3:
                        break


                    if choice == 1:
                        #now = datetime.datetime.now()
                        #month_name = now.strftime("%B") # Example output: July
                        #year = now.strftime("%Y")
                        today = datetime.datetime.today()
                        if today.day <= 5:
                            print(f"\n🗓️ You're early in {today.strftime('%B')} (only {today.day} days passed).")
                            print("Do you want to:")
                            print("1. Analyze This Month So Far")
                            print("2. Analyze Full Previous Month")
                            pass # just ignore this choice for now

                    elif choice == 2:
                        try:
                            selected_month = int(input("Enter Month (1-12): "))
                            selected_year = int(input("Enter Year (e.g. 2025): "))
                            if selected_month < 1 or selected_month > 12:
                                print("❌ Invalid month.")
                                continue
                        except ValueError:
                            print("❌ Invalid input.")
                            continue

                        month_df = df[(df["Month"] == selected_month) & (df["Year"] == selected_year)]

                        if month_df.empty:
                            print("⚠️ No data found for selected period.")

                        print("Monthly Summary and Detailed Analysis")

                        max_expense = month_df['Amount'].max()
                        max_spender = month_df[month_df['Amount'] == max_expense]
                        print(f"\n💰 Highest Expense Amount of this Month: ₹{max_expense}")
                        print(f"📦 Category of Max Expense of this Month: {max_spender['Category'].values[0]}")
                        print(f"📅 Date: {max_spender['Date'].values[0]}")
                        
                        min_expense = month_df['Amount'].min()
                        min_spender = month_df[month_df['Amount'] == min_expense]
                        print(f"\nLowest Expense Amount of this Month: ₹{min_expense}")
                        print(f"Category of Min Expense of this Month: {min_spender['Category'].values[0]}")
                        print(f"📅 Date: {min_spender['Date'].values[0]}")

                        most_used = month_df['Category'].value_counts().idxmax()
                        print(f"\n📌 Most Frequent Category of this Month: {most_used}")

                        cat_total = month_df.groupby('Category')['Amount'].sum()
                        max_spent_cat = cat_total.idxmax()
                        print(f"\n💸 Highest Spending Category of this Month: {max_spent_cat}")

                        print("\n📊 Summary:")
                        print(f"\nTotal Spent of this Month: ₹{month_df['Amount'].sum()}")
                        print(f"Average Expense of this Month: ₹{month_df['Amount'].mean():.2f}")
                        print(f"Number of Expenses of this Month: {month_df.shape[0]}")
                        print(f"Standard Deviation of this Month: {month_df['Amount'].std()}")

                        print("\n- Want to See the Analysis In Graph")
                        print("\n1. Yes")
                        print("2. No")

                        try:
                            choice = int(input("Enter Your Choice: "))
                            if choice not in [1,2]:
                                print("Invalid Input")
                                continue
                        except ValueError:
                            pass

                        if choice == 1:
                            category_counts = pd.Series(dict['Category']).value_counts()
                            plt.pie(category_counts.values, labels=category_counts.index, autopct="%1.1f%%", startangle=130)
                            plt.title("Monthly Expenses by Category")
                            plt.xlabel("Categories")
                            plt.show()
                            
                            plt.pie(dict['Payment_mode'],autopct="%1.1f%%", startangle=130)
                            plt.title("Monthly Expenses by Payment Mode")
                            plt.xlabel("Modes")
                            plt.show()

                            plt.boxplot(dict['Amount'])
                            plt.xlabel("Amount")
                            plt.title("Distribution of Amount by Boxplot")
                            plt.show()
                            
                            # Group by Category and sum the Amounts
                            head_amount = df.groupby('Category')['Amount'].sum()

                            # Plotting the bar chart
                            plt.figure(figsize=(10,6))
                            head_amount.plot(kind='bar', color="purple")
                            plt.title("💰 Total Expenses per Category")
                            plt.xlabel("Expense Category")
                            plt.ylabel("Total Amount (₹)")
                            plt.xticks(rotation=45)
                            plt.tight_layout()
                            plt.show()
                            

                            count_amount = df['Category'].value_counts()

                            plt.figure(figsize=(10,6))
                            count_amount.plot(kind='bar', color="purple")
                            plt.title("📊 Number of Expenses per Category")
                            plt.xlabel("Expense Category")
                            plt.ylabel("Count of Expenses")
                            plt.xticks(rotation=45)
                            plt.tight_layout()
                            plt.show()

                            plt.figure(figsize=(10,6))
                            plt.hist(df['Amount'], bins=10, color='skyblue', edgecolor='black')
                            plt.title("💵 Distribution of Expense Amounts")
                            plt.xlabel("Expense Amount (₹)")
                            plt.ylabel("Number of Expenses")
                            plt.grid(True, linestyle='--', alpha=0.5)
                            plt.tight_layout()
                            plt.show()
                        
                        else:
                            pass


        elif user == 8:
            while True:
                try:
                    name = input("\nEnter Your Name For Analysis: ").strip().lower()
                    if not name.isalpha() or len(name) < 2:
                        print("Name must be alphabetic and at least 2 characters.")
                        continue
                    expense = Expense()
                    check = expense.check_name_exists(name)
                    if not check:
                        print("Name Not Found")
                        break
                    break
                except ValueError:
                    pass
            
            if check:
                print("\n- Rank Analysis:-")
                print("- Select a Category for Showing")
                print("1. Rank Categories by Total Spending")
                print("2. Rank by Frequency (Number of Times a Category was Used)")
                print("3. Rank by Average Expense per Category")
                print("4. Rank Payment Modes by Usage")
                print("5. Rank Dates by Highest Total Spending")

                expense = Expense()
                data = expense.expense_load()

                def filter(to_filter,name): 
                    filter = [e[to_filter] for e in data if e['name'].lower() == name]
                    return filter
                
                category = filter("category",name)
                payment_mode = filter("payment_mode", name)
                amount = [float(e["amount"]) for e in data if e["name"].lower() == name]
                date = filter("date",name)
                dict = {
                    "Category": category,
                    "Payment_mode": payment_mode,
                    "Amount": amount,
                    "Date": date
                }

                df = pd.DataFrame(dict, columns=["Category","Payment_Mode","Amount","Date"])

                if len(dict['Category']) > 3:

                    while True:
                        try:
                            choice = int(input("Enter Your Choice: "))
                            if choice not in [1,2,3,4,5]:
                                print("Invalid Input")
                                continue
                            break
                        except ValueError:
                            pass

                    
                    if choice == 1:


                        # Rank by total amount spent per category
                        category_rank = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
                        category_rank = category_rank.reset_index()
                        category_rank["Rank"] = category_rank["Amount"].rank(ascending=False)

                        print(category_rank.to_string(index=False))

                        plt.figure(figsize=(10,6))
                        plt.bar(category_rank["Category"], category_rank["Amount"], color="steelblue")
                        plt.xlabel("Total Spent")
                        plt.title("Category Rank by Total Expenses")
                        plt.tight_layout()
                        plt.show()
                    
                    elif choice == 2:
                        freq_rank = df['Category'].value_counts().reset_index()
                        freq_rank.columns = ['Category', 'Count']
                        freq_rank['Rank'] = freq_rank['Count'].rank(ascending=False)

                        print(freq_rank)


                        freq_rank = df['Category'].value_counts()
                        freq_rank.plot(kind='bar', color="purple")
                        plt.xlabel("Category")
                        plt.ylabel("Count")
                        plt.title("Most Frequently Used Categories")
                        plt.tight_layout()
                        plt.show()


                    elif choice == 3:
                        avg_rank = df.groupby("Category")["Amount"].mean().sort_values(ascending=False).reset_index()
                        avg_rank.columns = ["Category", "Average Amount"]
                        avg_rank["Rank"] = avg_rank["Average Amount"].rank(ascending=False)

                        print(avg_rank)

                    elif choice == 4:
                        mode_rank = df['Payment_mode'].value_counts().reset_index()
                        mode_rank.columns = ['Payment Mode', 'Count']
                        mode_rank["Rank"] = mode_rank["Count"].rank(ascending=False)

                        print(mode_rank)

                    elif choice == 5:
                        date_rank = df.groupby("Date")["Amount"].sum().sort_values(ascending=False).reset_index()
                        date_rank.columns = ["Date", "Total Spent"]
                        date_rank["Rank"] = date_rank["Total Spent"].rank(ascending=False)

                        print(date_rank.head(5))  # Show top 5 expensive days


        elif user == 9:
            print("👋 Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid Input")
        
    except Exception as e:
        print("Error: ",e)  
        pass                      
