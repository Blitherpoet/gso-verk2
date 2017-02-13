#Þröstur Haraldsson
#1.2.2017

listi=[]
import os

simaskra="simaskra.txt"
skra=simaskra + ".txt"
haetta=0
while haetta==0:
    print("____________________")
    print("1.Bæta við nýjum í símaskránna.")
    print("2.Breyta upplýsingum í símaskránni.")
    print("3.Eyða upplýsingum / eyða línu úr símaskránni.")
    print("4.Prenta út alla símaskránna ein lína per notanda")
    print("5.Leita að ákveðnu nafni og prenta upplýsingar um það nafn, sima og kennitölu")
    print("6.Hætta í forritinu.")
    print("____________________")
    val=int(input("Hvað af eftirfarandi hlutum langar þér að gera?"))
    if val==1:
        nafn=input("skrifaðu nafn")
        simanumer=int(input("skrifaðu símanúmer"))
        kt=int(input("skrifaðu kennitölu"))
        simaskra=open("simaskra.txt", 'a')
        simaskra.write(nafn + '\t')
        simaskra.write(str(simanumer) + '\t')
        simaskra.write(str(kt) + '\n')
        simaskra.close()
    if val==2:
        efriteljari=0
        with open("simaskra.txt", "r") as open_file:
            print("Nafn\tKennitala\tSímanúmer")
            skra = open_file.read()
            for i in skra.split(","):
                if i != ",":
                    if efriteljari / 3 != 0:
                        print(i, end="\t")
                        efriteljari = efriteljari + 1
                    else:
                        print("\n" + i, end="\t")
                        efriteljari=1
        info = input("\n\nSlaðu inn upplýsingarnar sem þu vilt breyta: ")
        new_info = input("Í hvað viltu breyta: ")
        f1 = open('simaskra.txt', 'r')
        f2 = open('simaskra2.txt', 'w')
        for line in f1:
            f2.write(line.replace(info, new_info))
        f1.close()
        f2.close()
        os.remove("simaskra.txt")
        os.rename("simaskra2.txt", "simaskra.txt")
        with open("simaskra.txt", "r") as open_file:
            print("\nNafn\tKennitala\tSímanúmer")
            skra = open_file.read()
            for i in skra.split(","):
                if i != ",":
                    if efriteljari / 3 != 0:
                        print(i, end="\t")
                        efriteljari = efriteljari + 1
                    else:
                        print("\n" + i, end="\t")

                        efriteljari = 1
    if val==3:
        info = input("Sláðu inn kennitölu þeim sem þú vilt eyða: ")
        f1 = open('simaskra.txt', 'r')
        f2 = open('simaskra2.txt', 'w')
        for i in f1.readlines():
            if info not in i:
                f2.write(i)
        f1.close()
        f2.close()
        os.remove("simaskra.txt")
        os.rename("simaskra2.txt", "simaskra.txt")
    if val==4:
        skra=open("simaskra.txt",'r')
        simaskra=skra.read() .split("n")
        for x in simaskra:
            print(x, "\t")
    if val==5:
        info = input("Sláðu inn nafn: ")
        f1 = open('simaskra.txt', 'r')
        for i in f1.readlines():
            if info in i:
                print(i)
        f1.close()
    if val==6:
        haetta=1
        print ("Takk og bless")