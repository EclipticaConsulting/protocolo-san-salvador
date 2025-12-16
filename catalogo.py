# -*- coding: utf-8 -*-

# --- 1. LISTAS MAESTRAS DE CONFIGURACIÓN ---

LISTA_AGRUPAMIENTOS = [
    "Recepción del Derecho",
    "Contexto Financiero y Compromiso Presupuestario",
    "Capacidades Estatales",
    "Igualdad y No Discriminación",
    "Acceso a Información Pública y Participación",
    "Acceso a la Justicia",
    "Violencia / Conflictividad (Transversal)",
    "Otro"
]

LISTA_UNIDADES = [
    "Porcentaje (%)",
    "Binario (Sí/No)",
    "Tasa (x 1.000 / x 10.000 / x 100.000)",
    "Número Absoluto (Cantidad)",
    "Moneda Local / Dinero",
    "Texto / Cualitativo",
    "Ratio / Razón",
    "Años / Días / Horas",
    "Otro"
]

LISTA_DESAGREGACION = [
    "Total Nacional",
    "Por Sexo (Hombre/Mujer)",
    "Por Grupos Etarios (Edad)",
    "Por Etnia / Raza / Pueblos Indígenas",
    "Urbano / Rural",
    "Por Ingresos (Quintiles/Deciles)",
    "Por Discapacidad",
    "Por Nivel Educativo",
    "Por Estatus Migratorio (Refugiado/Apátrida)",
    "Por Jurisdicción (Estadual/Provincial)",
    "Otro"
]

LISTA_FUENTES = [
    "Informe Oficial del Estado",
    "Organismos Internacionales (OEA/ONU/OIT/OMS)",
    "Sociedad Civil / ONG",
    "Institución Nacional de DDHH (INDH)",
    "Encuesta Nacional de Hogares (INE/DANE/INDEC)",
    "Censos Nacionales",
    "Registros Administrativos",
    "Otro"
]

MAPA_PAISES = {
    "Argentina": "ARG", "Bolivia": "BOL", "Brasil": "BRA", "Canadá": "CAN", "Chile": "CHL", 
    "Colombia": "COL", "Costa Rica": "CRI", "Cuba": "CUB", "Ecuador": "ECU", "El Salvador": "SLV", 
    "Estados Unidos": "USA", "Guatemala": "GTM", "Haití": "HTI", "Honduras": "HND", "México": "MEX", 
    "Nicaragua": "NIC", "Panamá": "PAN", "Paraguay": "PRY", "Perú": "PER", "República Dominicana": "DOM", 
    "Uruguay": "URY", "Venezuela": "VEN"
}

MAPA_DERECHOS = {
    "Seguridad Social": "SS",
    "Salud": "SAL",
    "Educación": "EDU",
    "Trabajo": "TRA", 
    "Derechos Sindicales": "SIN",
    "Alimentación": "ALI",
    "Medio Ambiente": "MAM",
    "Cultura": "CUL"
}

# --- 2. CATÁLOGO MAESTRO DE INDICADORES (OEA / PSS) ---
# Estructura: DERECHO -> AGRUPAMIENTO -> CATEGORÍA -> LISTA DE TUPLAS (REF, TEXTO)

