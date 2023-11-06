# import mymodule
import mymodule as mm
from mymodule import person1 # from import for importing specifics

mm.greeting("Johnathan")
mm.hereWeGo("Mike", "Dreamland")
print(mm.person1["age"])
print(dir(mm)) # to list all the function names (or variable names) in a module

print(f"Welcome {person1["name"]}")