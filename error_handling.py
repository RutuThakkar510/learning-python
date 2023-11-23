try:
    # result = 10 + '10'
    result = 10 + 10
except:
    print("Something went wrong while adding")
else:
    print(f"Add went well {result}")
finally:
    print("This will be executed every time")