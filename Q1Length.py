# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.

x = str(input ("Input a Word:  "))
try:
    z = int(x)
    print ("Enter a Word")
except ValueError:
    y = len(x)
    print ("our input was", y, "characters long")

        
