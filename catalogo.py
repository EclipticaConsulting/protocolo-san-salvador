# -*- coding: utf-8 -*-

# --- 1. LISTAS MAESTRAS DE CONFIGURACIÓN ---

LISTA_AGRUPAMIENTOS = [
    "Acceso A Información Pública Y Participación",
    "Acceso A La Justicia",
    "Capacidades Estatales",
    "Contexto Financiero Básico Y Compromisos Presupuestarios",
    "Igualdad Y No Discriminación",
    "Recepción Del Derecho",
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
CATALOGO_INDICADORES = {
    "Seguridad Social": {
        "Recepción Del Derecho": {
            "Estructurales": [
                [
                    "SS-E-1",
                    "- Ratificación por parte del Estado de los siguientes Tratados Internacionales que reconocen el derecho a la seguridad social:\na) PIDESC\nb) CEDAW\nc) Convenio 102, OIT\nd) Convención sobre el estatuto de Refugiados de 1951 y su Protocolo de 1967.\ne) Convención sobre el Estatuto de los apátridas de 1954\nf) Convención Interamericana para la eliminación de todas formas de discriminación contra las personas con discapacidad,\ng) Convención internacional sobre la protección de todos los trabajadores migrantes y sus familias,\nh) Declaración de Naciones Unidas sobre los Derechos de los Pueblos Indígenas, entre otras.\n- Incorporación en la Constitución Política (y/o constituciones estaduales o provinciales) del derecho a la seguridad social.\n- Legislación específica que contempla el derecho a la seguridad social:\na) Código de Seguridad Social,\nb) Capítulos o títulos especiales en el Código de Trabajo,\nc) Conjunto de leyes y normativas dispersas,\nd) Normas de negociación colectiva\ne) Otras normas. Especificar."
                ],
                [
                    "SS-E-2",
                    "- Incorporación en la Constitución Política (y/o constituciones estaduales o provinciales) del derecho a la seguridad social."
                ],
                [
                    "SS-E-3",
                    "- Legislación específica que contempla el derecho a la seguridad social: \na) Código de Seguridad Social, \nb) Capítulos o títulos especiales en el Código de Trabajo, \nc) Conjunto de leyes y normativas dispersas, \nd) Normas de negociación colectiva \ne) Otras normas. Especificar."
                ]
            ],
            "Procesos": [
                [
                    "SS-P-1",
                    "- Tiempo promedio de reconocimiento del derecho a pensiones o jubilaciones por condición de actividad y por sexo."
                ],
                [
                    "SS-P-2",
                    "Porcentaje de la población asegurada por sistemas contributivos por sexo, etnia/raza y nivel educativo."
                ],
                [
                    "SS-P-3",
                    "- Porcentaje de la población cubierta por sistemas no contributivos por sexo, etnia/raza y nivel educativo."
                ],
                [
                    "SS-P-4",
                    "Porcentaje de población afiliada a regímenes especiales por sexo, etnia/raza y nivel educativo."
                ],
                [
                    "SS-P-5",
                    "Porcentaje de adultos mayores de 65 años cubiertos por programas de atención a la vejez por sexo, etnia/raza y nivel educativo."
                ],
                [
                    "SS-P-6",
                    "- Porcentaje de afiliados que perciben como satisfactorio el nivel de cobertura en seguridad social"
                ]
            ],
            "Resultados": [
                [
                    "SS-R-1",
                    "Tasa de población económicamente activa por sexo, edad, nivel educativo y quintiles de ingresos"
                ],
                [
                    "SS-R-2",
                    "- Población cubierta por una pensión o jubilación por grupo de edad, sexo y quintiles de ingreso."
                ],
                [
                    "SS-R-3",
                    "- Porcentaje de población asegurada a un régimen contributivo, por sexo, edad y quintiles de ingreso."
                ],
                [
                    "SS-R-4",
                    "-Número de afiliados cotizantes al sistema de pensiones por sexo, edad y quintiles de ingresos"
                ],
                [
                    "SS-R-5",
                    "- Total de subsidios al desempleo a personas no afiliadas a los sistemas contributivos."
                ]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                [
                    "SS-E-4",
                    "- Formas de financiamiento del sistema de seguridad social: i) porcentaje de aportes a cargo de los empleadores y ii) porcentaje a cargo de los trabajadores formales; iii) porcentaje de financiamiento del Estado"
                ],
                [
                    "SS-E-5",
                    "- Características y porcentaje de la administración del sistema otorgado a empresas privadas"
                ],
                [
                    "SS-E-6",
                    "- Origen de los fondos extrapresupuestarios (créditos de organismos internacionales, endeudamiento, reservas, otros)."
                ],
                [
                    "SS-E-7",
                    "Existencia de estimaciones del costo fiscal de las reformas previsionales"
                ],
                [
                    "SS-E-8",
                    "-Existencia de estudios y proyectos de reforma de los sistemas de seguridad social con enfoque de género, etnia y raza."
                ]
            ],
            "Procesos": [
                [
                    "SS-P-7",
                    "Porcentaje total de recursos del presupuesto nacional asignados a seguridad social"
                ],
                [
                    "SS-P-8",
                    "Tiempo de licencia por maternidad y paternidad en semanas y por fuentes de financiamiento (sistema de seguridad social en su totalidad; el empleador en su totalidad; formas mixtas)."
                ],
                [
                    "SS-P-9",
                    "Base y frecuencia de actualización de las prestaciones en seguridad social."
                ],
                [
                    "SS-P-10",
                    "Mecanismos para calcular la brecha salarial entre varones y mujeres a los efectos previsionales."
                ],
                [
                    "SS-P-11",
                    "Existencia de mecanismos para eximir los costos de litigio. Requisitos para calificar para ese beneficio."
                ],
                [
                    "SS-P-12",
                    "Disponibilidad y/o utilización de fondos extrapresupuestarios para financiar el sistema de seguridad social -o su déficit.-"
                ]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                [
                    "SS-E-9",
                    "Jerarquía y facultades de los organismos que gestionan la seguridad social"
                ],
                [
                    "SS-E-10",
                    "Cobertura y alcance de políticas públicas de inclusión de los no afiliados al sistema de seguridad social"
                ]
            ],
            "Procesos": [
                [
                    "SS-P-13",
                    "Número de pensiones por invalidez otorgadas en el último año por sexo, edad, nacionalidad, condición jurídica (estatuto de refugiado o apátrida), quintiles de ingresos y lugar de residencia."
                ],
                [
                    "SS-P-14",
                    "Total de cotizantes régimen contributivo por edad, sexo, nacionalidad, condición jurídica, categoría ocupacional y rama de actividad."
                ],
                [
                    "SS-P-15",
                    "Tasa de cobertura por accidentes de trabajo por sexo, edad, condición jurídica, categoría ocupacional y rama de actividad."
                ],
                [
                    "SS-P-16",
                    "Tasa de desempleo promedio anual."
                ],
                [
                    "SS-P-17",
                    "Tasa de informalidad laboral"
                ],
                [
                    "SS-P-18",
                    "Campañas de formalización del empleo no registrado llevadas a cabo por el Estado."
                ],
                [
                    "SS-P-19",
                    "Campañas oficiales en materia de prevención de riesgos del trabajo."
                ]
            ],
            "Resultados": [
                [
                    "SS-R-6",
                    "- Porcentaje de población sin cobertura en materia de seguridad social, por edad, sexo, por nacionalidad, condición jurídica (estatuto de refugiado o apátrida) condición de actividad, etnia y raza."
                ],
                [
                    "SS-R-7",
                    "-Porcentaje de la población desagregada por sexo, edad y origen étnico con cobertura en seguridad social"
                ],
                [
                    "SS-R-8",
                    "- Brecha entre cobertura previsional pública y privada"
                ],
                [
                    "SS-R-9",
                    "- Tasa de lesiones profesionales (accidentalidad laboral) por rama de actividad"
                ]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                [
                    "SS-E-11",
                    "Requisitos de acceso al sistema de seguridad social"
                ],
                [
                    "SS-E-12",
                    "Requisitos para el acceso al sistema para indígenas, afrodescendientes, refugiados, solicitantes de asilo y apátridas"
                ],
                [
                    "SS-E-13",
                    "Requisitos para el acceso al sistema para trabajadoras del servicio doméstico."
                ],
                [
                    "SS-E-14",
                    "- Requisitos para el acceso al sistema para trabajadores/as rurales."
                ]
            ],
            "Procesos": [
                [
                    "SS-P-20",
                    "Base de cálculo de las prestaciones de seguridad social para varones y mujeres."
                ],
                [
                    "SS-P-21",
                    "Extensión y formas de utilización de tablas actuariales en el cálculo del beneficio previsional (haber de la pensión)."
                ],
                [
                    "SS-P-22",
                    "Extensión y formas de utilización de tablas actuariales en el cálculo del beneficio previsional (haber de la pensión)."
                ]
            ],
            "Resultados": [
                [
                    "SS-R-10",
                    "- Población pensionada (jubilada) por sexo, edad, nivel educativo y por jurisdicciones."
                ],
                [
                    "SS-R-11",
                    "-Porcentaje de derecho-habientes que perciben una pensión o subsidio por sexo, por edad, etnia y raza, por jurisdicciones."
                ],
                [
                    "SS-R-12",
                    "-Porcentaje de migrantes, refugiados, solicitantes de asilo y apátridas con cobertura de seguridad social"
                ],
                [
                    "SS-R-13",
                    "Porcentaje de trabajadores y trabajadoras rurales con cobertura de seguridad social"
                ]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                [
                    "SS-E-15",
                    "Características y regularidad en la producción de información estadística en materia de seguridad social por sexo, etnia, raza, edad, nacionalidad, condición jurídica (estatuto de refugiado o apátrida) cobertura pública o privada, distribución territorial."
                ],
                [
                    "SS-E-16",
                    "- Características, frecuencia, cobertura de campañas oficiales de difusión sobre los derechos a la seguridad social."
                ],
                [
                    "SS-E-17",
                    "Características, frecuencia, cobertura de acciones sindicales de difusión de garantías de derechos de seguridad social a los trabajadores."
                ]
            ],
            "Procesos": [
                [
                    "SS-P-23",
                    "Reglamentación existente y tipo de control de la aplicación de medidas preventivas en riesgos profesionales y salud ocupacional."
                ],
                [
                    "SS-P-24",
                    "Frecuencia de los informes enviados a los cotizantes de los sistemas previsionales, tanto por cuentas de capitalización individual como por régimen público de reparto."
                ],
                [
                    "SS-P-25",
                    "Frecuencia de los informes enviados a los cotizantes de los sistemas previsionales, tanto por cuentas de capitalización individual como por régimen público de reparto."
                ],
                [
                    "SS-P-26",
                    "Características de -portales de Internet, cobertura televisiva, ventanillas específicas- de la información brindada sobre derechos a los receptores de programas de cobertura graciable o no contributiva."
                ]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                [
                    "SS-E-18",
                    "Instancias administrativas para radicar denuncias en materia de incumplimiento de obligaciones vinculadas al derecho a la seguridad social."
                ],
                [
                    "SS-E-19",
                    "- Cantidad de acciones constitucionales (amparos, acciones de protección, tutela) en seguridad social"
                ],
                [
                    "SS-E-20",
                    "- Existencia de servicios jurídicos gratuitos e integrales de protección del derecho a la seguridad social."
                ],
                [
                    "SS-E-21",
                    "-Existencia de oficinas públicas de mediación o conciliación para resolver cuestiones vinculadas con seguridad social."
                ],
                [
                    "SS-E-22",
                    "-Aplicación de garantías procesales en los procedimientos judiciales en materia de seguridad social: \ni) independencia e imparcialidad del tribunal; ii) plazo razonable; iii) igualdad de armas; iv) cosa juzgada; v) vias recursivas de sentencias en instancias superiores."
                ]
            ],
            "Procesos": [
                [
                    "SS-P-27",
                    "Número de denuncias relativas al derecho a la seguridad social recibidas"
                ],
                [
                    "SS-P-28",
                    "Duración promedio de los casos tramitados por la defensoría oficial sobre pensiones (contributivas y no contributivas)."
                ],
                [
                    "SS-P-29",
                    "Existencia de organismos estatales de control y fiscalización de las entidades encargadas de fondos de capitalización individual por entidades privadas."
                ],
                [
                    "SS-P-30",
                    "Existencia de organismos estatales de control y fiscalización de las entidades encargadas de fondos de capitalización individual por entidades privadas."
                ],
                [
                    "SS-P-31",
                    "Número de decisiones judiciales que otorgan cobertura de contingencias en seguridad social,"
                ],
                [
                    "SS-P-32",
                    "Número de acciones judiciales presentadas y resueltas por denegatoria de una pensión no contributiva."
                ],
                [
                    "SS-P-33",
                    "Políticas de capacitación de jueces y abogados en derecho a la seguridad social. Cobertura temática y alcance."
                ],
                [
                    "SS-P-34",
                    "Encuestas de satisfacción o percepción de los beneficiarios y usuarios respecto del sistema de seguridad social y de los programas de protección social"
                ],
                [
                    "SS-P-35",
                    "Características y cobertura de los medios que difunden información a las personas de sus derechos en relación con la seguridad social."
                ],
                [
                    "SS-P-36",
                    "Cobertura de los servicios de traducción en lenguas indígenas."
                ]
            ]
        }
    },
    "Salud": {
        "Recepción Del Derecho": {
            "Estructurales": [
                [
                    "SAL-E-1",
                    "Ratificación del Estado de los siguientes Tratados internacionales que reconocen el derecho a la salud (consignar fecha): \ni) PIDESC y Protocolo Facultativo\nii) CEDAW y Protocolo Facultativo \niii) CDN\niv) CIEDR\nv) Convenios de OIT;\nvi) Convención sobre el estatuto de Refugiados de 1951 y su Protocolo de 1967;\nvii) Convención sobre el Estatuto de los apátridas de 1954,\nviii) Convención Interamericana para la eliminación de todas formas de discriminación contra las personas con discapacidad,\nix) Convención internacional sobre la protección de todos los trabajadores migrantes y sus familias,\nx) Declaración de Naciones Unidas sobre los Derechos de los Pueblos Indígenas.\nxi) Directrices y pautas de la Organización Panamericana de la Salud."
                ],
                [
                    "SAL-E-2",
                    "- Incorporación en la Constitución Política (y/o constituciones estaduales o provinciales) del derecho a la salud."
                ],
                [
                    "SAL-E-3",
                    "- Legislación específica que contempla el derecho a la salud."
                ],
                [
                    "SAL-E-4",
                    "- Número y características de organizaciones de la sociedad civil reconocidas que participan en la promoción y la protección del derecho a la salud."
                ],
                [
                    "SAL-E-5",
                    "- Reconocimiento de sistemas de salud indígena."
                ]
            ],
            "Procesos": [
                [
                    "SAL-P-1",
                    "Cobertura y jurisdicción de programas que otorgan prioridad a sectores vulnerables para servicios de salud."
                ],
                [
                    "SAL-P-2",
                    "Disponibilidad de registros para conocer número de nacimientos, defunciones, matrimonios."
                ],
                [
                    "SAL-P-3",
                    "Porcentajes de adultos mayores de 65 años cubiertos por programas de protección social."
                ],
                [
                    "SAL-P-4",
                    "Cobertura en salud de la población por sexo, edad raza/etnia, quintiles de ingreso. Desagregar por tipo de cobertura (régimen subsidiado, contributivo o mixto)"
                ],
                [
                    "SAL-P-5",
                    "Estudios de satisfacción de los usuarios sobre la accesibilidad, disponibilidad y calidad de los servicios de salud."
                ]
            ],
            "Resultados": [
                [
                    "SAL-R-1",
                    "- Esperanza de vida al nacer (urbano/rural y por etnia/raza)"
                ],
                [
                    "SAL-R-2",
                    "- Tasa de mortalidad materna por grupo de edad, área geográfica, nivel educativo y quintiles de ingreso."
                ],
                [
                    "SAL-R-3",
                    "- Tasa de mortalidad infantil por sexo, por área geográfica, nivel educativo de la madre, quintiles de ingreso, etnia/raza, neonatal y post-natal."
                ],
                [
                    "SAL-R-4",
                    "- Tasa de mortalidad por sexo debido a accidentes, homicidios o suicidios."
                ],
                [
                    "SAL-R-5",
                    "- Tasa de mortalidad por enfermedades transmisibles."
                ],
                [
                    "SAL-R-6",
                    "- Porcentaje de la población con acceso a agua potable urbano/rural."
                ],
                [
                    "SAL-R-7",
                    "- Porcentaje de personas con acceso a servicios de saneamiento básico urbano/rural."
                ],
                [
                    "SAL-R-8",
                    "- Porcentaje de mujeres en edad reproductiva con anemia."
                ]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                [
                    "SAL-E-6",
                    "Características, fuentes y porcentajes de financiamiento del sector salud"
                ],
                [
                    "SAL-E-7",
                    "- Características, tipos, monto y extensión de incentivos, deducción de impuestos (incentivos fiscales) y subsidios para el sector privado de la salud."
                ],
                [
                    "SAL-E-8",
                    "Características, tipos, monto y extensión de incentivos estatales a la industria farmacéutica privada."
                ],
                [
                    "SAL-E-9",
                    "Relación entre crecimiento económicos vs cobertura en salud en los últimos 5 años."
                ]
            ],
            "Procesos": [
                [
                    "SAL-P-6",
                    "Porcentaje del Gasto Público Social destinado a salud"
                ],
                [
                    "SAL-P-7",
                    "Gasto Público per cápita en atención a la salud"
                ],
                [
                    "SAL-P-8",
                    "Gasto familiar en salud como proporción del ingreso familiar corriente"
                ],
                [
                    "SAL-P-9",
                    "Distribución del Gasto en salud por jurisdicciones (estaduales, provinciales, locales)"
                ],
                [
                    "SAL-P-10",
                    "Porcentaje de recursos destinados a la capacitación de recursos humanos en salud"
                ]
            ],
            "Resultados": [
                [
                    "SAL-R-9",
                    "- Porcentaje promedio de ingresos del hogar gastados en salud según quintil de ingreso per cápita familiar."
                ]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                [
                    "SAL-E-10",
                    "- Incorporación en documentos oficiales (política pública) el concepto básico de atención primaria de salud integral y universal."
                ],
                [
                    "SAL-E-11",
                    "- Alcance, jurisdicción y financiamiento de una política nacional sobre medicamentos esenciales, oncológicos, retrovirales, y medicamentos genéricos."
                ],
                [
                    "SAL-E-12",
                    "- Densidad del personal profesional auxiliar por cantidad de camas de hospital"
                ],
                [
                    "SAL-E-13",
                    "Características, extensión, montos y gestión de asistencia técnica y financiera internacional en el área de salud."
                ]
            ],
            "Procesos": [
                [
                    "SAL-P-11",
                    "Accesibilidad y disponibilidad de los servicios de salud por jurisdicción y región geográfica"
                ],
                [
                    "SAL-P-12",
                    "Porcentaje de la población con acceso frecuente a medicamentos esenciales oncológicos, retrovirales y o genéricos por lugar de residencia (urbano/rural)"
                ],
                [
                    "SAL-P-13",
                    "Porcentaje de servicios de salud de responsabilidad pública subcontratados a compañías privadas u otro tipo de efector"
                ],
                [
                    "SAL-P-14",
                    "Disparidades público-privadas significativas en el gasto y cobertura en salud."
                ],
                [
                    "SAL-P-15",
                    "Cantidad de Médicos/as por habitantes"
                ],
                [
                    "SAL-P-16",
                    "Cantidad de enfermeras/os por habitante"
                ],
                [
                    "SAL-P-17",
                    "Cantidad de partos atendidos por profesionales"
                ],
                [
                    "SAL-P-18",
                    "Existencia de planes/políticas para fortalecer la adaptabilidad cultural de los servicios de salud bajo un enfoque de derechos y étnico."
                ]
            ],
            "Resultados": [
                [
                    "SAL-R-10",
                    "- Cobertura, extensión, jurisdicción y financiamiento de los programas de atención primaria en salud"
                ],
                [
                    "SAL-R-11",
                    "-Cobertura de programas de asistencia a adultos mayores."
                ],
                [
                    "SAL-R-12",
                    "- Tasa de utilización de los servicios de salud"
                ],
                [
                    "SAL-R-13",
                    "Cobertura de planes de seguro de salud, por sexo, edad y región geográfica en calidad de cotizantes o beneficiarios."
                ]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                [
                    "SAL-E-14",
                    "Regulación del aborto."
                ],
                [
                    "SAL-E-15",
                    "- Ley o política nacional para los discapacitados físicos y mentales."
                ],
                [
                    "SAL-E-16",
                    "- Ley o política nacional de salud considerando la diversidad étnica (indígenas, afrodescendientes)."
                ],
                [
                    "SAL-E-17",
                    "- Ley de reconocimiento de los derechos sexuales y reproductivos."
                ],
                [
                    "SAL-E-18",
                    "Tipo, número, características, jurisdicción, presupuesto y accesibilidad a los servicios de salud mental por distribución territorial."
                ],
                [
                    "SAL-E-19",
                    "Características y frecuencia de encuestas de percepción de la población acerca de la relación entre fecundidad, mortalidad infantil y mortalidad materna."
                ]
            ],
            "Procesos": [
                [
                    "SAL-P-19",
                    "Porcentaje de mujeres y varones en edad de procrear que usan anticonceptivos."
                ],
                [
                    "SAL-P-20",
                    "Estimaciones de abortos inducidos, por edad, lugar de residencia (urbano o rural) y condiciones socioeconómicas de la mujer embarazada."
                ],
                [
                    "SAL-P-21",
                    "Estimaciones sobre casos de abortos ilegales, por edad, lugar de residencia (urbano o rural) y condiciones socioeconómicas de la mujer embarazada u otros datos disponibles"
                ],
                [
                    "SAL-P-22",
                    "Porcentaje de la población que utiliza sistemas indígenas o alternativos de atención de la salud"
                ],
                [
                    "SAL-P-23",
                    "Características, cobertura, presupuesto y jurisdicciones en programas de salud sexual y reproductiva."
                ],
                [
                    "SAL-P-24",
                    "Porcentaje de niños y niñas cubiertos por programas nutricionales."
                ],
                [
                    "SAL-P-25",
                    "Porcentaje de niños, niñas y adolescentes que reciben periódicamente atención/controles médicos"
                ],
                [
                    "SAL-P-26",
                    "Porcentaje de niños, niñas y adolescentes que reciben periódicamente atención/controles médicos"
                ],
                [
                    "SAL-P-27",
                    "Porcentaje de mujeres embarazadas con test de HIV/SIDA."
                ],
                [
                    "SAL-P-28",
                    "Porcentaje de niños nacidos de madres HIV positivas que contrajeron el virus HIV/SIDA en los dos primeros años de vida (casos notificados de SIDA por transmisión vertical)"
                ],
                [
                    "SAL-P-29",
                    "Porcentaje de mujeres embarazadas que reciben asistencia en salud prenatal."
                ],
                [
                    "SAL-P-30",
                    "- Indicadores de lactancia materna exclusiva hasta el cuarto mes y hasta el sexto mes."
                ],
                [
                    "SAL-P-31",
                    "- Características y frecuencia de estudios de percepción de la población en relación con enfermedades de trasmisión sexual (HIV-SIDA, entre otras)"
                ]
            ],
            "Resultados": [
                [
                    "SAL-R-14",
                    "-Porcentaje de niños menores de 5 años que presentan retraso en la talla o desnutrición crónica."
                ],
                [
                    "SAL-R-15",
                    "-Porcentaje de niños y niñas menores de 5 años con desnutrición global."
                ],
                [
                    "SAL-R-16",
                    "-Composición por sexo de los casos notificados de SIDA y diagnósticos VIH."
                ],
                [
                    "SAL-R-17",
                    "-Porcentaje de discapacitados físicos o mentales que tienen acceso a servicios de instituciones públicas o sociales."
                ],
                [
                    "SAL-R-18",
                    "-Prevalencia de uso de métodos anticonceptivos entre población adolescente sexualmente activa"
                ],
                [
                    "SAL-R-19",
                    "-Prevalencia del uso de anticonceptivos entre población adulta sexualmente activa"
                ],
                [
                    "SAL-R-20",
                    "-Tasa de fecundidad no deseada"
                ],
                [
                    "SAL-R-21",
                    "-Porcentaje de mujeres que realizan periódicamente exámenes ginecológicos (PAP, mamografías)"
                ],
                [
                    "SAL-R-22",
                    "- Porcentaje de mujeres con control prenatal en el primer trimestre"
                ],
                [
                    "SAL-R-23",
                    "-Cobertura de vacunación obligatoria."
                ]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                [
                    "SAL-E-20",
                    "Características, cobertura (territorial y temática), presupuesto y jurisdicción del sistema estadístico en materia de salud. Formas y frecuencia de actualización de la información, y difusión."
                ],
                [
                    "SAL-E-21",
                    "Normas y regulaciones de protección del estado sobre la confidencialidad de la información personal de salud."
                ],
                [
                    "SAL-E-22",
                    "- Disposiciones y/o legislación que requieran el consentimiento de la persona para aceptar o rechazar un tratamiento."
                ],
                [
                    "SAL-E-23",
                    "- Características, cobertura y periodicidad de campañas de difusión del derecho a la salud"
                ]
            ],
            "Procesos": [
                [
                    "SAL-P-32",
                    "Porcentaje de efectores de salud con protocolos de confidencialidad de la información sobre su salud"
                ],
                [
                    "SAL-P-33",
                    "Cobertura de acciones o campañas de difusión por parte del estado de información sobre políticas de salud sexual y reproductiva."
                ],
                [
                    "SAL-P-34",
                    "Cobertura de acciones o campañas de asesoramiento a mujeres embarazadas sobre formas de transmisión madre-hijo de HIV/SIDA."
                ],
                [
                    "SAL-P-35",
                    "Cobertura de acciones o campañas de información y programas de difusión sobre los efectos del consumo de alcohol, tabaco y otras drogas."
                ],
                [
                    "SAL-P-36",
                    "Distribución geográfica, jurisdiccional y étnica de servicios de traducción en los efectores de salud a otros idiomas hablados en el país."
                ],
                [
                    "SAL-P-37",
                    "Características y cobertura de los medios que difunden información a las personas de sus derechos en relación con la atención a la salud."
                ],
                [
                    "SAL-P-38",
                    "- Existencia de mecanismos permanentes participación ciudadana para la elaboración de recomendaciones en el diseño e implementación de políticas de salud."
                ]
            ],
            "Resultados": [
                [
                    "SAL-R-24",
                    "- Porcentaje de niños nacidos con malformaciones fetales por consumo de alcohol y otro tipo de drogas."
                ],
                [
                    "SAL-R-25",
                    "Porcentaje de nacimientos no registrados en término."
                ]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                [
                    "SAL-E-24",
                    "-Existencia de instancias administrativas para radicar denuncias en materia de incumplimiento de obligaciones vinculadas al derecho a la salud."
                ],
                [
                    "SAL-E-25",
                    "-Competencias de los Ministerios o de las Superintendencias para recibir quejas de los usuarios del sistema de salud."
                ],
                [
                    "SAL-E-26",
                    "-Existencia de acciones constitucionales (amparos, acciones de protección, tutela)"
                ],
                [
                    "SAL-E-27",
                    "-Existencia de servicios jurídicos gratuitos e integrales de protección del derecho a la salud."
                ],
                [
                    "SAL-E-28",
                    "-Existencia de oficinas públicas de mediación o conciliación para resolver cuestiones vinculadas con salud."
                ],
                [
                    "SAL-E-29",
                    "-Aplicación de garantías procesales en los procedimientos judiciales en materia de salud: i) independencia e imparcialidad del tribunal; ii) plazo razonable; iii) igualdad de armas; iv) cosa juzgada; v) vias recursivas de sentencias en instancias superiores."
                ]
            ],
            "Procesos": [
                [
                    "SAL-P-39",
                    "Número de decisiones judiciales que ha hecho lugar a garantías en salud en general y en casos específicos (salud sexual y reproductiva, personas con HIV-SIDA; entre otras)."
                ],
                [
                    "SAL-P-40",
                    "Número de denuncias relativas al derecho a la salud recibidas, investigadas y resueltas por las instituciones nacionales de derechos humanos competentes en el país"
                ],
                [
                    "SAL-P-41",
                    "Políticas de capacitación de jueces y abogados en materia de derecho a la salud. Cobertura temática y alcance."
                ],
                [
                    "SAL-P-42",
                    "Características y cobertura de los medios que difunden información a las personas de sus derechos en relación con la salud. Cobertura de los servicios de traducción en lenguas indígenas."
                ]
            ]
        }
    },
    "Educación": {
        "Recepción Del Derecho": {
            "Estructurales": [
                [
                    "EDU-E-1",
                    "Ratificación de tratados internacionales que reconocen el derecho a la educación: \ni) PIDESC y Protocolo Facultativo; ii) CEDAW y Protocolo Facultativo; iii) CDN; iv) CIEDR; \nv) Convención relativa a la lucha contra las discriminaciones en la esfera de la enseñanza; vi) Convención Interamericana para la eliminación de todas formas de discriminación contra las personas con discapacidad; vii) Metas educativas 2021; viii) Declaración de la XX Cumbre Iberoamericana (2010)."
                ],
                [
                    "EDU-E-2",
                    "Incorporación en la Constitución Política (y/o constituciones estaduales o provinciales) del derecho a la educación."
                ],
                [
                    "EDU-E-3",
                    "Legislación específica y/o planes de desarrollo educativo que contemplen el derecho a la educación. Alcance y metas de cumplimiento."
                ],
                [
                    "EDU-E-4",
                    "Obligatoriedad escolar: rangos de edad y duración."
                ],
                [
                    "EDU-E-5",
                    "Normas que regulan el derecho a la gratuidad educativa por nivel de escolaridad."
                ],
                [
                    "EDU-E-6",
                    "Tipo y características de la cobertura: criterios de universalidad, o de focalización o por lógicas de subsidio a la demanda en educación."
                ],
                [
                    "EDU-E-7",
                    "Número, tipo, características de organizaciones de la sociedad civil registradas que participan en la promoción, implementación y la protección del derecho a la educación."
                ]
            ],
            "Procesos": [
                [
                    "EDU-P-1",
                    "- Nivel de desempeño de los estudiantes según el sistema nacional de evaluación de la educación."
                ],
                [
                    "EDU-P-2",
                    "- Tasa de asistencia escolar neta por sexo, grupos de edad, área geográfica, nivel de enseñanza (inicial, primaria, secundaria básica y secundaria orientada), desagregada por sexo, quintiles de ingreso, etnia/raza, urbano rural."
                ],
                [
                    "EDU-P-3",
                    "- Porcentaje de sobreedad por sexo, etnia/raza y área geográfica."
                ],
                [
                    "EDU-P-4",
                    "- Cantidad de días de clase según la norma."
                ],
                [
                    "EDU-P-5",
                    "- Cobertura de programas y acciones concretas en todos los niveles educativos para el acceso y permanencia en el sistema educativo de sectores vulnerables por zona de residencia (urbano/rural)."
                ],
                [
                    "EDU-P-6",
                    "Cobertura de programas destinados a Educación de Primera Infancia y Educación de Jóvenes y Adultos (EDJA) por zona de residencia (urbano/rural)."
                ],
                [
                    "EDU-P-7",
                    "Encuestas y/o estudios sobre el grado de satisfacción de los destinatarios del sistema educativo considerando si el mismo es accesible (cultural, geográfica o económicamente) y se adapta a los requerimientos de la población."
                ],
                [
                    "EDU-P-8",
                    "Encuestas y/o estudios sobre el grado de satisfacción y cobertura de los programas bilingües e interculturales de provisión de educación a pueblos indígenas y afrodescendientes."
                ]
            ],
            "Resultados": [
                [
                    "EDU-R-1",
                    "- Tasa neta de cobertura educativa por niveles de enseñanza (educación primera infancia hasta EDJA)."
                ],
                [
                    "EDU-R-2",
                    "- Tasa de analfabetismo de la población mayor de 15 años de edad, por sexo, etnia, raza, grupos de edad, área geográfica y quintiles de ingreso."
                ],
                [
                    "EDU-R-3",
                    "- Tasa de conclusión de la primaria y secundaria, por sexo, edad, etnia/raza, área geográfica y quintiles de ingreso."
                ],
                [
                    "EDU-R-4",
                    "- Porcentaje de Alumnos con sobreedad y tasa de abandono interanual en el nivel primario."
                ],
                [
                    "EDU-R-5",
                    "Porcentaje de Alumnos con sobreedad y tasa de abandono interanual en el nivel secundario."
                ]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                [
                    "EDU-E-8",
                    "Fuentes de financiamiento del sector educación."
                ],
                [
                    "EDU-E-9",
                    "Leyes y medidas específicas que dispongan formas de financiamiento de la gratuidad de la educación obligatoria"
                ],
                [
                    "EDU-E-10",
                    "Monto y extensión de incentivos, deducción de impuestos (incentivos fiscales) y subsidios para el sector privado de la educación por nivel de instrucción"
                ]
            ],
            "Procesos": [
                [
                    "EDU-P-9",
                    "Porcentaje del Gasto Público Social destinado a educación."
                ],
                [
                    "EDU-P-10",
                    "- Gasto público en educación por niveles educativos (primera infancia, primaria, secundaria, técnica, superior)."
                ],
                [
                    "EDU-P-11",
                    "-Porcentaje de inversión en I+D en la región con respecto al PIB."
                ],
                [
                    "EDU-P-12",
                    "- Gasto por alumno, por niveles de educación, como porcentaje del PIB per cápita."
                ],
                [
                    "EDU-P-13",
                    "- Gasto privado en educación, como porcentaje del PIB."
                ],
                [
                    "EDU-P-14",
                    "-Distribución del Gasto por jurisdicciones (estaduales, locales, provinciales)."
                ],
                [
                    "EDU-P-15",
                    "Porcentaje de docentes sin título específico."
                ],
                [
                    "EDU-P-16",
                    "Avances específicos en el cumplimiento de la gratuidad, universalidad y obligatoriedad y de las metas educativas de los Estados."
                ]
            ],
            "Resultados": [
                [
                    "EDU-R-6",
                    "- Tamaño de la sección de alumnos por docente, según nivel de enseñanza."
                ],
                [
                    "EDU-R-7",
                    "Porcentaje promedio de ingresos del hogar gastados en educación por quintil de ingreso."
                ]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                [
                    "EDU-E-11",
                    "Porcentaje de escuelas que participan en programas de evaluación de contenidos y calidad educativa."
                ],
                [
                    "EDU-E-12",
                    "Participación del sector oficial en la matrícula por nivel educativo (desde Primera Infancia a ecuación superior)."
                ],
                [
                    "EDU-E-13",
                    "Características, montos y gestión de asistencia técnica y financiera internacional en el área de educación."
                ]
            ],
            "Procesos": [
                [
                    "EDU-P-17",
                    "- Oferta de establecimientos educativos públicos de acuerdo a niveles: Primera infancia (de 0 a 6 años); educación básica y media (6 a 17 años) universitarios, educación de jóvenes y adultos. Número de establecimiento y cantidad de vacantes."
                ],
                [
                    "EDU-P-18",
                    "- Porcentaje de establecimientos educativos (en todos los niveles incluyendo el universitario) con bibliotecas según cantidad de libros."
                ],
                [
                    "EDU-P-19",
                    "Tasa de crecimiento anual de las tasas específicas de escolarización por grupos de edad."
                ],
                [
                    "EDU-P-20",
                    "- Existencia de Planes con metas específicas de expansión del acceso a la educación secundaria cuando la misma no es obligatoria."
                ]
            ],
            "Resultados": [
                [
                    "EDU-R-8",
                    "- Nivel medio educativo de la población, por años de escolaridad y desagregado por sexo."
                ],
                [
                    "EDU-R-9",
                    "- Porcentaje de niños de 0 a 6 años que participan en programas educativos."
                ],
                [
                    "EDU-R-10",
                    "- Porcentaje de investigadores de jornada completa, por sexo y zona geográfica."
                ],
                [
                    "EDU-R-11",
                    "Porcentaje de escuelas y de docentes que participa en programas de formación continua y de innovación educativa."
                ],
                [
                    "EDU-R-12",
                    "Porcentaje de jóvenes y adultos que participa en programas de formación y capacitación continua presenciales y a distancia, por sexo y zona geográfica."
                ],
                [
                    "EDU-R-13",
                    "Porcentaje de jóvenes procedentes de la educación técnico-profesional que acceden al empleo al finalizar sus estudios y en puestos afines con su capacitación, por sexo y zona geográfica."
                ]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                [
                    "EDU-E-14",
                    "Existencia de marcos legales y de políticas que garanticen la no discriminación en la educación y una educación no discriminatoria."
                ],
                [
                    "EDU-E-15",
                    "Ley de reconocimiento de la educación bilingüe e intercultural."
                ],
                [
                    "EDU-E-16",
                    "Inclusión de enfoque de género, de derechos humanos y de cultura de pueblos indígenas y afrodescendientes en los contenidos básicos comunes."
                ],
                [
                    "EDU-E-17",
                    "Inclusión de educación sexual obligatoria en los distintos niveles."
                ],
                [
                    "EDU-E-18",
                    "Normas para la inclusión de niños, niñas y adolescentes con capacidades especiales o con capacidades excepcionales."
                ]
            ],
            "Procesos": [
                [
                    "EDU-P-21",
                    "-Porcentaje de familias con dificultades socioeconómicas que reciben apoyo para garantizar la asistencia habitual de sus hijos a las escuelas."
                ],
                [
                    "EDU-P-22",
                    "-Porcentaje de becas a alumnos/as de todos los niveles educativos."
                ],
                [
                    "EDU-P-23",
                    "- Porcentaje de educadores que tienen el título específico de educación inicial."
                ],
                [
                    "EDU-P-24",
                    "- Porcentaje de matrícula de primaria de tiempo completo o doble turno por gestión (pública o privada)."
                ],
                [
                    "EDU-P-25",
                    "- Tiempo semanal dedicado a la educación artística y a la educación física en las escuelas por nivel educativo."
                ],
                [
                    "EDU-P-26",
                    "- Cantidad de computadores en la escuela por alumno para tareas de aprendizaje."
                ],
                [
                    "EDU-P-27",
                    "-Existencia de programas, alcance y cobertura de sostenibilidad del aprendizaje de la cultura escrita."
                ],
                [
                    "EDU-P-28",
                    "- Frecuencia y resultados en la actualización de los contenidos básicos de la educación que incorpore el enfoque de género, étnico, de derechos humanos y ciudadanía en los currículos de las diferentes etapas educativas."
                ]
            ],
            "Resultados": [
                [
                    "EDU-R-14",
                    "- Relación entre el número de niñas y el de niños según nivel de enseñanza, por etnia/raza y área geográfica."
                ],
                [
                    "EDU-R-15",
                    "- Relación entre las tasas de alfabetización de las mujeres y los varones de 15 a 24 años de edad."
                ],
                [
                    "EDU-R-16",
                    "- Porcentaje de niños, niñas y adolescentes pertenecientes a etnias, población indígena, afrodescendiente, campesina escolarizados en la educación inicial, primaria y secundaria básica."
                ],
                [
                    "EDU-R-17",
                    "-Porcentaje de alumnado de minorías étnicas, poblaciones originarias y afrodescendientes que realiza estudios de educación técnico- profesional (ETP) y universitarios."
                ],
                [
                    "EDU-R-18",
                    "-Porcentaje de alumnos con necesidades educativas especiales escolarizados en escuelas regulares del sistema educativo"
                ],
                [
                    "EDU-R-19",
                    "-Porcentaje de alumnos que pertenecen a pueblos originarios que recibe educación bilingüe, por nivel educativo."
                ],
                [
                    "EDU-R-20",
                    "Máximo nivel educativo alcanzado de niños, niñas adolescentes pertenecientes a grupos originarios, afrodescendientes por sexo y por lugar de residencia (urbano/rural)."
                ]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                [
                    "EDU-E-19",
                    "Características, cobertura (territorial y temática), presupuesto y jurisdicción del sistema estadístico en materia educativa."
                ],
                [
                    "EDU-E-20",
                    "Características, cobertura y periodicidad de campañas de difusión del derecho a la educación."
                ],
                [
                    "EDU-E-21",
                    "Características, cobertura y periodicidad de campañas de difusión para la erradicación del analfabetismo."
                ]
            ],
            "Procesos": [
                [
                    "EDU-P-29",
                    "Mecanismos establecidos para la difusión y acceso a las bases de datos y estadísticas educativas."
                ],
                [
                    "EDU-P-30",
                    "-Mecanismos establecidos para la difusión de resultados de calidad educativa y cumplimiento de metas en educación."
                ],
                [
                    "EDU-P-31",
                    "-Número de proyectos presentados y aprobados en los que diferentes sectores sociales participan y que se aplican de forma integrada al diseño de la educación."
                ],
                [
                    "EDU-P-32",
                    "Características y cobertura de los medios que difunden información a las personas de su derecho a la educación en todos los niveles del sistema (educación formal, no formal, primera infancia, EDJA)."
                ]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                [
                    "EDU-E-22",
                    "Existencia de instancias administrativas para radicar denuncias en materia de incumplimiento de obligaciones vinculadas al derecho a la educación"
                ],
                [
                    "EDU-E-23",
                    "Existencia de instancias contenciosas administrativas."
                ],
                [
                    "EDU-E-24",
                    "Existencia de acciones constitucionales (amparos, acciones de protección, tutela)"
                ],
                [
                    "EDU-E-25",
                    "Existencia de servicios jurídicos gratuitos e integrales de protección del derecho a la educación."
                ],
                [
                    "EDU-E-26",
                    "Existencia de oficinas públicas de mediación o conciliación para resolver cuestiones vinculadas con educación."
                ],
                [
                    "EDU-E-27",
                    "Aplicación de garantías procesales en los procedimientos judiciales en materia de educación: i) independencia e imparcialidad del tribunal; ii) plazo razonable; iii) igualdad de armas; iv) cosa juzgada; v) vias recursivas de sentencias en instancias superiores."
                ]
            ],
            "Procesos": [
                [
                    "EDU-P-33",
                    "Número de decisiones judiciales que ha hecho lugar a garantías en educación."
                ],
                [
                    "EDU-P-34",
                    "Número de denuncias relativas al derecho a la educación recibidas, investigadas y resueltas por la instituciones nacionales de derechos humanos y/o educativas competentes en el país."
                ],
                [
                    "EDU-P-35",
                    "- Políticas de capacitación de jueces y abogados en derecho a la educación. Cobertura temática y alcance."
                ],
                [
                    "EDU-P-36",
                    "- Características y cobertura de los medios que difunden información a las personas de sus derechos en relación con la educación."
                ],
                [
                    "EDU-P-37",
                    "- Cobertura de los servicios de traducción en lenguas indígenas."
                ]
            ]
        }
    },
    "Trabajo": {
        "Recepción Del Derecho": {
            "Estructurales": [
                [
                    "TRA-E-1",
                    "Consagración del derecho al trabajo en la Constitución. ¿Cuáles de las siguientes garantías contiene el derecho constitucional del trabajo en el país?: \ni) Condiciones dignas, justas y satisfactorias, ii) Salario mínimo y móvil, iii) Estabilidad en el empleo, iv) Capacitación, v) Seguridad en el trabajo, vi) Promoción del acceso al pleno empleo, vii) No discriminación en el derecho al trabajo de las personas por razones de discapacidad, género, origen étnico u otros; viii) Protección de todo trabajo dañino en la niñez y la adolescencia."
                ],
                [
                    "TRA-E-2",
                    "-Ratificación y entrada en vigor de los convenios fundamentales de la OIT, entre otros: \nConvenio Relativo al Trabajo Forzoso u Obligatorio, 1930 (núm. 29); Convenio Relativo a la Abolición del Trabajo Forzoso, 1957 (núm. 105); Convenio sobre la Edad Mínima de Admisión al Empleo, 1973 (núm. 138); Convenio Sobre la Prohibición de las Peores Formas de Trabajo Infantil y la Acción Inmediata para su Eliminación, 1999 (núm. 182); Convenio Relativo a la Igualdad de Remuneración entre la Mano de Obra Masculina y la Mano de Obra Femenina por un Trabajo de Igual Valor, 1951 (núm. 100); Convenio Relativo a la Discriminación en Materia de Empleo y Ocupación, 1958 (núm. 111)."
                ],
                [
                    "TRA-E-3",
                    "-Convención Interamericana para la eliminación de todas las formas de discriminación contra las personas con discapacidad; Convención Internacional sobre los derechos de las personas con discapacidad; Convención sobre derechos del niño y su Protocolo sobre Venta de niños, prostitución infantil y utilización de niños para la pornografía. Principales instrumentos sistema Interamericano."
                ],
                [
                    "TRA-E-4",
                    "-Tipo de indemnizaciones por despido contempladas (discriminatorio, por razones económicas,) y mecanismos de acceso y cobertura."
                ]
            ],
            "Procesos": [
                [
                    "TRA-P-1",
                    "Existencia de políticas públicas o programas en las siguientes áreas: \n\na) Programas o políticas de eliminación del trabajo forzoso, \nb) Programas o políticas de Eliminación del trabajo infantil, \nc) Programas anti-discriminación por motivos étnicos, de género o por discapacidad en materia laboral; \nd) Programas de regularización de trabajadores migrantes; \ne) Programas encaminados a prevenir y atender accidentes ocupacionales, incluidos lesiones, enfermedades y muerte; \nf) Programas encaminados a prevenir y sancionar el trabajo forzoso, incluidas las formas más graves de trabajo infantil, doméstico, migrantes y trata de personas."
                ],
                [
                    "TRA-P-2",
                    "Existencia de mecanismos tripartitos para fijar acuerdos de normas laborales, planes de empleo, formación profesional, resolución de conflictos."
                ],
                [
                    "TRA-P-3",
                    "Impulso de medidas de acción positiva en materia de género, etnia, raza, personas con discapacidad y adolescentes trabajadores."
                ]
            ],
            "Resultados": [
                [
                    "TRA-R-1",
                    "-Tasa de trabajo Infantil (% de niños, niñas y adolescentes entre 5 y 17 años ocupados sobre la población infantil en ese rango de edad)."
                ],
                [
                    "TRA-R-2",
                    "-Tasa de desempleo desagregado por sexo, edad, nivel educativo"
                ],
                [
                    "TRA-R-3",
                    "-Porcentaje de trabajadores asalariados frente al total de ocupados, desagregado por sexo."
                ],
                [
                    "TRA-R-4",
                    "-Tasa de informalidad (% de los ocupados que no cuentan con un trabajo registrado y no se le aplican descuentos a salud y/o pensiones) desagregado por sexo y edad."
                ],
                [
                    "TRA-R-5",
                    "-Proporción de trabajadores con empleo precario (% de los ocupados que ganan ingresos inferiores al salario mínimo) desagregado por sexo y edad."
                ],
                [
                    "TRA-R-6",
                    "-Proporción de mujeres con empleo remunerado en el sector no agrícola."
                ],
                [
                    "TRA-R-7",
                    "-Proporción de incidencia de accidentes ocupacionales desagregado por sexo y nivel educativo."
                ],
                [
                    "TRA-R-8",
                    "-Porcentaje de mujeres en el funcionariado público, según niveles de jerarquía."
                ],
                [
                    "TRA-R-9",
                    "Tasa de participación de personas con discapacidad desagregada por sexo que se encuentra económicamente activa"
                ]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                [
                    "TRA-E-5",
                    "-% del presupuesto nacional asignado al Ministerio del Trabajo y/o Empleo."
                ],
                [
                    "TRA-E-6",
                    "-% del presupuesto nacional asignado a políticas laborales para sectores en situación de vulnerabilidad (niños, niñas y adolescentes, personas con discapacidad, indígenas, migrantes)."
                ],
                [
                    "TRA-E-7",
                    "Existencia de subsidios o incentivos para la generación de empleo."
                ]
            ],
            "Procesos": [
                [
                    "TRA-P-4",
                    "% de ejecución de los recursos en los programas laborales (% de recursos ejercidos vs % del tiempo transcurrido de duración del programa)"
                ],
                [
                    "TRA-P-5",
                    "% de inversión en programas y políticas de seguridad laboral (medio ambiente de trabajo, salud laboral, etc)."
                ]
            ],
            "Resultados": [
                [
                    "TRA-R-10",
                    "- % de la masa salarial dentro del PIB. Participación de los ingresos del trabajo en la distribución funcional del ingreso (cuentas nacionales)"
                ]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                [
                    "TRA-E-8",
                    "Existencia de un Ministerio de Trabajo y/o Empleo. ¿En qué porcentaje de las regiones/departamentos/estados/locales tienen oficinas?"
                ]
            ],
            "Procesos": [
                [
                    "TRA-P-6",
                    "% de avance en las metas de los programas relacionados con el derecho al trabajo en la Ley de Planeación o Plan de Desarrollo vigente (% de avance vs % del tiempo transcurrido de duración del programa)."
                ],
                [
                    "TRA-P-7",
                    "% de desempleados cubiertos con el seguro al desempleo por sexo y edad"
                ],
                [
                    "TRA-P-8",
                    "Número de inspectores laborales por cada 100.000 trabajadores."
                ],
                [
                    "TRA-P-9",
                    "Número de funcionarios del Ministerio de Trabajo/Población ocupada por sexo y edad."
                ]
            ],
            "Resultados": [
                [
                    "TRA-R-11",
                    "-Empleos creados en los programas del gobierno por año y por sexo."
                ],
                [
                    "TRA-R-12",
                    "- Tiempo promedio de duración en el desempleo (en días y desagregado por edades)."
                ],
                [
                    "TRA-R-13",
                    "-Tasas de desempleo de larga duración (un año o más)."
                ],
                [
                    "TRA-R-14",
                    "-Número de contratos colectivos suscritos anualmente."
                ],
                [
                    "TRA-R-15",
                    "-Trabajadores adolescentes registrados x región, edad, género, origen étnico y discapacidad."
                ]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                [
                    "TRA-E-9",
                    "Existencia de sanciones penales o civiles contra acciones de discriminación laboral en el ordenamiento jurídico."
                ],
                [
                    "TRA-E-10",
                    "- Existencia de mecanismos administrativos o judiciales para enfrentar acoso laboral."
                ],
                [
                    "TRA-E-11",
                    "- Existencia de un recurso judicial adecuado y efectivo para impedir acciones de discriminación laboral."
                ],
                [
                    "TRA-E-12",
                    "- Existencia de cuotas (de género, multiculturales) en cargos públicos o privados u otras acciones afirmativas contempladas en la legislación."
                ],
                [
                    "TRA-E-13",
                    "- Existencia de programas anti- discriminación laboral en los Ministerios con perspectiva poblacional (mujeres, jóvenes, personas adultas mayores) o en los Ministerios con competencias en el tema."
                ],
                [
                    "TRA-E-14",
                    "- Existencia de programas orientados a la conciliación de la vida laboral y familiar, y al reconocimiento del trabajo de cuidado no remunerado."
                ],
                [
                    "TRA-E-15",
                    "Existencia de programas que fomenten la inserción laboral en condiciones dignas de población vulnerable o tradicionalmente discriminada (mujeres, jóvenes, adultos mayores, afrodescendientes, indígenas, LGBTI, habitantes rurales, migrantes, personas con discapacidad, y otros.)"
                ]
            ],
            "Procesos": [
                [
                    "TRA-P-10",
                    "% de casos de discriminación laboral resueltos frente al total de las denuncias interpuestas por sexo y origen étnico."
                ],
                [
                    "TRA-P-11",
                    "% de las entidades públicas que no cumplen con las cuotas de incorporación laboral (por sexo, por grupo etario, etc.) establecidas en la legislación."
                ],
                [
                    "TRA-P-12",
                    "Cobertura de los sistemas de protección social para personas con inserción precaria como porcentaje de la población no afiliada al aseguramiento tradicional (Ej: afiliados a sistemas de pensiones no contributivas) por sexo, edad, origen étnico."
                ]
            ],
            "Resultados": [
                [
                    "TRA-R-16",
                    "Proporción de tasas de participación, desempleo, informalidad, ilegalidad salarial, exceso de horas de trabajo y subempleo para distintos sectores poblacionales (mujeres, jóvenes, personas con discapacidad, grupos étnicos, trabajadores rurales, etc.) en relación con estos mismos indicadores para el caso de la población en general y desagregados por sexo."
                ],
                [
                    "TRA-R-17",
                    "- Crecimiento promedio de los ingresos laborales per cápita del 20% más pobre de la población vs crecimiento promedio del ingreso laboral per cápita en los últimos cinco años (convergencia en los ingresos)."
                ],
                [
                    "TRA-R-18",
                    "% de trabajadoras mujeres cubiertas legalmente por la licencia de maternidad. 4. % de trabajadores varones cubiertos legalmente por la licencia de paternidad. 5. Medición de discriminación salarial entre varones y mujeres por el mismo trabajo"
                ]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                [
                    "TRA-E-16",
                    "- Existe una encuesta de hogares a nivel nacional para monitorear el funcionamiento del mercado laboral. ¿Cuál es su periodicidad?"
                ],
                [
                    "TRA-E-17",
                    "- La encuesta nacional sobre el mercado laboral permite las siguientes desagregaciones con significancia estadística: a. Rural/Urbana, b. Por sexo, c. Por divisiones político-administrativas, d. Por grupos etarios, e. por grupos étnicos, f. Para población con discapacidad, g. Por deciles de ingreso, h. Por actividad económica y i. Por posición ocupacional."
                ],
                [
                    "TRA-E-18",
                    "- Existencia de adecuación de las encuestas a la diversidad cultural y de lenguas y a las personas con discapacidad"
                ],
                [
                    "TRA-E-19",
                    "- Existe un portal virtual público de la entidad que administra las estadísticas a nivel nacional donde se presentan de forma periódica los principales indicadores del mercado laboral."
                ],
                [
                    "TRA-E-20",
                    "Existen mecanismos judiciales para ordenar a una entidad pública a remitir la información cuando se ha negado a hacerlo."
                ]
            ],
            "Procesos": [
                [
                    "TRA-P-13",
                    "Periodicidad con la cual se publican los principales indicadores del mercado laboral: mensual, bimensual, trimestral, semestral, anual., en versiones accesibles a las personas con discapacidad y en las lenguas más utilizadas en el país."
                ],
                [
                    "TRA-P-14",
                    "Solicitudes de información atendidas por la entidad estadística como % del total de solicitudes presentadas en el último año."
                ],
                [
                    "TRA-P-15",
                    "Existencia de protocolos en las entidades públicas para la protección de la confidencialidad de los datos suministrados por los encuestados."
                ]
            ],
            "Resultados": [
                [
                    "TRA-R-19",
                    "Número de usuarios del portal virtual público con información estadística y desagregación de los mismos por regiones, género, edad, discapacidad, migrantes, y otros."
                ]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                [
                    "TRA-E-21",
                    "Jueces pertenecientes a la jurisdicción laboral por cada 10.000 habitantes (desagregado por unidades político administrativas) y por sexo y edad."
                ],
                [
                    "TRA-E-22",
                    "- Existencia de instancias administrativas para presentar denuncias en materia de incumplimiento de obligaciones vinculadas al derecho al trabajo y a las libertades sindicales."
                ],
                [
                    "TRA-E-23",
                    "- Existencia de mecanismos que garanticen el acceso a la justicia laboral para población de escasos recursos económicos., población con discapacidad, de origen étnico, traductores culturales."
                ],
                [
                    "TRA-E-24",
                    "Existencia de mecanismos administrativos y judiciales para atender vulneraciones al derecho individual y colectivo al trabajo"
                ]
            ],
            "Procesos": [
                [
                    "TRA-P-16",
                    "Número de entradas y salidas de causas en la jurisdicción laboral (nivel de resolución)."
                ],
                [
                    "TRA-P-17",
                    "Tiempo promedio de duración de un proceso en la jurisdicción laboral."
                ],
                [
                    "TRA-P-18",
                    "Casos resueltos como porcentaje del total de quejas recibidas en instancias administrativas de atención a vulneración de derechos laborales, por derecho vulnerado."
                ],
                [
                    "TRA-P-19",
                    "Existe una jurisprudencia en los siguientes campos: i) Protección de la estabilidad laboral contra despidos injustificados, ii) Reconocimiento del tipo de contrato que realmente se tiene más allá de las formalidades, iii) Medidas anti- discriminación en el acceso al trabajo por sexo, identidad sexual, grupo etario, pertenencia étnica o por tener VIH, iv) Protección laboral en caso de embarazo, v) Protección laboral para personas con discapacidad, vi) Protección al trabajador contra decisiones arbitrarias del empleador (ej: ius variandi), vii) Condiciones mínimas de bienestar en el trabajo, viii) Ingreso mínimo vital para desempleados o trabajadores en situación de vulnerabilidad."
                ]
            ],
            "Resultados": [
                [
                    "TRA-R-20",
                    "Niveles de vulneración a derechos en materia laboral no atendidos por instancias judiciales o administrativas (% de las víctimas que no acuden a ningún recurso judicial o administrativo)"
                ],
                [
                    "TRA-R-21",
                    "- % de casos de explotación laboral de niños/as que fueron llevados a la justicia y cuántos de estos casos recibieron condena."
                ],
                [
                    "TRA-R-22",
                    "- % de casos de explotación de niños/as para comercio sexual y para pornografía que fueron llevados a la justicia y cuántos de estos casos recibieron condena."
                ],
                [
                    "TRA-R-23",
                    "- % de denuncias recibidas por discriminación laboral de personas con discapacidad, y de mujeres por abuso sexual que recibieron una respuesta judicial o administrativa positiva."
                ]
            ]
        }
    },
    "Derechos Sindicales": {
        "Recepción Del Derecho": {
            "Estructurales": [
                [
                    "SIN-E-1",
                    "nan"
                ],
                [
                    "SIN-E-2",
                    "nan"
                ],
                [
                    "SIN-E-3",
                    "nan"
                ],
                [
                    "SIN-E-4",
                    "nan"
                ],
                [
                    "SIN-E-5",
                    "nan"
                ],
                [
                    "SIN-E-6",
                    "Señales de progreso"
                ]
            ],
            "Procesos": [
                [
                    "SIN-P-1",
                    "Existen Políticas públicas o programas efectuados en los últimos cinco años en los siguientes campos (indicar cuáles): a) Promoción de la sindicalización. b) Promoción de la agremiación empresarial. c) Fortalecimiento de los sindicatos d) Eliminación de prácticas anti- sindicales e) Educación en libertades sindicales y ciudadanía laboral f) Resolución de conflictos laborales g) Monitoreo a la negociación colectiva."
                ],
                [
                    "SIN-P-2",
                    "-Porcentaje de los casos de conflictos labores estudiados en las instancias administrativas existentes que han sido resueltos."
                ],
                [
                    "SIN-P-3",
                    "-Porcentaje de solicitudes de inscripción de sindicatos rechazadas en los últimos cinco años (Especificar razones para rechazo)."
                ],
                [
                    "SIN-P-4",
                    "- Existencia de campañas realizadas por parte del Estado para la promoción de las libertades sindicales en los últimos años."
                ]
            ],
            "Resultados": [
                [
                    "SIN-R-1",
                    "Tasa de sindicalización (trabajadores afiliados a sindicatos/total de ocupados) por sexo y nivel educativo."
                ],
                [
                    "SIN-R-2",
                    "-Cobertura de negociación colectiva (trabajadores cubiertos por algún mecanismo de negociación colectiva/total de ocupados) por sexo y edad."
                ],
                [
                    "SIN-R-3",
                    "-Porcentaje del total de empresas que pertenecen a una organización gremial de empleadores."
                ],
                [
                    "SIN-R-4",
                    "-Número de días no laborados por efecto de huelgas (desagregado por sector económico) para los últimos dos años disponibles."
                ],
                [
                    "SIN-R-5",
                    "-Número de denuncias en los últimos cinco años por hechos sucedidos en el país ante el Comité de Libertad Sindical"
                ]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                [
                    "SIN-E-7",
                    "nan"
                ]
            ],
            "Procesos": [
                [
                    "SIN-P-5",
                    "% de ejecución de los recursos en los programas en materia de protección y promoción de las libertades sindicales (% de ejecución/% del tiempo de duración transcurrido de los programas)."
                ]
            ],
            "Resultados": [
                [
                    "SIN-R-6",
                    "-% de los sindicatos con un número de afiliados \ninferior a 500 (Para medir la estructura sindical del país, si es predominantemente con sindicatos pequeños o grandes)."
                ]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                [
                    "SIN-E-8",
                    "nan"
                ],
                [
                    "SIN-E-9",
                    "nan"
                ],
                [
                    "SIN-E-10",
                    "nan"
                ]
            ],
            "Procesos": [
                [
                    "SIN-P-6",
                    "-% de avance en las metas de los programas relacionados con las libertades sindicales en la Ley de Planeación o Plan de Desarrollo vigente (% de avance vs %del tiempo transcurrido de duración del programa)."
                ],
                [
                    "SIN-P-7",
                    "- Casos resueltos como % del total de casos abordados por tribunales de arbitramiento u otros mecanismos para solucionar disputas sobre negociación colectiva."
                ],
                [
                    "SIN-P-8",
                    "Existencia de una agenda de trabajo o pacto laboral en el marco de las instancias de diálogo social (% de cumplimiento estimado)."
                ]
            ],
            "Resultados": [
                [
                    "SIN-R-7",
                    "-Número de inspectores laborales por cada 100.000 trabajadores."
                ],
                [
                    "SIN-R-8",
                    "- Proporción entre la tasa de sindicalización más alta y la más baja entre entidades territoriales."
                ],
                [
                    "SIN-R-9",
                    "-Número de contratos colectivos suscritos anualmente."
                ],
                [
                    "SIN-R-10",
                    "-Registro de nuevos sindicatos anualmente."
                ],
                [
                    "SIN-R-11",
                    "Número de procesos de negociación colectiva apoyados por el Estado en los últimos cinco años."
                ]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                [
                    "SIN-E-11",
                    "Principio Transversal"
                ],
                [
                    "SIN-E-12",
                    "Principio Transversal"
                ]
            ],
            "Procesos": [
                [
                    "SIN-P-9",
                    "Existencia de mecanismos legales, programas o campañas para garantizar derecho de asociación, huelga y negociación colectiva de trabajadores tercerizados (no vinculados directamente a las empresas)."
                ],
                [
                    "SIN-P-10",
                    "-Existencia de jurisprudencia sobre prácticas anti-sindicales."
                ],
                [
                    "SIN-P-11",
                    "Existencia de programas que fomenten la organización y los espacios de negociación colectiva de población vulnerable o tradicionalmente discriminada (mujeres, jóvenes, adultos mayores, afrodescendientes, indígenas, LGBTI, población con discapacidad, habitantes rurales, migrantes, etc.)"
                ]
            ],
            "Resultados": [
                [
                    "SIN-R-12",
                    "Proporción de tasas sindicalización de distintos grupos poblacionales (mujeres, jóvenes, personas con discapacidad, grupos étnicos, trabajadores rurales, trabajadores tercerizados, etc.) en relación con la tasa de sindicalización general."
                ],
                [
                    "SIN-R-13",
                    "- Cobertura de la negociación colectiva desagregada por grupos poblacionales."
                ],
                [
                    "SIN-R-14",
                    "% de mujeres y jóvenes en la dirigencia sindical"
                ]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                [
                    "SIN-E-13",
                    "Principio Transversal"
                ],
                [
                    "SIN-E-14",
                    "Principio Transversal"
                ],
                [
                    "SIN-E-15",
                    "Principio Transversal"
                ]
            ],
            "Procesos": [
                [
                    "SIN-P-12",
                    "Periodicidad con la cual se publican boletines o información sobre el goce de las libertades sindicales por parte de la población, de manera culturalmente adecuada atendiendo a la diversidad de lenguas y a la población con discapacidad."
                ]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                [
                    "SIN-E-16",
                    "Principio Transversal"
                ],
                [
                    "SIN-E-17",
                    "Principio Transversal"
                ]
            ],
            "Procesos": [
                [
                    "SIN-P-13",
                    "Número de entradas y salidas de causas en la jurisdicción laboral por asuntos relacionados con las libertades sindicales (nivel de resolución)."
                ],
                [
                    "SIN-P-14",
                    "- Tiempo promedio de duración de un proceso en la jurisdicción laboral."
                ],
                [
                    "SIN-P-15",
                    "- Cobertura de la oferta de formación a funcionarios judiciales en derecho laboral colectivo."
                ]
            ]
        }
    },
    "Alimentación": {
        "Recepción Del Derecho": {
            "Estructurales": [
                [
                    "ALI-E-1",
                    "Ratificación por parte del Estado de tratados internacionales de derechos humanos que reconocen, entre otros, el derecho a la alimentación adecuada: a) PIDESC y Protocolo Facultativo; b) CEDAW y Protocolo Facultativo; c) Convención de Derechos del Niño (CDN); d) Convención sobre el estatuto de Refugiados de 1951 y su Protocolo de 1967; e) Convención sobre el Estatuto de los apátridas de 1954; f) Convención Interamericana para la eliminación de todas formas de discriminación contra las personas con discapacidad; g) Convención internacional sobre la protección de todos los trabajadores migrantes y sus familias; h) Declaración de Naciones Unidas sobre los Derechos de los Pueblos Indígenas; i) Directrices Voluntarias FAO de apoyo a la realización progresiva del derecho a una alimentación adecuada en el contexto de seguridad alimentaria nacional; entre otras. \nj) Principales instrumentos sistema interamericano: Declaración Americana de Derechos del Hombre, Convención Americana de Derechos Humanos, Carta Social de la OEA."
                ],
                [
                    "ALI-E-2",
                    "Consagración del derecho a la alimentación adecuada y derechos relacionados en la Constitución y/o legislación nacional."
                ],
                [
                    "ALI-E-3",
                    "Existencia de legislación sobre la aceptabilidad, accesibilidad, adaptabilidad y calidad de los alimentos suministrados en programas públicos de nutrición suplementaria."
                ]
            ],
            "Procesos": [
                [
                    "ALI-P-1",
                    "Existen políticas públicas o programas en las siguientes áreas (Estas áreas miden la manera en que han sido incorporados las principales obligaciones del derecho en la política pública como una forma de evaluar la asimilación de la perspectiva del derecho a la alimentación adecuada en la acción estatal): \na) Erradicación del hambre; \nb) Erradicación de la desnutrición infantil; \nc) Erradicación de la desnutrición materna; \nd) Acceso a consumo mínimo de agua; \ne) Eliminar los ácidos grasos trans en los alimentos y reemplazarlos por ácidos grasos insaturados; \nf) Disminuir el contenido de sodio/sal en los alimentos; \ng) Reducir el contenido de azúcares libres en los alimentos y en las bebidas sin alcohol. \nh) Promoción de la disponibilidad de alimentación saludables en todas las instituciones públicas incluyendo escuelas y otros lugares de trabajo; \ni) Prevención del desabastecimiento alimentario."
                ]
            ],
            "Resultados": [
                [
                    "ALI-R-1",
                    "Tasa de Mortalidad por malnutrición x cada 100,000 habitantes."
                ],
                [
                    "ALI-R-2",
                    "Porcentaje de personas (desagregadas por género, edad, etnia, situación geográfica, estatus socio – económico, situación particular (HIV/SIDA, privados de libertad), que padecen inseguridad alimentaria y nutricional."
                ],
                [
                    "ALI-R-3",
                    "Porcentaje de la población por debajo del nivel mínimo de consumo de energía alimentaria (Indicador ODM)."
                ],
                [
                    "ALI-R-4",
                    "Porcentaje de hogares sin acceso a servicios básicos de saneamiento (ODM)."
                ],
                [
                    "ALI-R-5",
                    "Porcentaje de hogares por debajo de la línea de indigencia o pobreza extrema total, urbana y rural."
                ],
                [
                    "ALI-R-6",
                    "Tasa de desnutrición infantil (niños y niñas menores de 5 años con algún grado de desnutrición)."
                ],
                [
                    "ALI-R-7",
                    "Tasa de desnutrición general (o de deficiencia de micronutrientes)."
                ],
                [
                    "ALI-R-8",
                    "Mujeres gestantes con bajo peso, anemia nutricional \nu obesidad para su edad gestacional."
                ],
                [
                    "ALI-R-9",
                    "Niños(as) de 6 a 59 meses con anemia nutricional."
                ],
                [
                    "ALI-R-10",
                    "Prevalencia de sobrepeso y obesidad en niños y niñas y adultos."
                ],
                [
                    "ALI-R-11",
                    "Prevalencia de diabetes en niños, niñas y adultos."
                ],
                [
                    "ALI-R-12",
                    "Prevalencia de hipertensión arterial en niños, niñas y adultos."
                ]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                [
                    "ALI-E-4",
                    "Existencia en la Constitución de alguna disposición que establezca la prioridad que el Estado tiene en impulsar el desarrollo del sector rural y agropecuario."
                ],
                [
                    "ALI-E-5",
                    "Porcentaje del presupuesto nacional asignado al Ministerio de Agricultura, Desarrollo Rural o quien haga sus veces, y a programas o a políticas alimentarias."
                ]
            ],
            "Procesos": [
                [
                    "ALI-P-2",
                    "Índice de ruralidad en entidades territoriales (% de la población total en zonas rurales vs transferencias per cápita del gobierno para cada entidad territorial en el último año disponible)."
                ]
            ],
            "Resultados": [
                [
                    "ALI-R-13",
                    "Participación del PIB agropecuario en el PIB nacional."
                ]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                [
                    "ALI-E-6",
                    "Existencia de un Ministerio de Agricultura, Desarrollo rural y/o Seguridad Alimentaria ¿En qué porcentaje de las regiones/ departamentos/estados tiene oficinas?"
                ],
                [
                    "ALI-E-7",
                    "Existencia de una autoridad que regule, inspeccione, controle y vigile las actividades de producción, distribución y venta de alimentos."
                ],
                [
                    "ALI-E-8",
                    "Existencia de un censo agropecuario o una encuesta que permita monitorear el comportamiento del sector agropecuario. ¿Cuál es su periodicidad?"
                ],
                [
                    "ALI-E-9",
                    "Existe un programa de salud pública en relación con la calidad de la alimentación y promoción de una alimentación saludable en vinculación con las enfermedades crónicas no transmisibles."
                ],
                [
                    "ALI-E-10",
                    "Existe alguna entidad encargada, una política pública o un programa gubernamental en los siguientes campos (en qué nivel de gobierno –nacional, departamental/estatal, municipal): a) Programas de fomento a la producción campesina; b) Programas de abastecimiento de emergencia en zonas de desastres naturales; c) Programas de asesoría técnica y transferencia tecnológica a productores agropecuarios; d) Investigación agropecuaria; e) Acceso de la población a fuentes hídricas; f) Sustitución de cultivos; g) Control de precios de los alimentos; h) Mitigación del cambio climático sobre agricultura; i) Garantía directa del derecho a la alimentación adecuada."
                ]
            ],
            "Procesos": [
                [
                    "ALI-P-3",
                    "Porcentaje de avance en las metas de los programas relacionados con el derecho a la alimentación en la Ley de Planeación o Plan de Desarrollo vigente (Porcentaje de avance vs porcentaje del tiempo transcurrido de duración del programa)."
                ],
                [
                    "ALI-P-4",
                    "- Porcentaje resultante de la población beneficiada por programas públicos de nutrición suplementaria/Población total con inseguridad alimentaria crónica."
                ],
                [
                    "ALI-P-5",
                    "Existencia de estándares para el uso de pesticidas y agroquímicos por parte de autoridades públicas y empresas privadas. Monitoreo y control. Mecanismos de denuncia."
                ]
            ],
            "Resultados": [
                [
                    "ALI-R-14",
                    "Muerte por intoxicación alimentaria por cada 100,000 muertes."
                ],
                [
                    "ALI-R-15",
                    "Incidencia de casos de intoxicación por ingesta de alimentos."
                ],
                [
                    "ALI-R-16",
                    "Porcentaje de la población cubierta por un programa público de nutrición suplementaria."
                ],
                [
                    "ALI-R-17",
                    "Porcentaje de personas con discapacidad por causas vinculadas con la mala nutrición x región, origen étnico, género y edad."
                ]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                [
                    "ALI-E-11",
                    "Incorpora la Constitución o la legislación el enfoque diferencial (por sexo, pertenencia étnica y grupo etario) en relación con la garantía del derecho a la alimentación adecuada."
                ],
                [
                    "ALI-E-12",
                    "Existencia programas para asegurar el derecho a la alimentación adecuada en los Ministerios con perspectiva poblacional (mujeres, jóvenes, niños, grupos étnicos, adultos mayores) o en los Ministerios con competencias en el tema (agricultura, desarrollo rural)."
                ],
                [
                    "ALI-E-13",
                    "Qué mecanismos constitucionales y legales existen para respetar el uso de la tierra y el territorio por parte de las comunidades étnicas conforme a sus propias prácticas."
                ],
                [
                    "ALI-E-14",
                    "Existen líneas de incentivos fiscales, transferencia de activos o programas de crédito especiales para productores campesinos, mujeres campesinas, grupos étnicos y otras poblaciones que afronten condiciones de exclusión."
                ],
                [
                    "ALI-E-15",
                    "Existencia de políticas destinadas a población rural adolescente y joven con perspectiva de género."
                ]
            ],
            "Procesos": [
                [
                    "ALI-P-6",
                    "Porcentaje de la población total beneficiaria de los programas públicos nutricionales que pertenece a grupos tradicionalmente excluidos/Participación porcentual de esos grupos en la población total."
                ],
                [
                    "ALI-P-7",
                    "Políticas de estímulo a la lactancia materna. Tipo de medidas de alimentación dedicada a mujeres embarazadas y niños en la primera infancia."
                ],
                [
                    "ALI-P-8",
                    "Estudios e indagaciones sobre las estrategias de consumo alimentario de los sectores más vulnerables, atendiendo la diversidad cultural."
                ]
            ],
            "Resultados": [
                [
                    "ALI-R-18",
                    "Tasa de desnutrición para distintos sectores poblacionales (niños, niñas, jóvenes, mujeres, adultos mayores, personas con discapacidad, grupos étnicos)/Tasa de desnutrición global."
                ],
                [
                    "ALI-R-19",
                    "Porcentaje del ingreso corriente que las familias destinan para la compra de alimentos por quintiles/deciles de ingresos."
                ],
                [
                    "ALI-R-20",
                    "Porcentaje del ingreso salarial que las familias destinan a la compra de alimentos por quintiles/deciles."
                ]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                [
                    "ALI-E-16",
                    "Existencia de recursos constitucionales adecuados y efectivos para impedir vulneraciones graves al derecho a la alimentación adecuada."
                ],
                [
                    "ALI-E-17",
                    "Existencia de recursos constitucionales adecuados y efectivos para la protección de la propiedad rural, tanto de la propiedad individual como colectiva."
                ],
                [
                    "ALI-E-18",
                    "Garantizar políticas que incluyan el principio de igualdad y no discriminación en el acceso a la alimentación saludable."
                ]
            ],
            "Procesos": [
                [
                    "ALI-P-9",
                    "Número de entradas y salidas de causas en la jurisdicción agraria (nivel de resolución)"
                ],
                [
                    "ALI-P-10",
                    "Tiempo promedio de duración de un proceso en la jurisdicción agraria."
                ],
                [
                    "ALI-P-11",
                    "Existencia de una jurisprudencia en los siguientes campos: \na) Salario mínimo vital y seguridad alimentaria; b) Accesibilidad económica a una alimentación adecuada, c) Acceso a tierras; d) Derecho al agua."
                ],
                [
                    "ALI-P-12",
                    "Cobertura de los servicios de traducción en lenguas indígenas."
                ]
            ],
            "Resultados": [
                [
                    "ALI-R-21",
                    "Número de conflictos relacionados con el derecho a \nla alimentación adecuada por año."
                ],
                [
                    "ALI-R-22",
                    "Porcentaje de demandas relacionadas con el derecho a la alimentación adecuada presentadas por vía administrativa o ante cortes / Porcentaje de causas resueltas."
                ],
                [
                    "ALI-R-23",
                    "Porcentaje de casos de víctimas que fueron adecuadamente reparadas / total de casos denunciados"
                ]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                [
                    "ALI-E-19",
                    "Existencia de una encuesta nacional que mida las condiciones nutricionales de la población atendiendo la diversidad cultural."
                ],
                [
                    "ALI-E-20",
                    "La encuesta nacional sobre las condiciones nutricionales permite las siguientes desagregaciones con significancia estadística: a. Rural/Urbana, b. Por sexo, c. Por divisiones político-administrativas, d. Por grupos etarios, e. Por grupos étnicos, f. Para población con discapacidad, y g. Por deciles de ingreso."
                ],
                [
                    "ALI-E-21",
                    "Encuesta de consumos de alimentos de la población."
                ],
                [
                    "ALI-E-22",
                    "Existencia de un censo agropecuario que monitoree la dinámica de la producción de distintos sectores."
                ],
                [
                    "ALI-E-23",
                    "Existencia de un portal virtual público de la entidad que administra las estadísticas a nivel nacional donde se presentan de forma periódica los principales resultados de las encuestas en el tema alimentario y nutricional."
                ],
                [
                    "ALI-E-24",
                    "Existencia de un mecanismo de información para que el sector productivo agropecuario conozca las variaciones climáticas y en las condiciones del entorno."
                ],
                [
                    "ALI-E-25",
                    "Existencia de mecanismos públicos de divulgación de precios para el fomento de la competencia en los siguientes medios: i) Prensa; \nii) Televisión; iii) Radio; iv) Internet."
                ],
                [
                    "ALI-E-26",
                    "Existencia de canales de información públicos o privados para la protección al consumidor."
                ],
                [
                    "ALI-E-27",
                    "Existencia de regulaciones para la publicidad que fomenta consumo de alimentos nutricionalmente inadecuados como aquellos ricos en azúcares y grasas."
                ]
            ],
            "Procesos": [
                [
                    "ALI-P-13",
                    "Jornadas pedagógicas realizadas por entidades estatales para el fortalecimiento de las capacidades de interpretación estadística para el público en materia alimentaria."
                ],
                [
                    "ALI-P-14",
                    "Existencia de programas de divulgación y promoción del derecho a la alimentación. Atendiendo la diversidad cultural."
                ],
                [
                    "ALI-P-15",
                    "Número de campañas realizadas por el Estado para propiciar hábitos alimenticios sanos en los últimos cinco años"
                ],
                [
                    "ALI-P-16",
                    "Características de portales de Internet, cobertura televisiva, ventanillas específicas- de la información brindada sobre el derecho a la alimentación adecuada."
                ]
            ],
            "Resultados": [
                [
                    "ALI-R-24",
                    "Programas de educación, información y comunicación para promover una alimentación saludable."
                ]
            ]
        }
    },
    "Medio Ambiente": {
        "Recepción Del Derecho": {
            "Estructurales": [
                [
                    "MAM-E-1",
                    "- Ratificación y entrada en vigor de acuerdos multilaterales sobre medio ambiente como los siguientes (no es exhaustivo): \na) Convenio de Basilea sobre el control de los movimientos transfronterizos de los desechos peligrosos y su eliminación. \nb) Protocolo de Cartagena sobre seguridad en la biotecnología del convenio sobre la diversidad biológica. \nc) Convenio sobre la Diversidad Biológica. \nd) Convención sobre el Comercio Internacional de Especies Amenazadas de Fauna y Flora Silvestres. \ne) Convenio sobre Especies Migratorias. \nf) Convención sobre la Protección del Patrimonio Mundial Cultural y Natural. \ng) Protocolo de Kyoto sobre cambio climático. \nh) Protocolo de Montreal sobre sustancias que agotan la capa de ozono. \ni) Convención de Ramsar sobre los Humedales de Importancia Internacional especialmente como Hábitat de Aves Acuáticas. \nj) Convenio de Rotterdam sobre el Procedimiento de Consentimiento Fundamentado Previo Aplicable a Ciertos Plaguicidas y Productos Químicos Peligrosos Objeto de Comercio Internacional. \ni) Convenio de Estocolmo sobre los Contaminantes Orgánicos Persistentes (COPs). \nk) Convención de las Naciones Unidas de Lucha contra la Desertificación. \nl) Convención de las Naciones Unidas sobre el derecho del mar. \nm) Convención Marco de las Naciones Unidas sobre el Cambio Climático. \nn) Convención 169 de la OIT sobre Pueblos Indígenas y Tribales."
                ],
                [
                    "MAM-E-2",
                    "Consagración en la Constitución del derecho al medio ambiente sano y al acceso a servicios públicos básicos."
                ],
                [
                    "MAM-E-3",
                    "Existencia de una institucionalidad medio ambiental en todos los niveles de gobierno."
                ]
            ],
            "Procesos": [
                [
                    "MAM-P-1",
                    "Existen políticas públicas o programas en las siguientes áreas: \na) Promoción del derecho a un consumo mínimo vital de agua potable; \nb) Saneamiento de recursos hídricos; \nc) Sustitución energética; \nd) Manejo de sustancias dañinas y residuos peligrosos; \ne) Educación ambiental."
                ],
                [
                    "MAM-P-2",
                    "Existencia de una política ambiental aprobada."
                ],
                [
                    "MAM-P-3",
                    "Existe un sistema oficial de indicadores de goce efectivo de los derechos al medio ambiente sano y al acceso a los servicios públicos básicos que sirva para el diseño, seguimiento, evaluación y toma decisiones de política pública."
                ]
            ],
            "Resultados": [
                [
                    "MAM-R-1",
                    "Proporción de la población con acceso sostenible a fuentes mejoradas de abastecimiento de agua, en zonas urbanas y rurales (ODM)."
                ],
                [
                    "MAM-R-2",
                    "Proporción de la población con acceso a métodos de saneamiento adecuados, en zonas urbanas y rurales. (ODM)."
                ],
                [
                    "MAM-R-3",
                    "- Proporción de la superficie cubierta por bosques. (ODM)."
                ],
                [
                    "MAM-R-4",
                    "- % de áreas afectadas por la degradación ambiental."
                ],
                [
                    "MAM-R-5",
                    "- % de áreas afectadas por la desertificación y por erosión del suelo."
                ],
                [
                    "MAM-R-6",
                    "- Relación entre las zonas protegidas para mantener la diversidad biológica y la superficie total. (ODM)"
                ],
                [
                    "MAM-R-7",
                    "- Uso de energía (equivalente en kilogramos de petróleo) por 1 dólar del producto interno bruto (PPA). (ODM)."
                ],
                [
                    "MAM-R-8",
                    "- Emisiones de dióxido de carbono (per cápita) y consumo de clorofluorocarburos que agotan la capa de ozono (toneladas de PAO). (ODM)"
                ],
                [
                    "MAM-R-9",
                    "- Proporción de la población que utiliza combustibles sólidos. (ODM)"
                ],
                [
                    "MAM-R-10",
                    "- Proporción de la población con acceso a cada uno de los SSPPBB."
                ],
                [
                    "MAM-R-11",
                    "- Emisiones de GEI."
                ],
                [
                    "MAM-R-12",
                    "- Niveles de Mortalidad infantil a causa de enfermedad respiratoria aguda."
                ],
                [
                    "MAM-R-13",
                    "- % de Concentración de contaminantes en el aire al que se ve expuesta la población."
                ],
                [
                    "MAM-R-14",
                    "- Número de vehículos automotores en uso por cada 1000 habitantes (UN Statistic División)."
                ],
                [
                    "MAM-R-15",
                    "- % de internaciones hospitalarias por infecciones respiratorias agudas de niños(as) menores de 5 años."
                ],
                [
                    "MAM-R-16",
                    "- % población afectada por enfermedades relacionadas con la falta de acceso a agua potable."
                ]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                [
                    "MAM-E-4",
                    "% del presupuesto nacional asignado al Ministerio del Medio Ambiente y a organismos técnicos encargados del control de las actividades de impacto ambiental."
                ],
                [
                    "MAM-E-5",
                    "- % de los recursos de cooperación internacional destinados al impulso de temas ambientales."
                ],
                [
                    "MAM-E-6",
                    "- Efectividad del Gasto Público medio ambiental."
                ],
                [
                    "MAM-E-7",
                    "Existencia y alcance de subsidios o incentivos tributarios para las empresas que asuman actitudes responsables con el medio ambiente, p. Ej. incentivos para empresas que implementen los mecanismos de eficiencia energética y en el uso de los recursos, o para las que implementen medidas para reducir los riesgos que plantean los productos químicos para la salud y el medio ambiente."
                ],
                [
                    "MAM-E-8",
                    "Existencia de algún mecanismo de estimación del riesgo ecológico en cada sector de actividad económica, para asignar el presupuesto para los programas sectoriales de protección al medio ambiente."
                ],
                [
                    "MAM-E-9",
                    "Existen Fondos financieros públicos/privados como mecanismos de apoyo para la sostenibilidad de las áreas protegidas (UNEP)"
                ]
            ],
            "Procesos": [
                [
                    "MAM-P-4",
                    "% de ejecución de los recursos en los programas en materia de conservación de fuentes hídricas, conservación de recursos energéticos, Protección de la calidad del aire, Conservación de la capa de ozono, Reducción en la producción de residuos contaminantes y manejo de los mismos, Atención al cambio climático, Conservación de los recursos forestales, Promoción del desarrollo sostenible y Conservación de la biodiversidad. (% de recursos vs % del tiempo transcurrido de duración del programa)."
                ],
                [
                    "MAM-P-5",
                    "Tasa de cobertura de los SSPPBB por divisiones político- administrativas vs transferencias per cápita por divisiones político-administrativas para el último año disponible."
                ],
                [
                    "MAM-P-6",
                    "Avance en el cumplimiento de las metas de los subsidios o incentivos para la responsabilidad ambiental."
                ]
            ],
            "Resultados": [
                [
                    "MAM-R-17",
                    "% de ingresos derivados de la explotación de recursos naturales dentro del PIB (cuentas nacionales) y que son distribuidos en diferentes niveles de gobierno."
                ],
                [
                    "MAM-R-18",
                    "- Recursos invertidos en generación de energías limpias / total de recursos invertidos en generación de energías."
                ],
                [
                    "MAM-R-19",
                    "- Valor del consumo en energías limpias / valor total del consumo en energías."
                ]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                [
                    "MAM-E-10",
                    "Existe una encuesta a nivel nacional para monitorear cuál es el impacto de los principales proyectos productivos sobre la vida o salud de las personas. ¿Cuál es su periodicidad?"
                ],
                [
                    "MAM-E-11",
                    "Existen entidades encargadas del análisis técnico de las condiciones medio ambientales."
                ],
                [
                    "MAM-E-12",
                    "- Existe alguna entidad encargada, una política pública o un programa gubernamental en los siguientes campos: a) Evaluación de las condiciones de los recursos hídricos del Estado, b) Evaluación de la calidad del aire, c) Contribución del Estado al daño a la capa de ozono, d) Posibilidades de remplazo de recursos energéticos por las opciones más amigables con el medio ambiente, e) elaboración de mapas de riesgo ambiental, tanto por zonas como por actividades económicas, f) Evaluación de existencia de amenazas a la supervivencia de especies, g) Medición de los niveles de producción de residuos tóxicos y contaminantes, h) conservación de áreas naturales protegidas. En qué nivel de gobierno (nacional, regional, municipal) tienen presencia las entidades que abordan estos temas."
                ],
                [
                    "MAM-E-13",
                    "Existe un sistema de información que registra las vulneraciones al medio ambiente, quiénes causan dichas vulneraciones y qué respuesta dan las autoridades estatales a dichas vulneraciones."
                ]
            ],
            "Procesos": [
                [
                    "MAM-P-7",
                    "Existen políticas públicas o programas en las siguientes áreas: \na. Conservación, calidad y suficiencia de fuentes hídricas. Y de recursos energéticos. \nb. Protección de la calidad del aire. \nc. Condiciones atmosféricas y conservación de la capa de ozono. \nd. Reducción en la producción de residuos contaminantes y manejo de los mismos. \ne. Atención al cambio climático. \nf. Gestión y protección de la calidad del suelo. \ng. Conservación de los recursos forestales. \nh. Conservación de la biodiversidad."
                ],
                [
                    "MAM-P-8",
                    "Existencia de instrumentos de políticas públicas en materia ambiental, tales como planeación ambiental, ordenamiento ecológico del territorio, instrumentos financieros, regulación ambiental de asentamientos humanos, evaluación de impacto ambiental, autorregulación y auditorias."
                ],
                [
                    "MAM-P-9",
                    "Existencia de plan o programa de educación medioambiental para la ciudadanía y los funcionarios públicos (% de cumplimiento estimado)."
                ],
                [
                    "MAM-P-10",
                    "% de intervenciones de los organismos de control de las actividades potencialmente dañinas para el medio ambiente que han sido oportunas en el último año."
                ],
                [
                    "MAM-P-11",
                    "% del territorio nacional sobre el que existen mapas actualizados al último año de riesgo de daño ambiental."
                ],
                [
                    "MAM-P-12",
                    "Existencia de un plan, planes o programa de acción para mitigar el riesgo en las zonas y en las actividades identificadas como potencialmente amenazadas y lesivas (respectivamente) del medio ambiente."
                ],
                [
                    "MAM-P-13",
                    "Existencia de estrategias de conservación de las especies amenazadas."
                ],
                [
                    "MAM-P-14",
                    "Existencia de un plan de reducción de la cantidad de residuos contaminantes producidos."
                ]
            ],
            "Resultados": [
                [
                    "MAM-R-20",
                    "- % de la población que cuenta con el servicio de acueducto en su hogar y lugar de trabajo."
                ],
                [
                    "MAM-R-21",
                    "- % de la población que cuenta con el servicio de energía eléctrica/red de gas en su hogar y trabajo."
                ],
                [
                    "MAM-R-22",
                    "- % de la población que cuenta con el servicio de aseo (recolección de residuos sólidos) en su hogar y trabajo."
                ],
                [
                    "MAM-R-23",
                    "- Generación de residuos sólidos y peligrosos per cápita."
                ],
                [
                    "MAM-R-24",
                    "- Minimización de desechos (tasa de reciclaje)."
                ],
                [
                    "MAM-R-25",
                    "- % de la población con acceso a servicio mejorado."
                ],
                [
                    "MAM-R-26",
                    "% de la población que cuenta con sistemas adecuados de eliminación de excretas (como inodoros o letrinas)."
                ],
                [
                    "MAM-R-27",
                    "- % de la población que vive en zonas de desastres naturales."
                ]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                [
                    "MAM-E-14",
                    "Incorporan la constitución o legislación nacionales enfoques diferenciales por sexo, pertenencia étnica, grupo etario u otros en relación con la garantía del derecho al medio ambiente sano"
                ],
                [
                    "MAM-E-15",
                    "¿Existen mecanismos de reconocimiento de los saberes tradicionales sobre el medio ambiente de los pueblos indígenas, en relación con la protección del mismo?"
                ],
                [
                    "MAM-E-16",
                    "¿Existe un mecanismo jurídico en la legislación nacional que haga operativo el Convenio 169 de la OIT sobre consulta previa?"
                ],
                [
                    "MAM-E-17",
                    "Existencia de políticas destinadas a población rural adolescente y joven con perspectiva de género."
                ]
            ],
            "Procesos": [
                [
                    "MAM-P-15",
                    "% de proyectos productivos adelantados en zonas de asentamiento indígena en los que ha realizado la consulta previa"
                ],
                [
                    "MAM-P-16",
                    "% de las zonas intervenidas por el Estado para mitigar el riesgo ambiental en las que dicha acción ha beneficiado a poblaciones tradicionalmente vulnerables (en especial, indígenas, campesinos, personas de escasos recursos, etc.) frente al total de zonas intervenidas para adoptar acciones de mitigación del riesgo."
                ]
            ],
            "Resultados": [
                [
                    "MAM-R-28",
                    "Proporción de hogares con acceso a cada uno de los SSPPBB de distintos grupos poblacionales (indígenas, población rural y personas en los distintos deciles de ingresos, etc.) frente al total de hogares con acceso a esos mismo servicios."
                ],
                [
                    "MAM-R-29",
                    "Proporción de la población perteneciente a grupos tradicionalmente vulnerables con acceso a servicios de saneamiento mejorados vs. proporción del total de la población con acceso a servicios de saneamiento mejorados."
                ],
                [
                    "MAM-R-30",
                    "% de hogares de distintos grupos poblacionales (indígenas, población rural y personas en los distintos deciles de ingresos, etc.) que viven en zonas de alto riesgo ambiental frente al % del total de hogares que viven en esas mismas zonas."
                ]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                [
                    "MAM-E-18",
                    "Existencia de tribunales administrativos especializados en materia medio ambiental."
                ],
                [
                    "MAM-E-19",
                    "- Jueces pertenecientes a la jurisdicción medioambiental por cada 10.000 habitantes (desagregado por unidades político administrativas)."
                ],
                [
                    "MAM-E-20",
                    "- Número de fiscales especializados en delitos ambientales por número de habitantes."
                ],
                [
                    "MAM-E-21",
                    "- Existencia de recursos constitucionales adecuados y efectivos para impedir vulneraciones graves al medio ambiente (como por ej. el principio de precaución) y exigir el acceso a los SSPPBB."
                ],
                [
                    "MAM-E-22",
                    "Existen mecanismos que garanticen la protección de los recursos naturales, incluso en áreas habitadas por poblaciones de escasos recursos."
                ],
                [
                    "MAM-E-23",
                    "Existen recursos judiciales expeditos, adecuados y efectivos, tales como la imposición de medidas cautelares, que sirvan para suspender el avance de proyectos que amenacen gravemente al medio ambiente."
                ]
            ],
            "Procesos": [
                [
                    "MAM-P-17",
                    "Casos resueltos como porcentaje de quejas recibidas en instancias administrativas o judiciales de atención a vulneración a los derechos al medio ambiente sano y/o al acceso a los SSPPBB."
                ],
                [
                    "MAM-P-18",
                    "Número de entradas y salidas de causas en la jurisdicción medioambiental (nivel de resolución)."
                ],
                [
                    "MAM-P-19",
                    "Número de entradas y salidas de causas relativas al reclamo de acceso a los SSPPBB (nivel de resolución)."
                ],
                [
                    "MAM-P-20",
                    "Número de causas relacionadas a ataques o amenazas a defensores y defensoras del medio ambiente."
                ],
                [
                    "MAM-P-21",
                    "Tiempo promedio de duración de los distintos tipos de procesos en la jurisdicción en cargada de los temas medioambientales."
                ],
                [
                    "MAM-P-22",
                    "Cobertura de la oferta de formación a funcionarios judiciales sobre la relevancia de la protección al medio ambiente y de los defensores y defensoras del medio ambiente."
                ],
                [
                    "MAM-P-23",
                    "¿Existe jurisprudencia que garantice el derecho al medio ambiente sano para poblaciones tradicionalmente excluidas?"
                ]
            ],
            "Resultados": [
                [
                    "MAM-R-31",
                    "Número de acciones de amparo interpuestas solicitando la defensa de un medio ambiente sano."
                ],
                [
                    "MAM-R-32",
                    "Número de denuncias penales por delitos contra el medio ambiente, la seguridad ambiental y en relación a ataques o amenazas a los defensores y defensoras de los de los derechos ambientales."
                ],
                [
                    "MAM-R-33",
                    "Número de denuncias ambientales interpuestas ante instancias administrativas."
                ],
                [
                    "MAM-R-34",
                    "Número de lugares protegidos por intervención judicial."
                ],
                [
                    "MAM-R-35",
                    "Número de sentencias ejecutadas en materia ambiental."
                ],
                [
                    "MAM-R-36",
                    "Número de defensores ambientales bajo protección estatal."
                ],
                [
                    "MAM-R-37",
                    "- Número de recursos presentados y resueltos."
                ]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                [
                    "MAM-E-24",
                    "Se encuentra garantizado en la Constitución y en la legislación el derecho al acceso a la información pública medioambiental sin expresión de causa."
                ],
                [
                    "MAM-E-25",
                    "¿Existe un portal virtual público de la entidad que administra las estadísticas a nivel nacional donde se presentan de forma periódica los indicadores claves sobre protección del medio ambiente?"
                ]
            ],
            "Procesos": [
                [
                    "MAM-P-24",
                    "Periodicidad con la cual se publican los principales indicadores de protección del medio ambiente: mensual, bimensual, trimestral, semestral, anual."
                ],
                [
                    "MAM-P-25",
                    "Existen programas de divulgación y promoción oficial de respeto a los derechos medioambientales y de acceso a servicios públicos básicos."
                ]
            ],
            "Resultados": [
                [
                    "MAM-R-38",
                    "Calificación por parte de los usuarios sobre la oportunidad y calidad de la información recibida de entidades públicas."
                ]
            ]
        }
    },
    "Cultura": {
        "Recepción Del Derecho": {
            "Estructurales": [
                [
                    "CUL-E-1",
                    "Ratificación por parte del Estado de los siguientes instrumentos internacionales, entre otros, que reconocen os derechos culturales: \na) Pacto Internacional de Derechos Económicos, Sociales y culturales. \nb) Ratificación de los instrumentos de la UNESCO (con prioridad la Convención sobre la protección y la promoción de la diversidad de las expresiones culturales, Convención para la salvaguardia del patrimonio cultural inmaterial, Convención sobre la protección del patrimonio mundial cultural y natural). \nc) Convención Internacional sobre la Eliminación de todas las Formas de Discriminación Racial. \nd) Convención sobre la eliminación de todas las formas de discriminación contra la mujer -CEDAW. \ne) Convención sobre los Derechos del Niño. \nf) Convención Internacional sobre la protección de los derechos de todos los trabajadores migratorios y de sus familiares. \ng) Convención sobre los derechos de las personas con discapacidad. \nh) Convenio N. 169 sobre pueblos indígenas y tribales en países independientes. \ni) Declaración del Milenio. \nj) Instrumentos de DDHH de la OEA: Convención Americana DHHH, Carta Social de la OEA;"
                ],
                [
                    "CUL-E-2",
                    "Apoyo público del país a la Declaración de las Naciones Unidas sobre los derechos de los Pueblos Indígenas."
                ],
                [
                    "CUL-E-3",
                    "Consagración en la Constitución, nacional o estaduales, del derecho a la cultura y otros derechos relacionados."
                ],
                [
                    "CUL-E-4",
                    "% de las lenguas del país a las que se han traducido las fuentes normativas del derecho a la cultura."
                ],
                [
                    "CUL-E-5",
                    "Existencia de legislación que protege intereses morales y materiales de los autores de producciones científicas, literarias y artísticas."
                ],
                [
                    "CUL-E-6",
                    "Existencia de legislación que garantice protección y autonomía para las minorías étnicas, regionales (inmigrantes) y culturales."
                ]
            ],
            "Procesos": [
                [
                    "CUL-P-1",
                    "Campañas realizadas por parte del Estado y la sociedad civil para divulgar o promover los derechos culturales en los últimos cinco años."
                ],
                [
                    "CUL-P-2",
                    "Existencia de un Plan Nacional de Cultura."
                ],
                [
                    "CUL-P-3",
                    "Fondos concursables para la sociedad civil que apunten a la protección específica de derechos culturales, particularmente de mujeres, niños, niñas y adolescentes, personas mayores, personas LGBTI, personas con discapacidad, migrantes, pueblos indígenas, personas que viven en la pobreza y todas las minorías."
                ],
                [
                    "CUL-P-4",
                    "Adecuaciones progresivas de acceso, a los espacios culturales para las personas con discapacidad."
                ]
            ],
            "Resultados": [
                [
                    "CUL-R-1",
                    "Tasa de alfabetismo."
                ],
                [
                    "CUL-R-2",
                    "Tasa de alfabetismo en lenguas originarias y de comunidades migrantes más articuladas."
                ],
                [
                    "CUL-R-3",
                    "Museos por cada 100.000 habitantes."
                ],
                [
                    "CUL-R-4",
                    "Bibliotecas por cada 100.000 habitantes."
                ],
                [
                    "CUL-R-5",
                    "Teatros por cada 100.000 habitantes."
                ],
                [
                    "CUL-R-6",
                    "Computadores x cada 1000 habitantes."
                ],
                [
                    "CUL-R-7",
                    "Porcentaje de las personas que tienen acceso a internet."
                ],
                [
                    "CUL-R-8",
                    "Porcentaje de personas que asistieron a presentaciones o espectáculos culturales en el último año."
                ],
                [
                    "CUL-R-9",
                    "Porcentaje de personas que asistieron a espacios culturales o deportivos (parques, museos, etc.) en el último año."
                ],
                [
                    "CUL-R-10",
                    "Estimación del tiempo promedio diario que los habitantes del país destinan al disfrute de la cultura o al consumo de bienes y servicios culturales."
                ],
                [
                    "CUL-R-11",
                    "Número de organizaciones de la sociedad civil por cada 100.000 habitantes."
                ],
                [
                    "CUL-R-12",
                    "Número de facultades de artes/Total de universidades."
                ],
                [
                    "CUL-R-13",
                    "Número de películas producidas anualmente en el país."
                ],
                [
                    "CUL-R-14",
                    "Número de comunidades indígenas, afrodescendientes que mantienen sus tradiciones."
                ],
                [
                    "CUL-R-15",
                    "Porcentaje de publicaciones artísticas y académicas."
                ],
                [
                    "CUL-R-16",
                    "Porcentaje de espacios públicos con agendas culturales."
                ]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                [
                    "CUL-E-7",
                    "Existencia en la Constitución de alguna disposición que establezca la prioridad que el Estado debe concederle al gasto público en los derechos culturales y a la ciencia."
                ],
                [
                    "CUL-E-8",
                    "% del presupuesto nacional asignado al Ministerio de Cultura o quien haga sus veces, por jurisdicción."
                ],
                [
                    "CUL-E-9",
                    "% del presupuesto asignado a los programas públicos relacionados con los derechos culturales en el último año."
                ],
                [
                    "CUL-E-10",
                    "% de recursos asignados al Plan Nacional de Cultura."
                ],
                [
                    "CUL-E-11",
                    "% del presupuesto nacional asignado a los programas de ciencia, tecnología e innovación en el último año."
                ],
                [
                    "CUL-E-12",
                    "Existencia de incentivos fiscales y/o créditos para el desarrollo de los derechos culturales."
                ]
            ],
            "Procesos": [
                [
                    "CUL-P-5",
                    "% de ejecución de los recursos asignados al sector cultura en el Plan Nacional de Desarrollo vigente (% de recursos vs % tiempo transcurrido de duración del Plan)."
                ],
                [
                    "CUL-P-6",
                    "% de ejecución de los recursos asignados a los programas de ciencia, tecnología e innovación en el Plan Nacional de Desarrollo vigente (% de recursos vs % tiempo transcurrido de duración del Plan)."
                ],
                [
                    "CUL-P-7",
                    "% de ejecución de los recursos asignados a los programas de I+D en el Plan Nacional de Desarrollo vigente (% de recursos vs % tiempo transcurrido de duración del Plan)."
                ],
                [
                    "CUL-P-8",
                    "Porcentaje de los recursos totales de cooperación internacional para el desarrollo destinado al sector cultura en los últimos cinco años."
                ],
                [
                    "CUL-P-9",
                    "% de las transferencias del Estado que se destinan a grupos étnicos o culturales minoritarios para la realización de sus derechos culturales."
                ],
                [
                    "CUL-P-10",
                    "Incentivo al sector privado para invertir en la promoción de derechos culturales en el marco de nociones como responsabilidad social empresarial, mecenazgo, etc."
                ]
            ],
            "Resultados": [
                [
                    "CUL-R-17",
                    "Valor total de los bienes y servicios culturales como % del PIB."
                ],
                [
                    "CUL-R-18",
                    "Participación de la ciencia y la tecnología en el PIB."
                ],
                [
                    "CUL-R-19",
                    "Gasto público per cápita en cultura, ciencia, tecnología e I+D en el último año."
                ],
                [
                    "CUL-R-20",
                    "% del gasto de los hogares que se destina al consumo de bienes y servicios culturales."
                ]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                [
                    "CUL-E-13",
                    "Existencia de un Ministerio de Cultura o Sistema Nacional de Cultura o similar. Establecer en qué porcentaje de los estados tiene oficinas/ dependencias."
                ],
                [
                    "CUL-E-14",
                    "Existencia de un inventario de la riqueza cultural intangible, religiones practicadas, lenguas existentes, escuelas de teatro, corrientes cinematográficas, tradiciones de artes plásticas, danzas, ritmos, grupos étnicos y culturales (ej.: tribus urbanas). ¿Cómo se actualiza este inventario?"
                ],
                [
                    "CUL-E-15",
                    "Existencia de un sistema público de divulgación de la oferta cultural. Este sistema contempla estrategias de divulgación en: prensa, radio, internet, televisión, entidades públicas, otros medios?"
                ],
                [
                    "CUL-E-16",
                    "Existencia de una actividad legislativa significativa en relación con el tema cultural (% de los proyectos legislativos presentados que tienen que ver con el tema)."
                ],
                [
                    "CUL-E-17",
                    "Existencia de una encuesta a nivel nacional que permita medir la diversidad cultural y la participación de la población en la cultura (Ej: encuesta de consumo cultural). ¿Cuál es su periodicidad y alcance?"
                ]
            ],
            "Procesos": [
                [
                    "CUL-P-11",
                    "% de avance en las metas de los programas relacionados con los derechos culturales en la Ley de Planeación o Plan de Desarrollo vigente (% de avance vs % del tiempo transcurrido de duración del programa)."
                ],
                [
                    "CUL-P-12",
                    "% de ejecución del gasto de las entidades con competencias en el tema cultural en el último año."
                ],
                [
                    "CUL-P-13",
                    "Cantidad de festivales nacionales y regionales con financiación pública existen en los siguientes ámbitos culturales: a. Música, b. Cine, c. Danzas, d. Artes Plásticas, e. Teatro, f. Televisión y g. Gastronomía. % de las entidades territoriales que tienen sus propios festivales en estos ámbitos."
                ],
                [
                    "CUL-P-14",
                    "Existencia de estrategias para garantizar que exista una comunicación fluida entre el Estado y las distintas minorías étnicas (Ej: la información para acceder a los servicios del Estado está traducida a las lenguas que se hablan en el país, o los servicios están en esas lenguas)."
                ],
                [
                    "CUL-P-15",
                    "% de los funcionarios del sector público que trabaja en el sector cultura."
                ],
                [
                    "CUL-P-16",
                    "% de funcionarios públicos capacitados en derechos culturales."
                ]
            ],
            "Resultados": [
                [
                    "CUL-R-21",
                    "Patentes concedidas al país por cada 100.000 habitantes."
                ],
                [
                    "CUL-R-22",
                    "Películas producidas anualmente en el país."
                ],
                [
                    "CUL-R-23",
                    "Equipamientos culturales x cada 100.000 habitantes."
                ],
                [
                    "CUL-R-24",
                    "% de la población total de minorías étnicas que no cuenta con documento de identidad."
                ],
                [
                    "CUL-R-25",
                    "Crecimiento porcentual de las personas que han acudido a espacios culturales en los últimos cinco años."
                ]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                [
                    "CUL-E-18",
                    "Incorpora la Constitución o la legislación el enfoque diferencial (por sexo, pertenencia étnica, grupo etario, personas con discapacidad) en relación con la garantía del derecho a la cultura."
                ],
                [
                    "CUL-E-19",
                    "Existen programas para asegurar el derecho a la cultura en los Ministerios con perspectiva poblacional (mujeres, jóvenes, niños, grupos étnicos, adultos mayores, etc.) o en los Ministerios con competencias en el tema."
                ],
                [
                    "CUL-E-20",
                    "Existe información sobre el goce del derecho a la cultura desagregada por sexo, zona (rural/urbana), región, grupo étnico, grupo etario y condición socioeconómica."
                ],
                [
                    "CUL-E-21",
                    "Contempla el Plan de Desarrollo o su equivalente, estrategias diferenciales para asegurar el derecho a la cultura de poblaciones tradicionalmente discriminadas."
                ],
                [
                    "CUL-E-22",
                    "Reconocimiento Constitucional o en legislación nacional de formas tradicionales de tenencia de la tierra de pueblos indígenas."
                ]
            ],
            "Procesos": [
                [
                    "CUL-P-17",
                    "% de la población destinataria de los programas públicos de acceso a bienes y servicios culturales/Participación porcentual de personas por pertenencia étnica, edad, sexo, en la población total."
                ],
                [
                    "CUL-P-18",
                    "Existen criterios para una asignación equitativa de bienes y servicios culturales entre regiones, grupos étnicos y grupos culturales en los planes de dotación de equipamientos."
                ],
                [
                    "CUL-P-19",
                    "Procesos de consulta con organizaciones de mujeres, grupos étnicos, grupos religiosos y grupos culturales minoritarios para concertar la política cultural en los últimos cinco años."
                ],
                [
                    "CUL-P-20",
                    "Aplicación de políticas públicas de carácter intercultural en particular en los sistemas de educación básica."
                ],
                [
                    "CUL-P-21",
                    "% de los programas del estado destinados a los grupos culturales o sectores históricamente excluidos."
                ]
            ],
            "Resultados": [
                [
                    "CUL-R-26",
                    "% del ingreso corriente que las familias destinan para el consumo de bienes y servicios culturales por deciles de ingresos, regiones y pertenencia étnica."
                ],
                [
                    "CUL-R-27",
                    "Crecimiento porcentual del ingreso (corriente y disponible –después del gasto en necesidades básicas) en el primer quintil de la población/Crecimiento porcentual del ingreso per cápita."
                ],
                [
                    "CUL-R-28",
                    ". Índice de concentración geográfica (% de la población que tiene cada región vs % de los bienes culturales del país que acapara) de distintos bienes culturales o recreativos: bibliotecas, librerías, teatros, cines, parques, etc."
                ],
                [
                    "CUL-R-29",
                    "Tasa de crecimiento o decrecimiento de la población hablante de lenguas indígenas."
                ],
                [
                    "CUL-R-30",
                    "Representación en los poderes legislativos de los gobiernos nacional y descentralizado de minorías culturales (mujeres, pueblos indígenas, LGBTI, afrodescendientes)."
                ],
                [
                    "CUL-R-31",
                    "Producciones o actividades culturales, artísticas o académicas representativas de los sectores históricamente excluidos."
                ]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                [
                    "CUL-E-23",
                    "Existencia de un sistema de preservación y divulgación del inventario de la riqueza cultural del país."
                ],
                [
                    "CUL-E-24",
                    "Existencia de un portal virtual público de la entidad que administra las estadísticas a nivel nacional donde se presentan de forma periódica los principales resultados de las encuestas de derechos culturales."
                ],
                [
                    "CUL-E-25",
                    "Existen mecanismos públicos de divulgación de la oferta cultural a través de: i) Prensa, ii) Televisión; iii) Radio; iv) Internet con formatos accesibles para las personas con discapacidad y para la población de diversas culturas."
                ],
                [
                    "CUL-E-26",
                    "Existencia de un sistema de información o mecanismos de rendición de cuentas que permitan hacer veeduría ciudadana a la asignación y la ejecución presupuestal de los programas en materia cultural. Asegurar que es accesible la información para las personas con discapacidad (visual, auditiva, intelectual)."
                ]
            ],
            "Procesos": [
                [
                    "CUL-P-22",
                    "% de los funcionarios del sector público que trabajan en la preservación y difusión de la riqueza cultural del país."
                ],
                [
                    "CUL-P-23",
                    "Periodicidad con la que se publican boletines con la oferta cultural en los medios disponibles."
                ],
                [
                    "CUL-P-24",
                    "Jornadas pedagógicas realizadas por entidades estatales para el fortalecimiento de las capacidades de interpretación estadística para el público en materia cultural."
                ]
            ],
            "Resultados": [
                [
                    "CUL-R-32",
                    "Número de instancias de participación, formulación y monitoreo de políticas públicas a nivel nacional, departamental y municipal."
                ],
                [
                    "CUL-R-33",
                    "Número de visitas de los portales virtuales."
                ],
                [
                    "CUL-R-34",
                    "Uso de indicadores culturales por parte de la sociedad civil en sus informes alternativos a los organismos internacionales de monitoreo de los DDHH."
                ],
                [
                    "CUL-R-35",
                    "Número de solicitudes de datos culturales por parte de la población."
                ]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                [
                    "CUL-E-27",
                    "Existencia de recursos jurídicos adecuados para impedir la vulneración a intereses morales y materiales de los autores de las producciones científicas, literarias y artísticas."
                ],
                [
                    "CUL-E-28",
                    "Existencia de mecanismos constitucionales y legales para proteger la diversidad étnica y cultural (y lingüística)"
                ],
                [
                    "CUL-E-29",
                    "El sistema judicial contempla la justicia tradicional de los pueblos indígenas."
                ]
            ],
            "Procesos": [
                [
                    "CUL-P-25",
                    "Casos resueltos/Total de casos abordados en los mecanismos judiciales y administrativos para proteger el derecho a la cultura o para resolver conflictos interculturales."
                ],
                [
                    "CUL-P-26",
                    ". Existencia de una jurisprudencia en los siguientes campos: \ni) Anti-discriminación por motivos culturales en el acceso a derechos sociales y a los programas del Estado o por motivos culturales en el trabajo; \nii) Protección de intereses morales y materiales de autores de producciones culturales y científicas; \niii) Mínimo vital de grupos minoritarios en riesgo; \niv) Límites de la autonomía cultural, \nv) Acceso a bienes culturales, \nvi) Protección de bienes culturales, \nvii) Garantía y protección de la libertad de cultos, a la libertad de expresión, a la protección del libre desarrollo de la personalidad, y a la libertad de cátedra; \nviii) Objeción de conciencia."
                ],
                [
                    "CUL-P-27",
                    "Aplicación de garantías procesales en los procedimientos judiciales en materia de violación a los derechos culturales: \ni) Independencia e imparcialidad del tribunal; \nii) Plazo razonable; \niii) Igualdad de armas; \niv) Cosa juzgada; \nv) Vías recursivas de sentencias en instancias superiores."
                ]
            ],
            "Resultados": [
                [
                    "CUL-R-36",
                    "Reducción porcentual de los episodios de violencia entre grupos religiosos, culturales o étnicos en los últimos cinco años."
                ],
                [
                    "CUL-R-37",
                    "Número de casos que utilizaron la consulta previa el Convenio 169 de la OIT."
                ],
                [
                    "CUL-R-38",
                    "Casos resueltos/Total de casos abordados en los mecanismos judiciales y administrativos para proteger los derechos culturales o para resolver conflictos interculturales."
                ]
            ]
        }
    }
}
