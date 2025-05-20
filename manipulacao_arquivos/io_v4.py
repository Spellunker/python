try:

    archive = open("persons.csv")
    for register in archive:
        print("Name: {}, Age: {}".format(register.strip().split(",")))
except IndexError:
    pass
finally:
    print("Finally")
    archive.close()

if archive.closed:
    print("Archive already closed")