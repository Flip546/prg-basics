# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   
   return 25

def seats_available(seats):
   seat = 0
   for i in cinema_seats:
      for l in i:
         if l == "A":
          seat += 1
   return seat

def seats_booked(seats):
   total = 0
   for i in cinema_seats:
      for l in i:
         if l == "B":
          total += 1

         
   return total

def seat_status(seats, row, place):
   return cinema_seats[row - 1][place - 1]

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in given place, B = BOOKED A = AVAILABLE:', seat_status(cinema_seats,0,2))
