# base_talos.py
#
# Guides for the Anomic Base Talos Mission

BASE_TALOS = {

    
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
            "**5:** *(< 30km)* Orbit 10km + Armor Repairer AN.",
            "**6:** *(< 10km)* Orbit 2.5km + MWD AUS + Afterburner AN.",
            "**7:** Talos aufschalten und zerstören.",
            "**8:** Lootbox eng umkreisen + Looten.",
            "**9:** Kurs neben nächste Talos (Doppelklick). AB AUS + MWD AN. Türme weiträumig (>10km) umfliegen.",
            "**10:** Annäherung: Armor Repairer AUS (Cap sparen).",
            "**11:** Ab Schritt **4** für nächste Talos wiederholen.",
            "**12:** Letzte Talos: Kein Armor Repairer nötig.",
            "**Zusatz:** Turm aggro? Transversal halten + Armor Repairer dauerhaft AN. Max. 1 Turm tankbar."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Nergal glänzt durch enormen Schaden nachdem die Waffe voll hochgespult ist. Es braucht also etwas Zeit, aber der aktive Panzerungs-Tank der Talos kann auf Dauer nicht mithalten. Das Fit ist ausgelegt die großen Strecken zwischen den 3 Talos schnell zurückzulegen und dabei genug transversale Geschwindigkeit zu ihnen zu haben. Dafür wird der MWD benutzt. Am Gegner wird ein enger Orbit gesetzt, damit die Waffe der Nergal ihr volles Potenzial entfalten kann. Dabei wird der Afterburner benutzt, um die eigene Signatur klein zu halten, und so den Schüssen der anderen Talos auszuweichen. Bei flachen Orbits kommt es aber immer wieder zu Treffern, die die Nergal dank guter Thermal und erhöhter Kinetik Resistenzen aushält. Den Türmen in der Mitte der Arena bleibt man einfach fern, so dass sie nicht ausgelöst werden. Du kannst die selbe Nergal für alle Anomischen Missionen benutzen: Rigs, Waffe und Armor Repairer bleiben gleich, die anderen Module werden je nach Mission angepasst.",
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