import streamlit as st
from modules.creative import ContentAI
from modules.trends import TrendScraper # Предполагаемый модуль
import os

st.set_page_config(page_title="NexusFlow AI 2026", layout="wide", initial_sidebar_state="collapsed")

# Кастомный CSS для темной темы 2026
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 10px; background: linear-gradient(45deg, #6200ea, #03dac6); color: white; border: none; }
    .card { padding: 20px; border-radius: 15px; background: #1a1c24; border: 1px solid #333; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 NexusFlow AI")
st.subheader("Автономная фабрика контента")

tabs = st.tabs(["Dashboard", "Trends & Radar", "Studio", "Scheduler", "Analytics"])

with tabs[0]: # Dashboard
    col1, col2, col3 = st.columns(3)
    col1.metric("Опубликовано", "128", "+12% за неделю")
    col2.metric("Охват", "450K", "+5% за неделю")
    col3.metric("Engagement", "8.4%", "+1.2%")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    niche = st.text_input("Введите вашу нишу (например: 'AI Tools for Business')", "Crypto Trading")
    if st.button("Запустить One-Click Генерацию"):
        with st.spinner('Анализируем тренды и создаем контент...'):
            ai = ContentAI()
            plan = ai.generate_plan(niche)
            st.success("План на 30 дней готов! Перейдите во вкладку Studio.")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[1]: # Trends
    st.write("### Текущие тренды (Real-time)")
    # Здесь будет вывод из modules/trends.py
    st.info("TikTok Trend: 'AI automation for agencies' is rising in USA/Ukraine")
    st.button("Создать контент под этот тренд")

with tabs[2]: # Studio
    st.write("### Контент-редактор")
    topic = st.text_input("Тема статьи/видео")
    if st.button("Сгенерировать статью и видео"):
        ai = ContentAI()
        article = ai.generate_article(topic)
        st.markdown(article)
        # Здесь вызов MediaAgent для генерации видео

with tabs[3]: # Scheduler
    st.write("### Очередь публикаций")
    # Таблица с будущими постами
    st.table([
        {"Дата": "2026-05-20", "Платформа": "Instagram", "Статус": "Ожидание"},
        {"Дата": "2026-05-20", "Платформа": "WordPress", "Статус": "Готово"}
    ])
