entpassword = None
setpassword = None
num = 3
import re

####################################################################################################

def no_special_characters(s, pat=re.compile('[@_!#$%^&*()<>?/\|}{~:]')):
    if pat.search(s):
        #print('Valid entry! Contains special characters')
        return True
    else:
        #print("Password must contain special characters")
        return False

def no_cap_letters(s):
    if s == s.lower():
        #print('Password must contain at least 1 uppercase letter')
        return False
    else:
        #print('Valid Entry')
        return True

def no_low_letters(s):
    if s == s.upper():
        #print('Password must contain at least 1 lowercase letter')
        return False
    else:
        #print('Valid Entry')
        return True

def not_8_characters(setpassword):
    if len(setpassword) < 8:
        #print('Password must contain at least 8 characters')
        return False
    else:
        #print('Valid character count')
        return True
        
def contains_spaces(setpassword):
    if ' ' in setpassword:
        #print('Password can not contain spaces')
        return False
    else: 
        #print('Valid, no spaces')
        return True                  

def validation(setpassword):
    return no_special_characters(setpassword) and no_cap_letters(setpassword) and not_8_characters(setpassword) and contains_spaces(setpassword) and no_low_letters(setpassword)

######################################################################################################

while True:
    print ('Please set your password: ')
    setpassword = input ('>')

    if validation(setpassword):
        break

    else:
        print('Password must contain contain combination of upper and lowercase letters, no spaces, at least 8 characters, and 1 special character')

######################################################################################################

while entpassword != setpassword:
    entpassword = input ('Please enter the set password: ')

    if entpassword != setpassword:
        print('incorrect password you have', num, 'more attempt(s)')
        num = num - 1
    
    if num < 0:
        print('Too many invalid attempts. Please try again')
        break

    if entpassword == setpassword:
        print('password accepted')
        break