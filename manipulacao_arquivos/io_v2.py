archive = open("persons.csv")
for register in archive:
    print("Name: {}, Age: {}".format(*register.split(",")))
archive.close()
