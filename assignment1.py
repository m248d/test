##1.1 function 1 one human year is equivalent to 7 dog years

def calculator_dog_age1(human_years):
    dog_years = human_years/ 7
    return dog_years

## test the function - Calculate the age of the dog that corresponds to a human of age 35
print(calculator_dog_age1(35))


# 1.1 function 2
def calculator_dog_age2(human_years):
    if human_years <= 2:                ### the first two human years as 10.5 dog years
        dog_years = human_years /10.5
    else:                               ### each additional human year (after first 2 years) as 4 dog years
        dog_years = ((human_years -(10.5*2))/4) + 2
    return dog_years

## test the function - Calculate the age of the dog that corresponds to a human of age 35
print(calculator_dog_age2(35))


###1.2 function to check triangle validation
def triangle_validation(x,y,z):
    if (x+y >= z) and (x+z >= y) and (y+z >= x): ###each one length must be smaller than or equal to the sum of the other two then the lengths 
        return True
    else:
        return False
      
 ###test function
triangle_validation(24,80,91)



## 1.3 Importing string library function
import string 

### Function to check whether a letter is vowel or not
def letter_check():
    ### Asking the user for input
    user_input = input("Please input a letter here: ").lower()
    
    ### Storing lowercase letters in variable letters,
    ###this list will help to find the letter that comes before the indicated letter in the alphabet
    letters = list(string.ascii_lowercase)
    
    ### check condition
    if user_input in 'aeiou':
        print("You enter a vowel, " "the letter that comes before is", (letters[letters.index(user_input)-1]))
    elif user_input == 'y':
        print("sometimes y is a vowel, and sometimes y is a consonant")
    else:
        print("You enter a consonant, " "the letter that comes before is", (letters[letters.index(user_input)-1]))
        
  ### test function
letter_check()
