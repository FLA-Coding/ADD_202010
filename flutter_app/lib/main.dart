import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final appTitle = "Générateur d'attestation";

    return MaterialApp(
      title: appTitle,
      home: Scaffold(
        appBar: AppBar(
          title: Text(appTitle),
        ),
        body: new Container(
          margin: new EdgeInsets.symmetric(horizontal: 20.0),
          child: MyCustomForm()
          )
        //MyCustomForm(),
      ),
    );
  }
}

// Create a Form widget.
class MyCustomForm extends StatefulWidget {
  @override
  MyCustomFormState createState() {
    return MyCustomFormState();
  }
}

// Create a corresponding State class.
// This class holds data related to the form.
class MyCustomFormState extends State<MyCustomForm> {
  // Create a global key that uniquely identifies the Form widget
  // and allows validation of the form.
  //
  // Note: This is a GlobalKey<FormState>,
  // not a GlobalKey<MyCustomFormState>.
  final _formKey = GlobalKey<FormState>();
  bool _checked1 = false;
  bool _checked2 = false;
  bool _checked3 = false;
  bool _checked4 = false;
  bool _checked5 = false;
  bool _checked6 = false;
  bool _checked7 = false;
  bool _checked8 = false;
  bool _checked9 = false;
  var tmotif1 = "Déplacements entre le domicile et le lieu d’exercice de l’activité professionnelle ou un établissement d’enseignement ou de formation, déplacements professionnels ne pouvant être différés, déplacements pour un concours ou un examen.";
  var tmotif2 = "Déplacements pour effectuer des achats de fournitures nécessaires à l’activité professionnelle, des achats de première nécessité dans des établissements dont les activités demeurent autorisées, le retrait de commande et les livraisons à domicile.";
  var tmotif3 = "Consultations, examens et soins ne pouvant être assurés à distance et l’achat de médicaments.";
  var tmotif4 = "Déplacements pour motif familial impérieux, pour l’assistance aux personnes vulnérables et précaires ou la garde d’enfants.";
  var tmotif5 = "Déplacement des personnes en situation de handicap et leur accompagnant.";
  var tmotif6 = "Déplacements brefs, dans la limite d’une heure quotidienne et dans un rayon maximal d’un kilomètre autour du domicile, liés soit à l'activité physique individuelle des personnes, à l'exclusion de toute pratique sportive collective et de toute proximité avec d'autres personnes, soit à la promenade avec les seules personnes regroupées dans un même domicile, soit aux besoins des animaux de compagnie.";
  var tmotif7 = "Convocation judiciaire ou administrative et pour se rendre dans un service public.";
  var tmotif8 = "Participation à des missions d’intérêt général sur demande de l’autorité administrative.";
  var tmotif9 = "Déplacement pour chercher les enfants à l’école et à l’occasion de leurs activités périscolaires.";
  @override
  Widget build(BuildContext context) {
    // Build a Form widget using the _formKey created above.
    return Form(
      key: _formKey,
      child: SingleChildScrollView(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Text(''),
          TextFormField(
            decoration: InputDecoration(
              labelText: "Prénom",
              border: const OutlineInputBorder(),
              ),
            validator: (value) {
              if (value.isEmpty) {
                return "Merci d'entrer votre prénom.";
              }
              return null;
            },
          ),
          TextFormField(
            decoration: InputDecoration(
              labelText: "Nom",
              border: const OutlineInputBorder(),
              ),
            validator: (value) {
              if (value.isEmpty) {
                return "Merci d'entrer votre nom.";
              }
              return null;
            },
          ),
          TextFormField(
            decoration: InputDecoration(
              labelText: "Date de naissance (JJ/MM/AAAA)",
              border: const OutlineInputBorder(),
              ),
            validator: (value) {
              if (value.isEmpty) {
                return "Merci d'entrer votre date de naissance.";
              }
              return null;
            },
          ),
          TextFormField(
            decoration: InputDecoration(
              labelText: "Lieu de naissance",
              border: const OutlineInputBorder(),
              ),
            validator: (value) {
              if (value.isEmpty) {
                return "Merci d'entrer votre lieu de naissance.";
              }
              return null;
            },
          ),
          TextFormField(
            decoration: InputDecoration(
              labelText: "Adresse (n° et rue)",
              border: const OutlineInputBorder(),
              ),
            validator: (value) {
              if (value.isEmpty) {
                return "Merci d'entrer votre adresse.";
              }
              return null;
            },
          ),
          TextFormField(
            decoration: InputDecoration(
              labelText: "Code postal",
              border: const OutlineInputBorder(),
              ),
            validator: (value) {
              if (value.isEmpty) {
                return "Merci d'entrer votre code postal.";
              }
              return null;
            },
          ),
          TextFormField(
            decoration: InputDecoration(
              labelText: "Ville",
              border: const OutlineInputBorder(),
              ),
            validator: (value) {
              if (value.isEmpty) {
                return "Merci d'entrer votre ville.";
              }
              return null;
            },
          ),
          CheckboxListTile(
            title: Text(tmotif1),
            value: _checked1,
            onChanged: (bool value) { 
                        setState(() {
                          _checked1 = value; 
                        }); 
                      },
            controlAffinity: ListTileControlAffinity.platform,
          ),
          CheckboxListTile(
            title: Text(tmotif2),
            value: _checked2,
            onChanged: (bool value) { 
                        setState(() {
                          _checked2 = value; 
                        }); 
                      },
            controlAffinity: ListTileControlAffinity.platform,
          ),
          CheckboxListTile(
            title: Text(tmotif3),
            value: _checked3,
            onChanged: (bool value) { 
                        setState(() {
                          _checked3 = value; 
                        }); 
                      },
            controlAffinity: ListTileControlAffinity.platform,
          ),
          CheckboxListTile(
            title: Text(tmotif4),
            value: _checked4,
            onChanged: (bool value) { 
                        setState(() {
                          _checked4 = value; 
                        }); 
                      },
            controlAffinity: ListTileControlAffinity.platform,
          ),
          CheckboxListTile(
            title: Text(tmotif5),
            value: _checked5,
            onChanged: (bool value) { 
                        setState(() {
                          _checked5 = value; 
                        }); 
                      },
            controlAffinity: ListTileControlAffinity.platform,
          ),
          CheckboxListTile(
            title: Text(tmotif6),
            value: _checked6,
            onChanged: (bool value) { 
                        setState(() {
                          _checked6 = value; 
                        }); 
                      },
            controlAffinity: ListTileControlAffinity.platform,
          ),
          CheckboxListTile(
            title: Text(tmotif7),
            value: _checked7,
            onChanged: (bool value) { 
                        setState(() {
                          _checked7 = value; 
                        }); 
                      },
            controlAffinity: ListTileControlAffinity.platform,
          ),
          CheckboxListTile(
            title: Text(tmotif8),
            value: _checked8,
            onChanged: (bool value) { 
                        setState(() {
                          _checked8 = value; 
                        }); 
                      },
            controlAffinity: ListTileControlAffinity.platform,
          ),
          CheckboxListTile(
            title: Text(tmotif9),
            value: _checked9,
            onChanged: (bool value) { 
                        setState(() {
                          _checked9 = value; 
                        }); 
                      },
            controlAffinity: ListTileControlAffinity.platform,
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 20.0),
            child: ElevatedButton(
              onPressed: () {
                // Validate returns true if the form is valid, or false
                // otherwise.
                if (_formKey.currentState.validate()) {
                  // If the form is valid, display a Snackbar.
                  Scaffold.of(context)
                      .showSnackBar(SnackBar(content: Text('Veuillez patienter...')));
                }
              },
              child: Text('Générer'),
            ),
          ),
        ],
      ),
    ),
    );
  }
}