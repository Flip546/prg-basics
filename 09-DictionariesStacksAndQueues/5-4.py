winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}
suma = 0

for i,j in winter_semester.items():
    suma += j

print(f'Total number of hours: {suma}')