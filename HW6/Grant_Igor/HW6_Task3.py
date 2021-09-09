text = "Some random text"
count = {}
for i in text:
    count[i] = count.setdefault(i, 0) + 1
print(count)
