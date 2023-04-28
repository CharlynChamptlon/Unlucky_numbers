# Créé par cassa, le 18/04/2023 en Python 3.7
from tkinter.messagebox import *
from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image
import random
from random import randint

# création de la fenêtre
canvasi=Tk()
canvasi.attributes('-fullscreen', True)
canvasi['background']='#AE567D'
canvasi.title("Unlucky numbers")


#Creation  d'un bouton "Quitter":
#Le bouton quitter est associer à la commande 'destroy' qui ferme la fenêtre de jeu après la pression du boutton
Bouton_Quitter=Button(canvasi, text ='Quitter', command = canvasi.destroy)
Bouton_Quitter.pack()

# Création du canva accueillant le jeu
canvara = Canvas(canvasi, width=2000, height=2000, bg="#DB56AD")

#Creation  du Canvas accueillant notre jeu:
def certain() :
    """demande à la personne lançant le programme si elle souhaite jouer:
    si oui la fonction lance le reste du programme, si non la fonction
    ferme la fenêtre et le programme"""
    if askyesno('Addict?', '"Bienvenue sur Unlucky Numbers. Voulez-vous démarrer une partie?"'):
        showinfo('Addict!', 'Dans ce cas, bonne partie !')
    else:
        showinfo("Non-addict", 'Compris! Bonne journée à vous.')
        canvasi.destroy()
certain()


def init():
    """permet au joueur d'associer leur nom à leur grille de jeu"""
    label1 = Label(canvasi, text="Enter your name:")
    label1.pack()

    name1 = Entry(canvasi, textvariable=StringVar(),  font=("Helvetica",20,"bold") ) # zone d'insertion joueur 1
    name1.focus_set()
    name1.pack()

    name2 = Entry(canvasi, textvariable=StringVar(),  font=("Helvetica",20,"bold")) # zone d'insertion joueur 2
    name2.focus_set()
    name2.pack()

    # placement des noms au dessus de la grille choisie
    def doSomething():
        name1.place(x=700, y=160)

    def doSomething2():
        name2.place(x=1175, y=160)

    # Boutton permettant l'affichage relié aux fonctions doSomething
    buttonconf1 = Button( text="Confirmation Joueur 1", command=doSomething)
    buttonconf1.pack()
    buttonconf2 = Button( text="Confirmation Joueur 2", command=doSomething2)
    buttonconf2.pack()
init()






# création tableau de jeu 1
colonne1 =canvara.create_line(650, 100, 650, 500)
colonne2 = canvara.create_line(750, 100, 750, 500)
colonne3 = canvara.create_line(850, 100, 850, 500)
colonne4 = canvara.create_line(950, 100, 950, 500)
colonne5 = canvara.create_line(1050, 100, 1050, 500)
ligne1 = canvara.create_line(650, 100, 1050, 100)
ligne2 = canvara.create_line(650, 200, 1050, 200)
ligne3 = canvara.create_line(650, 300, 1050, 300)
ligne4 = canvara.create_line(650, 400, 1050, 400)
ligne5 = canvara.create_line(650, 500, 1050, 500)

# création tableau de jeu 2
colonne1 = canvara.create_line(1125, 100, 1125, 500)
colonne2 = canvara.create_line(1225, 100, 1225, 500)
colonne3 = canvara.create_line(1325, 100, 1325, 500)
colonne4 = canvara.create_line(1425, 100, 1425, 500)
colonne5 = canvara.create_line(1525, 100, 1525, 500)
ligne1 = canvara.create_line(1125, 100, 1525, 100)
ligne2 = canvara.create_line(1125, 200, 1525, 200)
ligne3 = canvara.create_line(1125, 300, 1525, 300)
ligne4 = canvara.create_line(1125, 400, 1525, 400)
ligne5 = canvara.create_line(1125, 500, 1525, 500)

# création du tapis
canvara.create_rectangle(50,50,600,300 ,fill="white",outline="black",width=3)
canvara.create_rectangle(50,350,600,600 ,fill="white",outline="black",width=3)



# Cartes

chiffres=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] # liste des valeurs des cartes
nodes=[]
p=15
for i in range (16):
    """mélange les valeurs dans la liste"""
    b=random.randint(0,p)
    valeur=chiffres[b]
    nodes.append(valeur)
    chiffres.remove(valeur)
    p=p-1

chiffres=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] # réinitialise la liste de valeur possible
nodes2=[]
p=15
for i in range (16):
    """mélange les valeurs dans une autre liste"""
    b=random.randint(0,p)
    valeur=chiffres[b]
    nodes2.append(valeur)
    chiffres.remove(valeur)
    p=p-1

for i in range (16):
    """mise en commun des 2 listes précédantes
    Création des variables a et joueur utile pour la suite du programme"""
    nodes.append(nodes2[i])

    joueur=1
    a=31



#Creation  des règles:

Règles=Label(canvara,text=("Règles du jeux :" + "\n" + "\n" + "But : Placer les jetons dans le tableau dans l'ordre croissant."  + "\n" + "Le premier à compléter son tableau gagne."  + "\n" + "\n" + "Informations : Il y a 32 jetons numérotés de 1 à 16, chaque jeton est donc en double." + "\n" + "Les joueurs doivent jouer chacun leur tour." + "\n" + "Quand vous ne pouvez plus jouer mais que des cases sont vides, cliquez sur bloqué." +  "\n" + "\n" +  "Bon jeu à vous :D ! -Avec tout notre amour, l'équipe CassRo(lle)"), bd=2, font=("Helvetica",10,"bold"), bg='white')
Règles.place(x=56,y=375)

# Distinction entre les 2 joueurs

tableau1=Label(canvara,text="JOUEUR 1",bd=2, font=("Helvetica",20,"bold"), bg='#DB56AD') # marque la grille associée au joueur 1
tableau1.place(x=790,y=540)

tableau2=Label(canvara,text="JOUEUR 2",bd=2, font=("Helvetica",20,"bold"), bg='#DB56AD')# marque la grille associée au joueur 2
tableau2.place(x=1265,y=540)


player1=Label(canvara,text="C'est au joueur 1 de jouer",bd=2, font=("Helvetica",15,"bold"), bg='white')
player1.place(x=300,y=125)

player2=Label(canvara,text="C'est au joueur 2 de jouer",bd=2, font=("Helvetica",15,"bold"), bg='white')

def au_joueur1():
    """ supprime le label annonçant le tour du joueur 2 pour le remplacer par
    l'annonce du tour du joueur 1"""
    global player1
    global player2
    player1=Label(canvara,text="C'est au joueur 1 de jouer",bd=2, font=("Helvetica",15,"bold"), bg='white')
    player2=Label(canvara,text="C'est au joueur 2 de jouer",bd=2, font=("Helvetica",15,"bold"), bg='white')
    player2.after(1,player2.destroy())# suppression du label
    player1.place(x=300,y=125)# affichage du nouveau label

def au_joueur2():
    """ supprime le label annonçant le tour du joueur 1 pour le remplacer par
    l'annonce du tour du joueur 2"""
    global player1
    global player2
    player1=Label(canvara,text="C'est au joueur 1 de jouer",bd=2, font=("Helvetica",15,"bold"), bg='white')
    player2=Label(canvara,text="C'est au joueur 2 de jouer",bd=2, font=("Helvetica",15,"bold"), bg='white')
    player1.after(1,player1.destroy())# suppression du label
    player2.place(x=300,y=125)# affichage du nouveau label

# Création du boutton bloqué

def bloc ():
    """si un des joueurs se retrouve bloqué le joueur clique sur ce boutton et
    annonce la victoire du joueur non bloqué"""
    if joueur%2==1:
        showinfo("Gagnant","Le joueur 2 a gagné !")
    elif joueur%2==0:
        showinfo("Gagnant","Le joueur 1 a gagné !")

bloquer=Button(canvara,text='Bloqué', command=bloc)
bloquer.place(x=370,y=180)


# affichage des valeurs à placer

ct0=canvara.create_oval(200,140,270,210,fill="pink") # oval sur lequel les valeurs sont placées


#chaque valeur de la liste 'nodes', regroupant les valeurs mélangées, va être associée à un label
#Ces labels sont supperposé les un sur les autres
#La taille de l'écriture varie en fonction de la valeur (les nombres plus petit son écrit plus  gros pour cacher ceux en-dessous)

