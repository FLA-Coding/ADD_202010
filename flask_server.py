import flask, os
import weasyprint
from datetime import datetime

def prepare_html(creation, nom, prenom, date_naissance, lieu_naissance, ville, adresse, date_sortie, heure_sortie, motifs, file_name_gen):
    beginning_html = '<!DOCTYPE html><html><head><meta charset="UTF-8" /><title>Attestation de déplacement dérogatoire</title><style>@page{size: A4;margin: 0mm;}text{font-family: "Open Sans";font-size: 9px;}h1{text-align: center;font-size: 22px;font-family: "Open Sans";}h3{text-align: center;font-weight: normal;font-size: 15px;font-family: "Open Sans";}p{font-size: 13px;margin: 1px;font-family: "Open Sans";}.ptimg{width: 100%}.gdimg{width: 60%}</style></head><body><h1>ATTESTATION DE DÉPLACEMENT DÉROGATOIRE</h1><h3>En application des mesures générales nécessaires pour faire face à l\'épidémie de covid-19<br/>dans le cadre de l\'état d\'urgence sanitaire.</h3><p>Je soussigné(e),</p><p></p>'
    html_suite_1 = f'<p>Mme/M. : {nom} {prenom}</p><p>Né(e) le : {date_naissance}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;à : {lieu_naissance}</p><p>Demeurant : {adresse}</p><p>certifie que mon déplacement est lié au motif suivant (cocher la case) autorisé en application des mesures générales nécessaires pour faire face à l\'épidémie de Covid19 dans le cadre de l\'état d\'urgence sanitaire :</p><table style="width: 100%"><colgroup><col span="1" style="width: 15%;"><col span="1" style="width: 85%;"></colgroup><tbody>'
    html_list = []
    i = 0
    for motif in motifs:
        if motif == "travail":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>1. Déplacements entre le domicile et le lieu d’exercice de l’activité professionnelle ou un établissement d’enseignement ou de formation ; déplacements professionnels ne pouvant être différés ; déplacementspour un concours ou un examen ;</p><text>Note : A utiliser par les travailleurs non-salariés, lorsqu’ils ne peuvent disposer d’un justificatif de déplacement établi par leur employeur</text></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>Déplacements entre le domicile et le lieu d’exercice de l’activité professionnelle ou un établissement d’enseignement ou de formation ; déplacements professionnels ne pouvant être différés ; déplacementspour un concours ou un examen ;</p><text>Note : A utiliser par les travailleurs non-salariés, lorsqu’ils ne peuvent disposer d’un justificatif de déplacement établi par leur employeur</text></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "achats_culturel_cultuel":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>2. Déplacements pour se rendre dans un établissement culturel autorisé ou un lieu de culte ; déplacements pour effectuer des achats de biens, pour des services dont la fourniture est autorisée, pour les retraits de commandes et les livraisons à domicile ;</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>2. Déplacements pour se rendre dans un établissement culturel autorisé ou un lieu de culte ; déplacements pour effectuer des achats de biens, pour des services dont la fourniture est autorisée, pour les retraits de commandes et les livraisons à domicile ;</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "sante":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>3. Consultations, examens et soins ne pouvant être assurés à distance et achats de médicaments ;</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>3. Consultations, examens et soins ne pouvant être assurés à distance et achats de médicaments ;</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "famille":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>4. Déplacements pour motif familial impérieux, pour l’assistance aux personnes vulnérables et précaires ou la garde d’enfants ;</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>4. Déplacements pour motif familial impérieux, pour l’assistance aux personnes vulnérables et précaires ou la garde d’enfants ;</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "handicap":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>5. Déplacements des personnes en situation de handicap et leur accompagnant ;</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>5. Déplacements des personnes en situation de handicap et leur accompagnant ;</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "sport_animaux":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>6. Déplacements en plein air ou vers un lieu de plein air, sans changement du lieu de résidence, dans la limite de trois heures quotidiennes et dans un rayon maximal de vingt kilomètres autour du domicile, liés soit à l’activité physique ou aux loisirs individuels, à l’exclusion de toute pratique sportive collective et de toute proximité avec d’autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie ;</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>6. Déplacements en plein air ou vers un lieu de plein air, sans changement du lieu de résidence, dans la limite de trois heures quotidiennes et dans un rayon maximal de vingt kilomètres autour du domicile, liés soit à l’activité physique ou aux loisirs individuels, à l’exclusion de toute pratique sportive collective et de toute proximité avec d’autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie ;</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "convocation":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>7. Convocations judiciaires ou administratives et déplacements pour se rendre dans un service public ;</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>7. Convocations judiciaires ou administratives et déplacements pour se rendre dans un service public ;</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "missions":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>8. Participation à des missions d’intérêt général sur demande de l’autorité administrative ;</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>8. Participation à des missions d’intérêt général sur demande de l’autorité administrative ;</p></td></tr>")
    i = 0
    for motif in motifs:
        if motif == "enfants":
            html_list.append("<tr><td><h2>☑</h2></td><td><p>9. Déplacements pour chercher les enfants à l’école et à l’occasion de leurs activités périscolaires ;</p></td></tr>")
            i = 1
    if i == 0:
        html_list.append("<tr><td><h2>☐</h2></td><td><p>9. Déplacements pour chercher les enfants à l’école et à l’occasion de leurs activités périscolaires ;</p></td></tr>")
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

@app.errorhandler(500)
def internal_server_error(e):
    return flask.send_file("500.pdf", mimetype='application/pdf'), 500

@app.route("/test")
def test():
    print(f"/test - {flask.request.remote_addr}")
    return "The server is up."

@app.route("/")
def download():
    return flask.redirect("https://github.com/fla-coding/ADD_202010/releases/latest", code=301) 

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
    to_parse_data = f"Cree le: {creation};\nNom: {nom};\nPrenom: {prenom};\nNaissance: {naissance};\nAdresse: {adresse};\nSortie: {sortie};\nMotifs: {motifs}"
    os.system(f'qr --factory=pymaging "{to_parse_data}" > "{os.getcwd()}/results/{file_name_gen}.png"')
    prepare_html(creation=creation, nom=nom, prenom=prenom, date_naissance=date_naissance, lieu_naissance=lieu_naissance, ville=ville, adresse=adresse, date_sortie=date_sortie, heure_sortie=heure_sortie, motifs=motifs_list, file_name_gen=file_name_gen)
    pdf = weasyprint.HTML(f'results/{file_name_gen}.html').write_pdf()
    open(f'results/{file_name_gen}.pdf', 'wb').write(pdf)
    return flask.send_file(f"results/{file_name_gen}.pdf", mimetype='application/pdf')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=36500)