import requests, json, os
from datetime import datetime

print("\nGÉNÉRATEUR D'ATTESTATION DE DÉPLACEMENT DÉROGATOIRE\n\n")
prenom = input('Prénom : ')
nom = input('Nom : ')
date_naissance = input('Date de naissance (JJ/MM/AAAA) : ')
lieu_naissance = input('Lieu de naissance : ')
adresse = input('Adresse (n° et rue) : ')
cp = input('Code postal : ')
ville = input('Ville : ')
print('Écrivez « x » pour chaque motif que vous souhaitez voir apparaître coché :\n')
travail = input("Déplacements entre le domicile et le lieu d’exercice de l’activité professionnelle ou un établissement d’enseignement ou de formation ; déplacements professionnels ne pouvant être différés ; déplacements pour un concours ou un examen\n ")
achats_culturel_cultuel = input ("Déplacements pour se rendre dans un établissement culturel autorisé ou un lieu de culte ; déplacements pour effectuer des achats de biens, pour des services dont la fourniture est autorisée, pour les retraits de commandes et les livraisons à domicile\n ")
sante = input("Consultations, examens et soins ne pouvant être assurés à distance et achats de médicaments\n ")
famille = input("Déplacements pour motif familial impérieux, pour l’assistance aux personnes vulnérables et précaires ou la garde d’enfants\n ")
handicap = input("Déplacements des personnes en situation de handicap et leur accompagnant\n ")
sport_animaux = input("Déplacements en plein air ou vers un lieu de plein air, sans changement du lieu de résidence, dans la limite de trois heures quotidiennes et dans un rayon maximal de vingt kilomètres autour du domicile, liés soit à l’activité physique ou aux loisirs individuels, à l’exclusion de toute pratique sportive collective et de toute proximité avec d’autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie\n ")
convocation = input("Convocations judiciaires ou administratives et déplacements pour se rendre dans un service public\n ")
missions = input("Participation à des missions d’intérêt général sur demande de l’autorité administrative\n ")
enfants = input("Déplacements pour chercher les enfants à l’école et à l’occasion de leurs activités périscolaires\n ")
liste_motifs = []
if travail == "x":
    liste_motifs.append("travail")
if achats_culturel_cultuel == "x":
    liste_motifs.append("achats_culturel_cultuel")
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
try:
    url = 'https://fla-coding.freeboxos.fr:36500/generate'
    content = {"prenom": prenom, "nom": nom, "date_naissance": date_naissance, "lieu_naissance": lieu_naissance, "adresse": adresse, "ville": ville, "cp": cp, "date_sortie": f"{datetime.today().day}/{datetime.today().month}/{datetime.today().year}", "heure_sortie": f"{datetime.today().hour}:{datetime.today().minute}", "motifs": liste_motifs}
    headers = {"Content-Type": "application/json"}
    content = json.dumps(content)
    x = requests.get(url, data=content, headers=headers)
    open(f"attestation_{datetime.today()}_{datetime.today().hour}-{datetime.today().minute}-{datetime.today().second}.pdf", 'wb').write(x.content)
    print(f"\n\nL'attestation a bien été sauvegardée dans {os.getcwd()}/attestation_{datetime.today()}_{datetime.today().hour}-{datetime.today().minute}-{datetime.today().second}.pdf")
except:
    print("\n\nUne erreur est survenue.")
