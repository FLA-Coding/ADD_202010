#!/bin/sh

python3 -m PyInstaller --onefile --noconsole --icon ADD_logo.ico --name "Générateur d\'attestation de déplacement dérogatoire" --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' tkinter_client_lnx.pyw 