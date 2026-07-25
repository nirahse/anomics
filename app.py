import streamlit as st
import pandas as pd
from data import MISSION_DATA

st.set_page_config(
    page_title="EVE Guide - Anomische Missionen",
    page_icon="🔥",
    layout="wide"
)

# --- SIDEBAR NAVI ---
st.sidebar.title("🔥 Burner Missionen")
auswahl = st.sidebar.radio("Wähle eine Kombination:", list(MISSION_DATA.keys()))
daten = MISSION_DATA[auswahl]

# --- HAUPTFLÄCHE (Fokus auf die 3 Kernbereiche) ---
st.title(f"🚀 {auswahl}")
st.markdown("---")

# Layout mit 3 Spalten: Flugshow, Fit, Flugplan
col_flugshow, col_fit, col_flugplan = st.columns([1.2, 1.0, 1.2])

# 1. Kategorie: FLUGSHOW
with col_flugshow:
    st.header("📹 1. Flugshow")
    st.video(daten["flugshow_url"])

# 2. Kategorie: FIT
with col_fit:
    st.header("🛠️ 2. Fit")
    st.code(daten["fit"], language="text")

# 3. Kategorie: FLUGPLAN
with col_flugplan:
    st.header("📋 3. Flugplan")
    for schritt in daten["flugplan"]:
        st.markdown(schritt)

st.markdown("---")

# --- DETAILS (Eingeklappt für interessierte Spieler) ---
st.subheader("🧠 Deep Dive & Hintergrund-Infos")

with st.expander("Skills"):
    st.markdown("Skill-Anforderungen für Anomische Missionen sind in der Regel sehr hoch. :orange[Das ist nichts für Anfänger-Charaktere.] Hier sind die empfohlenen Skills.")
        
    df_skills = pd.DataFrame(daten["details_skills"])
    
    st.dataframe(
        df_skills, 
        use_container_width=True, # volle Breite des Aufklappmenüs
        hide_index=True          # Versteckt Zeilennummern
    )

with st.expander("Warum ist das Fit so gewählt? (Theorie & Module)"):
    st.write(daten["details_warum_fit"])

with st.expander("Schadensprofile & Resistenzen"):
    st.write(daten["details_resistenzen"])

with st.expander("Implantate"):
    st.write(daten["details_implants"])


