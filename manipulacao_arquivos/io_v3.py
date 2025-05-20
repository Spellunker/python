archive = open("persons.csv")
for register in archive:
    print("Name: {}, Age: {}".format(*register.strip().split(",")))

archive.close()
