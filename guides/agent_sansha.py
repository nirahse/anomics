# agent_sansha.py
#
# Guides for the Anomic Agent Sansha Mission

AGENT_SANSHA = {
    
    # ---------------------------------------------------------------------------------------
    #
    # --- AGENT Sansha - Nergal ---
    #
    "Nergal vs. Sansha's Nation Agent": {
        "flugshow_url": "https://youtu.be/FlxT7MEZD9M", # <-- YouTube-Video
        "fit": """[Nergal, Burner Agent: Sansha]
Centii A-Type Small Armor Repairer
Centus C-Type EM Armor Hardener
Entropic Radiation Sink II
Entropic Radiation Sink II

Tracking Computer II
Republic Fleet Small Cap Battery
Target Painter II

Veles Light Entropic Disintegrator

Small Auxiliary Nano Pump II
Small Capacitor Control Circuit II



Acolyte II x5


Baryon Exotic Plasma S x2000
Optimal Range Script x1
    
    """
    ,
        "flugplan": [
            "**1:** Baryon Exotic Plasma S in Waffe laden.",
            "**2:** Optimal Range Script in Tracking Computer laden.",
            "**3:** Armor Hardener, Repairer und Tracking Computer AN.",
            "**4:** Sprungtor nutzen.",
            "**5:** Kurs auf Gegner setzen (Annähern).",
            "**6:** Succubus aufschalten.",
            "**7:** Target Painter AN.",
            "**8:** Feuern und zerstören.",
            "**9:** Wertvollen Loot mitnehmen.",
            ":orange[**Kurskorrektur:**] Wenn der Gegner mit der Station kollidiert, fliege in gerader Linie (Doppelklick) senkrecht zu seinem Orbit und weg von der Station."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "In dieser (faulen) Version nutzen wir die gute Nachführung des Leichten Disintegrators. Diese wird durch den Target Painter unterstützt, der die Signatur der Succubus vergrößert. Dadurch treffen wir den Gegner trotz seiner hohen Geschwindigkeit zuverlässig.Der Tracking Computer wird mit einem **Optimal Range Script** bestückt, sodass unsere Waffe mit Baryon-Munition eine Reichweite von 16 km erreicht. Das passt perfekt zum Orbit von etwa 15 km, den die Succubus normalerweise hält. Unser Tank hält problemlos stand. Ohne Implantate kannst Du im Notfall den EM Armor Hardener überhitzen. Da der Tank der Succubus nicht besonders stark ist, dauert die Mission in der Regel nicht lange. Ein Problem kann entstehen, wenn die Succubus während ihres Orbits mit der Station kollidiert. Dadurch kann sie kurzzeitig auf eine Entfernung von mehr als 16 km geraten. In diesem Fall verliert unsere Waffe den Lock, wird deaktiviert und der durch das Hochspulen aufgebaute Schadensmultiplikator geht verloren. Behalte deshalb den Orbit des Gegners im Auge. Falls die Succubus mit der Station kollidiert, fliege senkrecht zu ihrem Orbit und gleichzeitig von der Station weg. Nach einigen Umkreisungen sollte sich das Problem von selbst erledigen.  Du kannst die selbe Nergal für alle Anomischen Missionen benutzen: Rigs, Waffe und Armor Repairer bleiben gleich, die anderen Module werden je nach Mission angepasst.",
        "details_resistenzen": "Gegner macht im Wesentlichen EM-Schaden, deswegen fitten wir den Centus C-Type EM Armor Hardener. Die Disintegrator Waffe macht Thermal- und Explosiv-Schaden der gut gegen den Schild-Tank der Succubus wirkt. ",
        "details_implants": "Es sind keine Implantate notwendig. Unterstütze den Tank notfalls mit einem Booster oder durch Überhitzen des EM Armor Hardeners. Du kannst Dir aber das Leben mit der Nergal leichter machen, wenn Du den Armor-Tank durch Implantate verstärkst. Ein Mid-grade Asklepian Set ist perfekt und unterstützt auch andere Armor-Tank Schiffe in Missionen. Zusätzlich könntest Du auch Implantate für mehr Gun-Feuerkraft einsetzen.",
        "details_skills": [
            {"Kategorie": "Spaceship Command", "Skill": "Assault Frigates", "Stufe": "V"},
            {"Kategorie": "Spaceship Command", "Skill": "Precursor Frigates", "Stufe": "V"},
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
            {"Kategorie": "Engineering", "Skill": "Thermodynamics", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Controlled Bursts", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Gunnery", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Motion Prediction", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Rapid Firing", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Sharpshooter", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Precursor Weapon", "Stufe": "V"},
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

}