# agent_serpentis.py
#
# Guides for the Anomic Agent Serpentis Mission

AGENT_SERPENTIS = {

#
# The solution of AGENT Serpentis vs Harpy has been depricated by the removal of optimal
# range buffs from the Harpy. This is no longer going to work since 2026-Sep-22 until
# someone is publishing the opposite.
#
#     # ---------------------------------------------------------------------------------------
#     #
#     # --- AGENT Serpentis - Harpy ---
#     #
#     "Harpy vs. Serpentis Agent": {
#         "flugshow_url": "https://youtu.be/-EFJPWlNb9c", # <-- YouTube-Video
#         "fit_misk" : 200,
#         "fit": """[Harpy, Agent Serpentis]
# Vortex Compact Magnetic Field Stabilizer
# Magnetic Field Stabilizer II
# Fourier Compact Tracking Enhancer

# Gistum C-Type Medium Shield Booster
# Small Compact Pb-Acid Cap Battery
# Federation Navy Stasis Webifier
# Pithum B-Type Kinetic Shield Amplifier

# Light Neutron Blaster II
# Light Neutron Blaster II
# Light Neutron Blaster II
# Light Neutron Blaster II

# Small Hybrid Locus Coordinator II
# Small Hybrid Locus Coordinator II



# Null S x4000
#         """,
#         "flugplan": [
#             "**1:** Null S laden, Schild Booster AN.",
#             "**2:** Sprungtor aktivieren.",
#             "**3:** Kurs auf Gegner setzen (Annähern).",
#             "**4:** Gegner aufschalten.",
#             "**5:** Webifier AN.",
#             "**6:** Feuern und zerstören.",
#             "**7:** Wertvollen Loot aus Wrack plündern.",
#         ],
#         # Optionale Details (Standardmäßig eingeklappt)
#         "details_warum_fit": "Der Gegner hat einen extrem starken Webifier, der dich praktisch auf der Stelle festnagelt. Zum Glück will er dich nah genug umkreisen, so dass er für die Null S Munition knapp über optimaler Reichweite ist. Dein Webfier unterstützt die Blaster bei der Nachführung. Gegen den hohen Schaden des Gegners ist ein Kinetik Schild Amplifier eingebaut, die Thermal-Resistenz der Schilde der Harpy sind ohne Verstärkung gut genug. Trotzdem ist ein recht teurer Schield-Booster notwendig, um gegen den Schaden der Daredevil klar zu kommen.",
#         "details_resistenzen": "Gegner macht Kinetik- und Thermal-Schadendeswegen. Die Kinetik Resistenz der Harpy wird durch den Pithum B-Type Kinetic Shield Amplifier verstärkt. Die Resistenzen der Daredevil sind relativ gut gegen den Thermal+Kinetik Schaden Deiner Blaster. ",
#         "details_implants": "Es sind keine Implantate notwendig. Unterstütze den Tank notfalls mit einem Booster. Mit einem luxuriösen Crystal-Set entsteht erst gar kein Stress. Du könntest auch Implantate für mehr Gun-Feuerkraft einsetzen, um die Missionszeit zu verkürzen.",
#         "details_skills": [
#             {"Kategorie": "Spaceship Command", "Skill": "Assault Frigates", "Stufe": "V"},
#             {"Kategorie": "Spaceship Command", "Skill": "Caldari Frigates", "Stufe": "V"},
#             {"Kategorie": "Armor", "Skill": "Hull Upgrades", "Stufe": "V"},
#             {"Kategorie": "Armor", "Skill": "Mechanics", "Stufe": "V"},
#             {"Kategorie": "Navigation", "Skill": "Acceleration Control", "Stufe": "V"},
#             {"Kategorie": "Navigation", "Skill": "Navigation", "Stufe": "V"},
#             {"Kategorie": "Engineering", "Skill": "Advanced Weapon Upgrades", "Stufe": "IV"},
#             {"Kategorie": "Engineering", "Skill": "Capacitor Management", "Stufe": "V"},
#             {"Kategorie": "Engineering", "Skill": "Capacitor Systems Operation", "Stufe": "V"},
#             {"Kategorie": "Engineering", "Skill": "CPU Management", "Stufe": "V"},
#             {"Kategorie": "Engineering", "Skill": "Power Grid Management", "Stufe": "V"},
#             {"Kategorie": "Engineering", "Skill": "Weapon Upgrades", "Stufe": "V"},
#             {"Kategorie": "Engineering", "Skill": "Thermodynamics", "Stufe": "III"},
#             {"Kategorie": "Gunnery", "Skill": "Controlled Bursts", "Stufe": "V"},
#             {"Kategorie": "Gunnery", "Skill": "Gunnery", "Stufe": "V"},
#             {"Kategorie": "Gunnery", "Skill": "Motion Prediction", "Stufe": "V"},
#             {"Kategorie": "Gunnery", "Skill": "Rapid Firing", "Stufe": "V"},
#             {"Kategorie": "Gunnery", "Skill": "Sharpshooter", "Stufe": "V"},
#             {"Kategorie": "Gunnery", "Skill": "Small Hybrid Turrets", "Stufe": "V"},
#             {"Kategorie": "Gunnery", "Skill": "Small Blaster Specialization", "Stufe": "IV"},
#             {"Kategorie": "Gunnery", "Skill": "Surgical Strike", "Stufe": "V"},
#             {"Kategorie": "Gunnery", "Skill": "Trajectory Analysis", "Stufe": "IV"},
#             {"Kategorie": "Rigging", "Skill": "Hybrid Weapon Rigging", "Stufe": "III"},
#         ]
#     },

    # ---------------------------------------------------------------------------------------
    #
    # --- AGENT Serpentis - Nergal ---
    #
    "Nergal vs. Serpentis Agent": {
        "flugshow_url": "", # <-- YouTube-Video
        "fit_misk" : 1100,
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
        "details_warum_fit": "Der Gegner hat einen extrem starken Webifier, der dich praktisch auf der Stelle festnagelt. Zum Glück will er dich nah genug umkreisen, so dass er für die Baryon Munition in Reichweite ist. Die beiden Webfier unterstützen deine Waffe bei der Nachführung. Gegen den hohen Schaden des Gegners sind zwei Kinetik Armor Hardener eingebaut, die Du nofalls beide für eine ganze Weile problemlos überhitzen kannst. Der Traktor-Strahl ist nicht wirklich wichtig, aber beschleunigt das Looten ein wenig. Du kannst die selbe Nergal für alle Anomischen Missionen benutzen: Rigs, Waffe und Armor Repairer bleiben gleich, die anderen Module werden je nach Mission angepasst.",
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


}