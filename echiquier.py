from tkinter import *
fenetre = Tk()
fenetre.geometry("700x650+400+100")
fenetre.title("échec")

marge = 30
cote = 500
lettre_grille = ["A", "B", "C", "D", "E", "F", "G", "H" ]
numero_grille = ['8', '7', '6', '5', '4', '3', '2', '1' ]
nombres_de_cases = 8
PAS = cote//nombres_de_cases

can=Canvas(fenetre,height = cote+100, width= cote+100)

can.pack()

"coordonnée"
for i in range (0,len(numero_grille)):
    x1 = marge
    y2 = marge*3 + PAS * i
    X1 = marge*3 + PAS * i
    Y2 = cote + marge*3
    a = numero_grille[i]
    b = lettre_grille[i]
    can.create_text(str(x1), str(y2), text = str(a), font="Arial 20")
    can.create_text(str(X1),str(Y2),text = str(b) , font= "Arial 20")

"couleur des carreaux"
for cC in range (1,nombres_de_cases+1):
    for cL in range (1,nombres_de_cases+1):
        carreaux = can.create_rectangle(cC*PAS,cL*PAS,(cC+1)*PAS,(cL+1)*PAS)
        if (cL%2!=0 and cC%2==0 or cL%2==0 and cC%2 != 0 ):
            can.create_rectangle(cC*PAS,cL*PAS,(cC+1)*PAS,(cL+1)*PAS,fill="black")

def click(event):
    can.create_rectangle(410,25,190,0,fill='white')
    i = event.y//(PAS)
    j = event.x//(PAS)
    if (i == 0 or i >= 9 or j == 0 or j >= 9 ):
        can.create_rectangle(410, 25, 190, 0, fill='white')
    else :
        P = numero_grille[i-1]
        O = lettre_grille[j-1]
        can.create_text(300,10,text = "Les coordonnées du carreau sont (" + str(P) + ',' + str(O) + ')')
fenetre.bind ( "<Button-1>" , click)


fenetre.mainloop()