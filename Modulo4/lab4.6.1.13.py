import calendar
class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        current_mes = 1
        numero_de_dias = 1
        while(current_mes <= 12):
            for data in self.monthdays2calendar(year, current_mes):
                if data[weekday][0] != 0:
                    numero_de_dias = numero_de_dias + 1

            current_mes = current_mes +1
        return numero_de_dias
mi_calendario = MyCalendar()
numero_de_dias = mi_calendario.count_weekday_in_year(2019, calendar.MONDAY)

print(numero_de_dias)