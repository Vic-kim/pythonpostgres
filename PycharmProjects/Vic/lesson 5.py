import math, statistics as stats, sqlite3 as sql3


print(dir(math))

print(math.sqrt(9))

print("-----Statistics------")
print(dir(stats))
y = [56, 87, 34, 786, 900]
avg_y = stats.mean(y)
print(avg_y)

print("--------Sqlite3--------")
print(dir(sql3))

# Create a Database
conn = sql3.connect("modcom.db")
C = conn.cursor()

# Create Table
C.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
C.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY', 'RHAT', 100,35.14)")
conn.close()
