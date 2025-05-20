archive = open("persons.csv")
data = archive.read()
archive.close()
for register in data.splitlines():
    print("Name: {}, Age: {}".format(*register.split(",")))