if nodes[0]>=10:
    node_value0=Label(canvara,text=nodes[0] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value0.place(x=222,y=160)
else:
    node_value0=Label(canvara,text=nodes[0] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value0.place(x=225,y=158)


if nodes[1]>=10:
    node_value1=Label(canvara,text=nodes[1] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value1.place(x=222,y=160)
else:
    node_value1=Label(canvara,text=nodes[1] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value1.place(x=225,y=158)


if nodes[2]>=10:
    node_value2=Label(canvara,text=nodes[2] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value2.place(x=222,y=160)
else:
    node_value2=Label(canvara,text=nodes[2] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value2.place(x=225,y=158)


if nodes[3]>=10:
    node_value3=Label(canvara,text=nodes[3] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value3.place(x=222,y=160)
else:
    node_value3=Label(canvara,text=nodes[3] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value3.place(x=225,y=158)


if nodes[4]>=10:
    node_value4=Label(canvara,text=nodes[4] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value4.place(x=222,y=160)
else:
    node_value4=Label(canvara,text=nodes[4] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value4.place(x=225,y=158)


if nodes[5]>=10:
    node_value5=Label(canvara,text=nodes[5] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value5.place(x=222,y=160)
else:
    node_value5=Label(canvara,text=nodes[5] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value5.place(x=225,y=158)


if nodes[6]>=10:
    node_value6=Label(canvara,text=nodes[6] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value6.place(x=222,y=160)
else:
    node_value6=Label(canvara,text=nodes[6] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value6.place(x=225,y=158)


if nodes[7]>=10:
    node_value7=Label(canvara,text=nodes[7] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value7.place(x=222,y=160)
else:
    node_value7=Label(canvara,text=nodes[7] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value7.place(x=225,y=158)


if nodes[8]>=10:
    node_value8=Label(canvara,text=nodes[8] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value8.place(x=222,y=160)
else:
    node_value8=Label(canvara,text=nodes[8] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value8.place(x=225,y=158)

if nodes[9]>=10:
    node_value9=Label(canvara,text=nodes[9] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value9.place(x=222,y=160)
else:
    node_value9=Label(canvara,text=nodes[9] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value9.place(x=225,y=158)


if nodes[10]>=10:
    node_value10=Label(canvara,text=nodes[10] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value10.place(x=222,y=160)
else:
    node_value10=Label(canvara,text=nodes[10] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value10.place(x=225,y=158)


if nodes[11]>=10:
    node_value11=Label(canvara,text=nodes[11] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value11.place(x=222,y=160)
else:
    node_value11=Label(canvara,text=nodes[11] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value11.place(x=225,y=158)


if nodes[12]>=10:
    node_value12=Label(canvara,text=nodes[12] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value12.place(x=222,y=160)
else:
    node_value12=Label(canvara,text=nodes[12] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value12.place(x=225,y=158)


if nodes[13]>=10:
    node_value13=Label(canvara,text=nodes[13] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value13.place(x=222,y=160)
else:
    node_value13=Label(canvara,text=nodes[13] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value13.place(x=225,y=158)


if nodes[14]>=10:
    node_value14=Label(canvara,text=nodes[14] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value14.place(x=222,y=160)
else:
    node_value14=Label(canvara,text=nodes[14] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value14.place(x=225,y=158)


if nodes[15]>=10:
    node_value15=Label(canvara,text=nodes[15] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value15.place(x=222,y=160)
else:
    node_value15=Label(canvara,text=nodes[15] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value15.place(x=225,y=158)


if nodes[16]>=10:
    node_value16=Label(canvara,text=nodes[16] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value16.place(x=222,y=160)
else:
    node_value16=Label(canvara,text=nodes[16] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value16.place(x=225,y=158)



if nodes[17]>=10:
    node_value17=Label(canvara,text=nodes[17] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value17.place(x=222,y=160)
else:
    node_value17=Label(canvara,text=nodes[17] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value17.place(x=225,y=158)


if nodes[18]>=10:
    node_value18=Label(canvara,text=nodes[18] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value18.place(x=222,y=160)
else:
    node_value18=Label(canvara,text=nodes[18] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value18.place(x=225,y=158)



if nodes[19]>=10:
    node_value19=Label(canvara,text=nodes[19] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value19.place(x=222,y=160)
else:
    node_value19=Label(canvara,text=nodes[19] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value19.place(x=225,y=158)



if nodes[20]>=10:
    node_value20=Label(canvara,text=nodes[20] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value20.place(x=222,y=160)
else:
    node_value20=Label(canvara,text=nodes[20] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value20.place(x=225,y=158)

if nodes[21]>=10:
    node_value21=Label(canvara,text=nodes[21] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value21.place(x=222,y=160)
else:
    node_value21=Label(canvara,text=nodes[21] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value21.place(x=225,y=158)

if nodes[22]>=10:
    node_value22=Label(canvara,text=nodes[22] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value22.place(x=222,y=160)
else:
    node_value22=Label(canvara,text=nodes[22] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value22.place(x=225,y=158)



if nodes[23]>=10:
    node_value23=Label(canvara,text=nodes[23] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value23.place(x=222,y=160)
else:
    node_value23=Label(canvara,text=nodes[23] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value23.place(x=225,y=158)



if nodes[24]>=10:
    node_value24=Label(canvara,text=nodes[24] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value24.place(x=222,y=160)
else:
    node_value24=Label(canvara,text=nodes[24] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value24.place(x=225,y=158)



if nodes[25]>=10:
    node_value25=Label(canvara,text=nodes[25] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value25.place(x=222,y=160)
else:
    node_value25=Label(canvara,text=nodes[25] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value25.place(x=225,y=158)


if nodes[26]>=10:
    node_value26=Label(canvara,text=nodes[26] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value26.place(x=222,y=160)
else:
    node_value26=Label(canvara,text=nodes[26] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value26.place(x=225,y=158)


if nodes[27]>=10:
    node_value27=Label(canvara,text=nodes[27] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value27.place(x=222,y=160)
else:
    node_value27=Label(canvara,text=nodes[27] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value27.place(x=225,y=158)


if nodes[28]>=10:
    node_value28=Label(canvara,text=nodes[28] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value28.place(x=222,y=160)
else:
    node_value28=Label(canvara,text=nodes[28] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value28.place(x=225,y=158)



if nodes[29]>=10:
    node_value29=Label(canvara,text=nodes[29] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value29.place(x=222,y=160)
else:
    node_value29=Label(canvara,text=nodes[29] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value29.place(x=225,y=158)


if nodes[30]>=10:
    node_value30=Label(canvara,text=nodes[30] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value30.place(x=222,y=160)
else :
    node_value30=Label(canvara,text=nodes[30] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value30.place(x=225,y=158)


if nodes[31]>=10:

    node_value31=Label(canvara,text=nodes[31] ,bd=2, font=("Helvetica",15,"bold"), bg='pink')
    node_value31.place(x=222,y=160)
else:

    node_value31=Label(canvara,text=nodes[31] ,bd=2, font=("Helvetica",20,"bold"), bg='pink')
    node_value31.place(x=225,y=158)





def test():
    """Cette fonction est appelée à chaque fin de fonction de déplacement associée
    à chaque case des grilles
    Cette fonction sert à supprimer le label du nombres posé par le joueur
    afin d'afficher le prochain nombre à jouer
    Elle se base sur la valeur 'a' de correspondant à l'indice auquel se trouve la
    valeur posée
    A la fin de la fonction la variable 'a' descend de 1 pour passer à la valeur
    suivante
    La variable'joueur' monte de 1 pour passer au tour de l'autre joueur
    """

    global joueur
    global node_value0
    global node_value1
    global node_value2
    global node_value3
    global node_value4
    global node_value5
    global node_value6
    global node_value7
    global node_value8
    global node_value9
    global node_value10
    global node_value11
    global node_value12
    global node_value13
    global node_value14
    global node_value15
    global node_value16
    global node_value17
    global node_value18
    global node_value19
    global node_value20
    global node_value21
    global node_value22
    global node_value23
    global node_value24
    global node_value25
    global node_value26
    global node_value27
    global node_value28
    global node_value29
    global node_value30
    global node_value31
    global a
    # recherche du label à supprimer
    if a==0:
        node_value0.after(1,node_value0.destroy())
    elif a==1:
        node_value1.after(1,node_value1.destroy())
    elif a==2:
        node_value2.after(1,node_value2.destroy())
    elif a==3:
        node_value3.after(1,node_value3.destroy())
    elif a==4:
        node_value4.after(1,node_value4.destroy())
    elif a==5:
        node_value5.after(1,node_value5.destroy())
    elif a==6:
        node_value6.after(1,node_value6.destroy())
    elif a==7:
        node_value7.after(1,node_value7.destroy())
    elif a==8:
        node_value8.after(1,node_value8.destroy())
    elif a==9:
        node_value9.after(1,node_value9.destroy())
    elif a==10:
        node_value10.after(1,node_value10.destroy())
    elif a==11:
        node_value11.after(1,node_value11.destroy())
    elif a==12:
        node_value12.after(1,node_value12.destroy())
    elif a==13:
        node_value13.after(1,node_value13.destroy())
    elif a==14:
        node_value14.after(1,node_value14.destroy())
    elif a==15:
        node_value15.after(1,node_value15.destroy())
    elif a==16:
        node_value16.after(1,node_value16.destroy())
    elif a==17:
        node_value17.after(1,node_value17.destroy())
    elif a==18:
        node_value18.after(1,node_value18.destroy())
    elif a==19:
        node_value19.after(1,node_value19.destroy())
    elif a==20:
        node_value20.after(1,node_value20.destroy())
    elif a==21:
        node_value21.after(1,node_value21.destroy())
    elif a==22:
        node_value22.after(1,node_value22.destroy())
    elif a==23:
        node_value23.after(1,node_value23.destroy())
    elif a==24:
        node_value24.after(1,node_value24.destroy())
    elif a==25:
        node_value25.after(1,node_value25.destroy())
    elif a==26:
        node_value26.after(1,node_value26.destroy())
    elif a==27:
        node_value27.after(1,node_value27.destroy())
    elif a==28:
        node_value28.after(1,node_value28.destroy())
    elif a==29:
        node_value29.after(1,node_value29.destroy())
    elif a==30:
        node_value30.after(1,node_value30.destroy())
    elif a==31:
        node_value31.after(1,node_value31.destroy())

    a=a-1 # passage au prochain nombre à jouer dans la liste
    joueur=joueur+1 # passage à l'autre joueur



# Création des fonctions de déplacement des bouttons dans les grilles de jeu

# Initialisation des variables associées chacune à une case du tableau
naturea=0
natureb=0
naturec=0
natured=0
naturee=0
naturef=0
natureg=0
natureh=0
naturei=0
naturej=0
naturek=0
naturel=0
naturem=0
naturen=0
natureo=0
naturep=0

naturea2=0
natureb2=0
naturec2=0
natured2=0
naturee2=0
naturef2=0
natureg2=0
natureh2=0
naturei2=0
naturej2=0
naturek2=0
naturel2=0
naturem2=0
naturen2=0
natureo2=0
naturep2=0

#Les fonctions à suivres sont associées chacune à une case et un boutton dans les grilles
#Pour commencer elles vérifient si c'est le bon joueur qui est en train de jouer
#En suite, si la condition précédente est respectée, elle associe le nombre joué à la variable 'nature' correspondant à cette case
# Elle vérifie si le nombre est bien placé dans la grille (pas trop grand ou trop petit) vérifie uniquement les cases gauches/droites et haut/bas (explique la possibilité d'être bloqué)
#Si le nombre ne peut pas être placé dans la case un message d'erreur est affiché, la variable 'nature' associée à la case est réinitialisée à 0 et le joueur doit choisir une autre case
#Si le nombre est bien placé il est affiché dans la case souhaité, appel de la fonction test() et la partie continue

# fonctions de déplacement de la grille 1
def dpct1():
    global joueur
    global player1
    global player2

    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep

    global M
    global a


    if joueur%2==1:
        naturea=nodes[a]

        if natureb != 0 and naturee != 0:
            if naturea < natureb and naturea<naturee:
                case1=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case1.place(x=687,y=132)
                test()
                au_joueur2()
            else:
                naturea=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif natureb != 0 and naturee == 0:
            if naturea < natureb :
                case1=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case1.place(x=687,y=132)
                test()
                au_joueur2()
            else:
                naturea=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif natureb == 0 and naturee != 0:
            if naturea < naturee :
                case1=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case1.place(x=687,y=132)
                test()
                au_joueur2()
            else:
                naturea=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return

        else :
            case1=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case1.place(x=687,y=132)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return


def dpct2():
    global joueur
    global player1
    global player2

    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep

    global a
    if joueur%2==1:
        natureb=nodes[a]
        if naturea != 0 and naturef!=0 and naturec!=0 :
            if natureb > naturea and natureb < naturef and natureb < naturec :
                case2=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2.place(x=787,y=132)
                test()
                au_joueur2()
            else :
                natureb=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return

        elif naturea != 0 and naturef!=0 and naturec==0 :
            if natureb > naturea and natureb < naturef  :
                case2=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2.place(x=787,y=132)
                test()
                au_joueur2()
            else :
                natureb=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return

        elif naturec != 0 and naturef!=0 and naturea==0 :
            if naturec > natureb and natureb < naturef  :
                case2=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2.place(x=787,y=132)
                test()
                au_joueur2()
            else :
                natureb=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return

        elif naturea != 0 and naturec!=0 and naturef==0 :
            if natureb > naturea and natureb < naturec  :
                case2=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2.place(x=787,y=132)
                test()
                au_joueur2()
            else :
                natureb=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return

        elif naturea != 0 and naturef ==0 and naturec==0 :
            if natureb > naturea :
                case2=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2.place(x=787,y=132)
                test()
                au_joueur2()
            else :
                natureb=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return

        elif naturec != 0 and naturef==0 and naturea==0 :
            if naturec > natureb :
                case2=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2.place(x=787,y=132)
                test()
                au_joueur2()
            else :
                natureb=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif naturef != 0 and naturec==0 and naturea==0 :
            if naturef > natureb :
                case2=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2.place(x=787,y=132)
                test()
                au_joueur2()
            else :
                natureb=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        else :

            case2=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case2.place(x=787,y=132)
            test()
            au_joueur2()

    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return


def dpct3():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep

    global a

    if joueur%2==1:
        naturec=nodes[a]
        if natureb != 0 and natured!=0 and natureg != 0 :
            if natureb < naturec and naturec < natured and naturec < natureg  :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=132)
                test()
                au_joueur2()
            else :
                naturec=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb != 0 and natured==0 and natureg != 0) :
            if (natureb < naturec and  naturec < natureg)  :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=132)
                test()
                au_joueur2()
            else :
                naturec=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb == 0 and natured!=0 and natureg != 0) :
            if (naturec < natured and  naturec < natureg) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=132)
                test()
                au_joueur2()
            else :
                naturec=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb != 0 and natured!=0 and natureg == 0) :
            if (naturec < natured and naturec < natured) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=132)
                test()
                au_joueur2()
            else :
                naturec=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb == 0 and natured==0 and natureg != 0) :
            if (naturec < natureg) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=132)
                test()
                au_joueur2()
            else :
                naturec=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb == 0 and natured!=0 and natureg == 0) :
            if (naturec < natured) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=132)
                test()
                au_joueur2()
            else :
                naturec=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb != 0 and natured==0 and natureg == 0) :
            if (natureb < naturec) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=132)
                test()
                au_joueur2()
            else :
                naturec=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        else :
            case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case3.place(x=887,y=132)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return


def dpct4():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep

    global a
    if joueur%2==1:
        natured=nodes[a]
        if naturec != 0 and natureh != 0 :
            if naturec < natured and natured < natureh  :
                case4=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case4.place(x=987,y=132)
                test()
                au_joueur2
            else :
                natured=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif naturec!= 0 and natureh==0 :
            if naturec < natured :
                case4=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case4.place(x=987,y=132)
                test()
                au_joueur2
            else :
                natured=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif natureh != 0 and naturec==0:
            if  natured < natureh  :
                case4=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case4.place(x=987,y=132)
                test()
                au_joueur2
            else :
                natured=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        else :
            case4=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case4.place(x=987,y=132)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return


def dpct5():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep

    global a

    if joueur%2==1:
        naturee=nodes[a]
        if naturea != 0 and naturef!=0 and naturei!= 0 :
            if naturea < naturee and naturef > naturee and naturei > naturee:
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=687,y=232)
                test()
                au_joueur2()
            else :
                naturee=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (naturea != 0 and naturef!=0 and naturei== 0) :
            if (naturea < naturee and naturef > naturee) :
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=687,y=232)
                test()
                au_joueur2()
            else :
                naturee=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (naturea == 0 and naturef!=0 and naturei!= 0) :
            if (naturef > naturee and naturei > naturee) :
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=687,y=232)
                test()
                au_joueur2()
            else :
                naturee=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (naturea != 0 and naturef==0 and naturei!= 0) :
            if (naturei > naturee and naturea < naturee):
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=687,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (naturea != 0 and naturef==0 and naturei== 0):
            if (naturea < naturee) :
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=687,y=232)
                test()
                au_joueur2()
            else :
                naturee=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (naturea == 0 and naturef!=0 and naturei== 0) :
            if (naturef > naturee):
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=687,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif  (naturea == 0 and naturef==0 and naturei!= 0) :
            if (naturei > naturee):
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=687,y=232)
                test()
                au_joueur2()
            else :
                naturee=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        else :
            case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case5.place(x=687,y=232)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return

def dpct6():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep

    global a
    if joueur%2==1:
        naturef=nodes[a]
        if natureb != 0 and naturee != 0 and natureg!=0 and naturej != 0 :
            if naturef > natureb and naturef > naturee and natureg > naturef and naturej > naturef:
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb != 0 and naturee != 0 and natureg!=0 and naturej == 0) :
            if (naturef > natureb and naturef > naturee and natureg > naturef):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb == 0 and naturee != 0 and natureg!=0 and naturej != 0) :
            if  (naturef > naturee and natureg > naturef and naturej > naturef):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb != 0 and naturee == 0 and natureg!=0 and naturej != 0) :
            if (natureg > naturef and naturej > naturef and naturef > natureb) :
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb != 0 and naturee != 0 and natureg==0 and naturej != 0) :
            if (naturej > naturef and naturef > natureb and naturef > naturee ):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return


        elif (natureb != 0 and naturee != 0 and natureg==0 and naturej == 0) :  # b e
            if (naturef > natureb and naturef > naturee):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb == 0 and naturee != 0 and natureg!=0 and naturej == 0) :  #e g
            if (naturef > naturee and natureg > naturef):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb == 0 and naturee == 0 and natureg!=0 and naturej != 0) :  # j g
            if (natureg > naturef and naturej > naturef):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb != 0 and naturee == 0 and natureg==0 and naturej != 0) :  # b j
            if (naturej > naturef and naturef > natureb):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return


        elif (natureb == 0 and naturee != 0 and natureg==0 and naturej != 0) :  #e j
            if (naturef > naturee and naturej > naturef):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return



        elif (natureb != 0 and naturee == 0 and natureg!=0 and naturej == 0) :  # b G
            if (natureg > naturef and naturef > natureb):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return


        elif (natureb != 0 and naturee == 0 and natureg==0 and naturej == 0):
            if (naturef > natureb):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb == 0 and naturee != 0 and natureg==0 and naturej == 0):
            if (naturef > naturee) :
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb == 0 and naturee == 0 and natureg!=0 and naturej == 0):
            if (natureg > naturef):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb == 0 and naturee == 0 and natureg==0 and naturej != 0):
            if (naturej > naturef):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=787,y=232)
                test()
                au_joueur2()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        else :
            case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case6.place(x=787,y=232)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return

def dpct7():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep
    global a

    if joueur%2==1:
        natureg=nodes[a]
        if naturec != 0 and naturef != 0 and natureh!=0 and naturej != 0:
            if natureg > naturec and natureg > naturef and natureh > natureg and naturek > natureg:
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        elif (naturec != 0 and naturef != 0 and natureh!=0 and naturek == 0) :
            if (natureg > naturec and natureg > naturef and natureh > natureg) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        elif (naturec == 0 and naturef != 0 and natureh!=0 and naturek != 0) :
            if (natureg > naturef and natureh > natureg and naturek > natureg ):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        elif (naturec != 0 and naturef == 0 and natureh!=0 and naturek != 0) :
            if  (natureh > natureg and naturek > natureg and natureg > naturec ) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        elif (naturec != 0 and naturef != 0 and natureh==0 and naturek != 0) :
            if  (naturek > natureg and natureg > naturec and natureg > naturef):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        elif (naturec != 0 and naturef != 0 and natureh==0 and naturek == 0) :
            if (natureg > naturec and natureg > naturef ):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        elif (naturec == 0 and naturef != 0 and natureh!=0 and naturek == 0) :
            if  (natureg > naturef and natureh > natureg ):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        elif (naturec == 0 and naturef == 0 and natureh!=0 and naturek != 0) :
            if (natureh > natureg and naturek > natureg) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        elif (naturec != 0 and naturef == 0 and natureh==0 and naturek != 0) :
            if (naturek > natureg and natureg > naturec):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        elif (naturec != 0 and naturef == 0 and natureh==0 and naturek == 0) :
            if (natureg > naturec) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        elif (naturec == 0 and naturef != 0 and natureh==0 and naturek == 0) :
            if (natureg > naturef) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        elif (naturec == 0 and naturef == 0 and natureh!=0 and naturek == 0) :
            if (natureh > natureg) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        elif (naturec == 0 and naturef == 0 and natureh==0 and naturek != 0) :
            if (naturek > natureg):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return


        elif (naturec== 0 and naturef != 0 and natureh==0 and naturek != 0) :  # f k
            if  (natureg > naturef and naturek > natureg ):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return

        elif (naturec != 0 and naturef == 0 and natureh!=0 and naturek == 0) :  # c h
            if (natureh > natureg and natureg > naturec):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=887,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg=0
                return
        else :

            case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case3.place(x=887,y=232)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return

def dpct8():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep
    global a

    if joueur%2==1:
        natureh=nodes[a]
        if naturel != 0 and natured!=0 and natureg != 0 :
            if naturel > natureh and natureh > natured and natureh > natureg :
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=987,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh=0
                return
        elif (naturel != 0 and natured!=0 and natureg == 0) :
            if (naturel > natureh and natureh > natured) :
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=987,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh=0
                return
        elif (naturel == 0 and natured!=0 and natureg != 0) :
            if (natureh > natured and natureh > natureg):
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=987,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh=0
                return
        elif  (naturel != 0 and natured==0 and natureg != 0) :
            if (natureh > natureg and naturel > natureh) :
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=987,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh=0
                return
        elif (naturel != 0 and natured==0 and natureg == 0) :
            if (naturel > natureh) :
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=987,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh=0
                return
        elif (naturel == 0 and natured!=0 and natureg == 0) :
            if  (natureh > natured)  :
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=987,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh=0
                return
        elif (naturel == 0 and natured==0 and natureg != 0) :
            if  (natureh > natureg) :
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=987,y=232)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh=0
                return


        else :
            case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case8.place(x=987,y=232)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return

def dpct9():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep
    global a

    if joueur%2==1:
        naturei=nodes[a]
        if naturee != 0 and naturej!=0 and naturem != 0:
            if naturei > naturee and naturej > naturei and naturem > naturei  :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=687,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei=0
                return
        elif (naturee != 0 and naturej!=0 and naturem == 0) :
            if (naturei > naturee and naturej > naturei) :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=687,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei=0
                return
        elif (naturee == 0 and naturej!=0 and naturem != 0) :
            if (naturej > naturei and naturem > naturei) :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=687,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei=0

                return
        elif (naturee != 0 and naturej==0 and naturem != 0) :
            if (naturem > naturei and naturei > naturee )  :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=687,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei=0
                return
        elif (naturee != 0 and naturej==0 and naturem == 0) :
            if (naturee<naturei) :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=687,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei=0
                return
        elif (naturee == 0 and naturej!=0 and naturem == 0) :
            if (naturei<naturej) :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=687,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei=0
                return
        elif (naturee == 0 and naturej==0 and naturem != 0) :
            if (naturem>naturei)  :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=687,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei=0
                return
        else :

            case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case9.place(x=687,y=332)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return

def dpct10():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep
    global a

    if joueur%2==1:
        naturej=nodes[a]
        if naturef != 0 and naturei != 0 and naturek!=0 and naturen != 0 :
            if naturej > naturef and naturej > naturei and naturek > naturej and naturen > naturej :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return
        elif (naturef != 0 and naturei != 0 and naturek!=0 and naturen == 0) :
            if (naturej > naturef and naturej > naturei and naturek > naturej) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return
        elif (naturef == 0 and naturei != 0 and naturek!=0 and naturen != 0) :
            if  (naturej > naturei and naturek > naturej and naturen > naturej ) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return
        elif (naturef != 0 and naturei == 0 and naturek!=0 and naturen != 0) :
            if  (naturek > naturej and naturen > naturej and naturej > naturef ) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return
        elif (naturef != 0 and naturei != 0 and naturek==0 and naturen != 0) :
            if (naturen > naturej and naturej > naturef and naturej > naturei ) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return
        elif (naturef != 0 and naturei != 0 and naturek==0 and naturen == 0) :
            if (naturej > naturef and naturej > naturei) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return

        elif (naturef != 0 and naturei == 0 and naturek!=0 and naturen == 0) : # f et k
            if (naturek > naturej and naturej > naturef) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return

        elif (naturef == 0 and naturei != 0 and naturek==0 and naturen != 0) :
            if  (naturej > naturei and naturen > naturej) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return

        elif (naturef == 0 and naturei != 0 and naturek!=0 and naturen == 0) :
            if  (naturej > naturei and naturek > naturej) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return
        elif (naturef == 0 and naturei == 0 and naturek!=0 and naturen != 0) :
            if (naturek > naturej and naturen > naturej) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return
        elif (naturef != 0 and naturei == 0 and naturek==0 and naturen != 0) :
            if (naturen > naturej and naturej > naturef) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return
        elif (naturef != 0 and naturei == 0 and naturek==0 and naturen == 0) :
            if (naturej > naturef) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return
        elif (naturef == 0 and naturei != 0 and naturek==0 and naturen == 0) :
            if  (naturej > naturei) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return
        elif (naturef == 0 and naturei == 0 and naturek!=0 and naturen == 0) :
            if (naturek > naturej) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return
        elif (naturef == 0 and naturei == 0 and naturek==0 and naturen != 0) :
            if (naturen > naturej) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=787,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej=0
                return
        else :
            case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case10.place(x=787,y=332)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return

def dpct11():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep
    global a

    if joueur%2==1:
        naturek=nodes[a]
        if natureg != 0 and naturej != 0 and naturel!=0 and natureo != 0 :
            if naturek > natureg and naturek > naturej and naturel > naturek and natureo > naturek :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return
        elif (natureg != 0 and naturej != 0 and naturel!=0 and natureo == 0) :
            if (naturek > natureg and naturek > naturej and naturel > naturek) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return
        elif (natureg == 0 and naturej != 0 and naturel!=0 and natureo != 0) :
            if (naturek > naturej and naturel > naturek and natureo > naturek) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return
        elif (natureg != 0 and naturej == 0 and naturel!=0 and natureo != 0) :
            if (naturel > naturek and natureo > naturek and naturek > natureg ) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return
        elif (natureg != 0 and naturej != 0 and naturel==0 and natureo != 0) :
            if  (natureo > naturek and naturek > natureg and naturek > naturej) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return
        elif (natureg != 0 and naturej != 0 and naturel==0 and natureo == 0) :
            if (naturek > natureg and naturek > naturej) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return
        elif (natureg == 0 and naturej != 0 and naturel!=0 and natureo == 0) :
            if (naturek > naturej and naturel > naturek) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0

                return
        elif (natureg == 0 and naturej == 0 and naturel!=0 and natureo != 0) :
            if (naturel > naturek and natureo > naturek) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return
        elif (natureg != 0 and naturej == 0 and naturel==0 and natureo != 0) :
            if (natureo > naturek and naturek > natureg ) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return

        elif (natureg== 0 and naturej!= 0 and naturel==0 and natureo != 0) : #j o
            if (naturek > naturej and natureo > naturek) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0

                return

        elif (natureg != 0 and naturej == 0 and naturel!=0 and natureo == 0) : # g l
            if (naturel > naturek and naturek > natureg ) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return
        elif (natureg != 0 and naturej == 0 and naturel==0 and natureo == 0) :
            if (naturek > natureg) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return
        elif (natureg == 0 and naturej != 0 and naturel==0 and natureo == 0) :
            if (naturek > naturej) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return
        elif (natureg == 0 and naturej == 0 and naturel!=0 and natureo == 0) :
            if  (naturel > naturek) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return
        elif (natureg == 0 and naturej == 0 and naturel==0 and natureo != 0) :
            if  (natureo > naturek) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=887,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek=0
                return
        else :

            case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case11.place(x=887,y=332)
            test()
            au_joueur2()

    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return

def dpct12():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep
    global a

    if joueur%2==1:
        naturel=nodes[a]
        if natureh != 0 and naturek!=0 and naturep != 0 :
            if naturel > natureh and naturel > naturek and naturep > naturel :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=987,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel=0
                return
        elif (natureh != 0 and naturek!=0 and naturep == 0):
            if (naturel > natureh and naturel > naturek ) :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=987,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel=0
                return
        elif (natureh == 0 and naturek!=0 and naturep != 0):
            if  (naturel > naturek and naturep > naturel)  :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=987,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel=0
                return
        elif (natureh != 0 and naturek==0 and naturep != 0):
            if  (naturep > naturel and naturel > natureh) :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=987,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel=0
                return
        elif (natureh != 0 and naturek==0 and naturep == 0) :
            if (naturel > natureh) :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=987,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel=0
                return
        elif  (natureh == 0 and naturek!=0 and naturep == 0) :
            if  (naturel > naturek) :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=987,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel=0
                return
        elif  (natureh == 0 and naturek==0 and naturep != 0):
            if (naturep > naturel) :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=987,y=332)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel=0
                return
        else :
            case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case12.place(x=987,y=332)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return

def dpct13():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep
    global a

    if joueur%2==1:
        naturem=nodes[a]
        if naturei != 0 and naturen != 0  :
            if naturem > naturei and naturen > naturem  :
                case13=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case13.place(x=687,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturem=0
                return
        elif (naturei != 0 and naturen == 0) :
            if (naturem > naturei) :
                case13=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case13.place(x=687,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturem=0
                return
        elif (naturei == 0 and naturen != 0)  :
            if (naturen > naturem)  :
                case13=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case13.place(x=687,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturem=0
                return
        else :

            case13=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case13.place(x=687,y=432)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return

def dpct14():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep
    global a

    if joueur%2==1:
        naturen=nodes[a]
        if naturem != 0 and naturej!=0 and natureo != 0:
            if naturen > naturem and naturen > naturej and natureo > naturen :
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=787,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen=0
                return
        elif (naturem != 0 and naturej!=0 and natureo == 0) :
            if (naturen > naturem and naturen>naturej ) :
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=787,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen=0
                return
        elif (naturem != 0 and naturej==0 and natureo != 0) :
            if (naturen > naturem and natureo>naturen):
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=787,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen=0
                return
        elif  (naturem == 0 and naturej!=0 and natureo != 0) :
            if  (natureo > naturen and naturen>naturej) :
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=787,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen=0
                return
        elif (naturem != 0 and naturej==0 and natureo == 0) :
            if (naturen > naturem) :
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=787,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen=0
                return
        elif (naturem == 0 and naturej!=0 and natureo == 0) :
            if (naturen > naturej) :
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=787,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen=0
                return
        elif (naturem == 0 and naturej==0 and natureo != 0) :
            if (natureo > naturen) :
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=787,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen=0
                return
        else :
            case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case14.place(x=787,y=432)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return


def dpct15():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep
    global a

    if joueur%2==1:
        natureo=nodes[a]
        if naturen != 0 and naturek!=0 and naturep != 0:
            if natureo > naturen and natureo > naturek and naturep > natureo :
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=887,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo=0
                return
        elif (naturen != 0 and naturek!=0 and naturep == 0) :
            if (natureo > naturen and natureo > naturek ):
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=887,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo=0
                return
        elif (naturen != 0 and naturek==0 and naturep != 0) :
            if (natureo > naturen and naturep > natureo) :
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=887,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo=0
                return
        elif (naturen == 0 and naturek!=0 and naturep != 0) :
            if (naturep > natureo and natureo > naturek) :
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=887,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo=0
                return
        elif (naturen != 0 and naturek==0 and naturep == 0) :
            if (natureo > naturen) :
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=887,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo=0
                return
        elif (naturen == 0 and naturek==0 and naturep != 0) :
            if (naturep > natureo) :
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=887,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo=0
                return
        elif (naturen == 0 and naturek!=0 and naturep == 0) :
            if (natureo > naturek) :
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=887,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo=0
                return
        else :

            case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case15.place(x=887,y=432)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return

def dpct16():
    global joueur
    global naturea
    global natureb
    global naturec
    global natured
    global naturee
    global naturef
    global natureg
    global natureh
    global naturei
    global naturej
    global naturek
    global naturel
    global naturem
    global naturen
    global natureo
    global naturep
    global a

    if joueur%2==1:
        naturep=nodes[a]
        if natureo != 0 and naturel != 0 :
            if naturep > natureo and naturep > naturel :
                case16=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case16.place(x=987,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturep=0
                return
        elif (natureo !=0 and naturel==0) :
            if (naturep > natureo) :
                case16=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case16.place(x=987,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturep=0
                return
        elif (natureo == 0 and naturel!=0) :
            if (naturep > naturel) :
                case16=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case16.place(x=987,y=432)
                test()
                au_joueur2()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturep=0
                return
        else :
            case16=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case16.place(x=987,y=432)
            test()
            au_joueur2()
    elif joueur%2==0:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 2 de jouer !")
        return

# fonctions de déplacement de la grille 2

def dpct1b():
    global joueur
    global player1
    global player2

    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        naturea2=nodes[a]
        if natureb2 != 0 and naturee2 != 0:
            if naturea2 < natureb2 and naturea2<naturee2:
                case1b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case1b.place(x=1162,y=132)
                test()
                au_joueur1()
            else:
                naturea2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif natureb2 != 0 and naturee2 == 0:
            if naturea2 < natureb2 :
                case1b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case1b.place(x=1162,y=132)
                test()
                au_joueur1()
            else:
                naturea2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif natureb2 == 0 and naturee2 != 0:
            if naturea2 < naturee2 :
                case1b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case1b.place(x=1162,y=132)
                test()
                au_joueur1()
            else:
                naturea2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        else :
            case1b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case1b.place(x=1162,y=132)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return


def dpct2b():
    global joueur
    global player1
    global player2
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        natureb2=nodes[a]
        if naturea2 != 0 and naturef2!=0 and naturec2!=0 :
            if natureb2 > naturea2 and natureb2 < naturef2 and natureb2 < naturec2 :
                case2b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2b.place(x=1262,y=132)

                test()
                au_joueur1()
            else :
                natureb2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return

        elif naturea2 != 0 and naturef2!=0 and naturec2==0 :
            if natureb2 > naturea2 and natureb2 < naturef2  :
                case2b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2b.place(x=1262,y=132)

                test()
                au_joueur1()
            else :
                natureb2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return

        elif naturec2 != 0 and naturef2!=0 and naturea2==0 :
            if naturec2 > natureb2 and natureb2 < naturef2  :
                case2b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2b.place(x=1262,y=132)

                test()
                au_joueur1()
            else :
                natureb=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return

        elif naturea2 != 0 and naturec2!=0 and naturef2==0 :
            if natureb2 > naturea2 and natureb2 < naturec2  :
                case2b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2b.place(x=1262,y=132)

                test()
                au_joueur1()
            else :
                natureb2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return

        elif naturea2 != 0 and naturef2 ==0 and naturec2==0 :
            if natureb2 > naturea2 :
                case2b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2b.place(x=1262,y=132)

                test()
                au_joueur1()
            else :
                natureb2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return

        elif naturec2 != 0 and naturef2==0 and naturea2==0 :
            if naturec2 > natureb2 :
                case2b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2b.place(x=1262,y=132)

                test()
                au_joueur1()
            else :
                natureb2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif naturef2 != 0 and naturec2==0 and naturea2==0 :
            if naturef2 > natureb2 :
                case2b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case2b.place(x=1262,y=132)

                test()
                au_joueur1()
            else :
                natureb2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        else :

            case2b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case2b.place(x=1262,y=132)

            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return


def dpct3b():
    global joueur
    global player1
    global player2
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        naturec2=nodes[a]
        if natureb2 != 0 and natured2!=0 and natureg2 != 0 :
            if natureb2 < naturec2 and naturec2 < natured2 and naturec2 < natureg2  :

                case3b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3b.place(x=1362,y=132)
                test()
                au_joueur1()
            else :
                naturec2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 != 0 and natured2==0 and natureg2 != 0) :
            if (natureb2 < naturec2 and  naturec2 < natureg2)  :

                case3b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3b.place(x=1362,y=132)
                test()
                au_joueur1()
            else :
                naturec2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 == 0 and natured2!=0 and natureg2 != 0) :
            if (naturec2 < natured2 and  naturec2 < natureg2) :

                case3b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3b.place(x=1362,y=132)
                test()
                au_joueur1()
            else :
                naturec2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 != 0 and natured2!=0 and natureg2 == 0) :
            if (naturec2 < natured2 and naturec2 < natured2) :

                case3b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3b.place(x=1362,y=132)
                test()
                au_joueur1()
            else :
                naturec2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 == 0 and natured2==0 and natureg2 != 0) :
            if (naturec2 < natureg2) :

                case3b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3b.place(x=1362,y=132)
                test()
                au_joueur1()
            else :
                naturec2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 == 0 and natured2!=0 and natureg2 == 0) :
            if (naturec2 < natured2) :

                case3b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3b.place(x=1362,y=132)
                test()
                au_joueur1()
            else :
                naturec2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 != 0 and natured2==0 and natureg2 == 0) :
            if (natureb2 < naturec2) :
                case3b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3b.place(x=1362,y=132)
                test()
                au_joueur1()
            else :
                naturec2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        else :
            case3b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case3b.place(x=1362,y=132)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return


def dpct4b():
    global joueur
    global player1
    global player2
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        natured2=nodes[a]
        if naturec2 != 0 and natureh2 != 0 :
            if naturec2 < natured2 and natured2 < natureh2  :
                case4b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case4b.place(x=1462,y=132)
                test()
                au_joueur1()
            else :
                natured2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif naturec2!= 0 and natureh2==0 :
            if naturec2 < natured2 :
                case4b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case4b.place(x=1462,y=132)
                test()
                au_joueur1()
            else :
                natured2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif natureh2 != 0 and naturec2==0:
            if  natured2 < natureh2  :
                case4b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case4b.place(x=1462,y=132)
                test()
                au_joueur1()
            else :
                natured2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        else :
            case4b=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case4b.place(x=1462,y=132)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return


def dpct5b():
    global joueur
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        naturee2=nodes[a]
        if naturea2 != 0 and naturef2!=0 and naturei2!= 0 :
            if naturea2 < naturee2 and naturef2 > naturee2 and naturei2 > naturee2:
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=1162,y=232)
                test()
                au_joueur1()
            else :
                naturee2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (naturea2 != 0 and naturef2!=0 and naturei2== 0) :
            if (naturea2 < naturee2 and naturef2 > naturee2) :
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=1162,y=232)
                test()
                au_joueur1()
            else :
                naturee2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (naturea2 == 0 and naturef2!=0 and naturei2!= 0) :
            if (naturef2 > naturee2 and naturei2 > naturee2) :
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=1162,y=232)
                test()
                au_joueur1()
            else :
                naturee2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (naturea2 != 0 and naturef2==0 and naturei2!= 0) :
            if (naturei2 > naturee2 and naturea2 < naturee2):
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=1162,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (naturea2 != 0 and naturef2==0 and naturei2== 0):
            if (naturea2 < naturee2) :
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=1162,y=232)
                test()
                au_joueur1()
            else :
                naturee2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (naturea2 == 0 and naturef2!=0 and naturei2== 0) :
            if (naturef2 > naturee2):
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=1162,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif  (naturea2 == 0 and naturef2==0 and naturei2!= 0) :
            if (naturei2 > naturee2):
                case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case5.place(x=1162,y=232)
                test()
                au_joueur1()
            else :
                naturee2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        else :
            case5=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case5.place(x=1162,y=232)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return

def dpct6b():
    global joueur
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        naturef2=nodes[a]
        if natureb2 != 0 and naturee2 != 0 and natureg2!=0 and naturej2 != 0 :
            if naturef2 > natureb2 and naturef2 > naturee2 and natureg2 > naturef2 and naturej2 > naturef2:
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 != 0 and naturee2 != 0 and natureg2!=0 and naturej2 == 0) :
            if (naturef2 > natureb2 and naturef2 > naturee2 and natureg2 > naturef2):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 == 0 and naturee2 != 0 and natureg2!=0 and naturej2 != 0) :
            if  (naturef2 > naturee2 and natureg2 > naturef2 and naturej2 > naturef2):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 != 0 and naturee2 == 0 and natureg2!=0 and naturej2 != 0) :
            if (natureg2 > naturef2 and naturej2 > naturef2 and naturef2 > natureb2) :
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 != 0 and naturee2 != 0 and natureg2==0 and naturej2 != 0) :
            if (naturej2 > naturef2 and naturef2 > natureb2 and naturef2 > naturee2 ):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 != 0 and naturee2 != 0 and natureg2==0 and naturej2 == 0) :
            if (naturef2 > natureb2 and naturef2 > naturee2):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 == 0 and naturee2!= 0 and natureg2!=0 and naturej2 == 0) :
            if (naturef2 > naturee2 and natureg2 > naturef2):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 == 0 and naturee2 == 0 and natureg2!=0 and naturej2 != 0) :
            if (natureg2 > naturef2 and naturej2 > naturef2):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 != 0 and naturee2 == 0 and natureg2==0 and naturej2 != 0) :
            if (naturej2 > naturef2 and naturef2 > natureb2):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 == 0 and naturee2 != 0 and natureg2==0 and naturej2 != 0) :
            if (naturej2 > naturef2 and naturef2 > naturee2):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 != 0 and naturee2 == 0 and natureg2==0 and naturej2 == 0):
            if (naturef2 > natureb2):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 == 0 and naturee2 != 0 and natureg2==0 and naturej2 == 0):
            if (naturef2 > naturee2) :
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 == 0 and naturee2== 0 and natureg2!=0 and naturej2 == 0):
            if (natureg2 > naturef2):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 == 0 and naturee2 == 0 and natureg2==0 and naturej2 != 0):
            if (naturej2 > naturef2):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return
        elif (natureb2 == 0 and naturee2 != 0 and natureg2==0 and naturej2 != 0) :  #e j
            if (naturef2 > naturee2 and naturej2 > naturef2):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return



        elif (natureb2 != 0 and naturee2 == 0 and natureg2!=0 and naturej2 == 0) :  # b G
            if (natureg2 > naturef2 and naturef2 > natureb2):
                case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case6.place(x=1262,y=232)
                test()
                au_joueur1()
            else :
                naturef2=0
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")
                return



        else :
            case6=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case6.place(x=1262,y=232)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return

def dpct7b():
    global joueur
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        natureg2=nodes[a]
        if naturec2 != 0 and naturef2 != 0 and natureh2!=0 and naturej2 != 0:
            if natureg2 > naturec2 and natureg2 > naturef2 and natureh2 > natureg2 and naturek2 > natureg2:
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return
        elif (naturec2 != 0 and naturef2 != 0 and natureh2!=0 and naturek2 == 0) :
            if (natureg2 > naturec2 and natureg2 > naturef2 and natureh2 > natureg2) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return
        elif (naturec2 == 0 and naturef2 != 0 and natureh2!=0 and naturek2 != 0) :
            if (natureg2 > naturef2 and natureh2 > natureg2 and naturek2 > natureg2 ):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return
        elif (naturec2 != 0 and naturef2 == 0 and natureh2!=0 and naturek2 != 0) :
            if  (natureh2 > natureg2 and naturek2 > natureg2 and natureg2 > naturec2 ) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return
        elif (naturec2 != 0 and naturef2 != 0 and natureh2==0 and naturek2 != 0) :
            if  (naturek2 > natureg2 and natureg2 > naturec2 and natureg2 > naturef2):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return



        elif (naturec2 != 0 and naturef2 != 0 and natureh2==0 and naturek2 == 0) :  # cf
            if (natureg2 > naturec2 and natureg2 > naturef2 ):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return
        elif (naturec2 == 0 and naturef2 != 0 and natureh2!=0 and naturek2 == 0) :  # f h
            if  (natureg2 > naturef2 and natureh2 > natureg2 ):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return
        elif (naturec2 == 0 and naturef2 == 0 and natureh2!=0 and naturek2 != 0) :  # h k
            if (natureh2 > natureg2 and naturek2 > natureg2) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return


        elif (naturec2 == 0 and naturef2 != 0 and natureh2==0 and naturek2 != 0) :  # f k
            if  (natureg2 > naturef2 and naturek2 > natureg2 ):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return

        elif (naturec2 != 0 and naturef2 == 0 and natureh2!=0 and naturek2 == 0) :  # c h
            if (natureh2 > natureg2 and natureg2 > naturec2):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return



        elif (naturec2 != 0 and naturef2 == 0 and natureh2==0 and naturek2 != 0) :  # kc
            if (naturek2 > natureg2 and natureg2 > naturec2):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return
        elif (naturec2 != 0 and naturef2 == 0 and natureh2==0 and naturek2 == 0) :
            if (natureg2 > naturec2) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return
        elif (naturec2 == 0 and naturef2 != 0 and natureh2==0 and naturek2 == 0) :
            if (natureg2 > naturef2) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return
        elif (naturec2 == 0 and naturef2 == 0 and natureh2!=0 and naturek2 == 0) :
            if (natureh2 > natureg2) :
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return
        elif (naturec2 == 0 and naturef2 == 0 and natureh2==0 and naturek2 != 0) :
            if (naturek2 > natureg2):
                case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case3.place(x=1362,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureg2=0
                return
        else :

            case3=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case3.place(x=1362,y=232)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return

def dpct8b():
    global joueur
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        natureh2=nodes[a]
        if naturel2 != 0 and natured2!=0 and natureg2 != 0 :
            if naturel2 > natureh2 and natureh2 > natured2 and natureh2 > natureg2 :
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=1462,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh2=0
                return
        elif (naturel2 != 0 and natured2!=0 and natureg2 == 0) :
            if (naturel2 > natureh2 and natureh2 > natured2) :
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=1462,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh2=0
                return
        elif (naturel2 == 0 and natured2!=0 and natureg2 != 0) :
            if (natureh2 > natured2 and natureh2 > natureg2):
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=1462,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh2=0
                return
        elif  (naturel2 != 0 and natured2==0 and natureg2 != 0) :
            if (natureh2 > natureg2 and naturel2 > natureh2) :
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=1462,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh2=0
                return
        elif (naturel2 != 0 and natured2==0 and natureg2 == 0) :
            if (naturel2 > natureh2) :
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=1462,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh2=0
                return
        elif (naturel2 == 0 and natured2!=0 and natureg2 == 0) :
            if  (natureh2 > natured2)  :
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=1462,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh2=0
                return
        elif (naturel2 == 0 and natured2==0 and natureg2 != 0) :
            if  (natureh2 > natureg2) :
                case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case8.place(x=1462,y=232)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureh2=0
                return
        else:
            case8=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case8.place(x=1462,y=232)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return

def dpct9b():
    global joueur
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        naturei2=nodes[a]
        if naturee2 != 0 and naturej2!=0 and naturem2 != 0:
            if naturei2 > naturee2 and naturej2 > naturei2 and naturem2 > naturei2  :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=1162,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei2=0
                return
        elif (naturee2 != 0 and naturej2!=0 and naturem2 == 0) :
            if (naturei2 > naturee2 and naturej2 > naturei2) :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=1162,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei2=0
                return
        elif (naturee2 == 0 and naturej2!=0 and naturem2 != 0) :
            if (naturej2 > naturei2 and naturem2 > naturei2) :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=1162,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei2=0

                return
        elif (naturee2 != 0 and naturej2==0 and naturem2 != 0) :
            if (naturem2 > naturei2 and naturei2 > naturee2 )  :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=1162,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei2=0
                return
        elif (naturee2 != 0 and naturej2==0 and naturem2 == 0) :
            if (naturee2<naturei2) :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=1162,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei2=0
                return
        elif (naturee2 == 0 and naturej2!=0 and naturem2 == 0) :
            if (naturei2<naturej2) :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=1162,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei2=0
                return
        elif (naturee2 == 0 and naturej2==0 and naturem2 != 0) :
            if (naturem2>naturei2)  :
                case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case9.place(x=1162,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturei2=0
                return
        else :
            case9=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case9.place(x=1162,y=332)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return

def dpct10b():
    global joueur
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        naturej2=nodes[a]
        if naturef2 != 0 and naturei2 != 0 and naturek2!=0 and naturen2 != 0 :
            if naturej2 > naturef2 and naturej2 > naturei2 and naturek2 > naturej2 and naturen2 > naturej2 :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return
        elif (naturef2 != 0 and naturei2 != 0 and naturek2!=0 and naturen2 == 0) :
            if (naturej2 > naturef2 and naturej2 > naturei2 and naturek2 > naturej2) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return
        elif (naturef2 == 0 and naturei2 != 0 and naturek2!=0 and naturen2 != 0) :
            if  (naturej2 > naturei2 and naturek2 > naturej2 and naturen2 > naturej2 ) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return
        elif (naturef2 != 0 and naturei2 == 0 and naturek2!=0 and naturen2 != 0) :
            if  (naturek2 > naturej2 and naturen2 > naturej2 and naturej2 > naturef2 ) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return

        elif (naturef2 != 0 and naturei2 != 0 and naturek2==0 and naturen2 != 0) :
            if (naturen2 > naturej2 and naturej2 > naturef2 and naturej2 > naturei2 ) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return

        elif (naturef2 != 0 and naturei2 != 0 and naturek2==0 and naturen2 == 0) : # f et i
            if (naturej2 > naturef2 and naturej2 > naturei2) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return

        elif (naturef2 == 0 and naturei2 != 0 and naturek2!=0 and naturen2 == 0) : # i et k
            if  (naturej2 > naturei2 and naturek2 > naturej2) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return


        elif (naturef2 == 0 and naturei2 == 0 and naturek2!=0 and naturen2 != 0) : # k et n
            if (naturek2 > naturej2 and naturen2 > naturej2) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return

        elif (naturef2 != 0 and naturei2 == 0 and naturek2==0 and naturen2 != 0) : # f et n
            if (naturen2 > naturej2 and naturej2 > naturef2) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return

        elif (naturef2 != 0 and naturei2 == 0 and naturek2!=0 and naturen2 == 0) : # f et k
            if (naturek2 > naturej2 and naturej2 > naturef2) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return

        elif (naturef2 == 0 and naturei2 != 0 and naturek2==0 and naturen2 != 0) : # i et n
            if  (naturej2 > naturei2 and naturen2 > naturej2) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return


        elif (naturef2 != 0 and naturei2 == 0 and naturek2==0 and naturen2 == 0) :
            if (naturej2 > naturef2) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return

        elif (naturef2 == 0 and naturei2 != 0 and naturek2==0 and naturen2 == 0) :
            if  (naturej2 > naturei2) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return
        elif (naturef2 == 0 and naturei2 == 0 and naturek2!=0 and naturen2 == 0) :
            if (naturek2 > naturej2) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return
        elif (naturef2 == 0 and naturei2 == 0 and naturek2==0 and naturen2 != 0) :
            if (naturen2 > naturej2) :
                case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case10.place(x=1262,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturej2=0
                return
        else :
            case10=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case10.place(x=1262,y=332)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return

def dpct11b():
    global joueur
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a

    if joueur%2==0:
        naturek2=nodes[a]

        if natureg2 != 0 and naturej2 != 0 and naturel2!=0 and natureo2 != 0 :
            if naturek2 > natureg2 and naturek2 > naturej2 and naturel2 > naturek2 and natureo2> naturek2 :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return
        elif (natureg2 != 0 and naturej2 != 0 and naturel2!=0 and natureo2 == 0) :
            if (naturek2 > natureg2 and naturek2 > naturej2 and naturel2 > naturek2) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return
        elif (natureg2 == 0 and naturej2 != 0 and naturel2!=0 and natureo2 != 0) :
            if (naturek2 > naturej2 and naturel2 > naturek2 and natureo2 > naturek2) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return
        elif (natureg2 != 0 and naturej2 == 0 and naturel2!=0 and natureo2 != 0) :
            if (naturel2 > naturek2 and natureo2 > naturek2 and naturek2 > natureg2 ) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return
        elif (natureg2 != 0 and naturej2 != 0 and naturel2==0 and natureo2 != 0) :
            if  (natureo2 > naturek2 and naturek2 > natureg2 and naturek2 > naturej2) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return
        elif (natureg2 != 0 and naturej2 != 0 and naturel2==0 and natureo2 == 0) : # g j
            if (naturek2 > natureg2 and naturek2 > naturej2) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return
        elif (natureg2 == 0 and naturej2 != 0 and naturel2!=0 and natureo2 == 0) : #j l
            if (naturek2 > naturej2 and naturel2 > naturek2) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0

                return
        elif (natureg2 == 0 and naturej2 == 0 and naturel2!=0 and natureo2 != 0) :  # l o
            if (naturel2 > naturek2 and natureo2 > naturek2) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return
        elif (natureg2 != 0 and naturej2 == 0 and naturel2==0 and natureo2 != 0) : # g o
            if (natureo2 > naturek2 and naturek2 > natureg2 ) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return

        elif (natureg2 == 0 and naturej2 != 0 and naturel2==0 and natureo2 != 0) : #j o
            if (naturek2 > naturej2 and natureo2 > naturek2) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0

                return

        elif (natureg2 != 0 and naturej2 == 0 and naturel2!=0 and natureo2 == 0) : # g l
            if (naturel2 > naturek2 and naturek2 > natureg2 ) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return

        elif (natureg2 != 0 and naturej2 == 0 and naturel2==0 and natureo2 == 0) :
            if (naturek2 > natureg2) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return
        elif (natureg2 == 0 and naturej2 != 0 and naturel2==0 and natureo2 == 0) :
            if (naturek2 > naturej2) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return
        elif (natureg2 == 0 and naturej2 == 0 and naturel2!=0 and natureo2 == 0) :
            if  (naturel2 > naturek2) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return
        elif (natureg2 == 0 and naturej2 == 0 and naturel2==0 and natureo2 != 0) :
            if  (natureo2 > naturek2) :
                case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case11.place(x=1362,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturek2=0
                return
        else :
            case11=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case11.place(x=1362,y=332)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return

def dpct12b():
    global joueur
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        naturel2=nodes[a]
        if natureh2!= 0 and naturek2!=0 and naturep2 != 0 :
            if naturel2 > natureh2 and naturel2 > naturek2 and naturep2 > naturel2 :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=1462,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel2=0
                return
        elif (natureh2 != 0 and naturek2!=0 and naturep2 == 0):
            if (naturel2 > natureh2 and naturel2 > naturek2 ) :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=1462,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel2=0
                return
        elif (natureh2 == 0 and naturek2!=0 and naturep2 != 0):
            if  (naturel2 > naturek2 and naturep2 > naturel2)  :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=1462,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel2=0
                return
        elif (natureh2 != 0 and naturek2==0 and naturep2 != 0):
            if  (naturep2 > naturel2 and naturel2 > natureh2) :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=1462,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel2=0
                return
        elif (natureh2 != 0 and naturek2==0 and naturep2 == 0) :
            if (naturel2 > natureh2) :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=1462,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel2=0
                return
        elif  (natureh2 == 0 and naturek2!=0 and naturep2 == 0) :
            if  (naturel2 > naturek2) :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=1462,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel2=0
                return
        elif  (natureh2 == 0 and naturek2==0 and naturep2 != 0):
            if (naturep2 > naturel2) :
                case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case12.place(x=1462,y=332)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturel2=0
                return
        else :
            case12=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case12.place(x=1462,y=332)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return

def dpct13b():
    global joueur
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        naturem2=nodes[a]
        if naturei2 != 0 and naturen2 != 0  :
            if naturem2 > naturei2 and naturen2 > naturem2  :
                case13=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case13.place(x=1162,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturem2=0
                return
        elif (naturei2 != 0 and naturen2 == 0) :
            if (naturem2 > naturei2) :
                case13=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case13.place(x=1162,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturem2=0
                return
        elif (naturei2 == 0 and naturen2 != 0)  :
            if (naturen2 > naturem2)  :
                case13=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case13.place(x=1162,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturem2=0
                return
        else :
            case13=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case13.place(x=1162,y=432)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return

def dpct14b():
    global joueur
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        naturen2=nodes[a]

        if naturem2 != 0 and naturej2!=0 and natureo2 != 0:
            if naturen2 > naturem2 and naturen2 > naturej2 and natureo2 > naturen2 :
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=1262,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen2=0
                return
        elif (naturem2 != 0 and naturej2!=0 and natureo2 == 0) :
            if (naturen2 > naturem2 and naturen2>naturej2 ) :
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=1262,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen2=0
                return
        elif (naturem2 != 0 and naturej2==0 and natureo2 != 0) :
            if (naturen2 > naturem2 and natureo2>naturen2):
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=1262,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen2=0
                return
        elif  (naturem2 == 0 and naturej2!=0 and natureo2 != 0) :
            if  (natureo2 > naturen2 and naturen2>naturej2) :
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=1262,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen2=0
                return
        elif (naturem2 != 0 and naturej2==0 and natureo2 == 0) :
            if (naturen2 > naturem2) :
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=1262,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen2=0
                return
        elif (naturem2 == 0 and naturej2!=0 and natureo2 == 0) :
            if (naturen2 > naturej2) :
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=1262,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen2=0
                return
        elif (naturem2 == 0 and naturej2==0 and natureo2 != 0) :
            if (natureo2 > naturen2) :
                case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case14.place(x=1262,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturen2=0
                return
        else :
            case14=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case14.place(x=1262,y=432)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return

def dpct15b():
    global joueur
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        natureo2=nodes[a]
        if naturen2 != 0 and naturek2!=0 and naturep2 != 0:
            if natureo2 > naturen2 and natureo2 > naturek2 and naturep2 > natureo2 :
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=1362,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo2=0
                return
        elif (naturen2 != 0 and naturek2!=0 and naturep2 == 0) :
            if (natureo2 > naturen2 and natureo2 > naturek2 ):
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=1362,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo2=0
                return
        elif (naturen2 != 0 and naturek2==0 and naturep2 != 0) :
            if (natureo2 > naturen2 and naturep2 > natureo2) :
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=1362,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo2=0
                return
        elif (naturen2 == 0 and naturek2!=0 and naturep2 != 0) :
            if (naturep2 > natureo2 and natureo2 > naturek2) :
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=1362,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo2=0
                return
        elif (naturen2 != 0 and naturek2==0 and naturep2 == 0) :
            if (natureo2 > naturen2) :
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=1362,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo2=0
                return
        elif (naturen2 == 0 and naturek2==0 and naturep2 != 0) :
            if (naturep2 > natureo2) :
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=1362,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo2=0
                return
        elif (naturen2 == 0 and naturek2!=0 and naturep2 == 0) :
            if (natureo2 > naturek2) :
                case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case15.place(x=1362,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                natureo2=0
                return
        else :
            case15=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case15.place(x=1362,y=432)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return

def dpct16b():
    global joueur
    global naturea2
    global natureb2
    global naturec2
    global natured2
    global naturee2
    global naturef2
    global natureg2
    global natureh2
    global naturei2
    global naturej2
    global naturek2
    global naturel2
    global naturem2
    global naturen2
    global natureo2
    global naturep2

    global a
    if joueur%2==0:
        naturep2=nodes[a]
        if natureo2 != 0 and naturel2 != 0 :
            if naturep2 > natureo2 and naturep2 > naturel2 :
                case16=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case16.place(x=1462,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturep2=0
                return
        elif (natureo2 !=0 and naturel2==0) :
            if (naturep2 > natureo2) :
                case16=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case16.place(x=1462,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturep2=0
                return
        elif (natureo2 == 0 and naturel2!=0) :
            if (naturep2 > naturel2) :
                case16=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
                case16.place(x=1462,y=432)
                test()
                au_joueur1()
            else :
                messagebox.showwarning("Non-respect des règles", "Votre nombre ne peut pas être placé là !")

                naturep2=0
                return
        else :
            case16=Label(canvara,text=nodes[a],bd=3, font=("Helvetica",20,"bold"), bg='#DB56AD')
            case16.place(x=1462,y=432)
            test()
            au_joueur1()
    elif joueur%2==1:
        messagebox.showwarning("Non-respect des règles", "C'est au joueur 1 de jouer !")
        return



# Bouttons grille 2

#ligne 1
Bouton_1b=Button(canvara, text ='', command =dpct1b,height=1,width=1)
Bouton_1b.place(x=1167, y=140)
Bouton_2b=Button(canvara, text ='', command =dpct2b,height=1,width=1)
Bouton_2b.place(x=1267, y=140)
Bouton_3b=Button(canvara, text ='', command =dpct3b,height=1,width=1)
Bouton_3b.place(x=1367, y=140)
Bouton_4b=Button(canvara, text ='', command =dpct4b,height=1,width=1)
Bouton_4b.place(x=1467, y=140)
# ligne 2
Bouton_5b=Button(canvara, text ='', command = dpct5b,height=1,width=1)
Bouton_5b.place(x=1167, y=240)
Bouton_6b=Button(canvara, text ='', command = dpct6b,height=1,width=1)
Bouton_6b.place(x=1267, y=240)
Bouton_7b=Button(canvara, text ='', command = dpct7b,height=1,width=1)
Bouton_7b.place(x=1367, y=240)
Bouton_8b=Button(canvara, text ='', command = dpct8b,height=1,width=1)
Bouton_8b.place(x=1467, y=240)
# ligne 3
Bouton_9b=Button(canvara, text ='', command = dpct9b,height=1,width=1)
Bouton_9b.place(x=1167, y=340)
Bouton_10b=Button(canvara, text ='', command = dpct10b,height=1,width=1)
Bouton_10b.place(x=1267, y=340)
Bouton_11b=Button(canvara, text ='', command = dpct11b,height=1,width=1)
Bouton_11b.place(x=1367, y=340)
Bouton_12b=Button(canvara, text ='', command = dpct12b,height=1,width=1)
Bouton_12b.place(x=1467, y=340)
# ligne 4
Bouton_13b=Button(canvara, text ='', command = dpct13b,height=1,width=1)
Bouton_13b.place(x=1167, y=440)
Bouton_14b=Button(canvara, text ='', command = dpct14b,height=1,width=1)
Bouton_14b.place(x=1267, y=440)
Bouton_15b=Button(canvara, text ='', command = dpct15b,height=1,width=1)
Bouton_15b.place(x=1367, y=440)
Bouton_16b=Button(canvara, text ='', command = dpct16b,height=1,width=1)
Bouton_16b.place(x=1467, y=440)

# Bouttons grille 1

#ligne 1
Bouton_1=Button(canvara, text ='', command =dpct1,height=1,width=1)
Bouton_1.place(x=692, y=140)
Bouton_2=Button(canvara, text ='', command =dpct2,height=1,width=1)
Bouton_2.place(x=792, y=140)
Bouton_3=Button(canvara, text ='', command =dpct3,height=1,width=1)
Bouton_3.place(x=892, y=140)
Bouton_4=Button(canvara, text ='', command =dpct4,height=1,width=1)
Bouton_4.place(x=992, y=140)
# ligne 2
Bouton_5=Button(canvara, text ='', command = dpct5,height=1,width=1)
Bouton_5.place(x=692, y=240)
Bouton_6=Button(canvara, text ='', command = dpct6,height=1,width=1)
Bouton_6.place(x=792, y=240)
Bouton_7=Button(canvara, text ='', command = dpct7,height=1,width=1)
Bouton_7.place(x=892, y=240)
Bouton_8=Button(canvara, text ='', command = dpct8,height=1,width=1)
Bouton_8.place(x=992, y=240)
# ligne 3
Bouton_9=Button(canvara, text ='', command = dpct9,height=1,width=1)
Bouton_9.place(x=692, y=340)
Bouton_10=Button(canvara, text ='', command = dpct10,height=1,width=1)
Bouton_10.place(x=792, y=340)
Bouton_11=Button(canvara, text ='', command = dpct11,height=1,width=1)
Bouton_11.place(x=892, y=340)
Bouton_12=Button(canvara, text ='', command = dpct12,height=1,width=1)
Bouton_12.place(x=992, y=340)
# ligne 4
Bouton_13=Button(canvara, text ='', command = dpct13,height=1,width=1)
Bouton_13.place(x=692, y=440)
Bouton_14=Button(canvara, text ='', command = dpct14,height=1,width=1)
Bouton_14.place(x=792, y=440)
Bouton_15=Button(canvara, text ='', command = dpct15,height=1,width=1)
Bouton_15.place(x=892, y=440)
Bouton_16=Button(canvara, text ='', command = dpct16,height=1,width=1)
Bouton_16.place(x=992, y=440)

# Annonce du gagnant si une grille est complétée

if naturea!=0 and natureb!=0 and naturec!=0 and natured!=0 and naturef!=0 and natureg!=0 and natureh!=0 and naturei!=0 and naturej!=0 and naturek!=0 and naturel!=0 and naturem!=0 and naturen!=0 and natureo!=0 and naturep!=0:
    showinfo("Gagnant","Le joueur 1 a gagné !")
if naturea2!=0 and natureb2!=0 and naturec2!=0 and natured2!=0 and naturef2!=0 and natureg2!=0 and natureh2!=0 and naturei2!=0 and naturej2!=0 and naturek2!=0 and naturel2!=0 and naturem2!=0 and naturen2!=0 and natureo2!=0 and naturep2!=0:
    showinfo("Gagnant","Le joueur 2 a gagné !")


# affichage du canvas
canvara.pack()

# boucle des événements
canvasi.mainloop()

