import os 
from dotenv import load_dotenv
# Načte hodnoty ze souboru .env
load_dotenv()

# Vytáhne konkrétní proměnnou
tajny_klic = os.getenv("API_KEY")

print(f"Načtený API klíč je: {tajny_klic}")