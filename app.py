import streamlit as st
import pandas as pd
import sys, importlib

# Streamlit Community Cloud App Reload Logik
# 1. Wir löschen die alten Modul-Referenzen radikal aus Pythons RAM-Register
for folder_name in ["data", "guides"]:
    if folder_name in sys.modules:
        del sys.modules[folder_name]
    
    for name in list(sys.modules.keys()):
        if name.startswith(f"{folder_name}."):
            del sys.modules[name]

# 2. Jetzt importieren wir die Daten
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
            padding-top: 4rem !important;
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
suchbegriff = st.sidebar.text_input("Suche:", "", label_visibility="collapsed").lower().strip()

# --- FILTER-LOGIK ---
gefilterte_keys = []
for key in MISSION_DATA.keys():
    key_lower = key.lower()
    if suchbegriff in key_lower:
        gefilterte_keys.append(key)

# --- GRUNDLAGEN ---
# Grundlagen-Seite standardmäßig ganz oben
grundlagen_label = "🏠 Grundlagen"
if not suchbegriff or suchbegriff in "grundlagen":
    gefilterte_keys.insert(0, grundlagen_label)

# --- ANZEIGE IN DER SIDEBAR ---
st.sidebar.subheader("📋 Auswahl")
if gefilterte_keys:
    auswahl = st.sidebar.radio("Wähle einen Guide", gefilterte_keys, label_visibility="collapsed")


    if auswahl == grundlagen_label:
        st.image("logo_title_bigbar.png")

        st.markdown("---")

        st.info("ℹ️ Nutze die Sidebar auf der linken Seite, um gezielt nach bestimmten Agenten oder Schiffen zu suchen. Jeder Guide liefert Dir das passende Fit, die Taktik und ein Video-Beispiel.")

        st.warning("⚠️ Wichtig: Anomische (Burner) Missionen verzeihen wenig Fehler. Sie zählen nicht zum Anfänger-Content in EVE Online. Prüfe Deine Skills, Konzentriere Dich, Überhitze rechtzeitig!")

        st.markdown("---")

        st.markdown("### Mit welchen Missionen und Schiffen fange ich am besten an?")
        st.markdown(
            "- Fang am besten mit günstigen Schiffen an, die Dein derzeitiger Skillstand unterstützt.\n"
            "- Mit Ausnahme der Kitsune für die Team Missionen sind die meisten günstigen Fits weniger flexibel. Schaffe günstige Schiffe nach und nach an, um Dein Spektrum zu erweitern.\n"
            "- Garmur und Nergal sind teuer in der Anschaffung können aber in mehrere Missionen eingesetzt werden.\n"
            "- Wenn Dein Konto gefüllt ist und Skills kein Problem sind, bietet sich die Nergal an. Für ca. 1.5b Investition kannst Du mit einem Schiff fast alle Anomischen Missionen fliegen. Die Module für alle Fits passen in einen Standard Container. Den Container kann ein Marauder im Cargo mitnehmen, während die Nergal in der *Frigate Escape Bay* gelagert wird. Damit hast Du ein flexibles und mobiles Setup, das sich leicht verlegen lässt.\n" 
            "- Die Nergal ist nicht nur extrem flexibel einsetzbar, sondern kann auch besonders gut mit Armor-Tank Schlachtschiffen (Paladin, Kronos, Apocalypse Navy Issue, etc) kombiniert werden, denn alle profitieren von einem Asklepian Implantat-Set und meistens auch von Gunnery Skill Implantaten. Du könntest also alles mit einem Klon fliegen."
        )

        st.markdown("### Günstige Lösungen für den Start:")
        df_uebersicht = pd.DataFrame([
            {"Mission" : "Angel Cartel Agent", "Schiff" : "Enyo (~100m ISK)", "Skill-Set" : "Gallente Frigates, Assault Frigates, Gunnery, Small Blaster, Armor Tank"},
            {"Mission" : "Guristas Agent", "Schiff" : "Enyo (~100m ISK)", "Skill-Set" : "Gallente Frigates, Assault Frigates, Gunnery, Small Blaster, Small Armor Tank"},
            {"Mission" : "Sansha's Nation Agent", "Schiff" : "Wolf (~60m ISK)", "Skill-Set" : "Minmatar Frigates, Assault Frigates, Gunnery, Small Auto-Cannons, Armor Tank"},
            {"Mission" : "Alle Teams", "Schiff" : "Kitsune (~50m ISK)", "Skill-Set" : "Caldari Frigates, Electronic Attack Ships, Light Missiles, ECM"},
        ])

        st.dataframe(df_uebersicht, width='stretch', hide_index=True)

        st.markdown("---")

        st.markdown("### ✉️ Kontakt & Feedback")

        # Layout mit 3 Spalten für die verschiedenen Kontaktwege
        col_ingame, col_yt, col_mail = st.columns(3)

        with col_ingame:
            st.markdown("**🎮 Ingame Name**")
            st.markdown(":orange[**Nirahse Haginen**]")

        with col_yt:
            st.markdown("**📺 YouTube Channel**")
            st.markdown("[@nirahse](https://youtube.com/@Nirahse)")

        with col_mail:
            st.markdown("**📧 E-Mail**")
            st.markdown("[nirahse@gmail.com](mailto:nirahse@gmail.com)")

    else:

        # daten Objekt setzen
        daten = MISSION_DATA[auswahl]

        # --- HAUPTFLÄCHE (Fokus auf die 3 Kernbereiche) ---
        st.title(f"🚀 {auswahl}")
        st.markdown("---")

        # Layout mit 3 Spalten: Flugshow, Fit, Flugplan
        col_fit, col_flugplan, col_flugshow = st.columns([1.0, 1.2, 1.2])

        # 1. Kategorie: FIT
        with col_fit:
            s_isk = ""
            if "fit_misk" in daten:
                s_isk = f" (~{daten['fit_misk']}m ISK)"
            st.header("🛠️ Fit" + s_isk)
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
