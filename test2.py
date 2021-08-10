#simple if else condition

sex = str(input("Input Sex (M or F only):"))  # M or F only
age = int(input("Input Age (postive interger):"))  # postive interger
revenue = str(input("Input revenue class (A, B, C, D):")) # class

def displaySkipping():
    print("No, we're sorry.")

def displayPassing():
    print("You've been selected.")

def selection():
    if sex == "M":
        if age >= 30 and age <= 34:
            displaySkipping()
        else:
            displayPassing()

    elif sex == "F":
        if age >= 20 and age <= 34:
            if revenue == "B":
                displaySkipping()
            else:
                displayPassing()
        elif age >= 35 and age <= 39:
            if revenue in ["C", "D"]:
                displaySkipping()
            else:
                displayPassing()

        else:
            displayPassing()
    
    else:
        print("Error!!!")

selection()


