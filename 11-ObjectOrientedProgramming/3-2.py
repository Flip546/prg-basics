# class definition
class Song:
   def __init___(self,title,author,year,age_ofauth):
      self.title =  str(title)
      self.author = str(author)
      self.year = int(year)
      self.age_ofauth = int(age_ofauth) 
      
   def __str__(self):
      return f"{self.title} {self.author} {self.year} {self.age_ofauth}"
      

# object creation
song1 = Song("Travis","Scoot",2018,21)
song2 = Song("Unknown", "Unknown", 2020, 25)


## object usage
print(song1)
print(song2)