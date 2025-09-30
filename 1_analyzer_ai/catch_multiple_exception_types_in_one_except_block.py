def test_zero():
    try:
        x = 10/0
    except (ZeroDivisionError , ValueError):
        return "Caught zero division"

def test_zero_reverse():
    try:
        x = 10/0
    except ValueError and ZeroDivisionError:
        return "Caught zero division"
        
    
def test_value():
    try:
        x = int("hello")
    except (ValueError , ZeroDivisionError):
        return "Caught value error"
    
def test_value():
    try:
        x = int("hello")
    except (ValueError ):
        return "Caught value errora"
    except(ZeroDivisionError):
        return "zero divison caught"
    
def test_bare_except_val_err():
    try:
        x=int("hello")
       
    except:
        return "bare_except"
    
def test_bare_except_zero_div_err():
    try:
        
        x=10/0
        
    except:
        return "bare_except"
    
def test_bare_except_other_err():
    try:
        
        while True:
            {
                
            }
    except:
        return "bare_except"    
    
    
def test_exception_except_val_err():
    try:
        x=int("hello")
       
    except Exception:
        return "exception_except"
    
def test_exception_except_zero_div_err():
    try:
        
        x=10/0
        
    except Exception:
        return "exception_except"
    
def test_exception_except_other_err():
    try:
        
        while True:
            {
                
            }
    except Exception:
        return "exception_except"    
def test_exception_except():
    try:
        x=int("hello")
        x=10/0
        while True:
            {
                
            }
    except Exception:
        return "exception_except"
    
def test_finally_vall_err():
    try:
        x=int("hello")
        
    finally:
        return "finally"
    
def test_finally_with_error():
    try:
        x = int("hello")
        print("This won't print")
    except ValueError:
        print("Caught ValueError")
    finally:
        print("Finally ALWAYS runs")
    print("Function continues")

def test_finally_without_error():
    try:
        x = int("42")
        print("Success!")
    except ValueError:
        print("This won't print")
    finally:
        print("Finally ALWAYS runs")
    print("Function continues")

def test_finally_with_return():
    try:
        return "From try"
    finally:
        print("Finally runs even with return!")

    
if __name__ == "__main__":
    # print(test_zero())
    # print(test_zero_reverse())
    # print(test_value())
    
    # print(test_bare_except_other_err())
    # print(test_bare_except_val_err())
    # print(test_bare_except_val_err())
    
    # print(test_exception_except_val_err())
    # print(test_exception_except_val_err())
    # print(test_exception_except_other_err())
    # print(test_finally_vall_err())
    print(test_finally_with_error())
    print("_____")
    print(test_finally_with_return())
    print("_____")

    print(test_finally_without_error())
    
    # print(test_exception_except())