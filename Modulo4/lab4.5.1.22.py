#Laboratorio 4.5.1.22
from datetime import datetime
date = datetime(2020, 11, 4, 14, 53)

print(date.strftime("%Y/%m/%d %H:%M:%S"))
print(date.strftime("%Y/%B/%d %H:%M:%S %p"))
print(date.strftime("%a, %Y %b %d"))
print(date.strftime("%A, %Y %B %d"))
print(date.strftime("Día del año : %j"))
print(date.strftime("Número de semana en el año : %W"))

