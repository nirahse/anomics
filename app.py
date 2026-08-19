import streamlit as st
import pandas as pd
import sys, importlib

# 1. Wir importieren die Module einmalig, damit sie Python sicher im RAM bekannt sind
try:
    import guides
    import data
except ImportError:
    pass

# 2. Wir listen alle geladenen Submodule auf (z.B. guides.agent_angel)
modules_to_reload = [
    name for name in list(sys.modules.keys())
    if (name == "data" or name.startswith("data.") or 
        name == "guides" or name.startswith("guides."))
    and sys.modules[name] is not None
]

# 3. WICHTIG: Wir sortieren die Module nach der Länge ihres Namens RÜCKWÄRTS.
# Dadurch werden die tiefsten Dateien (z.B. guides.agent_angel) zuerst aktualisiert,
# und ganz am Schluss das Hauptmodul "data".
for mod_name in sorted(modules_to_reload, key=len, reverse=True):
    try:
        importlib.reload(sys.modules[mod_name])
    except Exception:
        pass

# 4. Jetzt erst ziehen wir die absolut frisch geladene Variable in die app.py
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

# # Einfacher Filter mit Rücksetzen
# # Lokaler Callback zum Zurücksetzen des state labels
# def reset_search():
#     st.session_state["suchbegriff_state"] = ""
# # Container aus Eingabefeld und Reset Button
# filter_container = st.sidebar.container(gap="small")
# with filter_container:
#     # Eingabefeld
#     suchbegriff = st.sidebar.text_input(
#         "Suche:", 
#         label_visibility="collapsed",
#         key="suchbegriff_state",
#         placeholder="Suche..."  # Ein dezenter Platzhalter-Text für bessere Optik
#     ).lower().strip()
#     # Reset-Button: nur wenn Text im Feld steht
#     if st.session_state.get("suchbegriff_state", "") != "":
#         st.sidebar.button(
#             ":material/close: Suche zurücksetzen", 
#             on_click=reset_search,
#             type="tertiary", # Macht den Button zu einem dezenten Text-Link ohne klobigen Rahmen
#             use_container_width=False
#         )
#
# # --- FILTER-LOGIK ---
# gefilterte_keys = []
# for key in MISSION_DATA.keys():
#     key_lower = key.lower()
#     if suchbegriff in key_lower:
#         gefilterte_keys.append(key)
#
# # --- GRUNDLAGEN ---
# # Grundlagen-Seite standardmäßig ganz oben
# grundlagen_label = "🏠 Grundlagen"
# if not suchbegriff or suchbegriff in "grundlagen":
#     gefilterte_keys.insert(0, grundlagen_label)


# 1. Wir sammeln alle möglichen Begriffe, die der Nutzer als "Vorschlag" sehen könnte
# (z.B. Missionstyp, Schiffsnamen, Fraktionen)
alle_such_optionen = ["Agent", "Base", "Team", 
                      "Nergal", "Garmur", "Enyo", "Hawk", "Kitsune", "Jaguar", "Vengeance", "Wolf",
                      "Angel", "Blood Raiders", "Guristas", "Sansha's Nation", "Serpentis"]

# 2. Das Multiselect-Feld als modernes Tag-Eingabefeld
# Der Nutzer kann tippen, Enter drücken und so mehrere Tags sammeln
gewaehlte_tags = st.sidebar.multiselect(
    "Suche nach Tags:",
    options=alle_such_optionen,
    default=[],
    label_visibility="collapsed",
    placeholder="Tippe Filter-Begriffe...",
    accept_new_options=True
)

# --- FILTER-LOGIK FÜR MEHRERE TAGS ---
gefilterte_keys = []

# Wenn keine Tags gewählt sind, zeigen wir alle Guides an
if not gewaehlte_tags:
    gefilterte_keys = list(MISSION_DATA.keys())
else:
    # Wenn Tags gewählt sind, muss JEDER gewählte Tag im Namen des Guides vorkommen (AND-Verknüpfung)
    for key in MISSION_DATA.keys():
        key_lower = key.lower()
        # Prüfen, ob alle gewählten Tags in diesem Guide-Namen existieren
        if all(tag.lower() in key_lower for tag in gewaehlte_tags):
            gefilterte_keys.append(key)

