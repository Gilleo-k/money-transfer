# requirements.txt
# fpdf2==2.8.3
# requests==2.32.3

from fpdf import FPDF
import os

def generer_pdf_teleradiologie():
    # Création du PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Utilisation de la police Helvetica (incluse par défaut) qui supporte les caractères allemands
    pdf.set_font("helvetica", size=12)

    # Titre
    pdf.set_font("helvetica", style="B", size=14)
    pdf.cell(0, 10, "Mindestanforderungen an die Internetverbindung für Teleradiologen in Deutschland", ln=True, align="C")
    pdf.ln(10)

    # Fonction pour ajouter un chapitre
    def chapitre(titre, texte):
        pdf.set_font("helvetica", "B", 12)
        pdf.cell(0, 8, titre, ln=True)
        pdf.set_font("helvetica", "", 11)
        pdf.multi_cell(0, 6, texte)
        pdf.ln(5)

    # Contenu
    chapitre("Einleitung", 
            "Diese Übersicht fasst die technischen und rechtlichen Mindestanforderungen an die Internetverbindung für Teleradiologen in Deutschland zusammen. Sie basiert auf geltenden Gesetzen, technischen Standards und Empfehlungen der Fachgesellschaften.")

    chapitre("1. Technische Mindestanforderungen", 
            """- Stabile, sichere und ausreichend schnelle Internetverbindung:
    * Download: mindestens 50 Mbit/s
    * Upload: mindestens 10-20 Mbit/s (je nach Datenvolumen höher)
- Nutzung von verschlüsselten VPN-Verbindungen (z.B. IPsec, SSL/TLS)
- Einsatz von Firewalls und Sicherheitssoftware (Virenschutz, IDS)
- Redundanz: Backup-Internetverbindung empfohlen (z.B. LTE/5G)
- Niedrige Latenzzeiten für effiziente Fernzugriffe (z.B. PACS)""")

    chapitre("2. Rechtliche und organisatorische Anforderungen", 
            """- Einhaltung der Datenschutz-Grundverordnung (DSGVO)
- Revisionssichere, datenschutzkonforme Datenübertragung
- Nutzung zertifizierter medizinischer Bildwiedergabesysteme (gem. DIN 6868-157/159)
- Bestehender Kooperationsvertrag zwischen Radiologe und Teleradiologe
- Umsetzung gemäß Strahlenschutzverordnung (StrlSchV) und Richtlinien der Bundesärztekammer""")

    chapitre("Hinweis", 
            "Die genannten Werte stellen Mindestanforderungen dar. Höhere Bandbreiten und zusätzliche Sicherheitsmaßnahmen sind je nach Einsatzszenario ausdrücklich empfohlen.")

    # Sauvegarde du fichier
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, "Mindestanforderungen_Teleradiologie.pdf")
    pdf.output(filename)
    
    print(f"PDF généré avec succès: {os.path.abspath(filename)}")
    return filename

if __name__ == "__main__":
    generer_pdf_teleradiologie()