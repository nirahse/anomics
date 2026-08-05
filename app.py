import streamlit as st
import pandas as pd
from data import MISSION_DATA

st.set_page_config(
    page_title="EVE Guide - Anomische Missionen",
    page_icon="🔥",
    layout="wide"
)

# CSS: Abstände für das Hauptfenster UND die Sidebar reduzieren
st.markdown(
    """
    <style>
        /* 1. Abstand oben im Hauptfenster entfernen */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 0rem !important;
        }
        
        /* 2. Alle künstlichen Abstände um das st.sidebar.title (h1) entfernen */
        [data-testid="stSidebarUserContent"] h1 {
            margin-top: 0rem !important;
            margin-bottom: 0.5rem !important;
            padding-top: 0rem !important;
            padding-bottom: 0.5rem !important;
            line-height: 1.1 !important;
        }

        /* 3. Den umschließenden Block des Titels stutzen */
        [data-testid="stSidebarNav"] + div, 
        [data-testid="stVerticalBlock"] > div:first-child {
            padding-top: 0rem !important;
            margin-top: 0rem !important;
        }

        /* 4. Den Abstand ZWISCHEN allen Elementen in der Sidebar minimieren */
        [data-testid="stSidebarUserContent"] [data-testid="stVerticalBlock"] {
            gap: 0.7rem !important; /* Standard ist oft 1rem oder mehr */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- SIDE BAR ---
st.logo("logo_120.png")
st.sidebar.title("Burner Guides")
# --- SIDEBAR: FILTER-ELEMENTE ---
st.sidebar.subheader("🔍 Filter:")
# 3. Filter: Freitext (Sucht im gesamten Key)
suchbegriff = st.sidebar.text_input("Suche:", "", label_visibility="collapsed").lower().strip()
# --- FILTER-LOGIK ---
gefilterte_keys = []
for key in MISSION_DATA.keys():
    key_lower = key.lower()
    if suchbegriff in key_lower:
        gefilterte_keys.append(key)
# --- ANZEIGE IN DER SIDEBAR ---
st.sidebar.subheader("📋 Auswahl")
if gefilterte_keys:
    auswahl = st.sidebar.radio("Wähle einen Guide", gefilterte_keys, label_visibility="collapsed")
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
        #st.video(daten["flugshow_url"])
        if daten["flugshow_url"]:
            st.video(daten["flugshow_url"])
        else:
            st.info("📺 Das Video für diesen Guide ist noch in Arbeit.")

    st.markdown("---")

    # --- DETAILS (Eingeklappt für interessierte Spieler) ----
    st.subheader("🧠 Hintergrund-Infos")

    with st.expander("Warum ist das Fit so gewählt?"):
        st.write(daten["details_warum_fit"])

    with st.expander("Schadensprofile & Resistenzen"):
        st.write(daten["details_resistenzen"])

    with st.expander("Skills"):
            st.markdown("Skill-Anforderungen für Anomische Missionen sind in der Regel sehr hoch. :orange[Das ist nichts für Anfänger-Charaktere.] Hier sind die empfohlenen Skills.")
                
            df_skills = pd.DataFrame(daten["details_skills"])
            
            st.dataframe(
                df_skills, 
                #use_container_width=True, # volle Breite des Aufklappmenüs
                width='stretch',         # volle Breite des Aufklappmenüs
                hide_index=True          # Versteckt Zeilennummern 
            )

    with st.expander("Implantate"):
        st.write(daten["details_implants"])

else: # Kein Ergebnis nach Filter
    st.sidebar.warning("Keine Guides für diese Filter gefunden.")
    st.title("🛸 Burner Guides")
    st.info("Bitte passe die Filter in der Sidebar an, um einen Taktik-Guide anzuzeigen.")
