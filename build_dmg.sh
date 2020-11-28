#!/bin/sh

# Placer le .app dans un sous-dossier « source_folder »

test -f Application-Installer.dmg && rm Application-Installer.dmg
create-dmg \
  --volname "Générateur d’attestation de déplacement dérogatoire" \
  --volicon "ADD_logo.icns" \
  --background "dmg_background.png" \
  --window-pos 200 120 \
  --window-size 700 600 \
  --icon-size 150 \
  --icon "Générateur d'attestation de déplacement dérogatoire.app" 150 330 \
  --hide-extension "Générateur d'attestation de déplacement dérogatoire.app" \
  --app-drop-link 550 330 \
  "ADD_202010_macOS_amd64_1-1.dmg" \
  "source_folder/"
