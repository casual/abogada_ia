import streamlit as st
import requests
import json
import time

def response_gen(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

def run_laws(escrito: str):
    api_url = f"{st.secrets['BASE_API_URL']}/lf/{st.secrets['LANGFLOW_ID']}/api/v1/run/{st.secrets['ENDPOINT']}"

    prompt = "Busca en que leyes se puede encontrar información sobre el siguiente tema: " + escrito

    payload = {
        "input_value": prompt,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " + st.secrets["TOKEN"], "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def setup_laws():
    st.title("Leyes")
    st.subheader("Busca leyes que mencionen tu caso", help = "Describe un tópico y encuentra todas las leyes que hablen sobre ello", divider = "gray") 

    # Inicializa el historial de mensajes
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Muestra el historial de mensajes
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat escuchando
    prompt = st.chat_input("Ingresa aquí tu mensaje...")
    if prompt:
        # Escribe el mensaje del usuario y lo guarda
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
    
        # Procesa el mensaje
        with st.spinner("Pensando..."):
            response = run_laws(prompt)
        response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]

        # Escribe el mensaje del asistente y lo guarda
        with st.chat_message("assistant", avatar = "👩‍💻"):
            st.write_stream(response_gen(response))
        st.session_state.messages.append({"role": "assistant", "content": response})

# Pasa el estado de la sesion
authenticator = st.session_state['authenticator']

try:
    authenticator.login("unrendered")
    setup_laws()
except Exception as e:
    st.error(e)