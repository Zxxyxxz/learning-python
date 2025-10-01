def test_exception_flow(num):
    print(f"Starting with {num}")
    try:
        print("About to divide...")
        result = 10 / num
        print(f"Success! Result is {result}")
        return result
    except ZeroDivisionError:
        print("Caught division by zero!")
        return -1
    print("This line will never print if exception occurs")
    
def test_exception_flow_2(num):
    print(f"Starting with {num}")
    try:
        print("About to divide...")
        result = 10 / num
        print(f"Success! Result is {result}")
    except ZeroDivisionError:
        print("Caught division by zero!")
    print("This line will never print if exception occurs")
    return "Done"

if __name__ == "__main__":
    print(test_exception_flow(2))
    print(test_exception_flow(0))
    print(test_exception_flow_2(2))
    print(test_exception_flow_2(0))