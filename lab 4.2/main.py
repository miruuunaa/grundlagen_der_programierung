def ersetzen_der_worter(text_datei, zu_ersetzen, ersatz):
    try:
        with open(text_datei, 'r') as datei:
            text = datei.read()

        ersetzt_text, anzahl_ersetzt = text.replace(zu_ersetzen, ersatz), text.count(zu_ersetzen)

        if anzahl_ersetzt > 0:
            with open(text_datei, 'w') as datei:
                datei.write(ersetzt_text)
            print(f"Ersetzt '{zu_ersetzen}' durch '{ersatz}' an {anzahl_ersetzt} Stellen.")
        else:
            print(f"Das Wort '{zu_ersetzen}' wurde nicht gefunden.")

    except FileNotFoundError:
        print(f"Die Datei '{text_datei}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Fehler: {e}")

text_datei = input("Name der Datei: ")
zu_ersetzen = input("Wort zu ersetzen: ")
ersatz = input("Ersatzwort: ")

ersetzen_der_worter(text_datei, zu_ersetzen, ersatz)