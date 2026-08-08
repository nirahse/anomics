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

    
    # ---------------------------------------------------------------------------------------
    #
    # --- AGENT Sansha - Wolf ---
    #
    "Wolf vs. Sansha's Nation Agent": {
        "flugshow_url": "https://youtu.be/v3AQMDLtZ6Y", # <-- YouTube-Video
        "fit": """[Wolf, Agent Sansha]
Coreli A-Type Small Armor Repairer
Gyrostabilizer II
Gyrostabilizer II
Tracking Enhancer II
Tracking Enhancer II

Small Compact Pb-Acid Cap Battery
Tracking Computer II

200mm AutoCannon II
200mm AutoCannon II
200mm AutoCannon II
200mm AutoCannon II

Small Projectile Ambit Extension I
Small Projectile Collision Accelerator II




Republic Fleet EMP S x3000
Optimal Range Script x1
Agency 'Pyrolancea' DB3 Dose I x1    
        """
        ,
        "flugplan": [
            "**1:** Republic Fleet EMP S in Waffe laden.",
            "**2:** Optimal Range Script in Tracking Computer laden.",
            "**3:** Armor Repairer und Tracking Computer AN.",
            "**4:** Sprungtor aktivieren.",
            "**5:** Geraden Kurs setzen (Doppelklick ins All).",
            "**6:** Succubus aufschalten.",
            "**7:** Feuern und zerstören.",
            ":orange[**Kurskorrektur:**] Wenn der Gegner mit der Station kollidiert, fliege in gerader Linie (Doppelklick) senkrecht zu seinem Orbit und weg von der Station.",
            ":orange[**Waffen wieder aktivieren**] wenn nachgeladen wurde."
            "**9:** Wertvollen Loot mitnehmen.",
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Das Fit ist günstig und fokussiert stark auf hohe Nachführungsgeschwindigkeit der Auto-Cannons. Die Succubus hält einen Orbit von ca. 15km Radius und fliegt dabei mit ca. 3km/s. Versuche einen Kurs einzustellen der senkrecht zu ihrem Orbit und gleichzeitig von der Station weg geht. Durch das Optimal Range Script erreichen die EMP S Schüsse das Ziel gerade so im *Falloff* der Waffen. Der Kampf dauert dadurch relative lange, so dass die Waffen evtl. leer geschossen werden. Nach dem Nachladen solltest Du die Waffen sofort wieder aktivieren. Falls Deine Gunnery Skills noch nicht voll entwickelt sind, kannst Du den *Agency 'Pyrolancea'* Booster zur Unterstützung einsetzen. Durch die gute EM Resistenz ist der Tank der Wolf stabil.",
        "details_resistenzen": "Gegner macht im Wesentlichen EM-Schaden gegen den die Wolf sehr gute Resistenz hat. Die EMP Munition richtet sich gegen die schwache EM Resistenz der Succubus.",
        "details_implants": "Es sind keine Implantate notwendig. Gunnery Implantate könnten helfen, die Dauer des Kampfs zu reduzieren.",
        "details_skills": [
            {"Kategorie": "Spaceship Command", "Skill": "Assault Frigates", "Stufe": "V"},
            {"Kategorie": "Spaceship Command", "Skill": "Minmatar Frigates", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Hull Upgrades", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Mechanics", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Repair Systems", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Advanced Weapon Upgrades", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Systems Operation", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "CPU Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Power Grid Management", "Stufe": "III"},
            {"Kategorie": "Engineering", "Skill": "Weapon Upgrades", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Controlled Bursts", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Gunnery", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Motion Prediction", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Rapid Firing", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Sharpshooter", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Projectile Turret", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Autocannon Specialization", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Surgical Strike", "Stufe": "V"},
            {"Kategorie": "Rigging", "Skill": "Projectile Weapon Rigging", "Stufe": "IV"},
        ]
    },


}