Data={"PRIYANSHU JHA":9518476761,"SUNIL KUMAR MEHTA":123456789,"PRINCE":8974563211,"AYUSH TIWARI":1234567899,"ASHUTOSH SHUKLA":1234567889,"AYUSHI BHUTANI":1234567789,"JASPAL":1234566789}

def DisplayS():
    Data2=Data
    print(Data2)
    return Data2
def SearchName():
    Nm1=input("Enter Name of Student to Search : ")
    for i in Data:
        if Nm1.upper()==i.upper():
            print("The Searach for {} is Found and his Contact No. is {}".format(i,Data[i]))
            break
    else:
        print("The Searach for {} is Not Found".format(Nm1))

def SearchCont():
    Cn1=int(input("Enter Contact No. of Student to Search : "))
    for i in Data:
        if Cn1==Data[i]:
            print("The Searach for Contact No. {} is Found and his Name is {}".format(Data[i],i))
            break
    else:
        print("The Searach for Contact No. {} is Not Found ".format(Cn1))
def Extract():
    print(Data)
    out=input("Enter Name of the Student for which Data to be Extracted or Type ALL For Complete Extraction")
    if out.upper()=="ALL":
        outf=open(r'DataExtracted.txt','w')
        for i in Data:
            conc=str(i)+','+str(Data[i])
            outf.write(conc)
        outf.close()
        print("Files Extracted Successfully and Stored in the Same Directory of the Application")
    elif out.upper()in Data:
        outf=open("DataExtracted.txt",'w')
        write_data=[]
        for i in Data:
            write_data.append(i)
            for j in Data:
                write_data.append(Data[i])
        for k in write_data:
            outf.write(k)
        outf.close()
        print("Files Extracted Successfully and Stored in the Same Directory of the Application")
    else: print("Inavlid Key Enetered")
def Dlt():
    popping=input("Enter Name of the Student to be Deleted from the Database: ")
    popping=popping.upper()
    if popping in Data:
        x=Data.pop(popping)
        print("{}:{} has been deleted from the Databse".format(popping,x))
    else:
        print("No Such Name is Found in the Directory")
def Ins():
    Ins1=input("Enter Name of the Student to be Inserted in the Database : ")
    Ins2=int(input("Enter Contact Number of the Student to be Inserted in the Database : "))
    Ins1=Ins1.upper()
    Data.update({Ins1:Ins2})
    print("{}  has been inserted in the Databse".format(Ins1))
   


print('''
 ██████╗ ██████╗ ███╗   ██╗████████╗ █████╗  ██████╗████████╗     █████╗ ██████╗ ██████╗ ██╗     ██╗ ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██║     ██║   ██║██╔██╗ ██║   ██║   ███████║██║        ██║       ███████║██████╔╝██████╔╝██║     ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██║██║        ██║       ██╔══██║██╔═══╝ ██╔═══╝ ██║     ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╗   ██║       ██║  ██║██║     ██║     ███████╗██║╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝       ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
 --------------------->"Forget the Old ways to Save & Store Your Contacts Manually , One Stop Solution to Save Your Contacts" <------------------ )
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~) VERSION 2.O ( APLHA) (~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~) 
''')
print('''
1. Search by Name
2. Search by Contact Number
3. Dispay All Contact Information
4. Register New Contact
5. Delete Registered Contact Details
6. Exit
'''  )
while True:
    ans=int(input("Enter the No. to Choose from the above List (1 - 6): "))
    if ans==1:
        SearchName()
    elif ans==2:
        SearchCont()
    elif ans==3:
        DisplayS()
    elif ans==4:
        Ins()
    elif ans==5:
        Dlt()
    elif ans==6:
        print("\n     ---------------     Thanks For Using Our Software!!!     ---------------\n")
        break
    else:print("Invalid Input, Kindly Enter Options from the Above list (1 - 6 ) !!!!!!!!!!!!!!!")
    