# --- GRUNDLAGEN-LOGIK INJECTION (Unverändert) ---
# Die Grundlagen-Seite bleibt oben, wenn nicht gesucht wird oder explizit danach gesucht wird
grundlagen_label = "🏠 Grundlagen & Anleitung"
if not gewaehlte_tags or any(t.lower() in "grundlagen" for t in gewaehlte_tags):
    gefilterte_keys.insert(0, grundlagen_label)



# --- ANZEIGE IN DER SIDEBAR ---
st.sidebar.subheader("📋 Auswahl")
if gefilterte_keys:
    auswahl = st.sidebar.radio("Wähle einen Guide", gefilterte_keys, label_visibility="collapsed")


    if auswahl == grundlagen_label:
        st.image("logo_title_bigbar.png")

        st.markdown("---")

        st.info("ℹ️ Nutze die Sidebar auf der linken Seite, um gezielt nach bestimmten Agenten oder Schiffen zu suchen. Jeder Guide liefert Dir das passende Fit, die Taktik und ein Video-Beispiel.")

        st.warning("⚠️ Wichtig: Anomische (Burner) Missionen verzeihen wenig Fehler. Sie zählen nicht zum Anfänger-Content in EVE Online. Prüfe Deine Skills, Konzentriere Dich, Überhitze rechtzeitig! Lehne Anomische Missionen lieber ab, wenn Du nicht sicher bist ob Du sie schaffst.")

        st.markdown("### Mit welchen Missionen und Schiffen fange ich am besten an?")
        st.markdown(
            "- Fang am besten mit günstigen Schiffen an, die Dein derzeitiger Skillstand unterstützt.\n"
            "- Mit Ausnahme der Kitsune für die Team Missionen sind die meisten günstigen Fits weniger flexibel. Schaffe günstige Schiffe nach und nach an, um Dein Spektrum zu erweitern.\n"
            "- Garmur und Nergal sind teuer in der Anschaffung können aber in mehreren Missionen eingesetzt werden.\n"
            "- Wenn Dein Konto gefüllt ist und Skills kein Problem sind, bietet sich die Nergal an. Für ca. 1.5b Investition kannst Du mit einem Schiff fast alle Anomischen Missionen fliegen. Die Module für alle Fits passen in einen Standard Container. Den Container kann ein Marauder im Cargo mitnehmen, während die Nergal in der *Frigate Escape Bay* gelagert wird. Damit hast Du ein flexibles und mobiles Setup, das sich leicht verlegen lässt.\n" 
            "- Die Nergal ist nicht nur extrem flexibel einsetzbar, sondern kann auch besonders gut mit Armor-Tank Schlachtschiffen (Paladin, Kronos, Apocalypse Navy Issue, etc) kombiniert werden, denn alle profitieren von einem Asklepian Implantat-Set und meistens auch von Gunnery Skill Implantaten. Du könntest also alles entspannt mit einem Klon fliegen."
        )

        st.markdown("### Günstige Lösungen für den Start:")
        df_uebersicht = pd.DataFrame([
            {"Mission" : "Angel Cartel Agent", "Schiff" : "Daredevil (~130m ISK)", "Skill-Set" : "Minmatar Frigates, Gallente Frigates, Gunnery, Small Blaster, "},
            {"Mission" : "Base Talos", "Schiff" : "Enyo (~60m ISK)", "Skill-Set" : "Gallente Frigates, Assault Frigates, Gunnery, Small Blaster, Navigation, Armor Tank"},
            {"Mission" : "Guristas Agent", "Schiff" : "Enyo (~100m ISK)", "Skill-Set" : "Gallente Frigates, Assault Frigates, Gunnery, Small Blaster, Navigation, Armor Tank"},
            {"Mission" : "Sansha's Nation Agent", "Schiff" : "Wolf (~60m ISK)", "Skill-Set" : "Minmatar Frigates, Assault Frigates, Gunnery, Small Auto-Cannons, Armor Tank"},
            {"Mission" : "Alle Teams", "Schiff" : "Kitsune (~50m ISK)", "Skill-Set" : "Caldari Frigates, Electronic Attack Ships, Light Missiles, ECM"},
        ])

        #st.dataframe(df_uebersicht, width='stretch', hide_index=True) # pd frame looks not as good
        st.table(df_uebersicht)

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
