import re
import unittest

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def email_check(mail):   # Checking email

    if(re.search(regex,mail)):   
      
            return 'valid mail'
    else:   
        return 'Invalid mail' 


def Username(u):         # Checking Username   
 if(len(u)<6 or " "in u):
     return 'Invalid Username'
 else:
    return u 

def Password(p):         # Checking Password 

 if(len(p)<8 or p.islower() or (any(i.isdigit() for i in p)==False)):
  return 'Invalid Password'
 else:
    return p
 

from string import ascii_letters    # Checking Name
def Name(n):
 if(set(n).difference(ascii_letters)):
     return 'Invalid Name'
 else:
    return n  


def Validation (mail,u,p):          # Checking if requiered field is filled
 if(email_check(mail)!='Invalid mail' and Username(u)!='Invalid Username' and Password(p)!='Invalid Password'):
     return 'Requiered field filled'
 else:
      return 'Please enter all the requiered details'   


class Testmail(unittest.TestCase):   # Unittest for mail

 def test_email(self):
    self.assertEqual(email_check('rohan@gmail.com'),'valid mail')
    self.assertEqual(email_check('example@gmail.com'),'valid mail')
    self.assertEqual(email_check('verylongexample@gmail.com'),'valid mail')
    self.assertEqual(email_check('rohangmail.com'),'Invalid mail')
    self.assertNotEqual(email_check('not-valid@gmail.gmail'),'valid mail')
    self.assertEqual(email_check('very-long-examplegmail.com'),'Invalid mail')


class TestUsername(unittest.TestCase):  # Unittest for Username

 def test_Username(self):
    self.assertEqual(Username('Rohankr'),'Rohankr')
    self.assertEqual(Username('Rohan'),'Invalid Username')
    self.assertEqual(Username('Rohan K R'),'Invalid Username')
    self.assertNotEqual(Username('Rohan123'),'Invalid Username')    


class TestPassword(unittest.TestCase):  # Unittest for Password

 def test_Password(self):
    self.assertEqual(Password('Rohankr'),'Invalid Password')
    self.assertEqual(Password('Rohan'),'Invalid Password')
    self.assertEqual(Password('Rohan K R'),'Invalid Password')
    self.assertEqual(Password('Rohan@123'),'Rohan@123')
    self.assertNotEqual(Password('Rohan123'),'Invalid Password')


class TestName(unittest.TestCase):      # Unittest for Name

 def test_Name(self):
    self.assertEqual(Name('Rohankr'),'Rohankr')
    self.assertEqual(Name('Rohan@123'),'Invalid Name')
    self.assertEqual(Name('Rohan123)'),'Invalid Name')
    self.assertNotEqual(Name('ROHAN'),'Invalid Name')  
    

class TestValidation(unittest.TestCase):
    def test_Validation(self):
        self.assertEqual(Validation('rohan@gmail.com','Rohankr','Rohan@123'),'Requiered field filled')
        self.assertEqual(Validation('example@gmail.com','Username','Password@123'),'Requiered field filled')
        self.assertEqual(Validation('rohangmail.com','Rohan K R','Rohankr',),'Please enter all the requiered details')
        self.assertEqual(Validation('very-long-examplegmail.com','Rohan K R','Rohan123'),'Please enter all the requiered details')


if __name__=='__main__':
    unittest.main()