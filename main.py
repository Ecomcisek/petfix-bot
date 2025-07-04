import os
from datetime import datetime
from pathlib import Path

# === USTAWIENIA ===
today = datetime.now().strftime("%Y-%m-%d")
main_folder = f"daily_video/{today}"
short_folder = f"short_video/{today}"

# === UTWÓRZ FOLDERY ===
os.makedirs(main_folder, exist_ok=True)
os.makedirs(short_folder, exist_ok=True)

# === SYMULUJ POBRANIE WIDEO ===
for i in range(1, 11):  # np. 10 klipów
    dummy_path = Path(main_folder) / f"cat_clip_{i}.mp4"
    dummy_path.touch()  # pusty plik na razie

# === SHORT VIDEO ===
short_dummy = Path(short_folder) / "viral_short.mp4"
short_dummy.touch()

# === OPIS TEKSTOWY ===
desc_path = Path(main_folder) / "opis.txt"
desc_path.write_text(f"""\
🎬 Tytuł: Najlepsze śmieszne koty i psy z internetu – {today} 🐶🐱

📄 Opis:
Dziś przygotowaliśmy dla Ciebie porcję najnowszych, najbardziej viralowych śmiesznych zwierzaków z TikToka, Instagrama i YouTube. Mamy tu koty, psy, papugi i inne dziwolągi, które rozśmieszą Cię do łez!

👍 Zostaw lajka i suba, jeśli chcesz więcej!

#koty #psy #śmiesznezwierzęta #viral #funnyanimals #tiktok #petfixshorts #zwierzaki
""", encoding="utf-8")
