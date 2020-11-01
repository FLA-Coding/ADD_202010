import os, json, requests
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from functools import partial

def validateLogin(tkWindow, prenom, nom, date_naissance, lieu_naissance, adresse, cp, ville, travail, achats, sante, famille, handicap, sport_animaux, convocation, missions, enfants):
    prenom = prenom.get()
    nom = nom.get()
    date_naissance = date_naissance.get()
    lieu_naissance = lieu_naissance.get()
    adresse = adresse.get()
    cp = cp.get()
    ville = ville.get()
    travail = travail.get()
    achats = achats.get()
    sante = sante.get()
    famille = famille.get()
    handicap = handicap.get()
    sport_animaux = sport_animaux.get()
    convocation = convocation.get()
    missions = missions.get()
    enfants = enfants.get()
    liste_motifs = []
    if travail == 1:
        liste_motifs.append("travail")
    if achats == 1:
        liste_motifs.append("achats")
    if sante == 1:
        liste_motifs.append("sante")
    if famille == 1:
        liste_motifs.append("famille")
    if handicap == 1:
        liste_motifs.append("handicap")
    if sport_animaux == 1:
        liste_motifs.append("sport_animaux")
    if convocation == 1:
        liste_motifs.append("convocation")
    if missions == 1:
        liste_motifs.append("missions")
    if enfants == 1:
        liste_motifs.append("enfants") 
    try:
        url = 'http://82.65.106.58:36500/generate'
        content = {"prenom": prenom, "nom": nom, "date_naissance": date_naissance, "lieu_naissance": lieu_naissance, "adresse": adresse, "ville": ville, "cp": cp, "date_sortie": f"{datetime.today().day}/{datetime.today().month}/{datetime.today().year}", "heure_sortie": f"{datetime.today().hour}:{datetime.today().minute}", "motifs": liste_motifs}
        headers = {"Content-Type": "application/json"}
        content = json.dumps(content)
        x = requests.get(url, data=content, headers=headers)
        home = os.getenv('USERPROFILE')
        open(f"{home}\\Desktop\\attestation_{datetime.today().hour}h{datetime.today().minute}.pdf", 'wb').write(x.content)
        messagebox.showinfo("Sauvegardé", f"L'attestation a bien été sauvegardée sur votre bureau sous le nom « attestation_{datetime.today().hour}h{datetime.today().minute}.pdf »")
        tkWindow.destroy()
    except:
        messagebox.showerror("Erreur", "Une erreur est survenue.")
        tkWindow.destroy()




#window
tkWindow = Tk()  
tkWindow.geometry('585x580')  
tkWindow.resizable(width=True, height=True)
tkWindow.title('Générateur d\'attestation de déplacement dérogatoire')

#prenom label and text entry box
prenomLabel = Label(tkWindow, text="Prénom :", wraplength=450).grid(sticky='e', row=0, column=0)
prenom = StringVar()
prenomEntry = Entry(tkWindow, textvariable=prenom).grid(row=0, column=1)  

#nom label and password entry box
nomLabel = Label(tkWindow, text="Nom :", wraplength=450).grid(sticky='e', row=1, column=0)
nom = StringVar()
nomEntry = Entry(tkWindow, textvariable=nom).grid(row=1, column=1)  

#date_naissance label and url entry box
date_naissanceLabel = Label(tkWindow, text="Date de naissance (JJ/MM/AAAA) :", wraplength=450).grid(sticky='e', row=2, column=0)  
date_naissance = StringVar()
date_naissanceEntry = Entry(tkWindow, textvariable=date_naissance).grid(row=2, column=1)  

#lieu_naissance label and url entry box
lieu_naissanceLabel = Label(tkWindow, text="Lieu de naissance :", wraplength=450).grid(sticky='e', row=3, column=0)  
lieu_naissance = StringVar()
lieu_naissanceEntry = Entry(tkWindow, textvariable=lieu_naissance).grid(row=3, column=1)  

#adresse label and url entry box
adresseLabel = Label(tkWindow, text="Adresse (n° et rue) :", wraplength=450).grid(sticky='e', row=4, column=0)  
adresse = StringVar()
adresseEntry = Entry(tkWindow, textvariable=adresse).grid(row=4, column=1)

