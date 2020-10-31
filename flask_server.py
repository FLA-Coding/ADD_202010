import flask, os
import weasyprint
from waitress import serve
from datetime import datetime

def prepare_html(creation, nom, prenom, date_naissance, lieu_naissance, ville, adresse, date_sortie, heure_sortie, motifs, file_name_gen):
    beginning_html = '<!DOCTYPE html><html><head><meta charset="UTF-8" /><title>Attestation de déplacement dérogatoire</title><style>@page{size: A4;margin: 0mm;}h1{text-align: center;font-size: 22px}h3{text-align: center;font-weight: normal;font-size: 15px}p{font-size: 13px;margin: 1px}.ptimg{width: 100%}.gdimg{width: 60%}</style></head><body><h1>ATTESTATION DE DÉPLACEMENT DÉROGATOIRE</h1><h3>En application des mesures générales nécessaires pour faire face à l\'épidémie de covid-19<br/>dans le cadre de l\'état d\'urgence sanitaire.</h3><p>Je soussigné(e),</p><p></p>'
    html_suite_1 = f'<p>Mme/M. : {nom} {prenom}</p><p>Né(e) le : {date_naissance}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;à : {lieu_naissance}</p><p>Demeurant : {adresse}</p><p>certifie que mon déplacement est lié au motif suivant (cocher la case) autorisé en application des mesures générales nécessaires pour faire face à l\'épidémie de Covid19 dans le cadre de l\'état d\'urgence sanitaire :</p><table style="width: 100%"><colgroup><col span="1" style="width: 15%;"><col span="1" style="width: 85%;"></colgroup><tbody>'
    html_list = []
    i = 0
    for motif in motifs:
        if motif == "travail":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>Déplacements entre le domicile et le lieu d'exercice de l'activité professionnelle ou un établissement d'enseignement ou de formation, déplacements professionnels ne pouvant être différés, déplacements pour un concours ou un examen.</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>Déplacements entre le domicile et le lieu d'exercice de l'activité professionnelle ou un établissement d'enseignement ou de formation, déplacements professionnels ne pouvant être différés, déplacements pour un concours ou un examen.</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "achats":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>Déplacements pour effectuer des achats de fournitures nécessaires à l'activité professionelle, des achats de première nécessité dans des établissements dont les activités demeurent autorisées, le retrait de commande et les livraisons à domicile.</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>Déplacements pour effectuer des achats de fournitures nécessaires à l'activité professionelle, des achats de première nécessité dans des établissements dont les activités demeurent autorisées, le retrait de commande et les livraisons à domicile.</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "sante":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>Consultations, examens et soins ne pouvant être ni assurés à distance ni différés et l'achat de médicaments.</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>Consultations, examens et soins ne pouvant être ni assurés à distance ni différés et l'achat de médicaments.</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "famille":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>Déplacement pour motif familial impérieux, pour l'assistance aux personnes vulnérables et précaires ou la garde d'enfants.</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>Déplacement pour motif familial impérieux, pour l'assistance aux personnes vulnérables et précaires ou la garde d'enfants.</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "handicap":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>Déplacement des personnes en situation de handicap et leur accompagnant.</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>Déplacement des personnes en situation de handicap et leur accompagnant.</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "sport_animaux":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>Déplacements brefs, dans la limite d'une heure quotidienne et dans un rayon maximal d'un kilomètre autour du domicile, liés soit à l'activité physique individuelle des personnes, à l'exclusion de toute pratique sportive collective et de toute proximité avec d'autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie.</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>Déplacements brefs, dans la limite d'une heure quotidienne et dans un rayon maximal d'un kilomètre autour du domicile, liés soit à l'activité physique individuelle des personnes, à l'exclusion de toute pratique sportive collective et de toute proximité avec d'autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie.</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "convocation":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>Convocation judiciaire ou administrative et pour se rendre dans un service public</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>Convocation judiciaire ou administrative et pour se rendre dans un service public</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "missions":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>Participation à des missions d'intérêt général sur demande de l'autorité administrative</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>Participation à des missions d'intérêt général sur demande de l'autorité administrative</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "enfants":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>Déplacement pour chercher les enfants à l'école et à l'occasion de leurs activités périscolaires.</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>Déplacement pour chercher les enfants à l'école et à l'occasion de leurs activités périscolaires.</p></td></tr>")
    end_html = f'</tbody></table><table style="width: 100%"><colgroup><col span="1" style="width: 75%;"><col span="1" style="width: 25%;"></colgroup><tbody><tr><td><p>Fait à : {ville}</p><p>Le : {date_sortie}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;à : {heure_sortie}</p><p>(Date et heure de début de sortie à mentionner obligatoirement)</p><p>Signature :</p></td><td><img src={file_name_gen}.png class=ptimg></td></tr></tbody></table><p><img src={file_name_gen}.png class="gdimg"></p></body></html>'
    html_final = f"{beginning_html}{html_suite_1}"
    for element in html_list:
        html_final = f"{html_final}{element}"
    html_final = f"{html_final}{end_html}"
    with open (f"results/{file_name_gen}.html", "w") as html_file:
        html_file.write(html_final)

app = flask.Flask(__name__)
os.system('rm -rf results/')
os.system('mkdir results/')

@app.route("/test")
def test():
    print(f"/test - {flask.request.remote_addr}")
    return "The server is up."

@app.route("/generate")
def generate():
    print(f"/generate - {flask.request.remote_addr}")
    json = flask.request.json
    creation = f"{datetime.today().day}/{datetime.today().month}/{datetime.today().year} a {datetime.today().hour}h{datetime.today().minute}"
    nom = json["nom"]
    prenom = json["prenom"]
    date_naissance = json["date_naissance"]
    lieu_naissance = json["lieu_naissance"]
    naissance = f"{json['date_naissance']} a {json['lieu_naissance']}"
    ville = json["ville"]
    adresse = f"{json['adresse']} {json['cp']} {json['ville']}"
    date_sortie = json["date_sortie"]
    heure_sortie = json["heure_sortie"]
    sortie = f"{json['date_sortie']} a {json['heure_sortie']}"
    motifs_list = json["motifs"]
    motif = None
    k = 0
    for motif in json["motifs"]:
        if k == 0:
            motifs = motif
            k = 1
        else:
            motifs = f"{motifs}, {motif}"
    file_name_gen = "result"
    to_parse_data = f"Cree le: {creation};\n Nom: {nom};\n Prenom: {prenom};\n Naissance: {naissance};\n Adresse: {adresse};\n Sortie: {sortie};\n Motifs: {motifs}"
    os.system(f'qr --factory=pymaging "{to_parse_data}" > "{os.getcwd()}/results/{file_name_gen}.png"')
    prepare_html(creation=creation, nom=nom, prenom=prenom, date_naissance=date_naissance, lieu_naissance=lieu_naissance, ville=ville, adresse=adresse, date_sortie=date_sortie, heure_sortie=heure_sortie, motifs=motifs_list, file_name_gen=file_name_gen)
    pdf = weasyprint.HTML(f'results/{file_name_gen}.html').write_pdf()
    open(f'results/{file_name_gen}.pdf', 'wb').write(pdf)
    return flask.send_file(f"results/{file_name_gen}.pdf", mimetype='application/pdf')

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=36500)