#Rohit Rai
#Vidhik Dang
#Class X11-B
import mysql.connector
def cont():
    y=int(input("DO YOU WANT TO GO BACK TO MENU\nPRESS 1 FOR YES\nPRESS 2 TO EXIT:"))
    if(y==1):
        print("OK")
        i=1
    elif(y==2):
        print("GOOD BYE")
        exit()
    else:
        print("WRONG OPTION SELECTED")
r=0
while r==0:
    try:
        f=mysql.connector.connect(host="localhost",user="root",passwd="tiger")
        c=f.cursor()
        c.execute("CREATE DATABASE eshop")
        c.execute("USE eshop")
        c.execute("CREATE TABLE REVIEW(Name char(30) not null, E_Mail char(30) Primary Key, Star_Rating int not null, Review char(50) not null)")
        c.execute("CREATE TABLE HEADPHONES(Model_Name char(30) Primary Key, Brand_Name char(30) not null, Wired_Or_Wireless char(10) not null, Colour char(20) not null, Mrp int not null, Play_Time int not null, Bluetooth char(30) not null, Packaging_Content char(50) not null)")
        c.execute("CREATE TABLE EARPHONES(Model_Name char(30) Primary Key, Brand_Name char(30) not null, Wired_Or_Wireless char(10) not null, Colour char(20) not null, Mrp int not null, Play_Time int not null, Bluetooth char(30) not null, Packaging_Content char(50) not null)")
        c.execute("CREATE TABLE FRIDGE(Model_Name char(30) Primary Key, Brand_Name char(30) not null, Mrp int not null, Number_Of_Door_Pocket int not null, Inverter_Campatibility char(50) not null, Convertable char(50) not null, Colour char(20) not null, Star_Rating int not null, Litres char(20) not null, Packaging_Content char(50) not null)")
        c.execute("CREATE TABLE BOOKING(Name char(30) not null, E_Mail char(30) Primary Key, Model_Name char(20) not null, Add char(50) not null, Pno int not null)")
        break
    except:
        break