#cp label and url entry box
cpLabel = Label(tkWindow, text="Code postal :", wraplength=450).grid(sticky='e', row=5, column=0)  
cp = StringVar()
cpEntry = Entry(tkWindow, textvariable=cp).grid(row=5, column=1)

#ville label and url entry box
villeLabel = Label(tkWindow, text="Ville :", wraplength=450).grid(sticky='e', row=6, column=0)
ville = StringVar()
villeEntry = Entry(tkWindow, textvariable=ville).grid(row=6, column=1) 

#travail tick
travailLabel = Label(tkWindow, text="Déplacements entre le domicile et le lieu d'exercice de l'activité professionnelle ou un établissement d'enseignement ou de formation, déplacements professionnels ne pouvant être différés, déplacements pour un concours ou un examen.", wraplength=450).grid(sticky='e', row=7, column=0) 
travail = IntVar()
Checkbutton(tkWindow, variable=travail).grid(row=7, column=1)

#achats tick
achatsLabel = Label(tkWindow, text="Déplacements pour effectuer des achats de fournitures nécessaires à l'activité professionelle, des achats de première nécessité dans des établissements dont les activités demeurent autorisées, le retrait de commande et les livraisons à domicile.", wraplength=450).grid(sticky='e', row=8, column=0) 
achats = IntVar()
Checkbutton(tkWindow, variable=achats).grid(row=8, column=1)

#sante tick
santeLabel = Label(tkWindow, text="Consultations, examens et soins ne pouvant être ni assurés à distance ni différés et l'achat de médicaments.", wraplength=450).grid(sticky='e', row=9, column=0) 
sante = IntVar()
Checkbutton(tkWindow, variable=sante).grid(row=9, column=1)

#famille tick
familleLabel = Label(tkWindow, text="Déplacement pour motif familial impérieux, pour l'assistance aux personnes vulnérables et précaires ou la garde d'enfants.", wraplength=450).grid(sticky='e', row=10, column=0) 
famille = IntVar()
Checkbutton(tkWindow, variable=famille).grid(row=10, column=1)

#handicap tick
handicapLabel = Label(tkWindow, text="Déplacement des personnes en situation de handicap et leur accompagnant.", wraplength=450).grid(sticky='e', row=11, column=0) 
handicap = IntVar()
Checkbutton(tkWindow, variable=handicap).grid(row=11, column=1)

#sport_animaux tick
sport_animauxLabel = Label(tkWindow, text="Déplacements brefs, dans la limite d'une heure quotidienne et dans un rayon maximal d'un kilomètre autour du domicile, liés soit à l'activité physique individuelle des personnes, à l'exclusion de toute pratique sportive collective et de toute proximité avec d'autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie.", wraplength=450).grid(sticky='e', row=12, column=0) 
sport_animaux = IntVar()
Checkbutton(tkWindow, variable=sport_animaux).grid(row=12, column=1)

#convocation tick
convocationLabel = Label(tkWindow, text="Convocation judiciaire ou administrative et pour se rendre dans un service public", wraplength=450).grid(sticky='e', row=13, column=0) 
convocation = IntVar()
Checkbutton(tkWindow, variable=convocation).grid(row=13, column=1)

#missions tick
missionsLabel = Label(tkWindow, text="Participation à des missions d'intérêt général sur demande de l'autorité administrative", wraplength=450).grid(sticky='e', row=14, column=0) 
missions = IntVar()
Checkbutton(tkWindow, variable=missions).grid(row=14, column=1)

#enfants tick
enfantsLabel = Label(tkWindow, text="Déplacement pour chercher les enfants à l'école et à l'occasion de leurs activités périscolaires.", wraplength=450).grid(sticky='e', row=15, column=0) 
enfants = IntVar()
Checkbutton(tkWindow, variable=enfants).grid(row=15, column=1)

validateLogin = partial(validateLogin, tkWindow, prenom, nom, date_naissance, lieu_naissance, adresse, cp, ville, travail, achats, sante, famille, handicap, sport_animaux, convocation, missions, enfants)

#blank space
blankLabel = Label(tkWindow, text="").grid(row=16, column=0)

#login button
loginButton = Button(tkWindow, text="Générer", command=validateLogin).grid(sticky='e', row=17, column=0)  

tkWindow.mainloop()
