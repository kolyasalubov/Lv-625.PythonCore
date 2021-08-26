import sys
def vyvodDannyh(your_name_,your_age_,your_city_):
    print('Hello %s Your age is %s You live in  %s' %(your_name_,your_age_,your_city_))
print('What is your name')
your_name=sys.stdin.readline()
print('How old are you?')
your_age=sys.stdin.readline()
print('Where do you live?')
your_city=sys.stdin.readline()

vyvodDannyh(your_name,int(your_age),your_city)