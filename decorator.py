# def func_needs_decorator():
#     print("I need decorator")

# def new_decorator(original_func):
#     def wrapper():
#         print("text before original function")
#         original_func()
#         print("text after original function")
#     return wrapper

# new_func = new_decorator(func_needs_decorator)
# new_func()

def new_decorator(original_func):
    def wrapper():
        print("text before original function")
        original_func()
        print("text after original function")
    return wrapper


@new_decorator
def func_needs_decorator():
    print("I need decorator")

func_needs_decorator()

