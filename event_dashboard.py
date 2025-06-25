pip install streamlit pandas

import streamlit as st
import pandas as pd
from datetime import datetime

# Примерные данные (можно заменить на fetch из API)
data = [
    {
        "name": "Научная конференция AI 2025",
        "description": "Обсуждение новых подходов к генеративному ИИ",
        "date": "2025-07-15",
        "location": "Москва",
        "format": "Оффлайн",
        "topic": "Искусственный интеллект"
    },
    {
        "name": "Летняя школа по биоинформатике",
        "description": "Курс по анализу биологических данных",
        "date": "2025-08-01",
        "location": "Онлайн",
        "format": "Онлайн",
        "topic": "Биоинформатика"
    },
]

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])

# -------- Интерфейс Streamlit --------
st.set_page_config(page_title="EventHorizon", layout="wide")
st.title("🔭 EventHorizon — Рекомендованные мероприятия")

# --- Фильтры ---
st.sidebar.header("🔍 Фильтры")
topics = df["topic"].unique().tolist()
selected_topic = st.sidebar.multiselect("Тематика", topics, default=topics)

formats = df["format"].unique().tolist()
selected_format = st.sidebar.multiselect("Формат", formats, default=formats)

date_range = st.sidebar.date_input("Дата проведения", [df["date"].min(), df["date"].max()])

# --- Фильтрация данных ---
filtered_df = df[
    (df["topic"].isin(selected_topic)) &
    (df["format"].isin(selected_format)) &
    (df["date"] >= pd.to_datetime(date_range[0])) &
    (df["date"] <= pd.to_datetime(date_range[1]))
]

# --- Вывод карточек мероприятий ---
st.subheader(f"🔬 Найдено {len(filtered_df)} мероприятий")

for _, row in filtered_df.iterrows():
    with st.container():
        st.markdown(f"### 🗓️ {row['name']}")
        st.markdown(f"📅 Дата: {row['date'].strftime('%d.%m.%Y')}")
        st.markdown(f"📍 Локация: {row['location']}  |  Формат: {row['format']}")
        st.markdown(f"📌 Описание: {row['description']}")
        st.markdown("---")
