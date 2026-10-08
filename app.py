import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Chaos vs Defender: Cyber Cafe",
    page_icon="☕",
    layout="wide"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 100%);
    }
    .game-header {
        background: linear-gradient(90deg, #EF4444 0%, #8B5CF6 50%, #10B981 100%);
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-family: 'Segoe UI', sans-serif;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="game-header">
    <h1>🔥 CHAOS VS DEFENDER 💧</h1>
    <p><b>Player 1 (Chaos - Red):</b> Control <b>[W, A, S, D]</b> — suits blue objects and locations them<br>
    <b>Игрок 2 (Defender - Green):</b> Control <b>[Стрелочки]</b> — approaches the broken (red) ones and repairs them</p>
</div>
""", unsafe_allow_html=True)

# Загружаем и выводим HTML файл
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=620)