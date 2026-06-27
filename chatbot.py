import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

print("Blue Cup Coffee Assistant is ready! Type 'quit' to exit.\n")

messages = []

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("Thanks for chatting. Have a great day!")
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="""You are a friendly customer service assistant for Blue Cup Coffee, a cozy café in Los Angeles.

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

Only answer questions related to our café. For anything unrelated, politely let the customer know you can only help with Blue Cup Coffee inquiries.""",
        messages=messages
    )
    
    reply = response.content[0].text
    messages.append({"role": "assistant", "content": reply})
    
    print(f"Assistant: {reply}\n")
