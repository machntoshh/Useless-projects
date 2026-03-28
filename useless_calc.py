def useless_calculator():
    think_calc_think = []
    
    while True:
        first_number = int(input("Ahh, what's the first number? "))
        operator = input("*gulp* the operator?? ")
        last_number = int(input("And the second number? "))
        
        if operator not in ["+", "-", "*", "/"]:
            print("duh dummy, I need real O P E R A T O R S, get it?")
            return

        if operator == "+":
            result = first_number + last_number
        elif operator == "-":
            result = first_number - last_number
        elif operator == "*":
            result = first_number * last_number
        elif operator == "/":
            result = first_number / last_number
            
        think_calc_think.append(f"{first_number}{operator}{last_number}")
        count_times = think_calc_think.count(f"{first_number}{operator}{last_number}")
        
        if count_times == 3:
            print("This again bruv??")
        elif count_times == 5:
            print("bro... you know what, i'll just crash the program ok?")
            raise RuntimeError("An unexpected error occurred. (my patience runned out)")
            
        if operator == "+" and result <= 5:
            print(f"Guess its {result} right?")
        elif operator == "-" and result <= 5:
            print(f"Huh... {result} right?")
        elif operator == "*" and result <= 5:
            print(f"may... maybe... {result} right?")
        elif operator == "/" and result <= 5:
            print(f"dang... this one is hard... maybe... {result} right?")
        else:
            print("idk man, google or stmh")
        
        wisdom = input("Need my wisdom again? ")
        
        if wisdom not in ["yes", "yea", "sure", "y"]:
            break
            
        
        
        
useless_calculator()