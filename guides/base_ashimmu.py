# base_ashimmu.py
#
# Guides for the Anomic Base Ashimmu Mission

BASE_ASHIMMU = {

    # ---------------------------------------------------------------------------------------
    #
    # --- Base Ashimmu - Vagabond ---
    #
    "Vagabond vs. Base Ashimmu": {
            "flugshow_url": "https://youtu.be/2b-j9Y7fEUs", # Dein YouTube-Video
            "fit_misk" : 420,
            "fit": """[Vagabond, Base Ashimmu]
Gyrostabilizer II
Capacitor Flux Coil II
Tracking Enhancer II
Capacitor Flux Coil II
Gyrostabilizer II

Multispectrum Shield Hardener II
Pith X-Type Large Shield Booster
Republic Fleet Large Cap Battery
Multispectrum Shield Hardener II

220mm Vulcan AutoCannon II
220mm Vulcan AutoCannon II
220mm Vulcan AutoCannon II
220mm Vulcan AutoCannon II
220mm Vulcan AutoCannon II
Rapid Light Missile Launcher II

Medium Capacitor Control Circuit II
Medium Capacitor Control Circuit II




Hail M x3000
Republic Fleet Phased Plasma M x4000
Inferno Fury Light Missile x2000
"""
,
        "flugplan": [
            "**1:** Republic Fleet Phased Plasma M laden, Schild Booster und Hardener AN.",
            "**2:** Sprungtor aktivieren.",
            "**3:** Den nächsten Sentinel ansteuern",
            "**4:** Hadener überhitzen bei zu viel Schaden.",
            "**5:** 1. Sentinel zerstören.",
            "**6:** Tank jetzt stabil, nicht mehr überhitzen, Tracking ist auch besser",
            "**7:** 2. Sentinel zerstören.",
            "**8:** Loot einsammeln.",
            "**9:** Hail M laden und Ashimmu zerstören.",
            "**10:** Loot einsammeln."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Nergal glänzt durch enormen Schaden nachdem die Waffe voll hochgespult ist. Es braucht also etwas Zeit, aber der aktive Panzerungs-Tank der Talos kann auf Dauer nicht mithalten. Das Fit ist ausgelegt die großen Strecken zwischen den 3 Talos schnell zurückzulegen und dabei genug transversale Geschwindigkeit zu ihnen zu haben. Dafür wird der MWD benutzt. Am Gegner wird ein enger Orbit gesetzt, damit die Waffe der Nergal ihr volles Potenzial entfalten kann. Dabei wird der Afterburner benutzt, um die eigene Signatur klein zu halten, und so den Schüssen der anderen Talos auszuweichen. Bei flachen Orbits kommt es aber immer wieder zu Treffern, die die Nergal dank guter Thermal und erhöhter Kinetik Resistenzen aushält. Den Türmen in der Mitte der Arena bleibt man einfach fern, so dass sie nicht ausgelöst werden. Du kannst die selbe Nergal für alle Anomischen Missionen benutzen: Rigs, Waffe und Armor Repairer bleiben gleich, die anderen Module werden je nach Mission angepasst.",
        "details_resistenzen": "Die Ashimmu macht EM- und Thermal-Schaden, die Sentinels Kinetik- und Explosiv-Schaden. Deswegen fitten wir zwei Multispectrum Hardener und einen sehr guten Schild-Booster. Gegen die Sentinels nutzen wir Thermal-Munition und gegen die Ashimmu Explosiv-Kinetik.",
        "details_implants": "Es sind keine Implantate notwendig, aber ein Crystal-Set erleichtert den Anfang der Mission erheblich und erspart das Überhitzen.",
        "details_skills": [
            {"Kategorie": "Spaceship Command", "Skill": "Heavy Assault Cruiser", "Stufe": "V"},
            {"Kategorie": "Spaceship Command", "Skill": "Minmatar Cruiser", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Hull Upgrades", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Mechanics", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Navigation", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Evasive Maneuvering", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "Advanced Weapon Upgrades", "Stufe": "IV"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Capacitor Systems Operation", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "CPU Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Power Grid Management", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Weapon Upgrades", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Energy Grid Upgrades", "Stufe": "V"},
            {"Kategorie": "Engineering", "Skill": "Thermodynamics", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Controlled Bursts", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Gunnery", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Motion Prediction", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Rapid Firing", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Sharpshooter", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Medium Projectile Turret", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Medium Autocannon Specialization", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Surgical Strike", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Trajectory Analysis", "Stufe": "V"},
            {"Kategorie": "Missiles", "Skill": "Light Missiles", "Stufe": "V"},
            {"Kategorie": "Missiles", "Skill": "Light Missile Specialization", "Stufe": "III"},
            {"Kategorie": "Missiles", "Skill": "Missile Launcher Operation", "Stufe": "III"},
            {"Kategorie": "Missiles", "Skill": "Guided Missile Precision", "Stufe": "III"},
            {"Kategorie": "Missiles", "Skill": "Missile Bombardment", "Stufe": "IV"},
            {"Kategorie": "Missiles", "Skill": "Missile Projection", "Stufe": "IV"},
            {"Kategorie": "Missiles", "Skill": "Rapid Launch", "Stufe": "IV"},
            {"Kategorie": "Missiles", "Skill": "Target Navigation Prediction", "Stufe": "III"},
            {"Kategorie": "Missiles", "Skill": "Warhead Upgrades", "Stufe": "III"},
            {"Kategorie": "Shields", "Skill": "Shield Compensation", "Stufe": "V"},
            {"Kategorie": "Shields", "Skill": "Shield Management", "Stufe": "IV"},
            {"Kategorie": "Shields", "Skill": "Shield Operation", "Stufe": "IV"},
            {"Kategorie": "Shields", "Skill": "Shield Upgrades", "Stufe": "IV"},
            {"Kategorie": "Shields", "Skill": "Tactical Shield Manipulation", "Stufe": "V"},
        ]
    },

}