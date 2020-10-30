import requests, json
from datetime import datetime

prenom = input('Prénom : ')
nom = input('Nom : ')
date_naissance = input('Date de naissance (JJ/MM/AAAA) : ')
lieu_naissance = input('Lieu de naissance : ')
adresse = input('Adresse (n° et rue) : ')
cp = input('Code postal : ')
ville = input('Ville : ')
print('Écrivez « x » pour chaque motif que vous souhaitez voir apparaître coché :\n')
travail = input("Déplacements entre le domicile et le lieu d'exercice de l'activité professionnelle ou un établissement d'enseignement ou de formation, déplacements professionnels ne pouvant être différés, déplacements pour un concours ou un examen.\n ")
achats = input ("Déplacements pour effectuer des achats de fournitures nécessaires à l'activité professionelle, des achats de première nécessité dans des établissements dont les activités demeurent autorisées, le retrait de commande et les livraisons à domicile.\n ")
sante = input("Consultations, examens et soins ne pouvant être ni assurés à distance ni différés et l'achat de médicaments.\n ")
famille = input("Déplacement pour motif familial impérieux, pour l'assistance aux personnes vulnérables et précaires ou la garde d'enfants.\n ")
handicap = input("Déplacement des personnes en situation de handicap et leur accompagnant.\n ")
sport_animaux = input("Déplacements brefs, dans la limite d'une heure quotidienne et dans un rayon maximal d'un kilomètre autour du domicile, liés soit à l'activité physique individuelle des personnes, à l'exclusion de toute pratique sportive collective et de toute proximité avec d'autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie.Déplacements brefs, dans la limite d'une heure quotidienne et dans un rayon maximal d'un kilomètre autour du domicile, liés soit à l'activité physique individuelle des personnes, à l'exclusion de toute pratique sportive collective et de toute proximité avec d'autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie.\n ")
convocation = input("Convocation judiciaire ou administrative et pour se rendre dans un service public\n ")
missions = input("Participation à des missions d'intérêt général sur demande de l'autorité administrative\n ")
enfants = input("Déplacement pour chercher les enfants à l'école et à l'occasion de leurs activités périscolaires.\n ")
liste_motifs = []
if travail == "x":
    liste_motifs.append("travail")
if achats == "x":
    liste_motifs.append("achats")
if sante == "x":
    liste_motifs.append("sante")
if famille == "x":
    liste_motifs.append("famille")
if handicap == "x":
    liste_motifs.append("handicap")
if sport_animaux == "x":
    liste_motifs.append("sport_animaux")
if convocation == "x":
    liste_motifs.append("convocation")
if missions == "x":
    liste_motifs.append("missions")
if enfants == "x":
    liste_motifs.append("enfants")
url = 'http://82.65.106.58:36500/generate'
content = {"prenom": prenom, "nom": nom, "date_naissance": date_naissance, "lieu_naissance": lieu_naissance, "adresse": adresse, "ville": ville, "cp": cp, "date_sortie": f"{datetime.today().day}/{datetime.today().month}/{datetime.today().year}", "heure_sortie": f"{datetime.today().hour}:{datetime.today().minute}", "motifs": liste_motifs}
headers = {"Content-Type": "application/json"}
content = json.dumps(content)
x = requests.get(url, data = content, headers=headers)
open(f"attestation_{datetime.today()}_{datetime.today().hour}-{datetime.today().minute}-{datetime.today().second}.pdf", 'wb').write(x.content)