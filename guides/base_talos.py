# base_talos.py
#
# Guides for the Anomic Base Talos Mission

BASE_TALOS = {


    # ---------------------------------------------------------------------------------------
    #
    # --- Base Talos - Enyo ---
    #
    "Enyo vs. Base Talos": {
            "flugshow_url": "https://youtu.be/Ik5aE_GyOVg", # Dein YouTube-Video
            "fit_misk" : 60,
            "fit": """[Enyo, Base Talos]
Magnetic Field Stabilizer II
EFFA Compact Assault Damage Control
Magnetic Field Stabilizer II
Small Armor Repairer II

5MN Quad LiF Restrained Microwarpdrive
Imperial Navy Cap Recharger
1MN Y-S8 Compact Afterburner

Light Neutron Blaster II
Light Neutron Blaster II
Light Neutron Blaster II
Light Neutron Blaster II

Small Capacitor Control Circuit II
Small Ancillary Current Router I



Void S x4000
"""
,
        "flugplan": [
            "**1:** Void S laden.",
            "**2:** Sprungtor aktivieren.",
            "**3:** MWD AN. Rechts aus Türme-Feld fliegen (Doppelklick). :red[NIEMALS direkt auf Talos zuhalten! Transversal fliegen!]",
            "**4:** Annäherung via Doppelklick / Q-Taste. Kurs schrittweise anpassen. Transversal ca. 1000 m/s halten.",
            "**5:** *(< 30km)* Orbit 10km + Armor Repairer AN.",
            "**6:** *(< 15km)* Orbit 2.5km + MWD AUS + Afterburner AN.",
            "**7:** *(< 5km)* Finaler Orbit: 1km.",
            "**8:** Talos aufschalten und zerstören.",
            "**9:** Lootbox umkreisen (1km Orbit) und plündern.",
            "**10:** Kurs neben nächste Talos (Doppelklick). AB AUS + MWD AN. Türme weiträumig (>10km) umfliegen.",
            "**11:** Annäherung: Armor Repairer AUS (Cap sparen).",
            "**12:** Ab Schritt **4** für nächste Talos wiederholen.",
            "**13:** Letzte Talos: Armor Repairer kann aus bleiben.",
            ":red[**Notfall:** Assault Damage Control aktivieren.]",
            ":orange[**Zusatz:** Turm aggro? Transversal halten + Armor Repairer dauerhaft AN. Max. 1 Turm tankbar.]"
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Enyo kann sich mit ca. 400 DPS gut gegen den Tank der Talos durchsetzen, doch dafür musst Du Dich erst einmal auf kurze Distanz annähern. Das Fit ist ausgelegt die großen Strecken zwischen den 3 Talos schnell zurückzulegen und dabei genug transversale Geschwindigkeit zu ihnen zu haben, so dass die sie Dich fast nie treffen. Dafür wird der MWD benutzt. Am Gegner wird ein enger Orbit gesetzt, damit die Blaster ihr volles Potenzial entfalten können. Dabei wird der Afterburner benutzt, um die eigene Signatur klein zu halten, und so den Schüssen aller drei Talos möglichst auszuweichen. Bei flachen Orbits kommt es aber besonders bei der ersten Talos immer wieder zu Treffern, die die Enyo zwar dank guter Thermal und sehr guter Kinetik Resistenzen aushält, es kann aber durchaus ordentlich scheppern. In dem Fall aktivierst Du den Assault Damage Control für eine kurze Atempause und zur Regeneration des Armor Tanks. Den Türmen in der Mitte der Arena bleibst Du besser fern, so dass sie nicht ausgelöst werden. Das Fit ist extrem günstig und hat sich nach 3 Einsätzen amortisiert. Die Enyo bringt Dich in ca. 10 bis 15 Minuten durch diese Mission.",
        "details_resistenzen": "Die Talos macht Thermal- und Kinetik-Schaden, ebenso wie Deine Enyo. Beide haben gegen diese Schadensarten gute Resistenzen. Die meisten Schüsse der Talos treffen zum Glück nicht.",
        "details_implants": "Es sind keine Implantate notwendig. Implantate für mehr Gun-Feuerkraft kann die Missiondauer etwas reduzieren.",
        "details_skills": [
            {"Kategorie": "Spaceship Command", "Skill": "Assault Frigates", "Stufe": "IV"},
            {"Kategorie": "Spaceship Command", "Skill": "Gallente Frigates", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Hull Upgrades", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Mechanics", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Repair Systems", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Acceleration Control", "Stufe": "IV"},
            {"Kategorie": "Navigation", "Skill": "Afterburner", "Stufe": "IV"},
            {"Kategorie": "Navigation", "Skill": "Evasive Maneuvering", "Stufe": "IV"},
            {"Kategorie": "Navigation", "Skill": "Fuel Conservation", "Stufe": "IV"},
            {"Kategorie": "Navigation", "Skill": "High Speed Maneuvering", "Stufe": "IV"},
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
            {"Kategorie": "Gunnery", "Skill": "Motion Prediction", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Rapid Firing", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Sharpshooter", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Small Hybrid Turret", "Stufe": "V"},
            {"Kategorie": "Gunnery", "Skill": "Small Blaster Specialization", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Surgical Strike", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Trajectory Analysis", "Stufe": "IV"},
        ]
    },


    # ---------------------------------------------------------------------------------------
    #
    # --- Base Talos - Nergal ---
    #
    "Nergal vs. Base Talos": {
            "flugshow_url": "https://youtu.be/-2gsLViGDOo", # Dein YouTube-Video
            "fit_misk" : 600,
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
            "**12:** Letzte Talos: Armor Repairer kann aus bleiben.",
            "**Zusatz:** Turm aggro? Transversal halten + Armor Repairer dauerhaft AN. Max. 1 Turm tankbar."
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Nergal glänzt durch enormen Schaden nachdem die Waffe voll hochgespult ist. Es braucht also etwas Zeit, aber der aktive Panzerungs-Tank der Talos kann auf Dauer nicht mithalten. Das Fit ist ausgelegt die großen Strecken zwischen den 3 Talos schnell zurückzulegen und dabei genug transversale Geschwindigkeit zu ihnen zu haben. Dafür wird der MWD benutzt. Am Gegner wird ein enger Orbit gesetzt, damit die Waffe der Nergal ihr volles Potenzial entfalten kann. Dabei wird der Afterburner benutzt, um die eigene Signatur klein zu halten, und so den Schüssen der anderen Talos auszuweichen. Bei flachen Orbits kommt es aber besonders bei der ersten Talos immer wieder zu Treffern, die die Nergal dank guter Thermal und erhöhter Kinetik Resistenzen aushält. Den Türmen in der Mitte der Arena bleibt man einfach fern, so dass sie nicht ausgelöst werden. Du kannst die selbe Nergal für alle Anomischen Missionen benutzen: Rigs, Waffe und Armor Repairer bleiben gleich, die anderen Module werden je nach Mission angepasst.",
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