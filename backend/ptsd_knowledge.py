# backend/ptsd_knowledge.py

questions = {
    'evento_traumatico': '¿Ha experimentado un evento traumático?',
    'flashbacks': '¿Tiene recuerdos recurrentes e intrusivos del evento?',
    'evitacion': '¿Evita situaciones que le recuerdan al evento?',
    'pesadillas': '¿Tiene pesadillas relacionadas con el evento?',
    'hipervigilancia': '¿Se siente constantemente en guardia o hipervigilante?',
    'problemas_para_dormir': '¿Tiene problemas para dormir?',
    'irritabilidad': '¿Se siente irritable o tiene arrebatos de ira?',
    'dificultad_para_concentrarse': '¿Tiene dificultad para concentrarse?',
    'respuesta_de_sobresalto_excesiva': '¿Se sobresalta fácilmente?',
    'sentimientos_de_culpa': '¿Siente culpa o vergüenza relacionada con el evento?',
    'aislamiento_social': '¿Se ha aislado socialmente?',
    'sin_diagnostico_anterior':'¿No ha sufrido anteriormente de algún trastorno de estrés posttraumático?',
    'pérdida_de_interés': '¿Ha perdido interés en actividades que antes disfrutaba?',
    'sentimientos_de_desesperanza': '¿Se siente desesperanzado sobre el futuro?',
    'recuerdos_intrusivos': '¿Experimenta recuerdos intrusivos y angustiantes del evento?',
    'interaccion_con_personas_con_tept':'¿Ha interactuado anteriormente con personas que sufrían o sufren de trastorno de estres posttraumático?',
    'evitacion_de_recuerdos': '¿Evita pensamientos o sentimientos relacionados con el evento?',
    'mes_o_menos_desde_evento_traumatico':'¿Ha sufrido de algún evento traumático con una diferenciación máxima de 1 mes desde hoy?'
}

diseases = {
    'tept': ['evento_traumatico', 'flashbacks', 'evitacion', 'pesadillas', 'hipervigilancia', 'problemas_para_dormir', 'irritabilidad', 'dificultad_para_concentrarse', 'respuesta_de_sobresalto_excesiva'],
    'tept_agudo':['evento_traumatico', 'flashbacks', 'evitacion','pesadillas', 'hipervigilancia', 'problemas_para_dormir', 'irritabilidad', 'dificultad_para_concentrarse','sin_diagnostico_anterior','mes_o_menos_desde_evento_traumatico'],
    'tept_complejo': ['evento_traumatico', 'flashbacks', 'evitacion', 'pesadillas', 'hipervigilancia', 'problemas_para_dormir', 'irritabilidad', 'dificultad_para_concentrarse', 'sentimientos_de_culpa', 'aislamiento_social', 'pérdida_de_interés', 'sentimientos_de_desesperanza'],
    'tept_disociativo': ['evento_traumatico', 'flashbacks', 'evitacion', 'recuerdos_intrusivos', 'evitacion_de_recuerdos', 'despersonalizacion', 'desrealizacion'],
    'trauma_indirecto': ['pesadillas','problemas_para_dormir','irritabilidad','respuesta_de_sobresalto_excesiva','sin_diagnostico_anterior','sentimientos_de_desesperanza','interaccion_con_personas_con_tept']
}

rules = [
    {'if': ['evento_traumatico', 'flashbacks', 'evitacion'], 'then': 'tept'},
    {'if': ['evento_traumatico', 'flashbacks', 'evitacion','mes_o_menos_desde_evento_traumatico'], 'then': 'tept_agudo'},
    {'if': ['evento_traumatico', 'flashbacks', 'evitacion', 'pesadillas', 'hipervigilancia', 'problemas_para_dormir', 'irritabilidad', 'dificultad_para_concentrarse', 'sentimientos_de_culpa'], 'then': 'tept_complejo'},
    {'if': ['evento_traumatico', 'flashbacks', 'evitacion', 'recuerdos_intrusivos', 'evitacion_de_recuerdos', 'despersonalizacion', 'desrealizacion'], 'then': 'tept_disociativo'},
    {'if': ['irritabilidad','sin_diagnostico_anterior','sentimientos_de_desesperanza','interaccion_con_personas_con_tept'], 'then': 'trauma_indirecto'}
]

def has_symptom(disease, symptom):
    return symptom in diseases.get(disease, [])
