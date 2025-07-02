import streamlit as st
st.title("🎈 Transformers Learning Challenge")
st.write("Khaled Fathy")
!npm install localtunnel
 !pip install pyngrok
        # Then, after importing, set your auth token:
        # from pyngrok import ngrok
        # ngrok.set_auth_token("YOUR_NGROK_AUTH_TOKEN")
    !streamlit run app.py &>/content/logs.txt &
        !npx localtunnel --port 8501
  # from pyngrok import ngrok
        # public_url = ngrok.connect(port="8501")
        # print(public_url)
