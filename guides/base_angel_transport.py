# base_angel_transport.py
#
# Guides for the Anomic Base Angel Cartel Transport Mission

BASE_ANGELTRANSP = {

    # ---------------------------------------------------------------------------------------
    #
    # --- Base Angel Transport - Vigilant ---
    #
    "Vigilant vs. Base Angel Transport": {
            "flugshow_url": "https://youtu.be/D5cAQn2LSNA", # Dein YouTube-Video
            "fit_misk" : 500,
            "fit": """[Vigilant, Base Angel]
Capacitor Power Relay II
Capacitor Power Relay II
Medium Armor Repairer II
Medium Armor Repairer II
Explosive Armor Hardener II
Explosive Armor Hardener II

Large Compact Pb-Acid Cap Battery
Stasis Webifier II
Stasis Webifier II
Cap Recharger II

Heavy Ion Blaster II
Heavy Ion Blaster II
Heavy Ion Blaster II
Heavy Ion Blaster II
Heavy Ion Blaster II

Medium Auxiliary Nano Pump II
Medium EM Armor Reinforcer I
Medium Nanobot Accelerator II



Acolyte I x5

Void M x5229
50MN Y-T8 Compact Microwarpdrive x1
Mobile Depot x1
Mobile Tractor Unit x1
"""
,
        "flugplan": [
            "**1:** Void M laden, alle Hardener und Armor Repairer AN.",
            "**2:** Prüfe: Batterie eingebaut; MWD, Depot, MTU im Cargo.",
            "**3:** Sprungtor aktivieren.",
            "**4:** Mobile Depot und MTU abwerfen, alle 4 Dramiels aufschalten",
            "**5:** Eine Dramiel auf **3km Abstand halten**, beide Webifier an, Feuern und Zerstören!",
            "**6:** :red[**Überhitzen im Notfall:**] Armor Hardener, Armor Repairer, Drohnen auswerfen als Kanonenfutter",
            "**7:** Wie (5) bis alle Dramiels zerstört.",
            "**8:** Wertvollen Loot aus der MTU mitnehmen! MTU einsammeln!",
            "**9:** Am Depot: Batterie ausbauen, MWD einbauen! Depot einsammeln!",
            ":orange[**Info:** In AIR- und Starter-Systemen darf man keine MTU und kein Mobiles Depot verankern. Dort zum Umfitten andocken und danach wieder in die Mission warpen.]",
            "**10:** Orbit 1km auf Transporter und MWD AN! (vermeide Kollision)",
            "**11:** Am Transporter: MWD aus! Auf 3km Abstand halten und aufschalten!",
            "**12:** Feuern und zerstören!",
            "**13:** Wervollen Loot einsammeln!",
            "**14:** Zurück auf Station: MWD in den Cargo, Batterie ausrüsten."            
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Mit der Vigilant profitierst Du vor allem von der enormen Stärke der Webifier. Die Eskorte wäre ohne die starke Verlangsamung kaum zu treffen. Mit zwei Webifiern kommen die Dramiels fast zum Stillstand, so dass die Void S Munition auf optimaler Reichweite voll treffen kann. Durch doppelte Armor Repairer und zusätzliche Explosive Armor Hardener kann Dein Tank gerade so mithalten. Eventuell muss Du in der ersten Phase, wenn Du von 4 oder auch noch von 3 Dramiels beschossen wirst, etwas überhitzen. Damit der Energiespeicher bei doppeltem Armor Repairer nicht schlapp macht, sind Batterie, Cap Recharger und Capacitor Power Relays eingebaut. Das Fit ist sehr Skill-intensiv. Um die lange Distanz zwischen Eskorte und Transporter schnell zurücklegen zu können, hat Du ein Mobiles Depot und einen 50MN MWD im Cargo. Die MTU ist nicht nötig, sondern hilft Dir nur beim Einsammeln des Loots der Eskorte.",
        "details_resistenzen": "Die Vigilant verschießt Hybrid-Munition und ist damit auf Kinetik- und Thermal-Schaden festgelegt. Der Schild-Tank der Gegner ist auf den Schadensarten mittelmäßig bis gut.",
        "details_implants": "Es sind keine Implantate notwendig, aber ein Asklepian-Set hilft beim Tanken des hohen Schadens am Anfang der Mission. Hilfreiche Skill Hardwire Implantatate: für mehr Energiespeicher ('Squire' Capacitor Management EM-803 / EM-805) und für besseres Tracking ('Gunslinger' Motion Prediction MR-703 / MR-705).",
        "details_skills": [
            {"Kategorie": "Spaceship Command", "Skill": "Gallente Cruiser", "Stufe": "III"},
            {"Kategorie": "Spaceship Command", "Skill": "Minmatar Cruiser", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Hull Upgrades", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Mechanics", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Repair Systems", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Navigation", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "High Speed Maneuvering", "Stufe": "I"},
            {"Kategorie": "Engineering", "Skill": "Advanced Weapon Upgrades", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Systems Operation", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Power Grid Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Weapon Upgrades", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Energy Grid Upgrades", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Thermodynamics", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Controlled Bursts", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Gunnery", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Motion Prediction", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Rapid Firing", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Sharpshooter", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Medium Hybrid Turret", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Medium Blaster Specialization", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Surgical Strike", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Trajectory Analysis", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Drones", "Stufe": "V"},
            {"Kategorie": "Drones", "Skill": "Light Drone Operation", "Stufe": "III"},
        ]
    },

}