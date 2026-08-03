# data.py

MISSION_DATA = {

    # ---------------------------------------------------------------------------------------
    #
    # --- AGENT Angel Cartel - Daredevil ---
    #
    "Daredevil vs. Angel Cartel Agent": {
        "flugshow_url": "https://youtu.be/05W8vJn56go", # Dein YouTube-Video
        "fit": """[Daredevil, Agent Angel Burner]
Magnetic Field Stabilizer II
Magnetic Field Stabilizer II
Photonic Upgraded Co-Processor
Magnetic Field Stabilizer II

Stasis Webifier II
Republic Fleet Medium Shield Extender
Fleeting Compact Stasis Webifier

Light Neutron Blaster II
[Empty High slot]
Light Neutron Blaster II

Small Core Defense Field Extender II
Small EM Shield Reinforcer II
Small Explosive Shield Reinforcer II



Void S x2400
        """
        ,
        "flugplan": [
            "**1:** Void S laden.",
            "**2:** Sprungtor aktivieren.",
            "**3:** :orange[Waffen überhitzen!]",
            "**4:** Kurs setzen: 1.5km - 2.0km Abstand halten.",
            "**5:** Dramiel aufschalten.",
            "**6:** Beide Webifier aktivieren.",
            "**7:** Feuern und zerstören.",
            "**8:** Wrack plündern und wertvollen Loot mitnehmen."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Dieses Fit zwingt den Gegner auf einen DPS Vergleich, und verweigert ihm seine überlegene Waffennachführung und niedrige Signatur auszunutzen. Wer mehr Schaden anrichtet, gewinnt. Etwa 500 DPS auf dem Papier (ohne überhitzen) reichen aus. Du kontrollierst die Distanz mit Deinen beiden Webifiern, die auf der Daredevil besonders stark wirken. Dadurch kannst Du nah (leicht über) der optimalen Reichweite der beiden Light Neutron Blaster II mit Void S Munition bleiben. Falls das zu knapp wird, solltest Du die Waffen überhitzen (am besten immer überhitzen bis Du weißt, dass es auch ohne geht). Der Kampf geht sehr schnell vorbei (ca. 30s). Als Tank nutzt Du den Schild Puffer, verstärkt durch den Faction Extender und die 3 Rigs, die Dir Schildstärke und Resistenzen geben. Die Low-Slots verstärken den Waffenschaden und der Co-Processor sorgt dafür, dass Du genug CPU hast, um all das überhaupt fitten zu können. Sollte es trotzdem knapp werden mit der CPU, kannst Du den T2 Webifier gegen einen Fleeting Compact Stasis Webifier tauschen, und/oder einen Magnetic Field Stabilizer II gegen einen Vortex Compact Magnetic Field Stabilizer tauschen. Wirf auch einen Blick auf die Skills, die für dieses Fit empfohlen werden. Die sind nicht ohne, aber auch nicht unmöglich zu erreichen.",
        "details_resistenzen": "Gegner macht hauptsächlich Explosiv-Schaden, dazu ein wenig EM und Kinetik. Die mittelmäßige Thermal-Resistenz der Dramiel nutz unsere Waffe gut aus.",
        "details_implants": "Es sind keine Implantate notwendig. Ein Implantat für mehr Schildstärke (Shield Management) ist hilfreich und evtl. musst Du damit die Waffen nicht mehr überhitzen.",
        "details_skills": [
            {"Kategorie": "Spaceship Command", "Skill": "Minmatar Frigates", "Stufe": "IV"},
            {"Kategorie": "Spaceship Command", "Skill": "Gallente Frigates", "Stufe": "IV"},
            {"Kategorie": "Armor", "Skill": "Hull Upgrades", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Mechanics", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Navigation", "Stufe": "V"},
            {"Kategorie": "Electronic System", "Skill": "Propulsion Jamming", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "Advanced Weapon Upgrades", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Systems Operation", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "CPU Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Power Grid Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Weapon Upgrades", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Thermodynamics", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Small Hybrid Turret", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Blaster Specialization", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Controlled Bursts", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Gunnery", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Motion Prediction", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Rapid Firing", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Sharpshooter", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Surgical Strike", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Trajectory Analysis", "Stufe": "V"},
            {"Kategorie": "Rigging", "Skill": "Shield Rigging", "Stufe": "IV"},
            {"Kategorie": "Shield", "Skill": "Shield Management", "Stufe": "V"},
            {"Kategorie": "Shield", "Skill": "Tactical Shield Manipulation", "Stufe": "V"},
        ]
    },

    # ---------------------------------------------------------------------------------------
    #
    # --- AGENT Angel Cartel - Nergal ---
    #
    "Nergal vs. Angel Cartel Agent": {
        "flugshow_url": "https://youtu.be/Yg3qu6zAP-w", # Dein YouTube-Video
        "fit": """[Nergal, Burner Agent: Angel]
Centii A-Type Small Armor Repairer
Multispectrum Energized Membrane II
Overdrive Injector System II
Centum A-Type Explosive Energized Membrane

Coreli A-Type 1MN Afterburner
Stasis Webifier II
Stasis Webifier II

Veles Light Entropic Disintegrator

Small Auxiliary Nano Pump II
Small Capacitor Control Circuit II




Occult S x2500
    """
    ,
        "flugplan": [
            "**1:** Occult S laden, Armor Repairer AN.",
            "**2:** Sprungtor nutzen.",
            "**3:** Doppelklick ins All (Weg von der Station für einen geraden Kurs).",
            "**4:** Afterburner AN.",
            "**5:** Dramiel aufschalten und Feuer!",
            "**6:** Beide Webifier aktivieren.",
            "**7:** Abstand bei ca. 4,5 km per *Keep at Range* halten.",
            "**8:** Warten bis Gegner zerstört ist.",
            "**9:** Wrack plündern und wertvollen Loot mitnehmen."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Mit diesem Fit behältst du die volle Distanzkontrolle. Trotz des Webs der gegnerischen Dramiel muss deine Nergal mindestens 401 m/s fliegen. Das ist exakt die Geschwindigkeit, auf die deine zwei eigenen Webs die Dramiel herunterbremsen. Um dieses Tempo zu garantieren, nutzt du den Afterburner und das Overdrive Injector System. Den extrem hohen Explosivschaden der Dramiel fängst du dabei mit einer Centum A-Type Explosive Energized Membrane ab.",
        "details_resistenzen": "Gegner macht hauptsächlich Explosiv-Schaden, dazu ein wenig EM und Kinetik. Die mittelmäßige Thermal-Resistenz der Dramiel nutz unsere Waffe gut aus. ",
        "details_implants": "Es sind keine Implantate notwendig. Du kannst Dir aber das Leben mit der Nergal leichter machen, wenn Du den Armor-Tank durch Implantate verstärkst. Ein Mid-grade Asklepian Set ist perfekt und unterstützt auch andere Armor-Tank Schiffe in Missionen. Zusätzlich könntest Du auch Implantate für mehr Gun-Feuerkraft einsetzen.",
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
    # --- AGENT Blood Raiders - Nergal ---
    #
    "Nergal vs. Blood Raiders Agent": {
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
        "details_warum_fit": "Die Nergal glänzt durch enormen Schaden nachdem die Waffe voll hochgespult ist. Es braucht also etwas Zeit bis der Tank des Gegners bricht. Dadurch wird die Mission extrem einfach. Das Fit wirkt dem starken Energie-Neutralisierer des Gegners entgegen. Dafür ist eine große Batterie eingebaut und ein Power Core, um diese mit genug Strom zu versorgen. Die Panzerung ist gegen den EM Schaden des Gegners verstärkt.",
        "details_resistenzen": "Gegner macht EM-Schaden, deswegen fitten wir die Centum A-Type EM Energized Membrane. Die Disintegrator Waffe macht Thermal- und Explosiv-Schaden aber mehr als genug, so dass die Resistenzen der Cruor nicht stören. ",
        "details_implants": "Es sind keine Implantate notwendig. Du kannst Dir aber das Leben mit der Nergal leichter machen, wenn Du den Armor-Tank durch Implantate verstärkst. Ein Mid-grade Asklepian Set ist perfekt und unterstützt auch andere Armor-Tank Schiffe in Missionen. Zusätzlich könntest Du auch Implantate für mehr Gun-Feuerkraft einsetzen.",
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
    # --- AGENT Guristas - Nergal ---
    #
    "Nergal vs. Guristas Agent": {
        "flugshow_url": "https://youtu.be/GEnn2QDD1xE", # Dein YouTube-Video
        "fit": """[Nergal, Burner Agent: Guristas]
Centii A-Type Small Armor Repairer
Overdrive Injector System II
Overdrive Injector System II
Centus X-Type Kinetic Armor Hardener

True Sansha Warp Scrambler
Republic Fleet Small Cap Battery
Coreli A-Type 5MN Microwarpdrive

Veles Light Entropic Disintegrator

Small Auxiliary Nano Pump II
Small Capacitor Control Circuit II




Occult S x2000
    
    """
    ,
        "flugplan": [
            ":red[**Warnung:** Die Taktik kann durch ungünstigen Hitzeschaden fehlschlagen.]",
            "**1:** Occult S laden.",
            "**2:** Armor Hardener + Repairer AN.",
            "**3:** Sprungtor nutzen.",
            "**4:** Kurs auf 4.5km Abstand + MWD AN (1 normaler Zyklus).",
            "**5:** MWD Überhitzen (für max. 3 Zyklen, mitzählen!).",
            "**6:** Worm aufschalten.",
            "**7:** *(<11km)*: Warp Scrambler AN, MWD aus.",
            "**8:** Feuern und Worm zerstören.",
            "**9:** Wertvollen Loot mitnehmen.",
            ":orange[**Notausgang:**] Wenn der Scrambler oder der MWD durch das Überhitzen durchbrennt: Rep laufen lassen, MWD AUS/offline, Client schliessen (Alt+F4), 10 min warten, wieder einloggen (ihr landet am Gate zur Mission), Schiff reparieren und neu versuchen. Es gibt Berichte, dass diese Taktik leider nicht immer erfolgreich ist."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Nergal glänzt durch enormen Schaden nachdem die Waffe voll hochgespult ist. Es braucht also etwas Zeit bis der Tank des Gegners bricht. Das hilft besonders bei der Worm, denn die hat einen ganz ordentlichen Tank. Das Fit ist ausgelegt, die Worm einzufangen und ihren MWD auszuschalten. Die Worm fliegt mit 3.5km/s und versucht, auf 30 km Abstand zu bleiben. Du fängst sie ein, indem Du extra schnell wirst. Mit dem überhitzten MWD solltest du auf ca. 4.5km/s kommen. Bei unter 11km Abstand schalte den MWD der Worm mit dem Warp Scrambler aus. Damit die Wahrscheinlichkeit reduziert wird, dass MWD und Warp Scramble beide verbrennen, bau die beiden Module jeweils an die beiden Enden der Medium Bank ein.",
        "details_resistenzen": "Gegner macht Kinetik-Schaden, deswegen fitten wir den Centus X-Type Kinetic Armor Hardener. Die Disintegrator Waffe macht Thermal- und Explosiv-Schaden aber mehr als genug, so dass die Resistenzen der Worm nicht stören. ",
        "details_implants": "Es sind keine Implantate notwendig. Du kannst Dir aber das Leben mit der Nergal leichter machen, wenn Du den Armor-Tank durch Implantate verstärkst. Ein Mid-grade Asklepian Set ist perfekt und unterstützt auch andere Armor-Tank Schiffe in Missionen. Zusätzlich könntest Du auch Implantate für mehr Gun-Feuerkraft einsetzen.",
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
        "details_warum_fit": "In dieser (faulen) Version nutzen wir die gute Nachführung des Leichten Disintegrators. Diese wird durch den Target Painter unterstützt, der die Signatur der Succubus vergrößert. Dadurch treffen wir den Gegner trotz seiner hohen Geschwindigkeit zuverlässig.Der Tracking Computer wird mit einem **Optimal Range Script** bestückt, sodass unsere Waffe mit Baryon-Munition eine Reichweite von 16 km erreicht. Das passt perfekt zum Orbit von etwa 15 km, den die Succubus normalerweise hält. Unser Tank hält problemlos stand. Ohne Implantate kannst Du im Notfall den EM Armor Hardener überhitzen. Da der Tank der Succubus nicht besonders stark ist, dauert die Mission in der Regel nicht lange. Ein Problem kann entstehen, wenn die Succubus während ihres Orbits mit der Station kollidiert. Dadurch kann sie kurzzeitig auf eine Entfernung von mehr als 16 km geraten. In diesem Fall verliert unsere Waffe den Lock, wird deaktiviert und der durch das Hochspulen aufgebaute Schadensmultiplikator geht verloren. Behalte deshalb den Orbit des Gegners im Auge. Falls die Succubus mit der Station kollidiert, fliege senkrecht zu ihrem Orbit und gleichzeitig von der Station weg. Nach einigen Umkreisungen sollte sich das Problem von selbst erledigen.",
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
    # --- AGENT Serpentis - Nergal ---
    #
    "Nergal vs. Serpentis Agent": {
        "flugshow_url": "", # <-- YouTube-Video
        "fit": """[Nergal, Burner Agent: Serpentis]
Centii A-Type Small Armor Repairer
Entropic Radiation Sink II
Centus C-Type Kinetic Armor Hardener
Centus C-Type Kinetic Armor Hardener

Federation Navy Stasis Webifier
Federation Navy Stasis Webifier
Republic Fleet Small Cap Battery

Veles Light Entropic Disintegrator
Small Tractor Beam I

Small Auxiliary Nano Pump II
Small Capacitor Control Circuit II



Warrior II x5

Baryon Exotic Plasma S x2000    
        """,
        "flugplan": [
            "**:red[Vorläufige Version]**",
            "**1:** Baryon Exotic Plasma S laden, Armor Hardener und Repairer AN.",
            "**2:** Sprungtor aktivieren.",
            "**3:** Kurs auf Gegner setzen (Annähern).",
            "**4:** Gegner aufschalten.",
            "**5:** Feuern und zerstören.",
            ":orange[**Tank zu schwach:** Beide Armor Hardener überhitzen.]",
            "**6:** Wertvollen Loot aus Wrack plündern.",
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Der Gegner hat einen extrem starken Webifier, der dich praktisch auf der Stelle festnagelt. Zum Glück will er dich auf nah genug umkreisen, so dass er für die Baryon Munition in Reichweite ist. Die beiden Webfier unterstützen deine Waffe bei der Nachführung. Gegen den hohen Schaden des Gegners sind zwei Kinetik Armor Hardener eingebaut, die Du nofalls beide für eine ganze Weile problemlos überhitzen kannst. Der Traktor-Strahl ist nicht wirklich wichtig, aber beschleunigt das Looten ein wenig.",
        "details_resistenzen": "Gegner macht im Wesentlichen Kinetik-Schaden, deswegen fitten wir die zwei Centus C-Type Kinetic Armor Hardener. Die Disintegrator Waffe macht Thermal- und Explosiv-Schaden der gut gegen den Armor-Tank der passabel wirkt. ",
        "details_implants": "Es sind keine Implantate notwendig. Unterstütze den Tank notfalls mit einem Booster oder durch Überhitzen der Armor Hardener. Du kannst Dir aber das Leben mit der Nergal leichter machen, wenn Du den Armor-Tank durch Implantate verstärkst. Ein Mid-grade Asklepian Set ist perfekt und unterstützt auch andere Armor-Tank Schiffe in Missionen. Zusätzlich könntest Du auch Implantate für mehr Gun-Feuerkraft einsetzen.",
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
    # --- TEAM Enyo - Nergal ---
    #
    "Nergal vs. Team Enyo": {
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
        """,
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
        "details_warum_fit": "Die Nergal glänzt durch enormen Schaden nachdem die Waffe voll hochgespult ist. Es braucht also etwas Zeit, aber selbst die zwei Logistik-Fregatten des Teams können dem nicht standhalten. Das Fit ist ausgelegt, den Hauptgegner mit dem Webifier zu verlangsamen, um den Abstand kontrollieren zu können. Die Schadensart des Gegners ist Thermal und Kinetik. Von Haus aus hat die Nergal eine hohe Thermal-Resistenz. Wir schließen das Kinetik Loch in der Armor-Resistenz mit dem guten Resistenzhardener.",
        "details_resistenzen": "Gegner macht Thermal- und Kinetik-Schaden, deswegen fitten wir den Kinetik Armor Hardener. Die Disintegrator Waffe macht Thermal- und Explosiv-Schaden aber mehr als genug, so dass die Resistenzen der Enyo nicht stören.",
        "details_implants": "Es sind keine Implantate notwendig. Du kannst Dir aber das Leben mit der Nergal leichter machen, wenn Du den Armor-Tank durch Implantate verstärkst. Ein Mid-grade Asklepian Set ist perfekt und unterstützt auch andere Armor-Tank Schiffe in Missionen. Zusätzlich könntest Du auch Implantate für mehr Gun-Feuerkraft einsetzen.",
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
            {"Kategorie": "Drones", "Skill": "Minmatar Drone Specialization", "Stufe": "III"},
            {"Kategorie": "Drones", "Skill": "Light Drone Operation", "Stufe": "V"},
        ]
    },

    # ---------------------------------------------------------------------------------------
    #
    # --- TEAM Hawk - Nergal ---
    #
    "Nergal vs. Team Hawk": {
        "flugshow_url": "https://youtu.be/gj5GIopfmq8", # Dein YouTube-Video
        "fit": """[Nergal, Burner Team: Hawk]
Centii A-Type Small Armor Repairer
Entropic Radiation Sink II
Centus C-Type Kinetic Armor Hardener
Centus C-Type Kinetic Armor Hardener

Coreli A-Type 1MN Afterburner
Federation Navy Stasis Webifier
Republic Fleet Small Cap Battery

Veles Light Entropic Disintegrator

Small Auxiliary Nano Pump II
Small Capacitor Control Circuit II



Acolyte II x5

Baryon Exotic Plasma S x2000
Occult S x2000
        """,
        "flugplan": [
            "**1:** Baryon laden, Armor Hardener und Repairer AN.",
            "**2:** Sprungtor aktvieren.",
            "**3:** Afterburner AN und eine Bantam annähern auf 4.5km.",
            "**4:** Bantam aufschalten.",
            "**5:** Hawk aufschalten als 2. Ziel.",
            "**6:** Afterburner kurz überhitzen falls das Annähern zu lange dauert.",
            "**7:** *(< 14km)* Webifier auf Bantam, Feuern und zerstören.",
            "**8:** Webifier auf Hawk und auf 4.5km Abstand halten.",
            "**9:** Afterburner kurz überhitzen falls das Annähern zu lange dauert.",
            "**10:** Occult S laden.",
            "**11:** *(< 7km)* Auf Hawk feuern und zerstören. Zweite Logistik Fregatte ignorieren.",
            "**12:** Wrack inspizieren, wertvollen Loot mitnehmen."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Nergal kann zwar richtig viel Schaden austeilen, aber der reicht nicht gegen die Hawk und ihre zwei Logistik Fregatten (Bantams). Deswegen schalte einen Logistiker aus, bevor Du Dich um die Hawk kümmerst. Mit Afterburner und Webifier sollte es kein Problem sein, in Waffenreichweite einer Bantam zu kommen und danach eben so nah an die Hawk zu fliegen. Notfalls den Afterburner kurz überhitzen. Gegen die Bantam kannst Du auch schon aus größerer Entfernung mit Baryon vorgehen. Gegen die Hawk solltest Du mit Occult feuern und dafür auf etwa 7km heranfliegen. Die Mission dauert etwas länger, weil Du die Waffe gegen zwei Gegner hochspulen musst. Den zweiten Logistiker kannst Du ignorieren. Die Schadensart des Gegners ist reiner Kinetik-Schaden. Die beiden Hardener machen Deinen Tank sicher dagegen.",
        "details_resistenzen": "Gegner macht Kinetik-Schaden, deswegen fitten wir die zwei Centus C-Type Kinetic Armor Hardener. Gegen den Tank der Logistiker und der Hawk zusammen hat die Nergal einiges zu tun.",
        "details_implants": "Es sind keine Implantate notwendig. Du kannst Dir aber das Leben mit der Nergal leichter machen, wenn Du den Armor-Tank durch Implantate verstärkst. Ein Mid-grade Asklepian Set ist perfekt und unterstützt auch andere Armor-Tank Schiffe in Missionen. Zusätzlich könntest Du auch Implantate für mehr Gun-Feuerkraft einsetzen.",
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
            {"Kategorie": "Drones", "Skill": "Minmatar Drone Specialization", "Stufe": "III"},
            {"Kategorie": "Drones", "Skill": "Light Drone Operation", "Stufe": "V"},
        ]
    },

    # ---------------------------------------------------------------------------------------
    #
    # --- TEAM Jaguar - Kitsune ---
    #
    "Kitsune vs. Team Jaguar": {
        "flugshow_url": "https://youtu.be/RrpfklwbrVU", # Dein YouTube-Video
        "fit": """[Kitsune, Team Jaguar]
Ballistic Control System II
Ballistic Control System II

5MN Y-T8 Compact Microwarpdrive
Ladar ECM II
Ladar ECM II
Cap Recharger II
Domination Target Painter

Light Missile Launcher II
Light Missile Launcher II
Light Missile Launcher II

Small Particle Dispersion Augmentor II
Small Ancillary Current Router I




Scourge Fury Light Missile x2500
        """,
        "flugplan": [
            "**1:** Scourge Fury Light Missile laden.",
            "**2:** Sprungtor aktivieren.",
            "**3:** MWD AN und Jaguar auf 32km Abstand halten.",
            ":red[**Warnung:** Fliegst Du am Anfang direkt auf die Jaguar zu, könntest Du kurzzeitig in ihre Waffenreichweite gelangen. Evtl. manuell etwas seitlich fliegen und dann Abstand halten.]",
            "**4:** Jaguar und beide Burst aufschalten.",
            "**5:** ECM Jammer auf jede Burst.",
            "**6:** Target Painter auf Jaguar",
            "**7:** Feuern und warten bis Jaguar platzt.",
            "**9:** Wrack plündern und wertvollen Loot mitnehmen."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Kitsune ist auf ECM-Jammer spezialisiert. Sobald du deine Jams erfolgreich auf die Logistik-Fregatten (Burst) anwendest, können diese die Jaguar nicht mehr aufschalten und reparieren. Halte mit der Kitsune so viel Abstand, dass deine Fury Light Missiles gerade noch treffen. Du solltest eine Distanz von mindestens 28 km (besser 30 km) wahren, weshalb deine Raketen eine entsprechende Reichweite benötigen. Dank deines MWD ist das Halten des Abstands kein Problem: Die Jaguar erreicht maximal ca. 1.200 m/s, während deine Kitsune rund 2.500 m/s fliegt. Da der DPS der Kitsune nicht überragend ist, dauert der Kampf einige Minuten. Je besser deine Missile-Skills sind, desto schneller ist es vorbei. Das unschlagbare Argument für dieses Fit ist jedoch das extrem geringe finanzielle Risiko durch den niedrigen Preis von Schiff und Ausrüstung.",
        "details_resistenzen": "Da der Gegner Dich nicht treffen sollte ist seine Schadensart nicht relevant. Die geringste Schild-Resistenz der Jaguar ist Kinetik, deswegen schießt Du am besten mit Scourge Missiles.",
        "details_implants": "Die Mission ist komplett ohne Implantate machbar. Wenn überhaupt, kannst Du die Reichweite und den Schaden der Missiles durch Implantate erhöhen. Ein Hydra-Set wäre der absolute Luxus.",
        "details_skills": [
            {"Kategorie": "Spaceship Command", "Skill": "Electronic Attack Ships", "Stufe": "IV"},
            {"Kategorie": "Spaceship Command", "Skill": "Caldari Frigates", "Stufe": "IV"},
            {"Kategorie": "Armor", "Skill": "Hull Upgrades", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Mechanics", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Acceleration Control", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Navigation", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "High Speed Maneuvering", "Stufe": "IV"},
            {"Kategorie": "Navigation", "Skill": "Evasive Maneuvering", "Stufe": "V"},
            {"Kategorie": "Electronic Subsystems", "Skill": "Electronic Warfare", "Stufe": "IV"},
            {"Kategorie": "Electronic Subsystems", "Skill": "Frequency Modulation", "Stufe": "III"},
            {"Kategorie": "Electronic Subsystems", "Skill": "Long Distance Jamming", "Stufe": "IV"},
            {"Kategorie": "Electronic Subsystems", "Skill": "Signal Dispersion", "Stufe": "IV"},
            {"Kategorie": "Electronic Subsystems", "Skill": "Signature Focusing", "Stufe": "IV"},
            {"Kategorie": "Electronic Subsystems", "Skill": "Target Painting", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "Advanced Weapon Upgrades", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Systems Operation", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "CPU Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Power Grid Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Weapon Upgrades", "Stufe": "V"},
            {"Kategorie": "Missiles", "Skill": "Light Missiles", "Stufe": "V"},
            {"Kategorie": "Missiles", "Skill": "Light Missile Specialization", "Stufe": "V"},
            {"Kategorie": "Missiles", "Skill": "Guided Missile Precision", "Stufe": "IV"},
            {"Kategorie": "Missiles", "Skill": "Missile Bombardment", "Stufe": "V"},
            {"Kategorie": "Missiles", "Skill": "Missile Launcher Operation", "Stufe": "IV"},
            {"Kategorie": "Missiles", "Skill": "Missile Projection", "Stufe": "V"},
            {"Kategorie": "Missiles", "Skill": "Rapid Launch", "Stufe": "V"},
            {"Kategorie": "Missiles", "Skill": "Target Navigation Prediction", "Stufe": "V"},
            {"Kategorie": "Missiles", "Skill": "Warhead Upgrades", "Stufe": "IV"},
            {"Kategorie": "Rigging", "Skill": "Launcher Rigging", "Stufe": "IV"},
            {"Kategorie": "Rigging", "Skill": "Electronic Superiority Rigging", "Stufe": "III"},
            {"Kategorie": "Targeting", "Skill": "Long Range Targeting", "Stufe": "V"},
        ]
    },

    # ---------------------------------------------------------------------------------------
    #
    # --- TEAM Jaguar - Nergal ---
    #
    "Nergal vs. Team Jaguar": {
        "flugshow_url": "https://youtu.be/S-DfpMZt9sU", # Dein YouTube-Video
        "fit": """[Nergal, Burner Team: Jaguar]
Centii A-Type Small Armor Repairer
Capacitor Power Relay II
Entropic Radiation Sink II
Centus C-Type Explosive Armor Hardener

Coreli A-Type 1MN Afterburner
Federation Navy Stasis Webifier
Federation Navy Stasis Webifier

Veles Light Entropic Disintegrator

Small Auxiliary Nano Pump II
Small Capacitor Control Circuit II



Warrior II x5

Occult S x2000
Baryon Exotic Plasma S x2000
        """,
        "flugplan": [
            ":red[**Warnung:** Das Risiko die Nergal hier zu verlieren ist hoch.]",
            "**1:** Occult S laden, Armor Hardener und Repairer AN.",
            "**2:** Sprungtor aktivieren.",
            "**3:** Afterburner AN und Orbit 6.5km zur Jaguar.",
            "**4:** Jaguar aufschalten.",
            "**5:** *(< 14km)* Webifier AN.",
            "**6:** *(< 7km)* Auf Jaguar feuern zerstören. Logistik-Fregatten ignorieren.",
            "**7:** Zu viel Schaden kassiert? **:orange[Armor Hardener überhitzen, Booster nutzen,] :red[(Notfall) Armor Repairer überhitzen]**",
            "**8:** Wrack plündern und wertvollen Loot mitnehmen.",
            ":green[**Alternative** (geringeres Risiko): Baryon laden, 13km Orbit]"
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Nergal glänzt durch enormen Schaden nachdem die Waffe voll hochgespult ist. Es braucht also etwas Zeit, aber selbst die zwei Logistik-Fregatten des Teams können dem nicht standhalten. Das Fit ist ausgelegt, den Hauptgegner mit dem Webifier zu verlangsamen, um den Abstand kontrollieren zu können. Die Schadensart des Gegners ist hauptsächlich Explosiv. Von Haus aus hat die Nergal eine hohe Thermal-Resistenz. Wir schließen das Explosiv Loch in der Armor-Resistenz mit dem guten Resistenzhardener. Die Jaguar macht trotzdem sehr viel Schaden, deswegen kann es notwendig sein, der Hardener zu überhitzen.",
        "details_resistenzen": "Gegner macht viel Explosiv-, und etwas Kinetik- und EM-Schaden. Dagegen fitten wir den Centus C-Type Explosive Armor Hardener. Die Disintegrator Waffe macht Thermal- und Explosiv-Schaden, gegen den die Jaguar etwas mehr als 50% Resistenz hat.",
        "details_implants": "Die Mission ist ohne Implantate machbar, aber sehr risikoreich. Es wird empfohlen, Implantate zu verwenden, um das Risiko zu reduzieren. Ein Mid-grade Asklepian Set ist perfekt und unterstützt auch andere Armor-Tank Schiffe in Missionen. Zusätzlich könntest Du auch Implantate für mehr Gun-Feuerkraft einsetzen.",
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
            {"Kategorie": "Drones", "Skill": "Minmatar Drone Specialization", "Stufe": "III"},
            {"Kategorie": "Drones", "Skill": "Light Drone Operation", "Stufe": "V"},
        ]
    },
    
    # ---------------------------------------------------------------------------------------
    #
    # --- TEAM Vengeance - Nergal ---
    #
    "Nergal vs. Team Vengeance": {
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
    # --- Base Talos - Nergal ---
    #
    "Nergal vs. Base Talos": {
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
            {"Kategorie": "Drones", "Skill": "Minmatar Drone Specialization", "Stufe": "III"},
            {"Kategorie": "Drones", "Skill": "Light Drone Operation", "Stufe": "V"},
        ]
    },
}