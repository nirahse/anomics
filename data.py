# data.py

MISSION_DATA = {
    #
    # --- AGENT Blood Raider - Nergal ---
    #
    "Agent Blood Raider vs Nergal": {
        "flugshow_url": "https://youtu.be/c8wK3phVkdE", # Dein YouTube-Video
        "fit": """[Nergal, Burner Agent: Blood Raiders]
Centii A-Type Small Armor Repairer
Entropic Radiation Sink II
Centum A-Type EM Energized Membrane
Vigor Compact Micro Auxiliary Power Core

Stasis Webifier II
Stasis Webifier II
'Censer' Medium Cap Battery

Veles Light Entropic Disintegrator

Small Auxiliary Nano Pump II
Small Capacitor Control Circuit II



Warrior II x5

Occult S x2000

    """
    ,
        "flugplan": [
            "**1:** Occult S laden.",
            "**2:** Sprungtor nutzen.",
            "**3:** Cruor aufschalten.",
            "**4:** 4.5 km Abstand halten.",
            "**5:** Beide Webifier AN.",
            "**6:** Feuern und zerstören.",
            "**7:** Wertvollen Loot mitnehmen."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Nergal glänzt durch enormen Schaden nachdem die Waffe voll hochgespult ist. Es braucht also etwas Zeit bis der Tank des Gegners bricht. Dadurch wird die Mission extrem einfach. Das Fit wirkt dem starken Energie-Neutralisierer des Gegners entegen. Dafür ist eine große Batterie eingebaut und ein Power Core um diese mit genug Strom zu versorgen. Die Panzerung ist gegen den EM Schaden des Gegners verstärkt.",
        "details_resistenzen": "Gegner macht EM-Schaden, deswegen fitten wir die Centum A-Type EM Energized Membrane. Die Disintegrator Waffe macht Thermal- und Explosiv-Schaden aber mehr als genug, so dass die Resistenzen der XXX nicht stören. ",
        "details_implants": "Es sind keine Implantate notwendig. Du kannst Dir aber das Leben mit der Nergal leichter machen, wenn Du den Armor-Tank durch Implantate verstärkst. Ein Mid-grade Asklepian Set ist perfekt und unterstützt auch andere Armor-Tank Schiffe in Missionen. Zusätzlich könntest Du auch Implantate für mehr Gun-Feuerkraft einsetzen.",
        "details_skills": [
            {"Kategorie": "Assault Frigates", "Skill": "Precursor Fregatten", "Stufe": "V"},
            {"Kategorie": "Spaceship Command", "Skill": "Precursor Fregatten", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Hull Upgrades", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Mechanics", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Repair Systems", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Acceleration Control", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Navigation", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Advanced Weapon Upgrades", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Systems Operation", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "CPU Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Power Grid Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Weapon Upgrades", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Controlled Bursts", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Gunnery", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Motion Prediction", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Rapid Firing", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Sharpshooter", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Precursor Weaponr", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Disintegrator Specialization", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Surgical Strike", "Stufe": "V"},
            {"Kategorie": "Rigging", "Skill": "Armor Rigging", "Stufe": "IV"},
            {"Kategorie": "Drones", "Skill": "Drone Durability", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drone Interfacing", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drone Navigation", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drone Sharpshooting", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Gallente Drone Specialization", "Stufe": "III"},
            {"Kategorie": "Drones", "Skill": "Light Drone Operation", "Stufe": "V"},
        ]
    },
    #
    # --- TEAM Vengeance - Nergal ---
    #
    "Team Vengeance vs Nergal": {
        "flugshow_url": "https://youtu.be/ZpVujwTAP_w", # Dein YouTube-Video
        "fit": """[Nergal, Burner Team: Vengeance]
Centii A-Type Small Armor Repairer
Centus C-Type EM Armor Hardener
Entropic Radiation Sink II
Entropic Radiation Sink II

Coreli A-Type 1MN Afterburner
Federation Navy Stasis Webifier
Republic Fleet Small Cap Battery

Veles Light Entropic Disintegrator

Small Auxiliary Nano Pump II
Small Capacitor Control Circuit II



Hobgoblin II x5

Occult S x2000
"""
,
        "flugplan": [
            "**1:** Occult S laden, Armor Hardener und Repairer AN.",
            "**2:** Sprungtor nutzen.",
            "**3:** Afterburner AN, 4.5km Abstand zur Vengeance halten.",
            "**4:** Vengeance aufschalten.",
            "**5:** *(< 14km)* Webifier AN.",
            "**6:** *(< 7km)* Auf Vengeance feuern und zerstören. Logistik-Fregatten ignorieren.",
            "**7:** Zu viel Schaden kassiert? **:orange[Armor Hardener überhitzen]**",
            "**8:** Wertvollen Loot mitnehmen."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Nergal glänzt durch enormen Schaden nachdem die Waffe voll hochgespult ist. Es braucht also etwas Zeit, aber selbst die zwei Logistik-Fregatten des Teams können dem nicht standhalten. Dadurch wird die Mission extrem einfach. Das Fit ist ausgelegt, den Hauptgegner mit dem Webifier zu verlangsamen, um den Abstand kontrollieren zu können. Die Schadensart des Gegners ist EM, gegen die wir ein gutes Resistenzmodul mitnehmen.",
        "details_resistenzen": "Gegner macht EM-Schaden, deswegen fitten wir den EM Armor Hardener. Die Disintegrator Waffe macht Thermal- und Explosiv-Schaden aber mehr als genug, so dass die Resistenzen der Vengeance nicht stören. ",
        "details_implants": "Es sind keine Implantate notwendig. Du kannst Dir aber das Leben mit der Nergal leichter machen, wenn Du den Armor-Tank durch Implantate verstärkst. Ein Mid-grade Asklepian Set ist perfekt und unterstützt auch andere Armor-Tank Schiffe in Missionen. Zusätzlich könntest Du auch Implantate für mehr Gun-Feuerkraft einsetzen.",
        "details_skills": [
            {"Kategorie": "Assault Frigates", "Skill": "Precursor Fregatten", "Stufe": "V"},
            {"Kategorie": "Spaceship Command", "Skill": "Precursor Fregatten", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Hull Upgrades", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Mechanics", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Repair Systems", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Acceleration Control", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Navigation", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Advanced Weapon Upgrades", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Systems Operation", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "CPU Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Power Grid Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Weapon Upgrades", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Controlled Bursts", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Gunnery", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Motion Prediction", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Rapid Firing", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Sharpshooter", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Precursor Weaponr", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Disintegrator Specialization", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Surgical Strike", "Stufe": "V"},
            {"Kategorie": "Rigging", "Skill": "Armor Rigging", "Stufe": "IV"},
            {"Kategorie": "Drones", "Skill": "Drone Durability", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drone Interfacing", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drone Navigation", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drone Sharpshooting", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Gallente Drone Specialization", "Stufe": "III"},
            {"Kategorie": "Drones", "Skill": "Light Drone Operation", "Stufe": "V"},
        ]
    },

    #
    # --- TEAM Enyo - Nergal ---
    #
    "Team Enyo vs Nergal": {
            "flugshow_url": "https://youtu.be/IYEPW7bdMJ0", # Dein YouTube-Video
            "fit": """[Nergal, Burner Team: Enyo]
Centii A-Type Small Armor Repairer
Entropic Radiation Sink II
Entropic Radiation Sink II
Centus C-Type Kinetic Armor Hardener

Coreli A-Type 1MN Afterburner
Federation Navy Stasis Webifier
Republic Fleet Small Cap Battery

Veles Light Entropic Disintegrator

Small Auxiliary Nano Pump II
Small Capacitor Control Circuit II



Warrior II x5

Occult S x2000


"""
,
        "flugplan": [
            "**1:** Occult S laden, Armor Hardener und Repairer AN.",
            "**2:** Sprungtor nutzen.",
            "**3:** Afterburner AN und Orbit 6.5km zur Enyo.",
            "**4:** Enyo aufschalten.",
            "**5:** *(< 14km)* Webifier AN.",
            "**6:** *(< 7km)* Auf Enyo feuern zerstören. Logistik-Fregatten ignorieren.",
            "**7:** Zu viel Schaden kassiert? **:orange[Armor Hardener überhitzen]**",
            "**8:** Wertvollen Loot mitnehmen."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Nergal glänzt durch enormen Schaden nachdem die Waffe voll hochgespult ist. Es braucht also etwas Zeit, aber selbst die zwei Logistik-Fregatten des Teams können dem nicht standhalten. Dadurch wird die Mission extrem einfach. Das Fit ist ausgelegt, den Hauptgegner mit dem Webifier zu verlangsamen, um den Abstand kontrollieren zu können. Die Schadensart des Gegners ist Thermal und Kinetik. Von Haus aus hat die Nergal eine hohe Thermal-Resistenz. Wir schließen das Kinetik Loch in der Armor-Resistenz mit dem guten Resistenzhardener.",
        "details_resistenzen": "Gegner macht Thermal- und Kinetik-Schaden, deswegen fitten wir den Kinetik Armor Hardener. Die Disintegrator Waffe macht Thermal- und Explosiv-Schaden aber mehr als genug, so dass die Resistenzen der Enyo nicht stören.",
        "details_implants": "Es sind keine Implantate notwendig. Du kannst Dir aber das Leben mit der Nergal leichter machen, wenn Du den Armor-Tank durch Implantate verstärkst. Ein Mid-grade Asklepian Set ist perfekt und unterstützt auch andere Armor-Tank Schiffe in Missionen. Zusätzlich könntest Du auch Implantate für mehr Gun-Feuerkraft einsetzen.",
        "details_skills": [
            {"Kategorie": "Assault Frigates", "Skill": "Precursor Fregatten", "Stufe": "V"},
            {"Kategorie": "Spaceship Command", "Skill": "Precursor Fregatten", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Hull Upgrades", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Mechanics", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Repair Systems", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Acceleration Control", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Navigation", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Advanced Weapon Upgrades", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Systems Operation", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "CPU Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Power Grid Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Weapon Upgrades", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Controlled Bursts", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Gunnery", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Motion Prediction", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Rapid Firing", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Sharpshooter", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Precursor Weaponr", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Disintegrator Specialization", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Surgical Strike", "Stufe": "V"},
            {"Kategorie": "Rigging", "Skill": "Armor Rigging", "Stufe": "IV"},
            {"Kategorie": "Drones", "Skill": "Drone Durability", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drone Interfacing", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drone Navigation", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drone Sharpshooting", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Minmatar Drone Specialization", "Stufe": "III"},
            {"Kategorie": "Drones", "Skill": "Light Drone Operation", "Stufe": "V"},
        ]
    },
    #
    # --- Base Talos - Nergal ---
    #
    "Base Talos vs Nergal": {
            "flugshow_url": "https://youtu.be/-2gsLViGDOo", # Dein YouTube-Video
            "fit": """[Nergal, Burner Base: Talos]
Centii A-Type Small Armor Repairer
Entropic Radiation Sink II
Reactive Armor Hardener
Corpum A-Type Kinetic Energized Membrane

Coreli A-Type 1MN Afterburner
Coreli A-Type 5MN Microwarpdrive
Republic Fleet Small Cap Battery

Veles Light Entropic Disintegrator

Small Auxiliary Nano Pump II
Small Capacitor Control Circuit II




Occult S x2500


"""
,
        "flugplan": [
            "**1:** Occult S laden + Reaktiven Hardener AN.",
            "**2:** Sprungtor nutzen.",
            "**3:** MWD AN. Rechts aus Türme-Feld fliegen (Doppelklick). :red[NIEMALS direkt auf Talos zuhalten! Transversal fliegen!]",
            "**4:** Annäherung via Doppelklick / Q-Taste. Kurs schrittweise anpassen.",
            "**6:** *(< 30km)* Orbit 10km + Armor Repairer AN.",
            "**7:** *(< 10km)* Orbit 2.5km + MWD AUS + Afterburner AN.",
            "**8:** Talos aufschalten und zerstören.",
            "**9:** Lootbox eng umkreisen + Looten.",
            "**10:** Kurs neben nächste Talos (Doppelklick). AB AUS + MWD AN. Türme weiträumig (>10km) umfliegen.",
            "**11:** Annäherung: Armor Repairer AUS (Cap sparen).",
            "**12:** Ab Schritt **4** für nächste Talos wiederholen.",
            "**13:** Letzte Talos: Kein Armor Repairer nötig.",
            "**Zusatz:** Turm aggro? Transversal halten + Armor Repairer dauerhaft AN. Max. 1 Turm tankbar."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Nergal glänzt durch enormen Schaden nachdem die Waffe voll hochgespult ist. Es braucht also etwas Zeit, aber der aktive Panzerungs-Tank der Talos kann auf Dauer nicht mithalten. Das Fit ist ausgelegt die großen Strecken zwischen den 3 Talos schnell zurückzulegen und dabei genug transversale Geschwindigkeit zu ihnen zu haben. Dafür wird der MWD benutzt. Am Gegner wird ein enger Orbit gesetzt, damit die Waffe der Nergal ihr volles Potenzial entfalten kann. Dabei wird der Afterburner benutzt, um die eigene Signatur klein zu halten, und so den Schüssen der anderen Talos auszuweichen. Bei flachen Orbits kommt es aber immer wieder zu Treffern, die die Nergal dank guter Thermal und erhöhter Kinetik Resistenzen aushält. Den Türmen in der Mitte der Arena bleibt man einfach fern, so dass sie nicht ausgelöst werden.",
        "details_resistenzen": "Gegner macht Thermal- und Kinetik-Schaden, deswegen fitten wir extra eine Kinetik Energized Membrane. Zusätzlich wird der reaktive Hardener bei Treffern auf die Panzerung extra Resistenzen zu Thermal und Kinetik verschieben. Im wesentlichen wird der Exploiv-Schaden der Nergal den Panzerungs-Tank der Talos überwinden.",
        "details_implants": "Es sind keine Implantate notwendig. Du kannst Dir aber das Leben mit der Nergal leichter machen, wenn Du den Armor-Tank durch Implantate verstärkst. Ein Mid-grade Asklepian Set ist perfekt und unterstützt auch andere Armor-Tank Schiffe in Missionen. Zusätzlich könntest Du auch Implantate für mehr Gun-Feuerkraft einsetzen.",
        "details_skills": [
            {"Kategorie": "Assault Frigates", "Skill": "Precursor Fregatten", "Stufe": "V"},
            {"Kategorie": "Spaceship Command", "Skill": "Precursor Fregatten", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Hull Upgrades", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Mechanics", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Repair Systems", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Acceleration Control", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Navigation", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Advanced Weapon Upgrades", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Systems Operation", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "CPU Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Power Grid Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Weapon Upgrades", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Controlled Bursts", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Gunnery", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Motion Prediction", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Rapid Firing", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Sharpshooter", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Precursor Weaponr", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Disintegrator Specialization", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Surgical Strike", "Stufe": "V"},
            {"Kategorie": "Rigging", "Skill": "Armor Rigging", "Stufe": "IV"},
            {"Kategorie": "Drones", "Skill": "Drone Durability", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drone Interfacing", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drone Navigation", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drone Sharpshooting", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Minmatar Drone Specialization", "Stufe": "III"},
            {"Kategorie": "Drones", "Skill": "Light Drone Operation", "Stufe": "V"},
        ]
    },
}