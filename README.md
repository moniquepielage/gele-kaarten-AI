Markdown
# ⚽ Voetbal Gele Kaarten AI Assistent

Dit project is een AI-gestuurde assistent die natuurlijke taalvragen (Nederlands) beantwoordt over voetbalstatistieken. De assistent gebruikt de **Gemini 2.5 Flash API** om vragen om te zetten in SQL-queries, die vervolgens worden uitgevoerd op een lokale SQLite database met Premier League data.

## 🚀 Functionaliteiten
- **Natuurlijke Taal naar SQL:** Stel vragen zoals "Welke scheidsrechter gaf de meeste kaarten?" zonder zelf SQL te hoeven schrijven.
- **Geautomatiseerde Data:** Haalt voetbaldata op via de `Soccerdata` bibliotheek (FBref).
- **SQLite Integratie:** Slaat data efficiënt op in een gestructureerde database.
- **Veiligheid:** Gebruikt omgevingsvariabelen (`.env`) om API-sleutels te beschermen.

## 🛠️ Installatie

1. **Clone de repository:**
   ```bash
   git clone [https://github.com/moniquepielage/voetbal-kaarten-ai.git](https://github.com/jouwnaam/voetbal-kaarten-ai.git)
   cd voetbal-kaarten-ai
Installeer de benodigde Python-bibliotheken:

Bash
   pip install soccerdata pandas google-generativeai python-dotenv
Configureer je API Key:

Maak een bestand aan genaamd .env in de hoofdmap.

Voeg je Google Gemini API key toe:

Plaintext
GEMINI_API_KEY=jouw_api_key_hier
Database voorbereiden:

Zorg dat de SQLite database premier_league_test.db aanwezig is met de tabel/view overzicht_gele_kaarten.

📈 Gebruik
Start de assistent door het hoofdbestand uit te voeren:

Bash
python #informatie_ophalen.py
Voorbeeldvragen:
"Wie gaf de meeste gele kaarten in het seizoen 2023-2024?"

"Welke speler van Arsenal heeft de meeste kaarten?"

"Hoeveel gele kaarten vielen er gemiddeld per wedstrijd?"

📂 Projectstructuur
#informatie_ophalen.py: De hoofdapplicatie en AI-logica.

check_models.py: Hulpscript om beschikbare Gemini-modellen te controleren.

.env: (Niet meegeleverd) Bevat de geheime API-sleutels.

premier_league_test.db: De lokale database met wedstrijd- en spelersgegevens.

⚖️ Licentie
Dit project is gemaakt voor educatieve doeleinden. Data is afkomstig van FBref via Soccerdata.