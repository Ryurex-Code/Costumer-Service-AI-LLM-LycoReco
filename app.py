# Import library yang diperlukan
import gradio as gr
from groq import Groq
import os
from dotenv import load_dotenv

# Memuat API key dari file .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Memeriksa apakah API key telah disetel
if not api_key:
    raise ValueError("API key tidak ditemukan. Pastikan sudah diatur di file .env")

client = Groq(api_key=api_key)

# Baca prompt sistem dari file
with open("prompt.txt", "r", encoding="utf-8") as file:
    system_prompt = file.read()

# Fungsi untuk menghasilkan respons chatbot
def chatbot_response(user_input, history):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.3,
        max_tokens=200,
        top_p=0.8
    )
    reply = response.choices[0].message.content
    return reply

# Antarmuka Gradio tanpa styling khusus
with gr.Blocks() as demo:
    gr.Markdown("# ☕ Café LycoReco - Layanan Pelanggan")
    gr.Markdown("Selamat datang di layanan pelanggan Café LycoReco. Silakan ketik pesan Anda di bawah ini. ☕📩")
    gr.ChatInterface(fn=chatbot_response)
demo.launch()