i=0
j=0
while i<=0:
    print(" -------------------------------------------------------------M E N U-------------------------------------------------------------")
    print("|                                       1. OPTIONS FOR STAFF                                                                      |")
    print("|                                       2. TO CHECK FOR AN ITEM AND BOOKING                                                       |")
    print("|                                       3. CANCELLING ORDER                                                                       |")
    print("|                                       4. READ AND WRITE REVIEW                                                                  |")
    print("|                                       5. EXIT                                                                                   |")
    print(" ---------------------------------------------------------------------------------------------------------------------------------")
    t=0
    while(t==0):
        try:
            x=int(input("ENTER THE OPTION NUMBER:"))
            break
        except ValueError:
            print("ONLY INTEGER OPTIONS!!!")
            continue
        except:
            print("SOME ERROR HAS OCCURED PLEASE ENTER AGAIN!!!")
            continue
    if(x==1):
        for c in range(2,-1,-1):
            if(j==0):
                a=input("ENTER THE PASSWORD(HINT-TWO ALPHABETS):")
                if(a=="vr"):
                    print("WELCOME!!!")
                else:
                    if(c>0):
                        print("WRONG PASSWORD!!!")
                        print("YOU ARE STILL LEFT WITH",c,"TRIES!!!")
                        o=input("PRESS 1 TO RETRY\nPRESS 2 TO EXIT TO MENU\nPRESS ANY KEY TO EXIT THE PROGRAM:")
                        if(o=="1"):
                            print("OK")
                            continue
                        elif(o=="2"):
                            print("OK")
                            break
                        else:
                            print("GOOD BYE!!!")
                            exit()
                    elif(c==0):
                        print("WRONG PASSWORD!!!")
                        print("LOCKING")
                        j=1
                        break
            else:
                print("SORRY!!! MANY ATTEMPTS MADE.....")
                break
            print(" ----------------------------------------- S T A F F -- M E N U ------------------------------------------------------------------")
            print("|                                            1. TO ADD AN ITEM                                                                    |")
            print("|                                            2. TO DELETE AN ITEM                                                                 |")
            print("|                                            3. TO DELETE AN ORDER                                                                |")
            print("|                                            4. TO DELETE A REVIEW                                                                |")
            print("|                                            5. EXIT TO MENU                                                                      |")
            print(" ---------------------------------------------------------------------------------------------------------------------------------")
            so=int(input("ENTER OPTION NUMBER:"))
            if(so==1):
                print(" ---------------------------------------------------------------------------------------------------------------------------------")
                print("|  SELECT THE TYPE OF ITEM:\n|   1. MOBILE\n|   2. LAPTOP\n|   3. HEADPHONES\n|   4. EARPHONES\n|   5. FRIDGE")
                print(" ---------------------------------------------------------------------------------------------------------------------------------")
                g=input("ENTER THE TYPE NUMBER:")
                if(g=="3"):
                    #ENTERING ITEMS FOR HEADPHONES
                    f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
                    c=f.cursor()
                    mn=input("ENTER MODEL NAME:")
                    bn=input("ENTER BRAND NAME:")
                    type3="HEADPHONES"
                    w=input("PRESS 1 IF HEADPHONES ARE WIRED OR PRESS 2 IF HEADPHONES ARE WIRELESS:")
                    if(w=="1"):
                        w1="WIRED"
                    elif(w=="2"):
                        w1="WIRELESS"
                    else:
                        w1="NOT ENTERED"
                    col=input("ENTER THE COLOUR OF HEADPHONES:")
                    mrp=float(input("ENTER THE PRICE OF HEADPHONES:"))
                    pt=int(input("ENTER THE PLAY TIME OF HEADPHONES IN MINUTES:"))
                    blu=input("ENTER THE BLUETOOTH VERSION:")
                    pk=input("ENTER THE PACKAGING CONTENT:")
                    t=(mn,bn,w1,col,mrp,pt,blu,pk)
                    str1="""INSERT INTO HEADPHONES (Model_Name, Brand_Name, Wired_or_Wireless, Colour, Mrp, Play_Time, Bluetooth, Packaging_Content) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
                    c.execute(str1,t)
                    f.commit()
                    print("DONE!!!")
                    cont()
                    break
                elif(g=="4"):
                    #ENTERING ITEMS FOR EARPHONES
                    f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
                    c=f.cursor()
                    mn=input("ENTER MODEL NAME:")
                    bn=input("ENTER BRAND NAME:")
                    w=input("PRESS 1 IF EARPHONES ARE WIRED OR PRESS 2 IF EARPHONES ARE WIRELESS:")
                    if(w=="1"):
                        w1="WIRED"
                    elif(w=="2"):
                        w1="WIRELESS"
                    else:
                        w1="NOT ENTERED"
                    col=input("ENTER THE COLOUR OF EARPHONES:")
                    mrp=float(input("ENTER THE PRICE OF EARPHONES:"))
                    pt=int(input("ENTER THE PLAY TIME OF EARPHONES IN MINUTES:"))
                    blu=input("ENTER THE BLUETOOTH VERSION:")
                    pk=input("ENTER THE PACKAGING CONTENT:")
                    t=(mn,bn,w1,col,mrp,pt,blu,pk)
                    str1="""INSERT INTO EARPHONES (Model_Name, Brand_Name, Wired_or_Wireless, Colour, Mrp, Play_Time, Bluetooth, Packaging_Content) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
                    c.execute(str1,t)
                    f.commit()
                    print("DONE!!!")
                    cont()
                    break
                elif(g=="1"):
                    #ENTERING ITEMS FOR MOBILE
                    f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
                    c=f.cursor()
                    mn=input("ENTER MODEL NAME:")
                    bn=input("ENTER BRAND NAME:")
                    cont()
                    break
                elif(g=="2"):
                    #ENTERING ITEMS FOR LAPTOP
                    f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
                    c=f.cursor()
                    mn=input("ENTER MODEL NAME:")
                    bn=input("ENTER BRAND NAME:")
                    cont()
                    break
                elif(g=="5"):
                    #ENTERING ITEMS FOR FRIDGE
                    f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
                    c=f.cursor()
                    mn=input("ENTER MODEL NAME:")
                    bn=input("ENTER BRAND NAME:")
                    mrp=float(input("ENTER THE PRICE OF FRIDGE:"))
                    ndp=input("ENTER THE NUMBER OF DOOR POCKETS:")
                    ic=input("ENTER THE INVERTER COMPATIBILITY:")
                    cv=input("ENTER IF IT IS CONVERTABLE:")
                    col=input("ENTER THE COLOUR:")
                    st=int(input("ENTER THE STAR RATING:"))
                    l=input("ENTER THE LITRES:")
                    pk=input("ENTER THE PACKAGING CONTENT:")
                    t=(mn,bn,mrp,ndp,ic,cv,col,st,l,pk)
                    str1="""INSERT INTO FRIDGE (Model_Name, Brand_Name, Mrp, Number_Of_Door_Pocket, Inverter_Campatibility, Convertable, Colour, Star_Rating, Litres, Packaging_Content) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                    c.execute(str1,t)
                    f.commit()
                    print("DONE!!!")
                    cont()
                    break
            elif(so==2):
                #DELETING AN ITEM
                f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
                c=f.cursor()
                print(" ---------------------------------------------------------------------------------------------------------------------------------")
                print("|  SELECT THE TYPE OF ITEM:\n|   1. MOBILE\n|   2. LAPTOP\n|   3. HEADPHONES\n|   4. EARPHONES\n|   5. FRIDGE")
                print(" ---------------------------------------------------------------------------------------------------------------------------------")
                g=input("ENTER THE TYPE NUMBER:")
                if(g=="3"):
                    #DELETING AN ITEM FROM HEADPHONES
                    f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
                    c=f.cursor()
                    stris="SELECT Model_Name,Brand_Name,Mrp FROM HEADPHONES"
                    c.execute(stris)
                    r=c.fetchall()
                    for z in r:
                        print("--------------------------")
                        print("MODEL NAME=",z[0])
                        print("BRAND NAME=",z[1])
                        print("PRICE=",z[2])
                        print("--------------------------")
                    mr=input("ENTER THE MODEL NAME OF ITEM WHICH YOU WANT TO DELETE:")
                    ste="DELETE FROM HEADPHONES WHERE Model_Name=%s"
                    c.execute(ste,(mr,))
                    print("DONE!!!")
                    f.commit()
                    cont()
                    break
                elif(g=="4"):
                    #DELETING AN ITEM FROM EARPHONES
                    f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
                    c=f.cursor()
                    stris="SELECT Model_Name,Brand_Name,Mrp FROM EARPHONES"
                    c.execute(stris)
                    r=c.fetchall()
                    for z in r:
                        print("--------------------------")
                        print("MODEL NAME=",z[0])
                        print("BRAND NAME=",z[1])
                        print("PRICE=",z[2])
                        print("--------------------------")
                    mr=input("ENTER THE MODEL NAME OF ITEM WHICH YOU WANT TO DELETE:")
                    ste="DELETE FROM EARPHONES WHERE Model_Name=%s"
                    c.execute(ste,(mr,))
                    print("DONE!!!")
                    f.commit()
                    cont()
                    break
                elif(g=="5"):
                    #DELETING AN ITEM FROM FRIDGE
                    f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
                    c=f.cursor()
                    stris="SELECT Model_Name,Brand_Name,Mrp FROM FRIDGE"
                    c.execute(stris)
                    r=c.fetchall()
                    for z in r:
                        print("--------------------------")
                        print("MODEL NAME=",z[0])
                        print("BRAND NAME=",z[1])
                        print("PRICE=",z[2])
                        print("--------------------------")
                    mr=input("ENTER THE MODEL NAME OF ITEM WHICH YOU WANT TO DELETE:")
                    ste="DELETE FROM FRIDGE WHERE Model_Name=%s"
                    c.execute(ste,(mr,))
                    print("DONE!!!")
                    f.commit()
                    cont()
                    break
            elif(so==3):
                f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
                c=f.cursor()
                print("ALL PENDING ORDERS--")
                c.execute("SELECT * FROM BOOKING")
                r=c.fetchall()
                for z in r:
                    print("--------------------------")
                    print("NAME=",z[0])
                    print("E-MAIL=",z[1])
                    print("MODEL NAME=",z[2])
                    print("--------------------------")
                eml=input("ENTER THE E-MAIL ID OF THE PERSON WHOSE ORDER YOU WANT TO DELETE:")
                ste="DELETE FROM BOOKING WHERE E_Mail=%s"
                if eml in z:
                    c.execute(ste,(eml,))
                    print("DONE!!!")
                    f.commit()
                    break
                else:
                    print("SORRY!!!MAIL ID NOT FOUND...")
                cont()
                break
            elif(so==4):
                #DELETING A REVIEW
                f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
                c=f.cursor()
                print("ALL REVIEWS--")
                c.execute("SELECT * FROM REVIEW")
                r=c.fetchall()
                for z in r:
                    print("--------------------------")
                    print("NAME=",z[0])
                    print("E-MAIL=",z[1])
                    print("STAR RATNG=",z[2])
                    print("REVIEW=",z[3])
                    print("--------------------------")
                eml=input("ENTER THE E-MAIL ID OF THE PERSON WHOSE REVIEW YOU WANT TO DELETE:")
                ste="DELETE FROM REVIEW WHERE E_Mail=%s"
                if eml in z:
                    c.execute(ste,(eml,))
                    print("DONE!!!")
                    f.commit()
                    break
                else:
                    print("SORRY!!!MAIL ID NOT FOUND...")
                cont()
                break
            elif(so==5):
                print("OK")
                break
    elif(x==2):
        #CHECKING AN ITEM
        print(" ---------------------------------------------------------------------------------------------------------------------------------")
        print("|  AVAILABLE ITEMS ARE:\n|   1. MOBILE\n|   2. LAPTOP\n|   3. HEADPHONES\n|   4. EARPHONES\n|   5. FRIDGE")
        print(" ---------------------------------------------------------------------------------------------------------------------------------")
        m=input("ENTER THE ITEM FROM ABOVE LIST WHOSE MODELS YOU WANT TO SEE:")
        if(m=="3"):
            #CHECKING AN ITEM FROM HEADPHONES
            f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
            c=f.cursor()
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM HEADPHONES")
            r=c.fetchall()
            for z in r:
                print("--------------------------")
                print("MODEL NAME=",z[0])
                print("BRAND NAME=",z[1])
                print("PRICE=",z[2])
                print("--------------------------")
            km=input("ENTER THE MODEL NAME OF HEADPHONES ABOUT WHICH YOU WANT TO KNOW MORE:")
            str2nd="SELECT * FROM HEADPHONES WHERE Model_Name=%s"
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM HEADPHONES")
            r=c.fetchall()
            for z in r:
                if km in z:
                    c.execute(str2nd,(km,))
                    r=c.fetchall()
                    for z in r:
                        print("--------------------------")
                        print("MODEL NAME=",z[0])
                        print("BRAND NAME=",z[1])
                        print("WIRED OR WIRELESS=",z[2])
                        print("COLOUR=",z[3])
                        print("PRICE=",z[4])
                        print("PLAY TIME=",z[5])
                        print("BLUETOOTH VERSION=",z[6])
                        print("PACKAGING CONTENT=",z[7])
                        print("--------------------------")
                        book=int(input("DO YOU WANT TO BOOK THIS ITEM\nPRESS 1 FOR YES\nPRESS 2 FOR NO:"))
                        if(book==1):
                            name=input("ENTER YOUR NAME:")
                            email=input("ENTER YOUR E-MAIL ID:")
                            modelname=z[0]
                            t=(name, email, modelname)
                            str=("INSERT INTO BOOKING(Name, E_Mail, Model_Name) VALUES(%s,%s,%s)")
                            c.execute(str,t)
                            f.commit()
                            print("1. YOU WILL RECEIVE YOUR ORDER IN 3 DAYS\n2. YOU WILL HAVE TO PAY CASH ON DELIVERY\n3. YOU CAN CANCEL YOUR ORDER ANYTINE BEFORE DELIVRY")
                    cont()
            
        elif(m=="4"):
            #CHECKING AN ITEM FROM EARPHONES
            f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
            c=f.cursor()
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM EARPHONES")
            r=c.fetchall()
            for z in r:
                print("--------------------------")
                print("MODEL NAME=",z[0])
                print("BRAND NAME=",z[1])
                print("PRICE=",z[2])
                print("--------------------------")
            km=input("ENTER THE MODEL NAME OF EARPHONES ABOUT WHICH YOU WANT TO KNOW MORE:")
            str2nd="SELECT * FROM EARPHONES WHERE Model_Name=%s"
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM EARPHONES")
            r=c.fetchall()
            for z in r:
                if km in z:
                    c.execute(str2nd,(km,))
                    r=c.fetchall()
                    for z in r:
                        print("--------------------------")
                        print("MODEL NAME=",z[0])
                        print("BRAND NAME=",z[1])
                        print("WIRED OR WIRELESS=",z[2])
                        print("COLOUR=",z[3])
                        print("PRICE=",z[4])
                        print("PLAY TIME=",z[5])
                        print("BLUETOOTH VERSION=",z[6])
                        print("PACKAGING CONTENT=",z[7])
                        print("--------------------------")
                        book=int(input("DO YOU WANT TO BOOK THIS ITEM\nPRESS 1 FOR YES\nPRESS 2 FOR NO:"))
                        if(book==1):
                            name=input("ENTER YOUR NAME:")
                            email=input("ENTER YOUR E-MAIL ID:")
                            modelname=z[0]
                            t=(name, email, modelname)
                            str=("INSERT INTO BOOKING(Name, E_Mail, Model_Name) VALUES(%s,%s,%s)")
                            c.execute(str,t)
                            f.commit()
                            print("1. YOU WILL RECEIVE YOUR ORDER IN 3 DAYS\n2. YOU WILL HAVE TO PAY CASH ON DELIVERY\n3. YOU CAN CANCEL YOUR ORDER ANYTINE BEFORE DELIVRY")
                    cont()
        elif(m=="1"):
            #CHECKING AN ITEM FROM MOBILE
            print("OK")
        elif(m=="5"):
            #CHECKING AN ITEM FROM FRIDGE
            f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
            c=f.cursor()
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM FRIDGE")
            r=c.fetchall()
            for z in r:
                print("--------------------------")
                print("MODEL NAME=",z[0])
                print("BRAND NAME=",z[1])
                print("PRICE=",z[2])
                print("--------------------------")
            km=input("ENTER THE MODEL NAME OF FRIDGE ABOUT WHICH YOU WANT TO KNOW MORE:")
            str2nd="SELECT * FROM FRIDGE WHERE Model_Name=%s"
            c.execute("SELECT Model_Name,Brand_Name,Mrp FROM FRIDGE")
            r=c.fetchall()
            for z in r:
                if km in z:
                    c.execute(str2nd,(km,))
                    r=c.fetchall()
                    for z in r:
                        print("--------------------------")
                        print("MODEL NAME=",z[0])
                        print("BRAND NAME=",z[1])
                        print("PRICE=",z[2])
                        print("NUMBER OF DOOR POCKETS=",z[3])
                        print("INVERTER COMPATIBILITY=",z[4])
                        print("CONVERTABLE=",z[5])
                        print("COLOUR=",z[6])
                        print("STAR RATING=",z[7])
                        print("LITRES=",z[8])
                        print("PACKAGING CONTENT=",z[9])
                        print("--------------------------")
                        book=int(input("DO YOU WANT TO BOOK THIS ITEM\nPRESS 1 FOR YES\nPRESS 2 FOR NO:"))
                        if(book==1):
                            name=input("ENTER YOUR NAME:")
                            email=input("ENTER YOUR E-MAIL ID:")
                            modelname=z[0]
                            t=(name, email, modelname)
                            str=("INSERT INTO BOOKING(Name, E_Mail, Model_Name) VALUES(%s,%s,%s)")
                            c.execute(str,t)
                            f.commit()
                            print("1. YOU WILL RECEIVE YOUR ORDER IN 3 DAYS\n2. YOU WILL HAVE TO PAY CASH ON DELIVERY\n3. YOU CAN CANCEL YOUR ORDER ANYTINE BEFORE DELIVRY")
                    cont()
        elif(m=="2"):
            #CHECKING AN ITEM FROM LAPTOP
            print("OK") 
    elif(x==3):
        #BOOKING CANCELLATION
        f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
        c=f.cursor()
        email=input("ENTER YOUR EMAIL ID:")
        str="DELETE FROM BOOKING WHERE E_Mail=%s"
        c.execute(str,(email,))
        f.commit()
        print("DONE!!!")
        cont()
    elif(x==4):
        #REVIEW
        f=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="eshop")
        c=f.cursor()
        rev=input("PRESS 1 TO WRITE A REVIEW\nPRESS 2 TO READ REVIEWS:")
        if(rev=="1"):
            #ENTERING A REVIEW
            nam=input("ENTER YOUR NAME:")
            email=input("ENTER YOUR E-MAIL ID:")
            star=int(input("ENTER STAR RATING BY 5:"))
            rev=input("ENTER YOUR REVIEW ABOUT THIS PROGRAM:")
            print("REGISTERING....")
            t=(nam,email,star,rev)
            str1="""INSERT INTO REVIEW(Name, E_Mail, Star_Rating, Review) VALUES(%s,%s,%s,%s)"""
            c.execute(str1,t)
            f.commit()
            print("REGISTERED SUCCESSFULLY!!!")
            cont()
        elif(rev=="2"):
            #DISPLAYING A REVIEW
            c.execute("SELECT * FROM REVIEW")
            r=c.fetchall()
            for z in r:
                print("--------------------------")
                print("NAME=",z[0])
                print("E-MAIL=",z[1])
                print("STAR RATNG=",z[2])
                print("REVIEW=",z[3])
                print("--------------------------")
            cont()
    elif(x==5):
        print("GOOD BYE!!!")
        exit()
            
            
            
            
        
        
        
        
        
        
                
                
                    
                
                
            
                    
                        
 
