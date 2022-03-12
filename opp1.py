import re
class functionKeeper:
    def usernameExpector(username):  
            usernametogather=username[0]+username[1]
            x=re.findall("[a-zA-Z]",usernametogather)
            if( len(username[0])==0 or len(username[1])==0 or len(x)==len(usernametogather) ):
                raise Exception ("invalid Username")
            else:
                EnteredUsernameInTwoLine=username[0]+"\n"+username[0]
                return(EnteredUsernameInTwoLine)
                

    def passwordExpector(password):
            passLowerCase=re.findall("[a-z]",password)
            passupperCase=re.findall("[A-Z]",password)
            passnumber=re.findall("[0-9]",password)
            if( len(password)<8 or passLowerCase==0 or passupperCase==0  or passnumber==0):
                    raise Exception ("invalid password")
            else:
                return(password)
                
  
    def phoneNumberExpector(phonrNumber):
            if(phonrNumber[0]=="+"):
                phonrNumber=phonrNumber[2:]
                
            phoneNumberCount=re.findall("[0-9]",)
            
            if( len(phonrNumber)<=11 or len(phonrNumber)==0 or len(phoneNumberCount)!=len(phonrNumber) or phonrNumber[1]!="9" ):
                    raise Exception ("invalid phonrNumber")
            else:
                return(phonrNumber)
                

    def emailExpector(email):
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if(re.fullmatch(regex, email) ):
                   return(email)
            else:
                print("invalid phonrNumber")
        
                
class account:
     def __init__(self,username,password,phonrNumber,email) : 
         self.username=functionKeeper.usernameExpector(username)
         self.password=functionKeeper.passwordExpector(password)
         self.phonrNumber=functionKeeper.phoneNumberExpector(phonrNumber)      
         self.email=functionKeeper.emailExpector(email)
                 
class site:
    def __init__(self,URL_adress,register_user,active_user) :
        self.register_user=[]
        self.active_user=[]
        self.URL_adress=URL_adress
        
    def register():
        pass
    
    def login():
        pass
    def logout():
        pass
    
    

'''

EnteredUserFirstName=input("please enter your first name : ")
EnteredUsersecondName=input("please enter your last name : ")
username=[EnteredUserFirstName,EnteredUsersecondName]
EnteredPassword=input("please enter your password : ")
EnteredPhoneNumber=input("please enter your phone number : ")
EnteredEmail=input("please enter your email address : ")

firstRun= account(username,EnteredPassword,EnteredPhoneNumber,EnteredEmail)
'''
firstRun=account(["fatemeh","fazlali"],"12345678Aa","09184913796","fatemeh@gmail.com")
firstRun.usernameExpector()







