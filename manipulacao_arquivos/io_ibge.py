#!/usr/bin/python3

import csv
from urllib import request


def read(url):
    with request.urlopen(url) as input:
        with open("cities.txt", "w") as output:
            print("Downloading the csv file...")
            data = input.read().decode("latin1")
            print("Download Completed!")
            for city in csv.reader(data.splitlines()[1:]):
                print(city[3], city[8], file=output)


if __name__ == "__main__":
    read(r"http://files.cod3r.com.br/curso-python/desafio-ibge.csv")
