#Þröstur Haraldsson
#1.2.2017

listi=[]

simaskra="simaskra"
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
        lina1=input("Sláðu inn nafn, kennitölu og símanúmer")
        simaskra=open(simaskra, 'a')
        simaskra.write(lina1 + '\n')
        simaskra.close()
    if val==2:
        print("")
    if val==3:
        print ("")
    if val==4:
        skra=open("simaskra",'r')
        simaskra=skra.read() .split("\n")
        for x in simaskra:
            print(x, "\t")
    if val==5:
        print ("")
    if val==6:
        haetta=1
        print ("Takk og bless")