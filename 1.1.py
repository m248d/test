"""1.1.1 function 1 one human year is equivalent to 7 dog years"""
def calculator_dog_age1(human_years):
   dog_years = human_years* 7
   return dog_years
"""test the function - Calculate the age of the dog that corresponds to a human of age 35"""
print(calculator_dog_age1(35))

"""1.1.2 function 2"""
def calculator_dog_age2(human_years):
   if human_years <= 2:
      dog_years = human_years * 10.5   """the first two human years as 10.5 dog years"""
   else:
      dog_years = ((human_years - 2)*4) + 10.5*2  """each additional human year (after first 2 years) as 4 dog years"""
   return dog_years
"""test the function - Calculate the age of the dog that corresponds to a human of age 35"""
print(calculator_dog_age2(35))


"""1.2. function to check triangle validation"""
def triangle_validation(x,y,z):
   if x+y >= z and x+z >= y and y+z >= x: """each one length must be smaller than or equal to the sum of the other two then the lengths"""
      return True
   else:
      return False
   
  """1.3 importing string library function"""
import string 

"""Asking the user for input"""
letter = input('please enter a letter here: ').lower()

"""checking condition"""
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter, "is a vowel", f"the letter that comes before is {string.ascii_lowercase[string.ascii_lowercase.index(letter)-1]}")
elif letter == 'y':
    print('sometimes y is a vowel, and sometimes y is a consonant')
else:
    print(letter, "is a consonant", f"the letter that comes before is {string.ascii_lowercase[string.ascii_lowercase.index(letter)-1]}")
