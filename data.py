# data.py

MISSION_DATA = {
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
            "**1:** *(vor dem Sprungtor)* Occult S Munition in die Waffe laden.",
            "**2:** *(vor dem Sprungtor)* Tank aktivieren (Armor Hardener und Armor Repairer).",
            "**3:** Sprungtor nutzen.",
            "**4:** Afterburner aktivieren und auf ca. 5km zum Gegner (Vengeance) Abstand halten.",
            "**5:** Vengeance aufschalten.",
            "**6:** *(< 14km Abstand)* Webifier aktivieren.",
            "**7:** *(< 7km Abstand)* Waffe feuern bis die Vengeance zerstört ist. Logistik-Fregatten ignorieren.",
            "**8:** **:orange[Armor Hardener überhitzen]** wenn Du zu viel Schaden kassierst.",
            "**9:** Wertvollen Loot mitnehmen."
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
            "**1:** *(vor dem Sprungtor)* Occult S Munition in die Waffe laden.",
            "**2:** *(vor dem Sprungtor)* Tank aktivieren (Armor Hardener und Armor Repairer).",
            "**3:** Sprungtor nutzen.",
            "**4:** Afterburner aktivieren und Orbit auf 6.5km zum Gegner (Enyo).",
            "**5:** Enyo aufschalten.",
            "**6:** *(< 14km Abstand)* Webifier aktivieren.",
            "**7:** *(< 7km Abstand)* Waffe feuern bis die Enyo zerstört ist. Logistik-Fregatten ignorieren.",
            "**8:** **:orange[Armor Hardener überhitzen]** wenn Du zu viel Schaden kassierst.",
            "**9:** Wertvollen Loot mitnehmen."
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
}