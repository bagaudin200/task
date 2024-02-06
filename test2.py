# Функция, которая возвращает количество дней в месяце в календаре ящеров
def days_in_month(year, month):
  # Массив с количеством дней в каждом месяце
  days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  # Если месяц февраль, то возвращаем 28 дней
  if month == 2:
    return 28
  # Иначе возвращаем соответствующее значение из массива
  else:
    return days[month - 1]

# Функция, которая возвращает количество дней с начала года до заданной даты в календаре ящеров
def days_from_year_start(year, month, day):
  # Счётчик дней
  count = 0
  # Добавляем количество дней в каждом месяце до заданного месяца
  for i in range(1, month):
    count += days_in_month(year, i)
  # Добавляем количество дней в заданном месяце
  count += day
  # Возвращаем счётчик
  return count

# Функция, которая возвращает количество дней между двумя датами в календаре ящеров
def days_between_dates(year1, month1, day1, year2, month2, day2):
  # Счётчик дней
  count = 0
  # Добавляем количество дней в каждом году между заданными годами
  for i in range(year1 + 1, year2):
    count += 365
  # Добавляем количество дней с начала года до конечной даты
  count += days_from_year_start(year2, month2, day2)
  # Вычитаем количество дней с начала года до начальной даты
  count -= days_from_year_start(year1, month1, day1)
  # Возвращаем счётчик
  return count

# Функция, которая возвращает количество секунд в неполном дне между двумя датами в календаре ящеров
def seconds_in_partial_day(hour1, min1, sec1, hour2, min2, sec2):
  # Счётчик секунд
  count = 0
  # Добавляем количество секунд в каждом часе между заданными часами
  for i in range(hour1 + 1, hour2):
    count += 3600
  # Добавляем количество секунд в конечном часе
  count += min2 * 60 + sec2
  # Вычитаем количество секунд в начальном часе
  count -= min1 * 60 + sec1
  # Возвращаем счётчик
  return count

# Функция, которая решает задачу
def solve(year1, month1, day1, hour1, min1, sec1, year2, month2, day2, hour2, min2, sec2):
  # Находим количество полных дней между датами
  days = days_between_dates(year1, month1, day1, year2, month2, day2)
  # Находим количество секунд в неполном дне между датами
  seconds = seconds_in_partial_day(hour1, min1, sec1, hour2, min2, sec2)
  # Выводим результат
  print(days, seconds)

# Считываем ввод
year1, month1, day1, hour1, min1, sec1 = map(int, input().split())
year2, month2, day2, hour2, min2, sec2 = map(int, input().split())

# Решаем задачу
solve(year1, month1, day1, hour1, min1, sec1, year2, month2, day2, hour2, min2, sec2)