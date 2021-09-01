import contextlib, io

zen = io.StringIO()
with contextlib.redirect_stdout(zen):
    import this

zen_of_python = zen.getvalue()

search_a_word = zen_of_python.count("better")
print("better used: ", search_a_word)

search_a_word = zen_of_python.count("never")
print("never used: ", search_a_word)

search_a_word = zen_of_python.count("is")
print("is used: ", search_a_word, '\n')

print(zen_of_python.upper(), '\n')

print(zen_of_python.replace('i', '&'))