our_string = ""
from_file = open('Zen.txt')
for line in from_file:
    our_string = str(our_string) + str(line.rstrip())
from_file.close()

print(our_string,'\n')

number_of_better = our_string.count("better")
number_of_is = our_string.count("is")
number_of_never = our_string.count("never")

print("the word 'better' is repeated %d times"%(number_of_better))
print("the word 'is' is repeated {} times".format(number_of_is))
print(f"the word 'never' is repeated {number_of_never} times\n")

print (our_string.upper(),'\n')
print (our_string.replace('i','&'))