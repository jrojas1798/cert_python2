#Laboratorio 4.3.1.15
from os import strerror
counters = {chr(ch):0 for ch in range(ord('a'), ord('z')+1)}
file_name = input("Nombre: ")

try:
    f = open(file_name, "rt")
    for line in f:
        for char in line:
            if char.isalpha():
                counters[char.lower() ] +=1
    f.close()
    for char in counters.keys():
        cnt = counters[char]
        if cnt > 0:
            print(char, '->', cnt)
except IOError as e:
    print("I/O error", strerror(e.errno))
