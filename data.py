# data.py
#
# Assemble full anomic guides data from guides files

from guides.agent_angel import AGENT_ANGEL
from guides.agent_blood import AGENT_BLOOD
from guides.agent_guristas import AGENT_GURISTAS
from guides.agent_sansha import AGENT_SANSHA
from guides.agent_serpentis import AGENT_SERPENTIS

from guides.team_enyo import TEAM_ENYO
from guides.team_hawk import TEAM_HAWK
from guides.team_jaguar import TEAM_JAGUAR
from guides.team_vengeance import TEAM_VENGEANCE

from guides.base_talos import BASE_TALOS


# Store root keys in new dict
MISSION_DATA = {

    **AGENT_ANGEL,
    **AGENT_BLOOD,
    **AGENT_GURISTAS,
    **AGENT_SANSHA,
    **AGENT_SERPENTIS,

    **TEAM_ENYO,
    **TEAM_HAWK,
    **TEAM_JAGUAR,
    **TEAM_VENGEANCE,

    **BASE_TALOS
    
}