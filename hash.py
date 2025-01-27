import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(["juan123"]).generate()

print(hashed_passwords)