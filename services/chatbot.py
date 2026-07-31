from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

client1 = Groq(api_key=api_key)

def llm(context,question):
    data_query = f"""
You are an expert GitHub Repository Assistant.

Your task is to answer the user's question using ONLY the provided repository context.

Instructions:
- Use only the information available in the context.
- Do not make assumptions or invent details.
- If the answer is not present in the context, reply:
  "I couldn't find that information in the repository."
- Mention the file name whenever possible.
- Keep the answer concise and accurate.

======================
Repository Context
======================

{context}

======================
User Question
======================

{question}

======================
Answer
======================
"""
    
    
    response = client1.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": data_query}
        ]
  )
    return response.choices[0].message.content