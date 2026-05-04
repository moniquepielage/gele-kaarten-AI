#gelekaarten data 20/25

import soccerdata as sd
import sqlite3
import pandas as pd

# 1. Database verbinding (nieuwe naam voor deze test)
db_path = 'premier_league_test.db'
conn = sqlite3.connect(db_path)

print("Start test voor de Premier League...")

try:
    # 2. Soccerdata initialiseren voor de Premier League
    # Deze competitie staat standaard in de 'Valid leagues' lijst
    seizoenen = ['2024-2025']
    fbref = sd.FBref(leagues=['ENG-Premier League'], seasons=seizoenen)

    print("Data ophalen van FBref... De eerste keer kan dit 1-2 minuten duren.")

    # --- STAP 1: WEDSTRIJDEN & SCHEIDSRECHTERS ---
    schedule = fbref.read_schedule().reset_index()
    
    # Scheidsrechters tabel
    referees = schedule[['referee']].drop_duplicates().dropna().reset_index(drop=True)
    referees['referee_id'] = referees.index + 1
    referees.to_sql('scheidsrechters', conn, if_exists='replace', index=False)

    # Wedstrijden tabel
    wedstrijden = schedule.merge(referees, on='referee', how='left')
    wedstrijden = wedstrijden[['game_id', 'season', 'date', 'home_team', 'away_team', 'referee_id']]
    wedstrijden.to_sql('wedstrijden', conn, if_exists='replace', index=False)

    # --- STAP 2: SPELERS & GELE KAARTEN ---
    print("Spelerstatistieken ophalen (kaarten per wedstrijd)...")
    # We pakken de summary stats
    player_stats = fbref.read_player_match_stats(stat_type='summary').reset_index()
    
    # Flatten multi-level columns
    player_stats.columns = ['_'.join(col).strip('_') for col in player_stats.columns]
    
    # Spelers tabel
    players = player_stats[['player']].drop_duplicates().reset_index(drop=True)
    players['player_id'] = players.index + 1
    players.to_sql('spelers', conn, if_exists='replace', index=False)

    # Gele kaarten tabel
    kaarten_overzicht = player_stats.merge(players, on='player', how='left')
    gele_kaarten = kaarten_overzicht[kaarten_overzicht['Performance_CrdY'] > 0][['game_id', 'player_id', 'team', 'Performance_CrdY']]
    gele_kaarten = gele_kaarten.rename(columns={'Performance_CrdY': 'cards_yellow'})
    gele_kaarten.to_sql('gele_kaarten', conn, if_exists='replace', index=False)

    print(f"\nHOERA! Het script werkt voor de Premier League.")
    print(f"Database '{db_path}' is succesvol aangemaakt.")

except Exception as e:
    print(f"\nEr ging iets mis tijdens de test: {e}")

finally:
    conn.close()