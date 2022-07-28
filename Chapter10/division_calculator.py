try:
    print(5/0) # Python will throw an error as it can't divide int by zero
except ZeroDivisionError:
    print("You can't divide by zero!") # print this when error occurs