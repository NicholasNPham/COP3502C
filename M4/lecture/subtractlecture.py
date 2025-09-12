# Calling from a different  file

from addlecture import a, b
print(b-a)

"""
import addlecture
print(addlecture.b - addlecture.a)

"""

"""
print(__name__) # Known as a printing the "dunder variable" meaning double underscore
print results:
    6             # This is printing 6 because of the addlecture.py file has a print(a + b)
    addlecture    # this is printing the name of diff file because print(__name__) exist on other file
    
                  # importing from a different file runs the whole py file resulting in 6, addlecture
                  
    2             # prints 2 because of this file
    __main__      # prints __name__ because its running the top file being ran.

"""

def main():
    print(b-a)
    print("This is the file i want to run")

if __name__ == "__main__":
    main()

print(__name__)