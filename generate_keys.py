import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Diego Gajardo", "Juan Amezquita"]
usernames = ["cerebro", "cornetin"]
passwords = ["diego123", "juan123"]

# Para hashear los passwords
hashed_passwords = stauth.Hasher(passwords).generate()

# Luego los hash se guardan en un archivo pickle
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)