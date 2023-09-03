def add(m,n):
    return round(m+n,3)

def sub(m,n):
    return m-n

def mul(m,n):
    return m*n
    
def div(m,n):
    if n == 0:
        return ("Zero is Not divisible")
    return m/n

def remain(m,n):
    return m % n

def power(m,n):
    return m ** n
    
def main():
    print("{}\nBasic Calculator\n{}".format("-"*16,"-"*16))
    while True:
        print("\nChoose the below operation")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Remainder")
        print("6.power")
        
        option_choosing = input("Select the operations:  ")
        
        a = float(input("First Input: "))
        b = float(input("Secound Input: "))
        
        if option_choosing == "1":
            print("{} + {} = {} ".format(a, b, add(a,b)))
            
        elif option_choosing == '2':
            print("{} - {} = {} ".format(a, b, sub(a,b)))
        
        elif option_choosing == "3":
            print("{} * {} = {} ".format(a, b, mul(a,b)))
            
        elif option_choosing == "4":
            print("{} / {} = {} ".format(a, b, div(a,b)))
            
        elif option_choosing == "5":
            print("{} % {} = {} ".format(a, b, remain(a,b)))
            
        elif option_choosing == "6":
            print("{} ^ {} = {} ".format(a, b, power(a,b)))
        
        else:
            print("select the proper option")
        
main()