CATALOGO_INDICADORES = {
    
    # ==============================================================================
    # 1. DERECHO A LA SEGURIDAD SOCIAL
    # ==============================================================================
    "Seguridad Social": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("001", "Ratificación de Tratados Internacionales (PIDESC, CEDAW, Convenio 102 OIT, etc.)"),
                ("002", "Incorporación en la Constitución Política del derecho a la seguridad social"),
                ("003", "Legislación específica (Código SS, Código Trabajo, Normas dispersas)")
            ],
            "Procesos": [
                ("004", "Tiempo promedio de reconocimiento del derecho a pensiones o jubilaciones"),
                ("005", "Porcentaje de la población asegurada por sistemas contributivos"),
                ("006", "Porcentaje de la población cubierta por sistemas no contributivos"),
                ("007", "Porcentaje de población afiliada a regímenes especiales"),
                ("008", "Porcentaje de adultos mayores de 65 años cubiertos por programas de atención a la vejez"),
                ("009", "Porcentaje de afiliados que perciben como satisfactorio el nivel de cobertura [Señal de Progreso]")
            ],
            "Resultados": [
                ("010", "Tasa de población económicamente activa (PEA) con cobertura"),
                ("011", "Población cubierta por una pensión o jubilación"),
                ("012", "Porcentaje de población asegurada a un régimen contributivo"),
                ("013", "Número de afiliados cotizantes al sistema de pensiones"),
                ("014", "Total de subsidios al desempleo a no afiliados")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("015", "Formas de financiamiento del sistema"),
                ("016", "Características y porcentaje de la administración privada del sistema"),
                ("017", "Existencia de estimaciones del costo fiscal de las reformas previsionales [Señal de Progreso]")
            ],
            "Procesos": [
                ("018", "Porcentaje total de recursos del presupuesto nacional asignados a seguridad social"),
                ("019", "Tiempo de licencia por maternidad y paternidad y fuentes de financiamiento"),
                ("020", "Base y frecuencia de actualización de las prestaciones"),
                ("021", "Origen de los fondos extrapresupuestarios (créditos, reservas)"),
                ("022", "Mecanismos para calcular la brecha salarial varones/mujeres"),
                ("023", "Existencia de mecanismos para eximir los costos de litigio"),
                ("024", "Disponibilidad de fondos extrapresupuestarios para financiar déficit"),
                ("025", "Existencia de estudios de reforma con enfoque de género, etnia y raza [Señal de Progreso]")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("026", "Jerarquía y facultades de los organismos que gestionan la seguridad social"),
                ("027", "Cobertura y alcance de políticas de inclusión de no afiliados [Señal de Progreso]")
            ],
            "Procesos": [
                ("028", "Número de pensiones por invalidez otorgadas en el último año"),
                ("029", "Total de cotizantes régimen contributivo (desagregado)"),
                ("030", "Tasa de cobertura por accidentes de trabajo"),
                ("031", "Campañas de formalización del empleo no registrado [Señal de Progreso]"),
                ("032", "Campañas oficiales en materia de prevención de riesgos [Señal de Progreso]")
            ],
            "Resultados": [
                ("033", "Porcentaje de población sin cobertura en seguridad social"),
                ("034", "Porcentaje de población con cobertura (desagregado)"),
                ("035", "Brecha entre cobertura previsional pública y privada"),
                ("036", "Tasa de desempleo promedio anual"),
                ("037", "Tasa de informalidad laboral"),
                ("038", "Tasa de lesiones profesionales por rama de actividad")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("039", "Requisitos de acceso al sistema de seguridad social"),
                ("040", "Requisitos de acceso para indígenas, afrodescendientes, refugiados"),
                ("041", "Requisitos de acceso para trabajadoras del servicio doméstico"),
                ("042", "Requisitos de acceso para trabajadores/as rurales")
            ],
            "Procesos": [
                ("043", "Base de cálculo de las prestaciones para varones y mujeres"),
                ("044", "Uso de tablas actuariales en el cálculo del beneficio"),
                ("045", "Mecanismos de inclusión de trabajo reproductivo/cuidado"),
                ("046", "Reglamentación y control de medidas preventivas en riesgos profesionales"),
                ("047", "Población pensionada por sexo, edad, nivel educativo y jurisdicción"),
                ("048", "Porcentaje de derecho-habientes que perciben pensión/subsidio"),
                ("049", "Porcentaje de migrantes/refugiados con cobertura"),
                ("050", "Porcentaje de trabajadores rurales con cobertura")
            ]
        },
        "Acceso a Información Pública y Participación": {
            "Estructurales": [
                ("051", "Características y regularidad de información estadística"),
                ("052", "Campañas oficiales de difusión sobre derechos [Señal de Progreso]")
            ],
            "Procesos": [
                ("053", "Frecuencia de informes enviados a los cotizantes"),
                ("054", "Acciones sindicales de difusión de garantías [Señal de Progreso]")
            ],
            "Resultados": [
                ("055", "Total de accidentes de trabajo reportados"),
                ("056", "Características de portales/medios sobre programas no contributivos [Señal de Progreso]")
            ]
        },
        "Acceso a la Justicia": {
            "Estructurales": [
                ("057", "Instancias administrativas para radicar denuncias"),
                ("058", "Cantidad de acciones constitucionales (amparos, tutelas)"),
                ("059", "Servicios jurídicos gratuitos de protección"),
                ("060", "Oficinas públicas de mediación o conciliación"),
                ("061", "Aplicación de garantías procesales")
            ],
            "Procesos": [
                ("062", "Número de denuncias relativas a seguridad social"),
                ("063", "Duración promedio de casos tramitados por defensoría"),
                ("064", "Organismos estatales de control de fondos privados (capitalización)"),
                ("065", "Organismos estatales de control de fondos privados (salud/riesgos)"),
                ("066", "Encuestas de satisfacción de beneficiarios [Señal de Progreso]")
            ],
            "Resultados": [
                ("067", "Número de decisiones judiciales que otorgan cobertura"),
                ("068", "Acciones judiciales por denegatoria de pensión no contributiva"),
                ("069", "Políticas de capacitación de jueces y abogados"),
                ("070", "Cobertura de medios que difunden información de derechos [Señal de Progreso]"),
                ("071", "Cobertura de servicios de traducción en lenguas indígenas [Señal de Progreso]")
            ]
        }
    },

    # ==============================================================================
    # 2. DERECHO A LA SALUD
    # ==============================================================================
    "Salud": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("072", "Ratificación de Tratados (PIDESC, CEDAW, CDN, etc.)"),
                ("073", "Directrices y pautas de la OPS"),
                ("074", "Incorporación en la Constitución del derecho a la salud"),
                ("075", "Legislación específica que contempla el derecho a la salud"),
                ("076", "Organizaciones de sociedad civil reconocidas [Señal de Progreso]"),
                ("077", "Reconocimiento de sistemas de salud indígena [Señal de Progreso]")
            ],
            "Procesos": [
                ("078", "Cobertura y jurisdicción de programas para sectores vulnerables"),
                ("079", "Disponibilidad de registros vitales (nacimientos, defunciones)"),
                ("080", "Porcentaje de adultos mayores cubiertos por protección social"),
                ("081", "Cobertura en salud por sexo, edad, etnia, quintil"),
                ("082", "Estudios de satisfacción de usuarios [Señal de Progreso]")
            ],
            "Resultados": [
                ("083", "Esperanza de vida al nacer"),
                ("084", "Tasa de mortalidad materna"),
                ("085", "Tasa de mortalidad infantil"),
                ("086", "Tasa de mortalidad por accidentes/homicidios"),
                ("087", "Tasa de mortalidad por enfermedades transmisibles"),
                ("088", "Porcentaje de población con acceso a agua potable"),
                ("089", "Porcentaje con acceso a saneamiento básico"),
                ("090", "Porcentaje de mujeres en edad reproductiva con anemia")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("091", "Características y fuentes de financiamiento del sector salud"),
                ("092", "Incentivos/subsidios al sector privado"),
                ("093", "Incentivos a la industria farmacéutica"),
                ("094", "Relación crecimiento económico vs cobertura en salud [Señal de Progreso]")
            ],
            "Procesos": [
                ("095", "Porcentaje del Gasto Público Social destinado a salud"),
                ("096", "Gasto Público per cápita en atención a la salud"),
                ("097", "Gasto familiar en salud como proporción del ingreso"),
                ("098", "Distribución del Gasto en salud por jurisdicciones"),
                ("099", "Porcentaje de recursos para capacitación de RRHH")
            ],
            "Resultados": [
                ("100", "Porcentaje promedio de ingresos del hogar gastados en salud por quintil")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("101", "Política pública de atención primaria integral"),
                ("102", "Política nacional sobre medicamentos"),
                ("103", "Densidad de personal profesional por camas"),
                ("104", "Asistencia técnica y financiera internacional"),
                ("105", "Planes para fortalecer adaptabilidad cultural [Señal de Progreso]")
            ],
            "Procesos": [
                ("106", "Accesibilidad de servicios por jurisdicción"),
                ("107", "Porcentaje de población con acceso a medicamentos esenciales"),
                ("108", "Porcentaje de servicios subcontratados a privados"),
                ("109", "Disparidades público-privadas en gasto y cobertura"),
                ("110", "Cantidad de médicos/as por habitantes"),
                ("111", "Cantidad de enfermeras/os por habitante"),
                ("112", "Cantidad de partos atendidos por profesionales")
            ],
            "Resultados": [
                ("113", "Cobertura de programas de atención primaria"),
                ("114", "Cobertura de programas de asistencia a adultos mayores"),
                ("115", "Tasa de utilización de los servicios de salud"),
                ("116", "Cobertura de planes de seguro de salud")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("117", "Regulación del aborto"),
                ("118", "Ley/política para discapacitados"),
                ("119", "Ley/política de salud con diversidad étnica"),
                ("120", "Ley de derechos sexuales y reproductivos"),
                ("121", "Servicios de salud mental (características)"),
                ("122", "Encuestas de percepción sobre fecundidad/mortalidad [Señal de Progreso]"),
                ("123", "Estudios de percepción sobre ETS [Señal de Progreso]")
            ],
            "Procesos": [
                ("124", "Uso de anticonceptivos (mujeres y varones)"),
                ("125", "Estimaciones de abortos inducidos"),
                ("126", "Estimaciones sobre casos de abortos ilegales"),
                ("127", "Uso de sistemas indígenas/alternativos"),
                ("128", "Programas de salud sexual y reproductiva"),
                ("129", "Niños cubiertos por programas nutricionales"),
                ("130", "Controles médicos periódicos (niños/adolescentes)"),
                ("131", "Asistencia en salud perinatal"),
                ("132", "Mujeres embarazadas con test HIV"),
                ("133", "Casos SIDA transmisión vertical"),
                ("134", "Asistencia prenatal"),
                ("135", "Lactancia materna exclusiva")
            ],
            "Resultados": [
                ("136", "Desnutrición crónica (talla) en niños"),
                ("137", "Desnutrición global en niños"),
                ("138", "Composición sexo casos SIDA/VIH"),
                ("139", "Acceso de discapacitados a servicios"),
                ("140", "Prevalencia anticonceptivos (adolescente/adulta)"),
                ("141", "Tasa de fecundidad no deseada"),
                ("142", "Exámenes ginecológicos periódicos"),
                ("143", "Control prenatal primer trimestre"),
                ("144", "Cobertura vacunación obligatoria")
            ]
        },
        "Acceso a Información Pública y Participación": {
            "Estructurales": [
                ("145", "Características del sistema estadístico en salud"),
                ("146", "Campañas de difusión del derecho a la salud [Señal de Progreso]")
            ],
            "Procesos": [
                ("147", "Normas sobre confidencialidad"),
                ("148", "Disposiciones sobre consentimiento"),
                ("149", "Protocolos de confidencialidad en efectores"),
                ("150", "Campañas salud sexual y reproductiva"),
                ("151", "Campañas asesoramiento embarazadas (HIV)"),
                ("152", "Campañas consumo alcohol/drogas"),
                ("153", "Servicios de traducción en efectores"),
                ("154", "Características medios difusión derechos [Señal de Progreso]"),
                ("155", "Mecanismos de participación ciudadana [Señal de Progreso]")
            ],
            "Resultados": [
                ("156", "Niños con malformaciones por consumo sustancias"),
                ("157", "Nacimientos no registrados en término")
            ]
        },
        "Acceso a la Justicia": {
            "Estructurales": [
                ("158", "Instancias administrativas para denuncias"),
                ("159", "Competencias para recibir quejas"),
                ("160", "Acciones constitucionales"),
                ("161", "Servicios jurídicos gratuitos"),
                ("162", "Oficinas de mediación"),
                ("163", "Garantías procesales")
            ],
            "Resultados": [
                ("164", "Decisiones judiciales favorables en salud"),
                ("165", "Denuncias investigadas por instituciones DDHH"),
                ("166", "Políticas de capacitación de jueces y abogados"),
                ("167", "Medios difusión derechos y traducción [Señal de Progreso]")
            ]
        }
    },

    # ==============================================================================
    # 3. DERECHO A LA EDUCACIÓN
    # ==============================================================================
    "Educación": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("168", "Ratificación de tratados internacionales"),
                ("169", "Incorporación en la Constitución"),
                ("170", "Legislación y planes desarrollo"),
                ("171", "Obligatoriedad escolar"),
                ("172", "Normas gratuidad"),
                ("173", "Tipo de cobertura (universalidad/focalización) [Señal de Progreso]"),
                ("174", "Organizaciones sociedad civil [Señal de Progreso]")
            ],
            "Procesos": [
                ("175", "Nivel de desempeño estudiantes"),
                ("176", "Tasa asistencia escolar neta"),
                ("177", "Porcentaje sobreedad"),
                ("178", "Días de clase según norma"),
                ("179", "Cobertura programas acceso vulnerables"),
                ("180", "Cobertura programas Primera Infancia/EDJA"),
                ("181", "Encuestas satisfacción accesibilidad [Señal de Progreso]"),
                ("182", "Encuestas satisfacción bilingüe [Señal de Progreso]")
            ],
            "Resultados": [
                ("183", "Tasa neta cobertura por niveles"),
                ("184", "Tasa analfabetismo"),
                ("185", "Tasa conclusión primaria/secundaria"),
                ("186", "Sobreedad/abandono primaria"),
                ("187", "Sobreedad/abandono secundaria")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("188", "Fuentes de financiamiento"),
                ("189", "Leyes financiamiento gratuidad"),
                ("190", "Incentivos sector privado"),
                ("191", "Avances gratuidad/universalidad [Señal de Progreso]")
            ],
            "Procesos": [
                ("192", "Porcentaje Gasto Público Social en educación"),
                ("193", "Gasto público por niveles"),
                ("194", "Porcentaje inversión I+D"),
                ("195", "Gasto por alumno (% PIB per cápita)"),
                ("196", "Gasto privado (% PIB)"),
                ("197", "Distribución Gasto por jurisdicciones"),
                ("198", "Porcentaje docentes sin título específico")
            ],
            "Resultados": [
                ("199", "Tamaño sección alumnos por docente"),
                ("200", "Porcentaje ingresos hogar gastados en educación")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("201", "Oferta establecimientos públicos"),
                ("202", "Porcentaje escuelas evaluación calidad"),
                ("203", "Participación sector oficial matrícula"),
                ("204", "Asistencia técnica internacional"),
                ("205", "Planes expansión secundaria [Señal de Progreso]")
            ],
            "Procesos": [
                ("206", "Porcentaje establecimientos con bibliotecas"),
                ("207", "Nivel medio educativo"),
                ("208", "Porcentaje niños 0-6 años programas"),
                ("209", "Porcentaje investigadores jornada completa"),
                ("210", "Porcentaje escuelas/docentes formación continua")
            ],
            "Resultados": [
                ("211", "Tasa crecimiento escolarización"),
                ("212", "Porcentaje jóvenes/adultos formación continua"),
                ("213", "Inserción laboral egresados técnicos")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("214", "Marcos legales no discriminación"),
                ("215", "Ley educación bilingüe"),
                ("216", "Inclusión género/DDHH contenidos"),
                ("217", "Educación sexual obligatoria"),
                ("218", "Normas inclusión capacidades especiales"),
                ("219", "Actualización contenidos enfoque derechos [Señal de Progreso]")
            ],
            "Procesos": [
                ("220", "Apoyo familias dificultades socioeconómicas"),
                ("221", "Porcentaje becas"),
                ("222", "Educadores título inicial"),
                ("223", "Matrícula tiempo completo"),
                ("224", "Tiempo educación artística/física"),
                ("225", "Computadores por alumno"),
                ("226", "Programas cultura escrita"),
                ("227", "Alumnos originarios educación bilingüe")
            ],
            "Resultados": [
                ("228", "Relación niñas/niños"),
                ("229", "Relación alfabetización mujeres/varones"),
                ("230", "Escolarización etnias"),
                ("231", "Minorías en ETP/Universitaria"),
                ("232", "Alumnos necesidades especiales escuelas regulares"),
                ("233", "Máximo nivel educativo grupos originarios")
            ]
        },
        "Acceso a Información Pública y Participación": {
            "Estructurales": [
                ("234", "Características sistema estadístico"),
                ("235", "Campañas difusión derecho educación [Señal de Progreso]"),
                ("236", "Campañas erradicación analfabetismo [Señal de Progreso]")
            ],
            "Procesos": [
                ("237", "Mecanismos difusión bases de datos"),
                ("238", "Mecanismos difusión resultados calidad"),
                ("239", "Proyectos con participación social"),
                ("240", "Medios difusión información derecho [Señal de Progreso]")
            ]
        },
        "Acceso a la Justicia": {
            "Estructurales": [
                ("241", "Instancias administrativas denuncias"),
                ("242", "Instancias contenciosas administrativas"),
                ("243", "Acciones constitucionales"),
                ("244", "Servicios jurídicos gratuitos"),
                ("245", "Oficinas mediación"),
                ("246", "Garantías procesales")
            ],
            "Procesos": [
                ("247", "Decisiones judiciales favorables"),
                ("248", "Denuncias investigadas DDHH"),
                ("249", "Políticas capacitación jueces/abogados"),
                ("250", "Medios difusión derechos [Señal de Progreso]"),
                ("251", "Servicios traducción lenguas indígenas [Señal de Progreso]")
            ]
        }
    },

    # ==============================================================================
    # 4. DERECHO AL TRABAJO
    # ==============================================================================
    "Trabajo": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("252", "Consagración constitucional"),
                ("253", "Ratificación convenios OIT"),
                ("254", "Ratificación convenciones interamericanas"),
                ("255", "Tipo indemnizaciones despido [Señal de Progreso]")
            ],
            "Procesos": [
                ("256", "Políticas públicas (forzoso, infantil, antidiscrim, migrantes, accidentes, trata)"),
                ("257", "Mecanismos tripartitos"),
                ("258", "Impulso medidas acción positiva [Señal de Progreso]")
            ],
            "Resultados": [
                ("259", "Tasa trabajo infantil"),
                ("260", "Tasa desempleo"),
                ("261", "Porcentaje asalariados"),
                ("262", "Tasa informalidad"),
                ("263", "Empleo precario"),
                ("264", "Mujeres empleo no agrícola"),
                ("265", "Incidencia accidentes"),
                ("266", "Mujeres funcionariado público"),
                ("267", "Participación discapacidad")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("268", "Presupuesto Ministerio Trabajo"),
                ("269", "Presupuesto políticas vulnerables"),
                ("270", "Subsidios generación empleo")
            ],
            "Procesos": [
                ("271", "Ejecución recursos programas"),
                ("272", "Inversión seguridad laboral")
            ],
            "Resultados": [
                ("273", "Masa salarial en PIB")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("274", "Existencia Ministerio y cobertura"),
                ("275", "Inspectores laborales"),
                ("276", "Funcionarios MinTrabajo vs Población")
            ],
            "Procesos": [
                ("277", "Avance metas programas"),
                ("278", "Desempleados con seguro"),
                ("279", "Empleos creados gobierno"),
                ("280", "Tiempo desempleo"),
                ("281", "Desempleo larga duración"),
                ("282", "Contratos colectivos")
            ],
            "Resultados": [
                ("283", "Adolescentes registrados")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("284", "Sanciones discriminación"),
                ("285", "Mecanismos acoso"),
                ("286", "Recurso judicial"),
                ("287", "Cuotas laborales"),
                ("288", "Programas anti-discriminación"),
                ("289", "Programas conciliación"),
                ("290", "Programas inserción vulnerables")
            ],
            "Procesos": [
                ("291", "Casos discriminación resueltos"),
                ("292", "Incumplimiento cuotas"),
                ("293", "Cobertura protección precaria")
            ],
            "Resultados": [
                ("294", "Proporción tasas vulnerables"),
                ("295", "Crecimiento ingresos pobres"),
                ("296", "Licencia maternidad"),
                ("297", "Licencia paternidad"),
                ("298", "Discriminación salarial")
            ]
        },
        "Acceso a Información Pública y Participación": {
            "Estructurales": [
                ("299", "Encuesta hogares mercado laboral"),
                ("300", "Adecuación encuestas diversidad"),
                ("301", "Portal virtual indicadores"),
                ("302", "Mecanismos judiciales info")
            ],
            "Procesos": [
                ("303", "Solicitudes info atendidas"),
                ("304", "Periodicidad publicación"),
                ("305", "Protocolos confidencialidad")
            ],
            "Resultados": [
                ("306", "Usuarios portal virtual")
            ]
        },
        "Acceso a la Justicia": {
            "Estructurales": [
                ("307", "Jueces laborales"),
                ("308", "Instancias administrativas denuncias"),
                ("309", "Mecanismos acceso justicia"),
                ("310", "Mecanismos vulneraciones")
            ],
            "Procesos": [
                ("311", "Entradas/salidas causas"),
                ("312", "Tiempo promedio"),
                ("313", "Casos resueltos administrativas"),
                ("314", "Existencia jurisprudencia")
            ],
            "Resultados": [
                ("315", "Vulneración no atendida"),
                ("316", "Explotación infantil condena"),
                ("317", "Explotación sexual condena"),
                ("318", "Denuncias discriminación respuesta")
            ]
        }
    },

    # ==============================================================================
    # 5. DERECHOS SINDICALES
    # ==============================================================================
    "Derechos Sindicales": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("319", "Ratificación convenios OIT"),
                ("320", "Consagración constitucional"),
                ("321", "Reglamentación huelga"),
                ("322", "Requisitos legales asociación"),
                ("323", "Garantía ilegalidad huelga"),
                ("324", "Solicitud cooperación OIT [Señal de Progreso]")
            ],
            "Procesos": [
                ("325", "Políticas públicas sindicales"),
                ("326", "Conflictos resueltos administrativamente"),
                ("327", "Solicitudes sindicatos rechazadas"),
                ("328", "Campañas estatales promoción [Señal de Progreso]")
            ],
            "Resultados": [
                ("329", "Tasa sindicalización"),
                ("330", "Cobertura negociación"),
                ("331", "Empresas gremios"),
                ("332", "Días huelga"),
                ("333", "Denuncias Comité Libertad")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("334", "Recursos justicia laboral")
            ],
            "Procesos": [
                ("335", "Ejecución recursos libertad sindical")
            ],
            "Resultados": [
                ("336", "Sindicatos < 500 afiliados")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("337", "Diálogo Social"),
                ("338", "Tipos penales"),
                ("339", "Sistema información vulneraciones"),
                ("340", "Mecanismos protección (fuero)"),
                ("341", "Restricciones legales")
            ],
            "Procesos": [
                ("342", "Avance metas"),
                ("343", "Inspectores laborales"),
                ("344", "Proporción tasa sindicalización"),
                ("345", "Casos resueltos arbitramento"),
                ("346", "Agenda diálogo social")
            ],
            "Resultados": [
                ("347", "Contratos colectivos"),
                ("348", "Nuevos sindicatos"),
                ("349", "Negociaciones apoyadas"),
                ("350", "Proporción sindicalización vulnerables"),
                ("351", "Cobertura negociación vulnerables"),
                ("352", "Mujeres/jóvenes dirigencia")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("353", "Garantías tercerizados"),
                ("354", "Programas organización vulnerable")
            ],
            "Procesos": [
                ("355", "Jurisprudencia anti-sindicales")
            ]
        },
        "Acceso a Información Pública y Participación": {
            "Estructurales": [
                ("356", "Censo sindical"),
                ("357", "Preguntas encuestas"),
                ("358", "Herramientas públicas normas")
            ],
            "Procesos": [
                ("359", "Boletines info")
            ]
        },
        "Acceso a la Justicia": {
            "Estructurales": [
                ("360", "Instancias administrativas"),
                ("361", "Tribunales arbitramento")
            ],
            "Procesos": [
                ("362", "Entradas/salidas causas"),
                ("363", "Tiempo promedio"),
                ("364", "Cobertura formación")
            ]
        }
    },

    # ==============================================================================
    # 6. DERECHO A LA ALIMENTACIÓN
    # ==============================================================================
    "Alimentación": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("365", "Ratificación tratados"),
                ("366", "Consagración constitucional"),
                ("367", "Legislación calidad alimentos")
            ],
            "Procesos": [
                ("368", "Políticas públicas (hambre, desnutrición, agua, etc)"),
                ("369", "Mujeres gestantes bajo peso/anemia"),
                ("370", "Niños anemia"),
                ("371", "Prevalencia sobrepeso")
            ],
            "Resultados": [
                ("372", "Mortalidad malnutrición"),
                ("373", "Inseguridad alimentaria"),
                ("374", "Consumo mínimo energía"),
                ("375", "Hogares sin saneamiento"),
                ("376", "Indigencia"),
                ("377", "Desnutrición infantil"),
                ("378", "Desnutrición general"),
                ("379", "Diabetes/Hipertensión")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("380", "Prioridad constitucional rural"),
                ("381", "Presupuesto Agricultura")
            ],
            "Procesos": [
                ("382", "Índice ruralidad vs transferencias")
            ],
            "Resultados": [
                ("383", "PIB agropecuario")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("384", "Ministerio Agricultura"),
                ("385", "Autoridad control"),
                ("386", "Censo agropecuario"),
                ("387", "Programa salud pública"),
                ("388", "Entidades/políticas específicas")
            ],
            "Procesos": [
                ("389", "Avance metas"),
                ("390", "Beneficiarios vs inseguridad"),
                ("391", "Estándares pesticidas")
            ],
            "Resultados": [
                ("392", "Muerte intoxicación"),
                ("393", "Incidencia intoxicación"),
                ("394", "Población cubierta nutrición"),
                ("395", "Discapacidad mala nutrición")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("396", "Enfoque diferencial"),
                ("397", "Programas ministerios"),
                ("398", "Mecanismos tierra étnica"),
                ("399", "Incentivos fiscales"),
                ("400", "Políticas rural joven"),
                ("401", "Estudios consumo vulnerables [Señal de Progreso]")
            ],
            "Procesos": [
                ("402", "Población beneficiaria excluidos"),
                ("403", "Estímulo lactancia")
            ],
            "Resultados": [
                ("404", "Tasa desnutrición sectores"),
                ("405", "Gasto alimentos ingreso corriente"),
                ("406", "Gasto alimentos ingreso salarial")
            ]
        },
        "Acceso a la Justicia": {
            "Estructurales": [
                ("407", "Recursos constitucionales alimentación"),
                ("408", "Recursos propiedad rural"),
                ("409", "Políticas igualdad acceso")
            ],
            "Procesos": [
                ("410", "Entradas/salidas agraria"),
                ("411", "Tiempo promedio"),
                ("412", "Jurisprudencia"),
                ("413", "Traducción lenguas indígenas [Señal de Progreso]")
            ],
            "Resultados": [
                ("414", "Conflictos alimentación"),
                ("415", "Demandas resueltas"),
                ("416", "Víctimas reparadas")
            ]
        },
        "Acceso a Información Pública y Participación": {
            "Estructurales": [
                ("417", "Encuesta nutricional"),
                ("418", "Encuesta consumo"),
                ("419", "Censo agropecuario"),
                ("420", "Portal virtual"),
                ("421", "Mecanismo clima"),
                ("422", "Divulgación precios"),
                ("423", "Canales protección consumidor"),
                ("424", "Regulaciones publicidad"),
                ("425", "Características portales [Señal de Progreso]")
            ],
            "Procesos": [
                ("426", "Jornadas pedagógicas"),
                ("427", "Programas divulgación"),
                ("428", "Campañas hábitos sanos")
            ],
            "Resultados": [
                ("429", "Programas educación alimentación")
            ]
        }
    },

    # ==============================================================================
    # 7. DERECHO AL MEDIO AMBIENTE
    # ==============================================================================
    "Medio Ambiente": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("430", "Ratificación acuerdos"),
                ("431", "Consagración constitucional"),
                ("432", "Institucionalidad ambiental")
            ],
            "Procesos": [
                ("433", "Políticas públicas (agua, saneamiento, energía, residuos)"),
                ("434", "Política ambiental aprobada"),
                ("435", "Sistema indicadores"),
                ("436", "Uso energía"),
                ("437", "Emisiones CO2")
            ],
            "Resultados": [
                ("438", "Acceso agua"),
                ("439", "Acceso saneamiento"),
                ("440", "Superficie bosques"),
                ("441", "Áreas degradadas"),
                ("442", "Zonas protegidas"),
                ("443", "Combustibles sólidos"),
                ("444", "Acceso servicios públicos"),
                ("445", "Emisiones GEI"),
                ("446", "Mortalidad infantil respiratoria"),
                ("447", "Contaminantes aire"),
                ("448", "Vehículos"),
                ("449", "Internaciones respiratorias"),
                ("450", "Enfermedades agua")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("451", "Presupuesto Medio Ambiente"),
                ("452", "Recursos cooperación"),
                ("453", "Efectividad Gasto"),
                ("454", "Subsidios responsabilidad"),
                ("455", "Estimación riesgo"),
                ("456", "Fondos áreas protegidas")
            ],
            "Procesos": [
                ("457", "Ejecución recursos"),
                ("458", "Cobertura servicios vs transferencias"),
                ("459", "Avance metas subsidios")
            ],
            "Resultados": [
                ("460", "Ejecución hídricos/energéticos"),
                ("461", "Inversión energías limpias"),
                ("462", "Consumo energías limpias"),
                ("463", "Ingresos explotación recursos")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("464", "Encuesta impacto"),
                ("465", "Entidades análisis"),
                ("466", "Entidades/políticas específicas"),
                ("467", "Sistema información vulneraciones")
            ],
            "Procesos": [
                ("468", "Políticas públicas específicas"),
                ("469", "Instrumentos políticas"),
                ("470", "Plan educación"),
                ("471", "Intervenciones control"),
                ("472", "Mapas riesgo"),
                ("473", "Plan mitigación"),
                ("474", "Estrategias conservación"),
                ("475", "Plan reducción residuos")
            ],
            "Resultados": [
                ("476", "Acueducto"),
                ("477", "Energía"),
                ("478", "Aseo"),
                ("479", "Generación residuos"),
                ("480", "Reciclaje"),
                ("481", "Servicio mejorado")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("482", "Incorporación enfoques diferenciales"),
                ("483", "Saberes tradicionales"),
                ("484", "Mecanismo consulta previa"),
                ("485", "Políticas rural joven")
            ],
            "Procesos": [
                ("486", "Proyectos consulta previa"),
                ("487", "Zonas mitigación vulnerables")
            ],
            "Resultados": [
                ("488", "Eliminación excretas"),
                ("489", "Zonas desastres"),
                ("490", "Hogares servicios vulnerables"),
                ("491", "Saneamiento mejorado vulnerables"),
                ("492", "Riesgo ambiental vulnerables")
            ]
        },
        "Acceso a la Justicia": {
            "Estructurales": [
                ("493", "Tribunales administrativos"),
                ("494", "Jueces medioambientales"),
                ("495", "Fiscales delitos"),
                ("496", "Recursos constitucionales"),
                ("497", "Protección recursos pobres"),
                ("498", "Recursos expeditos"),
                ("499", "Garantía acceso info")
            ],
            "Procesos": [
                ("500", "Casos resueltos"),
                ("501", "Entradas/salidas causas"),
                ("502", "Tiempo promedio"),
                ("503", "Cobertura formación"),
                ("504", "Jurisprudencia excluidos")
            ],
            "Resultados": [
                ("505", "Acciones amparo"),
                ("506", "Denuncias penales"),
                ("507", "Denuncias administrativas"),
                ("508", "Causas defensores"),
                ("509", "Lugares protegidos"),
                ("510", "Sentencias ejecutadas"),
                ("511", "Defensores protegidos"),
                ("512", "Recursos resueltos")
            ]
        },
        "Acceso a Información Pública y Participación": {
            "Estructurales": [
                ("513", "Portal virtual"),
                ("514", "Periodicidad publicación")
            ],
            "Resultados": [
                ("515", "Programas divulgación"),
                ("516", "Calificación usuarios")
            ]
        }
    },

    # ==============================================================================
    # 8. DERECHOS CULTURALES
    # ==============================================================================
    "Cultura": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("517", "Ratificación instrumentos"),
                ("518", "Apoyo Declaración Indígenas"),
                ("519", "Consagración constitucional"),
                ("520", "Traducción normas"),
                ("521", "Legislación autor"),
                ("522", "Legislación minorías")
            ],
            "Procesos": [
                ("523", "Campañas divulgar"),
                ("524", "Plan Nacional"),
                ("525", "Fondos concursables"),
                ("526", "Adecuaciones acceso")
            ],
            "Resultados": [
                ("527", "Tasa alfabetismo"),
                ("528", "Alfabetismo lenguas"),
                ("529", "Museos/Bibliotecas/Teatros"),
                ("530", "Computadores/Internet"),
                ("531", "Asistencia espectáculos"),
                ("532", "Tiempo promedio"),
                ("533", "Organizaciones civil"),
                ("534", "Facultades artes"),
                ("535", "Películas"),
                ("536", "Comunidades tradiciones"),
                ("537", "Publicaciones"),
                ("538", "Espacios públicos")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("539", "Prioridad gasto"),
                ("540", "Presupuesto Cultura"),
                ("541", "Presupuesto programas"),
                ("542", "Recursos Plan"),
                ("543", "Presupuesto ciencia"),
                ("544", "Incentivos fiscales")
            ],
            "Procesos": [
                ("545", "Ejecución cultura"),
                ("546", "Ejecución ciencia"),
                ("547", "Ejecución I+D"),
                ("548", "Cooperación internacional"),
                ("549", "Transferencias étnicos"),
                ("550", "Incentivo privado")
            ],
            "Resultados": [
                ("551", "Valor bienes PIB"),
                ("552", "Participación ciencia PIB"),
                ("553", "Gasto per cápita"),
                ("554", "Gasto hogares")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("555", "Ministerio Cultura"),
                ("556", "Inventario riqueza"),
                ("557", "Sistema divulgación"),
                ("558", "Actividad legislativa"),
                ("559", "Encuesta consumo [Señal de Progreso]")
            ],
            "Procesos": [
                ("560", "Avance metas"),
                ("561", "Ejecución gasto"),
                ("562", "Festivales"),
                ("563", "Estrategias comunicación"),
                ("564", "Funcionarios cultura"),
                ("565", "Funcionarios capacitados")
            ],
            "Resultados": [
                ("566", "Patentes"),
                ("567", "Películas producidas"),
                ("568", "Equipamientos"),
                ("569", "Minorías sin documento"),
                ("570", "Crecimiento asistencia")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("571", "Enfoque diferencial"),
                ("572", "Programas ministerios"),
                ("573", "Información desagregada"),
                ("574", "Plan estrategias diferenciales"),
                ("575", "Tenencia tierra")
            ],
            "Procesos": [
                ("576", "Población beneficiaria"),
                ("577", "Criterios asignación"),
                ("578", "Procesos consulta"),
                ("579", "Políticas interculturales"),
                ("580", "Programas excluidos")
            ],
            "Resultados": [
                ("581", "Ingreso familiar cultura"),
                ("582", "Crecimiento ingreso"),
                ("583", "Concentración geográfica"),
                ("584", "Crecimiento hablantes"),
                ("585", "Representación minorías"),
                ("586", "Producciones excluidos")
            ]
        },
        "Acceso a Información Pública y Participación": {
            "Estructurales": [
                ("587", "Sistema preservación"),
                ("588", "Portal virtual"),
                ("589", "Mecanismos divulgación"),
                ("590", "Sistema rendición cuentas")
            ],
            "Procesos": [
                ("591", "Funcionarios preservación"),
                ("592", "Boletines oferta"),
                ("593", "Jornadas pedagógicas"),
                ("594", "Uso indicadores")
            ],
            "Resultados": [
                ("595", "Instancias participación"),
                ("596", "Visitas portales"),
                ("597", "Solicitudes datos")
            ]
        },
        "Acceso a la Justicia": {
            "Estructurales": [
                ("598", "Recursos autor"),
                ("599", "Mecanismos diversidad"),
                ("600", "Justicia tradicional"),
                ("601", "Garantías procesales")
            ],
            "Procesos": [
                ("602", "Casos resueltos"),
                ("603", "Jurisprudencia")
            ],
            "Resultados": [
                ("604", "Reducción violencia"),
                ("605", "Casos consulta previa"),
                ("606", "Casos resueltos derechos")
            ]
        }
    }
}
            ]
        }
    }

}
