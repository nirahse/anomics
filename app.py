import streamlit as st
import pandas as pd
from data import MISSION_DATA

st.set_page_config(
    page_title="EVE Guide - Anomische Missionen",
    page_icon="🔥",
    layout="wide"
)

# 2. Das Logo direkt ganz oben auf der Hauptfläche anzeigen
# (use_container_width=False sorgt dafür, dass es in Originalgröße bleibt)
#st.image("logo_title.png", use_container_width=False)

# CSS-Trick: Abstände für das Hauptfenster UND die Sidebar reduzieren
st.markdown(
    """
    <style>
        /* 1. Abstand oben im Hauptfenster entfernen */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 0rem !important;
        }
        
        /* 2. NEU: Abstand oben in der linken Sidebar entfernen */
        .stSidebarUserContent {
            padding-top: 0.5rem !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# --- SIDEBAR NAVI ---
st.sidebar.title("🔥 Burner Missionen")
auswahl = st.sidebar.radio("Wähle einen Guide:", list(MISSION_DATA.keys()))
daten = MISSION_DATA[auswahl]

# --- HAUPTFLÄCHE (Fokus auf die 3 Kernbereiche) ---
st.title(f"🚀 {auswahl}")
st.markdown("---")

# Layout mit 3 Spalten: Flugshow, Fit, Flugplan
col_fit, col_flugplan, col_flugshow = st.columns([1.0, 1.2, 1.2])

# 1. Kategorie: FIT
with col_fit:
    st.header("🛠️ Fit")
    st.code(daten["fit"], language="text")

# 2. Kategorie: FLUGPLAN
with col_flugplan:
    st.header("📋 Taktik")
    for schritt in daten["flugplan"]:
        st.markdown(schritt)

# 3. Kategorie: FLUGSHOW
with col_flugshow:
    st.header("📹 Beispiel")
    st.video(daten["flugshow_url"])


st.markdown("---")

# --- DETAILS (Eingeklappt für interessierte Spieler) ---
st.subheader("🧠 Hintergrund-Infos")

with st.expander("Skills"):
    st.markdown("Skill-Anforderungen für Anomische Missionen sind in der Regel sehr hoch. :orange[Das ist nichts für Anfänger-Charaktere.] Hier sind die empfohlenen Skills.")
        
    df_skills = pd.DataFrame(daten["details_skills"])
    
    st.dataframe(
        df_skills, 
        use_container_width=True, # volle Breite des Aufklappmenüs
        hide_index=True          # Versteckt Zeilennummern
    )

with st.expander("Warum ist das Fit so gewählt?"):
    st.write(daten["details_warum_fit"])

with st.expander("Schadensprofile & Resistenzen"):
    st.write(daten["details_resistenzen"])

with st.expander("Implantate"):
    st.write(daten["details_implants"])

