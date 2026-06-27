import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

st.set_page_config(page_title="Blue Cup Coffee", page_icon="☕")
st.title("☕ Blue Cup Coffee Assistant")
st.caption("Ask me anything about our café!")

SYSTEM_PROMPT = """You are a friendly customer service assistant for Blue Cup Coffee, a cozy café in Los Angeles.

Location: 2847 Sunset Boulevard, Los Angeles, CA 90026
Hours: Monday to Sunday, 7am - 9pm
Phone: (323) 555-0184

Menu:
- Latte: $6.50
- Cappuccino: $6.00
- Americano: $4.50
- Cold Brew: $5.50
- Matcha Latte: $6.50
- Blueberry Muffin: $4.00
- Avocado Toast: $9.00

Only answer questions related to our café. For anything unrelated, politely let the customer know you can only help with Blue Cup Coffee inquiries."""

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=st.session_state.messages
        )
        reply = response.content[0].text
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
