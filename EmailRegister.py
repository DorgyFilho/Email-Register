#E-Mail Register

#Functions: YourName, YourID, Register, Show, Change, Search, Main

#P.S: The domain 'YourCorp.com' (Line 39) is just an example. 

#Global Variables.
AuxMail = [] #Filter all logins before domain
ListMail = '' #Final List with all data users.
Change = False #Indicates any changes.

#1 - YourName

def YourName(name=''):
    Name = input('Your Name and Surname: ')
    if Name == '':
        Name = name
    return Name

#2 - Your Login
def YourID(ID=''):
    Ident = input('Ident: ')
    if Ident == '':
        Ident = ID
    return Ident

def YourPass(password=''):
    Password = input('Password: ')
    if Password == '':
        Password = password
    return Password

#4 - Search Your Data.
def Search(Name):
    search = Name
    for n, e in enumerate(ListMail):
        if e[0] == search:
            return n

#5 - New User
def register():
    global AuxMail, ListMail, Change
    yourName = YourName()
    Login = YourID()
    Server = '@YourCorp.com'
    Email = Login+Server
    if Email not in AuxMail:
        PassWord = YourPass()
        # Password = input('Your Password: ')
        AuxMail.extend([yourName, Email, PassWord])
        #I used List Comprehension because I wanted to store the corresponding data to each user.
        ListMail = [AuxMail[i:i+3] for i in range(0, len(AuxMail), 3)]
        print('Email registered.')
        Change = True
    else:
        print('E-mail already registered in our server.')
        Change = False 

#6 - Change/Delete
def Confirm(op):
    while True:
        print('Do You Want to Change? Y or N')
        op = input('Answer: ').upper()
        if op in 'YN':
            return op
        else:
            print('Invalid answer. Y or N.')

#7 - Delete Your Data
def Delete():
    global ListMail, Change
    Name = YourName()
    search = Search(Name)
    if search != None:
        if Confirm('Delete') == 'Y':
            del ListMail[search]
            Change = True
    else:
        print('Name not found.')

#8 - Change Your Data
def ChangeInfo():
    global Change
    search = Search(YourName())
    if search != None:
        name = ListMail[search][0]
        email = ListMail[search][1]
        password = ListMail[search][2]
        print('Name Found!')
        Name = YourName(name)
        Password = YourPass(password)
        if Confirm('Change') == 'Y':
            ListMail[search] = [Name, email, Password]
            Change = True
    else:
        print('Name Not Found.')
        Change = False

#9 -  Show All Data
def Show():
    global ListMail
    print(ListMail)

#10 - Main Menu
def main():
    while True:
        print()
        print('Welcome to YourCorp\nChoose one of below options\n1-Add\n2-Change\n3-Delete\n4-Show List\n5-Exit')
        print()
        answer = input('Answer: ')
        if answer == '1':
            register()
        elif answer == '2':
            ChangeInfo()
        elif answer == '3':
            Delete()
        elif answer == '4':
            Show()
        elif answer == '5':
            print('Turn Off')
            break
    else:
        print('Invalid Option!')

main()

