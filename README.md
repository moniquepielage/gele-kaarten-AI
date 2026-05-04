# ⚽ Football Yellow Cards AI Assistant

In my quest to practice my python I've been asking people for projects. My oldest son asked me for this one. Originally, he wanted it on the Dutch competition. the request made me realise some things to consider when planning projects.... first of all, a lot of databases cost money. To circumvent this, I searched for free data I could use. I hit problem number 2: free data is not very extensive. So I switched to a free data set with limitations, seeing this is only to practice. And I had to change to the Premier League

This project is an AI-driven assistant that answers natural language questions (Dutch/English) about football statistics. The assistant utilizes the **Gemini 2.5 Flash API** to convert user questions into SQL queries, which are then executed against a local SQLite database containing Premier League data.

## 🚀 Features
- **Natural Language to SQL:** Ask questions like "Which referee issued the most cards?" without needing to write SQL yourself.
- **Automated Data:** Fetches football data via the `Soccerdata` library (FBref).
- **SQLite Integration:** Stores data efficiently in a structured local database.
- **Security:** Uses environment variables (`.env`) to protect API keys.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/moniquepielage/gele-kaarten-AI.git
   cd gele-kaarten-AI

2. **Install required Python libraries:**
   ```bash
   pip install soccerdata pandas google-generativeai python-dotenv

3. **Configure your API Key:**
   - Create a file named `.env` in the root directory.
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     
4. **Prepare the Database:**
   Ensure the SQLite database `premier_league_test.db` is present and contains the table/view `overzicht_gele_kaarten`.

## 📈 Usage
Start the assistant by running the main script:

```bash
python #informatie_ophalen.py
```

Example Questions:
- "Who issued the most yellow cards in the 2023-2024 season?"
- "Which Arsenal player has the most cards?"
- "What was the average number of yellow cards per match?"

## 📂 Project Structure
- `#informatie_ophalen.py`: The main application and AI logic.
- `check_models.py`: Utility script to check available Gemini models.
- `.env`: (Not included in repo) Contains secret API keys.
- `premier_league_test.db`: Local database containing match and player data.

## ⚖️ License
This project was created for educational purposes. Data is sourced from FBref via Soccerdata.
