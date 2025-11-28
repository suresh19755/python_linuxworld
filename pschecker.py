#--simple positive,neagtive or zero checker
while True:
    def numbercheck():
    
        try:
            number = float(input("enter a number:"))
            if number > 0:
                print("the number is positive.")
            elif number < 0:
                print("the number is negative.")
            else: 
                print("the number is zero0")
             
        except ValueError:
            print("please enter a valid number!.")
        
    if __name__ == "__main__":
        numbercheck()
            