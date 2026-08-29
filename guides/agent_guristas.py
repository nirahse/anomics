# agent_guristas.py
#
# Guides for the Anomic Agent Guristas Mission

AGENT_GURISTAS = {


    # ---------------------------------------------------------------------------------------
    #
    # --- AGENT Guristas - Enyo ---
    #
    "Enyo vs. Guristas Agent": {
        "flugshow_url": "https://youtu.be/bJLX-Paym5A", # Dein YouTube-Video
        "fit_misk" : 100,
        "fit": """[Enyo, Guristas Agent]
Coreli B-Type Small Armor Repairer
Overdrive Injector System II
Magnetic Field Stabilizer II
Overdrive Injector System II

Faint Epsilon Scoped Warp Scrambler
Eutectic Compact Cap Recharger
Coreli A-Type 5MN Microwarpdrive

Rocket Launcher II
Light Neutron Blaster II
Light Neutron Blaster II
Light Neutron Blaster II
Light Neutron Blaster II

Small Auxiliary Thrusters II
Small Auxiliary Thrusters II



Hornet II x1

Mjolnir Rage Rocket x1500
Void S x3000""",
        "flugplan": [
            ":red[**Warnung:** Die Taktik kann durch ungünstigen Hitzeschaden fehlschlagen.]",
            "**1:** Void S und Raketen laden.",
            "**2:** Armor Repairer AN.",
            "**3:** Sprungtor aktivieren.",
            "**4:** Kurs auf 2km Abstand + MWD AN (1 normaler Zyklus).",
            "**5:** MWD Überhitzen (für max. 2 Zyklen, mitzählen!).",
            "**6:** Worm aufschalten.",
            "**7:** *(<8.2km)*: Warp Scrambler AN, MWD aus.",
            "**8:** Feuern und Worm zerstören.",
            "**9:** Wertvollen Loot mitnehmen.",
            ":orange[**Notausgang 1:**] Wenn der Scrambler oder der MWD durch das Überhitzen durchbrennt: Rep laufen lassen, MWD AUS/offline, EIne Drohne starten und hoffen dass die Worm die Drohne attackiert und den Scramble auf Dein Schiff aufhebt (kann etwas dauern). Dann aus der Mission warpen.",
            ":orange[**Notausgang 2:**] Wenn der Scrambler oder der MWD durch das Überhitzen durchbrennt: Rep laufen lassen, MWD AUS/offline, Client schliessen (Alt+F4), 10 min warten, wieder einloggen (ihr landet am Gate zur Mission), Schiff reparieren und neu versuchen. Es gibt Berichte, dass diese Taktik leider nicht immer erfolgreich ist.",
            ":orange[**Notausgang 3:**] Wenn man den Anflug verpatzt: Rechtzeitig gegen die Flugrichtung der Worm abdrehen und aus der Mission warpen. Beim zweiten Versuch den eventuell jetzt größeren Abstand zur Worm mit kaltem MWD verkürzen und erst wenn Du merkst, dass sie von Dir wegfliegen will den MWD für max. 3 Zyklen überhitzen.",
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Enyo hat extrem gute Kinetik-Resistenzen, was ihren Tank sehr stabil macht. Zudem ist sie mit diesem Fit extrem schnell und schafft es in der Regel mühelos, die Worm mit dem Warp Scrambler einzufangen. Dank der ca. 400 DPS aus den vier Blastern ist der Kampf schnell erledigt. Damit das Aufschließen gelingt, wird die Geschwindigkeit der Enyo durch den MWD, die Rigs und die Overdrive Injectors massiv erhöht. Mit überhitztem MWD erreichst Du ein Tempo von über 5 km/s, während die Worm versucht, mit 3,5 km/s auf 30 km Abstand zu bleiben. Zwei überhitzte MWD-Zyklen reichen in der Regel aus. Bei unter 8,2 km Abstand aktivierst Du den Warp Scrambler, um den MWD der Worm auszuschalten. Dadurch wird sie schlagartig langsamer als Deine Enyo - selbst wenn Dein eigener MWD aus ist. Du kontrollierst ab jetzt den Abstand und hältst mit Void S die optimale Reichweite der Blaster. Schalte in dieser Situation Deinen MWD ab, um Deinen Signaturradius klein zu halten. Damit MWD und Warp Scrambler nicht gegenseitig überhitzen und verbrennen, solltest Du die beiden Module jeweils an die äußeren Enden der Medium-Slots bauen. Mit einem Preis von ca. 100 Mio. ISK ist das Fit zudem vergleichsweise günstig.",
        "details_resistenzen": "Gegner macht Kinetik-Schaden, was perfekt zu den hohen Resistenzen der Enyo passt. Die Thermal- und Kinetic-Resistenzen der Worm sind gut, aber kein Problem für die Enyo.",
        "details_implants": "Es sind keine Implantate notwendig.",
        "details_skills": [
            {"Kategorie": "Spaceship Command", "Skill": "Assault Frigates", "Stufe": "I"},
            {"Kategorie": "Spaceship Command", "Skill": "Gallente Frigates", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Hull Upgrades", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Mechanics", "Stufe": "V"},
            {"Kategorie": "Armor", "Skill": "Repair Systems", "Stufe": "V"},
            {"Kategorie": "Navigation", "Skill": "Acceleration Control", "Stufe": "IV"},
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
            {"Kategorie": "Gunnery", "Skill": "Small Blaster Specialization", "Stufe": "III"},
            {"Kategorie": "Gunnery", "Skill": "Surgical Strike", "Stufe": "IV"},
            {"Kategorie": "Gunnery", "Skill": "Trajectory Analysis", "Stufe": "IV"},
            {"Kategorie": "Rigging", "Skill": "Astronautics Rigging", "Stufe": "III"},
        ]
    },


    # ---------------------------------------------------------------------------------------
    #
    # --- AGENT Guristas - Nergal ---
    #
    "Nergal vs. Guristas Agent": {
        "flugshow_url": "https://youtu.be/GEnn2QDD1xE", # Dein YouTube-Video
        "fit_misk" : 700,
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
            ":orange[**Notausgang 1:**] Wenn der Scrambler oder der MWD durch das Überhitzen durchbrennt: Rep laufen lassen, MWD AUS/offline, EIne Drohne starten und hoffen dass die Worm die Drohne attackiert und den Scramble auf Dein Schiff aufhebt (kann etwas dauern). Dann aus der Mission warpen.",
            ":orange[**Notausgang 2:**] Wenn der Scrambler oder der MWD durch das Überhitzen durchbrennt: Rep laufen lassen, MWD AUS/offline, Client schliessen (Alt+F4), 10 min warten, wieder einloggen (ihr landet am Gate zur Mission), Schiff reparieren und neu versuchen. Es gibt Berichte, dass diese Taktik leider nicht immer erfolgreich ist.",
            ":orange[**Notausgang 3:**] Wenn man den Anflug verpatzt: Rechtzeitig gegen die Flugrichtung der Worm abdrehen und aus der Mission warpen. Beim zweiten Versuch den eventuell jetzt größeren Abstand zur Worm mit kaltem MWD verkürzen und erst wenn Du merkst, dass sie von Dir wegfliegen will den MWD für max. 3 Zyklen überhitzen.",
        ],
        # Optionale Details (Standardmäßig eingeklappt)
        "details_warum_fit": "Die Nergal glänzt durch enormen Schaden nachdem die Waffe voll hochgespult ist. Es braucht also etwas Zeit bis der Tank des Gegners bricht. Das hilft besonders bei der Worm, denn die hat einen ganz ordentlichen Tank. Das Fit ist ausgelegt, die Worm einzufangen und ihren MWD auszuschalten. Die Worm fliegt mit 3.5km/s und versucht, auf 30 km Abstand zu bleiben. Du fängst sie ein, indem Du extra schnell wirst. Mit dem überhitzten MWD solltest du auf ca. 4.5km/s kommen. Bei unter 11km Abstand schalte den MWD der Worm mit dem Warp Scrambler aus. Damit die Wahrscheinlichkeit reduziert wird, dass MWD und Warp Scramble beide verbrennen, bau die beiden Module jeweils an die beiden Enden der Medium Bank ein. Du kannst die selbe Nergal für alle Anomischen Missionen benutzen: Rigs, Waffe und Armor Repairer bleiben gleich, die anderen Module werden je nach Mission angepasst.",
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

}