def divide_numbers(num1, num2):
   
    try:
        return num1, num1 / num2, num2
    except ZeroDivisionError:
        return None
    
def divide_numbers_with_different_error(num1,num2):
    try:
        a=num1/num2
        return a,num2
    except ValueError:
        return None
    
if __name__ == "__main__":
    print(divide_numbers(10,0))
    print(divide_numbers_with_different_error(10,0))