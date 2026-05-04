#informatie ophalen

import os
import sqlite3
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
os.environ["GOOGLE_API_USE_MTLS_ENDPOINT"] = "never"

# --- 1. CONFIGURATIE & VEILIGHEID ---
# Laad de variabelen uit het .env bestand
load_dotenv()

# Haal de API-key op
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("FOUT: Geen GEMINI_API_KEY gevonden in het .env bestand!")
    print("Zorg dat je een bestand hebt genaamd .env met daarin: GEMINI_API_KEY=jouw_sleutel")
    exit()

# Configureer de AI
genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name='gemini-2.5-flash'
)

# --- 2. DE AI-SQL FUNCTIE ---
def vraag_ai_om_sql(gebruikers_vraag, tabel_naam):
    """
    Vraagt de AI om de natuurlijke taalvraag om te zetten in een SQL-query
    gebaseerd op de specifieke kolommen van jouw gecombineerde tabel.
    """
    prompt = f"""
    Je bent een SQL-expert gespecialiseerd in voetbalstatistieken. 
    Geef ALLEEN de rauwe SQL-query terug als resultaat. Geen tekst, geen uitleg, geen markdown.
    
    De database is een SQLite database met één centrale tabel (of view) genaamd '{tabel_naam}'.
    
    De kolommen in '{tabel_naam}' zijn:
    - Seizoen (bijv. '2023-2024')
    - Datum (bijv. '2024-02-04')
    - Thuisclub
    - Uitclub
    - Speler_Naam
    - Team_Speler
    - Aantal_Geel
    - Scheidsrechter

    Vraag van de gebruiker: {gebruikers_vraag}
    SQL:
    """
    
    response = model.generate_content(prompt)
    # Schoon de output op van de AI (verwijder markdown ```sql blokken)
    clean_query = response.text.replace('```sql', '').replace('```', '').strip()
    return clean_query

# --- 3. DE HOOFDAPPLICATIE ---
def start_assistent():
    # --- INSTELLINGEN ---
    db_bestand = 'premier_league_test.db' 
    tabel_naam = 'overzicht_gele_kaarten' # gecombineerde tabel/view
    
    # Controleer of de database bestaat
    if not os.path.exists(db_bestand):
        print(f"FOUT: Databasebestand '{db_bestand}' niet gevonden!")
        return

    conn = sqlite3.connect(db_bestand)
    
    print("="*40)
    print("VOETBAL DATA ASSISTENT (AI-POWERED)")
    print(f"Gekoppeld aan: {tabel_naam}")
    print("Type 'stop' om af te sluiten.")
    print("="*40)
    
    while True:
        vraag = input("\nWat wil je weten? ")
        
        if vraag.lower() in ['stop', 'exit', 'quit']:
            break
        
        if not vraag.strip():
            continue

        try:
            # 1. AI vertaalt vraag naar SQL
            sql_query = vraag_ai_om_sql(vraag, tabel_naam)
            
            # (Optioneel) Print de query voor debugging:
            # print(f"DEBUG SQL: {sql_query}")
            
            # 2. Voer SQL uit op je SQLite database
            df = pd.read_sql_query(sql_query, conn)
            
            # 3. Toon resultaat
            if df.empty:
                print("Geen gegevens gevonden die voldoen aan je vraag.")
            else:
                print("\nResultaat:")
                print(df.to_string(index=False))
                
        except Exception as e:
            print(f"Er ging iets mis: {e}")
            print("Probeer je vraag anders te formuleren.")

    conn.close()
    print("\nAssistent afgesloten. Tot ziens!")

if __name__ == "__main__":
    start_assistent()