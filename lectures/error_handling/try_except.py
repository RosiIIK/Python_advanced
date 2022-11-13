while True:
    try:
        x = int(input("Please enter a number 1:"))
        y = int(input("Please enter a number 2:"))
        print(x/y)
        break
    except ValueError: # or except(ValueError, ZeroDivisionError):
        print("Invalid data")
    except ZeroDivisionError: #if is the second one as tuples - this is not needed anymore
        print("Invalid data")
    finally:
        print("Finally clause")
