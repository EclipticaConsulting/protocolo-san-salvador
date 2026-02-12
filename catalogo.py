# -*- coding: utf-8 -*-

# --- 1. LISTAS MAESTRAS DE CONFIGURACIÓN ---

LISTA_AGRUPAMIENTOS = [
    "Recepción Del Derecho",
    "Contexto Financiero Básico Y Compromisos Presupuestarios",
    "Capacidades Estatales",
    "Igualdad Y No Discriminación",
    "Acceso A Información Pública Y Participación",
    "Acceso A La Justicia",
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
                ["SS-E-1", "Ratificación de Tratados Internacionales (PIDESC, CEDAW, OIT 102, etc.)."],
                ["SS-E-2", "Incorporación en la Constitución Política del derecho a la seguridad social."],
                ["SS-E-3", "Legislación específica sobre seguridad social (Código SS, Código Trabajo, etc.)."]
            ],
            "Procesos": [
                ["SS-P-1", "Tiempo promedio de reconocimiento del derecho a pensiones o jubilaciones."],
                ["SS-P-2", "Porcentaje de la población asegurada por sistemas contributivos."],
                ["SS-P-3", "Porcentaje de la población cubierta por sistemas no contributivos."],
                ["SS-P-4", "Porcentaje de población afiliada a regímenes especiales."],
                ["SS-P-5", "Porcentaje de adultos mayores de 65 años cubiertos por programas de atención."],
                ["SS-P-6", "Porcentaje de afiliados que perciben como satisfactorio el nivel de cobertura."]
            ],
            "Resultados": [
                ["SS-R-1", "Tasa de población económicamente activa."],
                ["SS-R-2", "Población cubierta por una pensión o jubilación."],
                ["SS-R-3", "Porcentaje de población asegurada a un régimen contributivo."],
                ["SS-R-4", "Número de afiliados cotizantes al sistema de pensiones."],
                ["SS-R-5", "Total de subsidios al desempleo a personas no afiliadas."]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                ["SS-E-4", "Formas de financiamiento del sistema de seguridad social (Estado, Empleador, Trabajador)."],
                ["SS-E-5", "Características y porcentaje de la administración del sistema otorgado a privados."],
                ["SS-E-6", "Origen de los fondos extrapresupuestarios."],
                ["SS-E-7", "Existencia de estimaciones del costo fiscal de las reformas previsionales."],
                ["SS-E-8", "Estudios de reforma de seguridad social con enfoque de género/etnia."]
            ],
            "Procesos": [
                ["SS-P-7", "Porcentaje total de recursos del presupuesto nacional asignados a seguridad social."],
                ["SS-P-8", "Tiempo de licencia por maternidad y paternidad."],
                ["SS-P-9", "Base y frecuencia de actualización de las prestaciones."],
                ["SS-P-10", "Mecanismos para calcular la brecha salarial de género en pensiones."],
                ["SS-P-11", "Mecanismos para eximir costos de litigio."],
                ["SS-P-12", "Disponibilidad de fondos extrapresupuestarios."]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ["SS-E-9", "Jerarquía y facultades de los organismos que gestionan la seguridad social."],
                ["SS-E-10", "Cobertura y alcance de políticas de inclusión de los no afiliados."]
            ],
            "Procesos": [
                ["SS-P-13", "Número de pensiones por invalidez otorgadas."],
                ["SS-P-14", "Total de cotizantes régimen contributivo."],
                ["SS-P-15", "Tasa de cobertura por accidentes de trabajo."],
                ["SS-P-16", "Tasa de desempleo promedio anual."],
                ["SS-P-17", "Tasa de informalidad laboral."],
                ["SS-P-18", "Campañas de formalización del empleo."],
                ["SS-P-19", "Campañas oficiales en prevención de riesgos del trabajo."]
            ],
            "Resultados": [
                ["SS-R-6", "Porcentaje de población sin cobertura en seguridad social."],
                ["SS-R-7", "Porcentaje de la población con cobertura (desagregada)."],
                ["SS-R-8", "Brecha entre cobertura previsional pública y privada."],
                ["SS-R-9", "Tasa de lesiones profesionales (accidentalidad laboral)."]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                ["SS-E-11", "Requisitos de acceso al sistema de seguridad social."],
                ["SS-E-12", "Requisitos para acceso de grupos vulnerables (indígenas, refugiados, etc.)."],
                ["SS-E-13", "Requisitos para el acceso de trabajadoras del servicio doméstico."],
                ["SS-E-14", "Requisitos para el acceso de trabajadores/as rurales."]
            ],
            "Procesos": [
                ["SS-P-20", "Base de cálculo de prestaciones para varones y mujeres."],
                ["SS-P-21", "Uso de tablas actuariales en el cálculo del beneficio."],
                ["SS-P-22", "Extensión y formas de utilización de tablas actuariales."]
            ],
            "Resultados": [
                ["SS-R-10", "Población pensionada (jubilada) desagregada."],
                ["SS-R-11", "Porcentaje de derecho-habientes que perciben pensión."],
                ["SS-R-12", "Porcentaje de migrantes/refugiados con cobertura."],
                ["SS-R-13", "Porcentaje de trabajadores rurales con cobertura."]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                ["SS-E-15", "Características y regularidad en la producción de estadística."],
                ["SS-E-16", "Campañas oficiales de difusión sobre derechos."],
                ["SS-E-17", "Acciones sindicales de difusión de garantías."]
            ],
            "Procesos": [
                ["SS-P-23", "Reglamentación y control de salud ocupacional."],
                ["SS-P-24", "Frecuencia de informes enviados a cotizantes."],
                ["SS-P-25", "Frecuencia de informes (duplicado en protocolo, verificar)."],
                ["SS-P-26", "Características de la información brindada en portales/ventanillas."]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                ["SS-E-18", "Instancias administrativas para radicar denuncias."],
                ["SS-E-19", "Cantidad de acciones constitucionales (amparos) en seguridad social."],
                ["SS-E-20", "Servicios jurídicos gratuitos de protección."],
                ["SS-E-21", "Oficinas públicas de mediación o conciliación."],
                ["SS-E-22", "Aplicación de garantías procesales en procedimientos judiciales."]
            ],
            "Procesos": [
                ["SS-P-27", "Número de denuncias recibidas."],
                ["SS-P-28", "Duración promedio de casos tramitados."],
                ["SS-P-29", "Organismos estatales de control de fondos privados."],
                ["SS-P-30", "Organismos de control (duplicado en protocolo)."],
                ["SS-P-31", "Decisiones judiciales que otorgan cobertura."],
                ["SS-P-32", "Acciones judiciales por denegatoria de pensión no contributiva."],
                ["SS-P-33", "Capacitación de jueces y abogados."],
                ["SS-P-34", "Encuestas de satisfacción de beneficiarios."],
                ["SS-P-35", "Medios de difusión de información sobre derechos."],
                ["SS-P-36", "Cobertura de servicios de traducción en lenguas indígenas."]
            ]
        }
    },
    "Salud": {
        "Recepción Del Derecho": {
            "Estructurales": [
                ["SAL-E-1", "Ratificación de Tratados internacionales (PIDESC, CEDAW, CDN, etc.)."],
                ["SAL-E-2", "Incorporación en la Constitución del derecho a la salud."],
                ["SAL-E-3", "Legislación específica sobre derecho a la salud."],
                ["SAL-E-4", "Organizaciones de la sociedad civil en promoción de salud."],
                ["SAL-E-5", "Reconocimiento de sistemas de salud indígena."]
            ],
            "Procesos": [
                ["SAL-P-1", "Cobertura de programas para sectores vulnerables."],
                ["SAL-P-2", "Disponibilidad de registros vitales (nacimientos, defunciones)."],
                ["SAL-P-3", "Porcentaje de adultos mayores cubiertos."],
                ["SAL-P-4", "Cobertura en salud por tipo (subsidiado/contributivo)."],
                ["SAL-P-5", "Estudios de satisfacción de usuarios."]
            ],
            "Resultados": [
                ["SAL-R-1", "Esperanza de vida al nacer."],
                ["SAL-R-2", "Tasa de mortalidad materna."],
                ["SAL-R-3", "Tasa de mortalidad infantil."],
                ["SAL-R-4", "Tasa de mortalidad por accidentes/homicidios/suicidios."],
                ["SAL-R-5", "Tasa de mortalidad por enfermedades transmisibles."],
                ["SAL-R-6", "Acceso a agua potable."],
                ["SAL-R-7", "Acceso a saneamiento básico."],
                ["SAL-R-8", "Porcentaje de mujeres con anemia."]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                ["SAL-E-6", "Fuentes y porcentajes de financiamiento del sector salud."],
                ["SAL-E-7", "Incentivos y subsidios para el sector privado de salud."],
                ["SAL-E-8", "Incentivos a la industria farmacéutica."],
                ["SAL-E-9", "Relación crecimiento económico vs cobertura."]
            ],
            "Procesos": [
                ["SAL-P-6", "Porcentaje del Gasto Público Social destinado a salud."],
                ["SAL-P-7", "Gasto Público per cápita en salud."],
                ["SAL-P-8", "Gasto familiar en salud (proporción ingreso)."],
                ["SAL-P-9", "Distribución del Gasto por jurisdicciones."],
                ["SAL-P-10", "Recursos para capacitación de RRHH."]
            ],
            "Resultados": [
                ["SAL-R-9", "Gasto de bolsillo en salud por quintil de ingreso."]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ["SAL-E-10", "Incorporación del concepto de atención primaria integral."],
                ["SAL-E-11", "Política nacional sobre medicamentos esenciales."],
                ["SAL-E-12", "Densidad del personal profesional por camas."],
                ["SAL-E-13", "Asistencia técnica y financiera internacional."]
            ],
            "Procesos": [
                ["SAL-P-11", "Accesibilidad geográfica de servicios."],
                ["SAL-P-12", "Acceso a medicamentos esenciales."],
                ["SAL-P-13", "Porcentaje de servicios subcontratados."],
                ["SAL-P-14", "Disparidades público-privadas en gasto."],
                ["SAL-P-15", "Médicos por habitante."],
                ["SAL-P-16", "Enfermeras por habitante."],
                ["SAL-P-17", "Partos atendidos por profesionales."],
                ["SAL-P-18", "Adaptabilidad cultural de servicios."]
            ],
            "Resultados": [
                ["SAL-R-10", "Cobertura de programas de atención primaria."],
                ["SAL-R-11", "Cobertura de asistencia a adultos mayores."],
                ["SAL-R-12", "Tasa de utilización de servicios."],
                ["SAL-R-13", "Cobertura de planes de seguro de salud."]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                ["SAL-E-14", "Regulación del aborto."],
                ["SAL-E-15", "Ley/política para personas con discapacidad."],
                ["SAL-E-16", "Ley/política de salud con enfoque étnico."],
                ["SAL-E-17", "Reconocimiento de derechos sexuales y reproductivos."],
                ["SAL-E-18", "Servicios de salud mental."],
                ["SAL-E-19", "Encuestas sobre percepción de salud reproductiva."]
            ],
            "Procesos": [
                ["SAL-P-19", "Uso de anticonceptivos."],
                ["SAL-P-20", "Estimaciones de abortos inducidos."],
                ["SAL-P-21", "Estimaciones de abortos ilegales."],
                ["SAL-P-22", "Uso de medicina indígena/alternativa."],
                ["SAL-P-23", "Programas de salud sexual y reproductiva."],
                ["SAL-P-24", "Cobertura de programas nutricionales."],
                ["SAL-P-25", "Controles médicos niños/as."],
                ["SAL-P-26", "Controles médicos adolescentes."],
                ["SAL-P-27", "Test de HIV en embarazadas."],
                ["SAL-P-28", "Transmisión vertical de HIV."],
                ["SAL-P-29", "Asistencia prenatal."],
                ["SAL-P-30", "Lactancia materna exclusiva."],
                ["SAL-P-31", "Estudios de percepción sobre ETS."]
            ],
            "Resultados": [
                ["SAL-R-14", "Desnutrición crónica en menores de 5 años."],
                ["SAL-R-15", "Desnutrición global en menores de 5 años."],
                ["SAL-R-16", "Casos de SIDA/VIH por sexo."],
                ["SAL-R-17", "Acceso de personas con discapacidad a servicios."],
                ["SAL-R-18", "Uso de anticonceptivos en adolescentes."],
                ["SAL-R-19", "Uso de anticonceptivos en adultos."],
                ["SAL-R-20", "Tasa de fecundidad no deseada."],
                ["SAL-R-21", "Exámenes ginecológicos periódicos."],
                ["SAL-R-22", "Control prenatal primer trimestre."],
                ["SAL-R-23", "Cobertura de vacunación."]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                ["SAL-E-20", "Sistema estadístico en salud."],
                ["SAL-E-21", "Confidencialidad de información personal."],
                ["SAL-E-22", "Consentimiento informado."],
                ["SAL-E-23", "Campañas de difusión del derecho a la salud."]
            ],
            "Procesos": [
                ["SAL-P-32", "Protocolos de confidencialidad."],
                ["SAL-P-33", "Difusión de salud sexual y reproductiva."],
                ["SAL-P-34", "Asesoramiento sobre transmisión vertical HIV."],
                ["SAL-P-35", "Campañas sobre alcohol, tabaco y drogas."],
                ["SAL-P-36", "Servicios de traducción en salud."],
                ["SAL-P-37", "Medios de difusión de derechos."],
                ["SAL-P-38", "Mecanismos de participación ciudadana."]
            ],
            "Resultados": [
                ["SAL-R-24", "Malformaciones por consumo de sustancias."],
                ["SAL-R-25", "Nacimientos no registrados."]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                ["SAL-E-24", "Instancias administrativas para denuncias."],
                ["SAL-E-25", "Competencias para recibir quejas."],
                ["SAL-E-26", "Acciones constitucionales (amparos)."],
                ["SAL-E-27", "Servicios jurídicos gratuitos."],
                ["SAL-E-28", "Oficinas de mediación."],
                ["SAL-E-29", "Garantías procesales."]
            ],
            "Procesos": [
                ["SAL-P-39", "Decisiones judiciales sobre salud."],
                ["SAL-P-40", "Denuncias ante INDH."],
                ["SAL-P-41", "Capacitación de jueces/abogados."],
                ["SAL-P-42", "Difusión de derechos y traducción."]
            ]
        }
    },
    "Derechos Sindicales": {
        "Recepción Del Derecho": {
            "Estructurales": [
                ["SIN-E-1", "Ratificación de convenios OIT (87, 98, etc.)."],
                ["SIN-E-2", "Reconocimiento constitucional de la libertad sindical."],
                ["SIN-E-3", "Legislación que garantiza el derecho a fundar sindicatos."],
                ["SIN-E-4", "Legislación que garantiza el derecho a la huelga."],
                ["SIN-E-5", "Legislación que garantiza la negociación colectiva."],
                ["SIN-E-6", "Señales de progreso en normativa sindical."]
            ],
            "Procesos": [
                ["SIN-P-1", "Políticas públicas de promoción sindical."],
                ["SIN-P-2", "Porcentaje de conflictos laborales resueltos."],
                ["SIN-P-3", "Solicitudes de inscripción de sindicatos rechazadas."],
                ["SIN-P-4", "Campañas de promoción de libertades sindicales."]
            ],
            "Resultados": [
                ["SIN-R-1", "Tasa de sindicalización."],
                ["SIN-R-2", "Cobertura de negociación colectiva."],
                ["SIN-R-3", "Porcentaje de empresas en gremios."],
                ["SIN-R-4", "Días no laborados por huelgas."],
                ["SIN-R-5", "Denuncias ante el Comité de Libertad Sindical."]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                ["SIN-E-7", "Presupuesto para la protección de la libertad sindical."]
            ],
            "Procesos": [
                ["SIN-P-5", "Ejecución de recursos en programas sindicales."]
            ],
            "Resultados": [
                ["SIN-R-6", "Porcentaje de sindicatos pequeños (<500 afiliados)."]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ["SIN-E-8", "Existencia de organismos de registro sindical."],
                ["SIN-E-9", "Existencia de inspección del trabajo especializada."],
                ["SIN-E-10", "Mecanismos de diálogo social."]
            ],
            "Procesos": [
                ["SIN-P-6", "Avance en metas de programas sindicales."],
                ["SIN-P-7", "Casos resueltos por tribunales de arbitramento."],
                ["SIN-P-8", "Agenda de trabajo en diálogo social."]
            ],
            "Resultados": [
                ["SIN-R-7", "Inspectores laborales por cada 100.000 trabajadores."],
                ["SIN-R-8", "Brecha de sindicalización entre territorios."],
                ["SIN-R-9", "Contratos colectivos suscritos."],
                ["SIN-R-10", "Registro de nuevos sindicatos."],
                ["SIN-R-11", "Procesos de negociación apoyados por el Estado."]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                ["SIN-E-11", "Normativa contra discriminación antisindical."],
                ["SIN-E-12", "Normativa de inclusión en sindicatos."]
            ],
            "Procesos": [
                ["SIN-P-9", "Derechos sindicales de tercerizados."],
                ["SIN-P-10", "Jurisprudencia sobre prácticas antisindicales."],
                ["SIN-P-11", "Programas de fomento para grupos vulnerables."]
            ],
            "Resultados": [
                ["SIN-R-12", "Tasa de sindicalización por grupos poblacionales."],
                ["SIN-R-13", "Cobertura de negociación por grupos."],
                ["SIN-R-14", "Porcentaje de mujeres y jóvenes en dirigencia."]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                ["SIN-E-13", "Sistemas de información sindical."],
                ["SIN-E-14", "Transparencia en el registro sindical."],
                ["SIN-E-15", "Acceso a estatutos sindicales."]
            ],
            "Procesos": [
                ["SIN-P-12", "Publicación de boletines sobre libertades sindicales."]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                ["SIN-E-16", "Recursos judiciales para tutela de libertad sindical."],
                ["SIN-E-17", "Protección contra el despido antisindical."]
            ],
            "Procesos": [
                ["SIN-P-13", "Causas judiciales sobre libertades sindicales."],
                ["SIN-P-14", "Tiempo promedio de procesos."],
                ["SIN-P-15", "Formación judicial en derecho colectivo."]
            ]
        }
    },
    "Trabajo": {
        "Recepción Del Derecho": {
            "Estructurales": [
                ["TRA-E-1", "Consagración constitucional del derecho al trabajo y garantías."],
                ["TRA-E-2", "Ratificación de convenios OIT fundamentales."],
                ["TRA-E-3", "Ratificación de convenciones sobre discriminación y trabajo infantil."],
                ["TRA-E-4", "Tipo de indemnizaciones por despido."]
            ],
            "Procesos": [
                ["TRA-P-1", "Políticas públicas (trabajo forzoso, infantil, discriminación, etc.)."],
                ["TRA-P-2", "Mecanismos tripartitos."],
                ["TRA-P-3", "Medidas de acción positiva."]
            ],
            "Resultados": [
                ["TRA-R-1", "Tasa de trabajo Infantil."],
                ["TRA-R-2", "Tasa de desempleo."],
                ["TRA-R-3", "Porcentaje de trabajadores asalariados."],
                ["TRA-R-4", "Tasa de informalidad."],
                ["TRA-R-5", "Proporción de empleo precario."],
                ["TRA-R-6", "Mujeres en empleo no agrícola."],
                ["TRA-R-7", "Accidentes ocupacionales."],
                ["TRA-R-8", "Mujeres en funcionariado público."],
                ["TRA-R-9", "Participación de personas con discapacidad."]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                ["TRA-E-5", "Presupuesto asignado al Ministerio del Trabajo."],
                ["TRA-E-6", "Presupuesto para sectores vulnerables."],
                ["TRA-E-7", "Subsidios para generación de empleo."]
            ],
            "Procesos": [
                ["TRA-P-4", "Ejecución de recursos en programas laborales."],
                ["TRA-P-5", "Inversión en seguridad laboral."]
            ],
            "Resultados": [
                ["TRA-R-10", "Masa salarial dentro del PIB."]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ["TRA-E-8", "Existencia y cobertura del Ministerio de Trabajo."]
            ],
            "Procesos": [
                ["TRA-P-6", "Avance en metas de programas laborales."],
                ["TRA-P-7", "Cobertura seguro de desempleo."],
                ["TRA-P-8", "Inspectores laborales por 100.000 trabajadores."],
                ["TRA-P-9", "Funcionarios del Ministerio vs Población ocupada."]
            ],
            "Resultados": [
                ["TRA-R-11", "Empleos creados por programas de gobierno."],
                ["TRA-R-12", "Tiempo promedio de desempleo."],
                ["TRA-R-13", "Desempleo de larga duración."],
                ["TRA-R-14", "Contratos colectivos suscritos."],
                ["TRA-R-15", "Trabajadores adolescentes registrados."]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                ["TRA-E-9", "Sanciones contra discriminación laboral."],
                ["TRA-E-10", "Mecanismos contra acoso laboral."],
                ["TRA-E-11", "Recurso judicial contra discriminación."],
                ["TRA-E-12", "Cuotas o acciones afirmativas."],
                ["TRA-E-13", "Programas anti-discriminación."],
                ["TRA-E-14", "Conciliación vida laboral y familiar."],
                ["TRA-E-15", "Programas de inserción para vulnerables."]
            ],
            "Procesos": [
                ["TRA-P-10", "Casos de discriminación resueltos."],
                ["TRA-P-11", "Incumplimiento de cuotas en entidades públicas."],
                ["TRA-P-12", "Cobertura para inserción precaria."]
            ],
            "Resultados": [
                ["TRA-R-16", "Brechas en tasas laborales por grupos."],
                ["TRA-R-17", "Crecimiento ingresos 20% más pobre."],
                ["TRA-R-18", "Cobertura licencias y brecha salarial."]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                ["TRA-E-16", "Encuesta de hogares sobre mercado laboral."],
                ["TRA-E-17", "Desagregación de la encuesta nacional."],
                ["TRA-E-18", "Adecuación cultural de encuestas."],
                ["TRA-E-19", "Portal virtual público de estadísticas."],
                ["TRA-E-20", "Mecanismos para acceso a información."]
            ],
            "Procesos": [
                ["TRA-P-13", "Periodicidad de publicación de indicadores."],
                ["TRA-P-14", "Solicitudes de información atendidas."],
                ["TRA-P-15", "Protocolos de confidencialidad."]
            ],
            "Resultados": [
                ["TRA-R-19", "Usuarios del portal virtual."]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                ["TRA-E-21", "Jueces laborales por habitantes."],
                ["TRA-E-22", "Instancias administrativas para denuncias."],
                ["TRA-E-23", "Acceso a justicia para vulnerables."],
                ["TRA-E-24", "Mecanismos para derechos colectivos."]
            ],
            "Procesos": [
                ["TRA-P-16", "Entradas y salidas de causas laborales."],
                ["TRA-P-17", "Tiempo promedio de procesos laborales."],
                ["TRA-P-18", "Casos resueltos en instancias administrativas."],
                ["TRA-P-19", "Existencia de jurisprudencia clave."]
            ],
            "Resultados": [
                ["TRA-R-20", "Vulneraciones no atendidas."],
                ["TRA-R-21", "Casos de explotación laboral infantil juzgados."],
                ["TRA-R-22", "Casos de explotación sexual infantil juzgados."],
                ["TRA-R-23", "Denuncias por discriminación resueltas."]
            ]
        }
    },
    "Alimentación": {
        "Recepción Del Derecho": {
            "Estructurales": [
                ["ALI-E-1", "Ratificación de Tratados (PIDESC, CEDAW, CDN, etc.)."],
                ["ALI-E-2", "Consagración constitucional del derecho a la alimentación."],
                ["ALI-E-3", "Legislación sobre calidad de alimentos en programas públicos."]
            ],
            "Procesos": [
                ["ALI-P-1", "Políticas públicas (hambre, desnutrición, agua, etc.)."]
            ],
            "Resultados": [
                ["ALI-R-1", "Tasa de Mortalidad por malnutrición."],
                ["ALI-R-2", "Inseguridad alimentaria y nutricional."],
                ["ALI-R-3", "Población bajo nivel mínimo de energía alimentaria."],
                ["ALI-R-4", "Hogares sin saneamiento básico."],
                ["ALI-R-5", "Hogares en indigencia."],
                ["ALI-R-6", "Desnutrición infantil."],
                ["ALI-R-7", "Desnutrición general."],
                ["ALI-R-8", "Mujeres gestantes con bajo peso/anemia."],
                ["ALI-R-9", "Niños con anemia."],
                ["ALI-R-10", "Prevalencia de sobrepeso y obesidad."],
                ["ALI-R-11", "Prevalencia de diabetes."],
                ["ALI-R-12", "Prevalencia de hipertensión arterial."]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                ["ALI-E-4", "Prioridad constitucional al desarrollo rural."],
                ["ALI-E-5", "Presupuesto asignado a Agricultura/Alimentación."]
            ],
            "Procesos": [
                ["ALI-P-2", "Índice de ruralidad vs transferencias."]
            ],
            "Resultados": [
                ["ALI-R-13", "Participación del PIB agropecuario."]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ["ALI-E-6", "Existencia y cobertura del Ministerio de Agricultura."],
                ["ALI-E-7", "Autoridad de control de alimentos."],
                ["ALI-E-8", "Censo agropecuario."],
                ["ALI-E-9", "Programa de alimentación saludable."],
                ["ALI-E-10", "Entidades/programas específicos (fomento, emergencia, técnica)."]
            ],
            "Procesos": [
                ["ALI-P-3", "Avance en metas de programas alimentarios."],
                ["ALI-P-4", "Población beneficiada por programas vs Inseguridad alimentaria."],
                ["ALI-P-5", "Estándares para uso de pesticidas."]
            ],
            "Resultados": [
                ["ALI-R-14", "Muerte por intoxicación alimentaria."],
                ["ALI-R-15", "Incidencia de intoxicación."],
                ["ALI-R-16", "Cobertura de programas de nutrición."],
                ["ALI-R-17", "Discapacidad por mala nutrición."]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                ["ALI-E-11", "Enfoque diferencial en legislación."],
                ["ALI-E-12", "Programas con perspectiva poblacional."],
                ["ALI-E-13", "Uso de tierra por comunidades étnicas."],
                ["ALI-E-14", "Incentivos para productores excluidos."],
                ["ALI-E-15", "Políticas para población rural joven."]
            ],
            "Procesos": [
                ["ALI-P-6", "Población vulnerable en programas vs Total."],
                ["ALI-P-7", "Lactancia y alimentación gestantes."],
                ["ALI-P-8", "Estudios sobre estrategias de consumo."]
            ],
            "Resultados": [
                ["ALI-R-18", "Desnutrición por sectores poblacionales."],
                ["ALI-R-19", "Gasto en alimentos vs Ingreso corriente."],
                ["ALI-R-20", "Gasto en alimentos vs Ingreso salarial."]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                ["ALI-E-16", "Recursos constitucionales por vulneraciones."],
                ["ALI-E-17", "Recursos para protección de propiedad rural."],
                ["ALI-E-18", "Políticas de igualdad en acceso."]
            ],
            "Procesos": [
                ["ALI-P-9", "Causas en jurisdicción agraria."],
                ["ALI-P-10", "Tiempo promedio procesos agrarios."],
                ["ALI-P-11", "Jurisprudencia (salario, tierras, agua)."],
                ["ALI-P-12", "Traducción en lenguas indígenas."]
            ],
            "Resultados": [
                ["ALI-R-21", "Conflictos por alimentación."],
                ["ALI-R-22", "Demandas presentadas vs resueltas."],
                ["ALI-R-23", "Casos reparados."]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                ["ALI-E-19", "Encuesta nutricional diversa."],
                ["ALI-E-20", "Desagregación de encuesta nutricional."],
                ["ALI-E-21", "Encuesta de consumo de alimentos."],
                ["ALI-E-22", "Censo agropecuario (monitoreo)."],
                ["ALI-E-23", "Portal virtual de estadísticas alimentarias."],
                ["ALI-E-24", "Información climática para productores."],
                ["ALI-E-25", "Divulgación de precios."],
                ["ALI-E-26", "Protección al consumidor."],
                ["ALI-E-27", "Regulación de publicidad de alimentos."]
            ],
            "Procesos": [
                ["ALI-P-13", "Jornadas pedagógicas estadísticas."],
                ["ALI-P-14", "Divulgación del derecho a la alimentación."],
                ["ALI-P-15", "Campañas sobre hábitos sanos."],
                ["ALI-P-16", "Características de la información brindada."]
            ],
            "Resultados": [
                ["ALI-R-24", "Programas de promoción saludable."]
            ]
        }
    },
    "Medio Ambiente": {
        "Recepción Del Derecho": {
            "Estructurales": [
                ["MAM-E-1", "Ratificación de acuerdos ambientales (Kyoto, Basilea, etc.)."],
                ["MAM-E-2", "Consagración constitucional del ambiente sano."],
                ["MAM-E-3", "Institucionalidad ambiental."]
            ],
            "Procesos": [
                ["MAM-P-1", "Políticas públicas (agua, energía, residuos)."],
                ["MAM-P-2", "Política ambiental aprobada."],
                ["MAM-P-3", "Sistema oficial de indicadores."]
            ],
            "Resultados": [
                ["MAM-R-1", "Acceso a agua (zonas urbanas/rurales)."],
                ["MAM-R-2", "Acceso a saneamiento (zonas urbanas/rurales)."],
                ["MAM-R-3", "Superficie cubierta por bosques."],
                ["MAM-R-4", "Áreas con degradación ambiental."],
                ["MAM-R-5", "Áreas con desertificación/erosión."],
                ["MAM-R-6", "Zonas protegidas."],
                ["MAM-R-7", "Uso de energía por PIB."],
                ["MAM-R-8", "Emisiones CO2 y CFC."],
                ["MAM-R-9", "Uso de combustibles sólidos."],
                ["MAM-R-10", "Acceso a servicios públicos básicos."],
                ["MAM-R-11", "Emisiones GEI."],
                ["MAM-R-12", "Mortalidad infantil por enfermedad respiratoria."],
                ["MAM-R-13", "Concentración de contaminantes en aire."],
                ["MAM-R-14", "Vehículos por 1000 habitantes."],
                ["MAM-R-15", "Internaciones por IRA en niños."],
                ["MAM-R-16", "Enfermedades por falta de agua potable."]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                ["MAM-E-4", "Presupuesto Ministerio Ambiente."],
                ["MAM-E-5", "Recursos cooperación internacional."],
                ["MAM-E-6", "Efectividad Gasto Público ambiental."],
                ["MAM-E-7", "Incentivos tributarios responsabilidad ambiental."],
                ["MAM-E-8", "Mecanismo estimación riesgo ecológico."],
                ["MAM-E-9", "Fondos para áreas protegidas."]
            ],
            "Procesos": [
                ["MAM-P-4", "Ejecución recursos programas ambientales."],
                ["MAM-P-5", "Cobertura SSPPBB vs transferencias."],
                ["MAM-P-6", "Avance metas incentivos."]
            ],
            "Resultados": [
                ["MAM-R-17", "Ingresos explotación recursos naturales en PIB."],
                ["MAM-R-18", "Inversión en energías limpias."],
                ["MAM-R-19", "Consumo energías limpias."]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ["MAM-E-10", "Encuesta impacto ambiental."],
                ["MAM-E-11", "Entidades de análisis técnico."],
                ["MAM-E-12", "Entidades/políticas específicas (aire, agua, residuos)."],
                ["MAM-E-13", "Sistema de información vulneraciones."]
            ],
            "Procesos": [
                ["MAM-P-7", "Políticas específicas (biodiversidad, clima, etc.)."],
                ["MAM-P-8", "Instrumentos de política (ordenamiento, EIA)."],
                ["MAM-P-9", "Educación ambiental."],
                ["MAM-P-10", "Intervenciones de control oportunas."],
                ["MAM-P-11", "Mapas de riesgo ambiental."],
                ["MAM-P-12", "Planes mitigación riesgo."],
                ["MAM-P-13", "Estrategias conservación especies."],
                ["MAM-P-14", "Plan reducción residuos."]
            ],
            "Resultados": [
                ["MAM-R-20", "Acceso a acueducto."],
                ["MAM-R-21", "Acceso a energía/gas."],
                ["MAM-R-22", "Acceso a aseo."],
                ["MAM-R-23", "Residuos per cápita."],
                ["MAM-R-24", "Tasa de reciclaje."],
                ["MAM-R-25", "Acceso a servicio mejorado."],
                ["MAM-R-26", "Sistemas eliminación excretas."],
                ["MAM-R-27", "Población en zonas de desastre."]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                ["MAM-E-14", "Enfoques diferenciales en legislación."],
                ["MAM-E-15", "Reconocimiento saberes indígenas."],
                ["MAM-E-16", "Mecanismo consulta previa."],
                ["MAM-E-17", "Políticas rurales jóvenes género."]
            ],
            "Procesos": [
                ["MAM-P-15", "Consulta previa en proyectos."],
                ["MAM-P-16", "Mitigación riesgo en poblaciones vulnerables."]
            ],
            "Resultados": [
                ["MAM-R-28", "Acceso SSPPBB grupos vulnerables."],
                ["MAM-R-29", "Saneamiento grupos vulnerables."],
                ["MAM-R-30", "Riesgo ambiental grupos vulnerables."]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                ["MAM-E-18", "Tribunales ambientales."],
                ["MAM-E-19", "Jueces ambientales por habitantes."],
                ["MAM-E-20", "Fiscales ambientales."],
                ["MAM-E-21", "Recursos constitucionales."],
                ["MAM-E-22", "Protección recursos en áreas pobres."],
                ["MAM-E-23", "Medidas cautelares ambientales."]
            ],
            "Procesos": [
                ["MAM-P-17", "Casos resueltos."],
                ["MAM-P-18", "Causas ambientales."],
                ["MAM-P-19", "Causas SSPPBB."],
                ["MAM-P-20", "Ataques a defensores ambientales."],
                ["MAM-P-21", "Tiempo promedio procesos."],
                ["MAM-P-22", "Formación judicial."],
                ["MAM-P-23", "Jurisprudencia poblaciones excluidas."]
            ],
            "Resultados": [
                ["MAM-R-31", "Amparos ambientales."],
                ["MAM-R-32", "Denuncias penales ambientales."],
                ["MAM-R-33", "Denuncias administrativas."],
                ["MAM-R-34", "Lugares protegidos judicialmente."],
                ["MAM-R-35", "Sentencias ejecutadas."],
                ["MAM-R-36", "Defensores protegidos."],
                ["MAM-R-37", "Recursos resueltos."]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                ["MAM-E-24", "Derecho acceso información ambiental."],
                ["MAM-E-25", "Portal estadísticas ambientales."]
            ],
            "Procesos": [
                ["MAM-P-24", "Periodicidad indicadores."],
                ["MAM-P-25", "Programas divulgación."]
            ],
            "Resultados": [
                ["MAM-R-38", "Calidad información pública."]
            ]
        }
    },
    "Cultura": {
        "Recepción Del Derecho": {
            "Estructurales": [
                ["CUL-E-1", "Ratificación tratados culturales (UNESCO, PIDESC)."],
                ["CUL-E-2", "Apoyo Declaración ONU Pueblos Indígenas."],
                ["CUL-E-3", "Consagración constitucional."],
                ["CUL-E-4", "Traducción normas a lenguas."],
                ["CUL-E-5", "Protección derechos de autor."],
                ["CUL-E-6", "Protección minorías."]
            ],
            "Procesos": [
                ["CUL-P-1", "Campañas divulgación."],
                ["CUL-P-2", "Plan Nacional de Cultura."],
                ["CUL-P-3", "Fondos concursables específicos."],
                ["CUL-P-4", "Acceso personas con discapacidad."]
            ],
            "Resultados": [
                ["CUL-R-1", "Tasa de alfabetismo."],
                ["CUL-R-2", "Alfabetismo en lenguas originarias."],
                ["CUL-R-3", "Museos por habitantes."],
                ["CUL-R-4", "Bibliotecas por habitantes."],
                ["CUL-R-5", "Teatros por habitantes."],
                ["CUL-R-6", "Computadores por habitantes."],
                ["CUL-R-7", "Acceso a internet."],
                ["CUL-R-8", "Asistencia a espectáculos."],
                ["CUL-R-9", "Asistencia a espacios culturales."],
                ["CUL-R-10", "Tiempo destinado a cultura."],
                ["CUL-R-11", "Organizaciones sociedad civil."],
                ["CUL-R-12", "Facultades de artes."],
                ["CUL-R-13", "Películas producidas."],
                ["CUL-R-14", "Comunidades tradicionales."],
                ["CUL-R-15", "Publicaciones."],
                ["CUL-R-16", "Espacios públicos con agenda."]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                ["CUL-E-7", "Prioridad constitucional gasto cultura/ciencia."],
                ["CUL-E-8", "Presupuesto Ministerio Cultura."],
                ["CUL-E-9", "Presupuesto programas culturales."],
                ["CUL-E-10", "Recursos Plan Nacional Cultura."],
                ["CUL-E-11", "Presupuesto ciencia y tecnología."],
                ["CUL-E-12", "Incentivos fiscales."]
            ],
            "Procesos": [
                ["CUL-P-5", "Ejecución recursos cultura."],
                ["CUL-P-6", "Ejecución recursos ciencia/tecnología."],
                ["CUL-P-7", "Ejecución recursos I+D."],
                ["CUL-P-8", "Cooperación internacional cultura."],
                ["CUL-P-9", "Transferencias a grupos minoritarios."],
                ["CUL-P-10", "Incentivo sector privado."]
            ],
            "Resultados": [
                ["CUL-R-17", "Valor bienes culturales en PIB."],
                ["CUL-R-18", "Participación ciencia/tecnología en PIB."],
                ["CUL-R-19", "Gasto público per cápita."],
                ["CUL-R-20", "Gasto hogares en cultura."]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ["CUL-E-13", "Ministerio de Cultura."],
                ["CUL-E-14", "Inventario riqueza cultural."],
                ["CUL-E-15", "Sistema divulgación oferta."],
                ["CUL-E-16", "Actividad legislativa cultural."],
                ["CUL-E-17", "Encuesta consumo cultural."]
            ],
            "Procesos": [
                ["CUL-P-11", "Avance metas programas culturales."],
                ["CUL-P-12", "Ejecución gasto entidades culturales."],
                ["CUL-P-13", "Festivales nacionales/regionales."],
                ["CUL-P-14", "Comunicación con minorías."],
                ["CUL-P-15", "Funcionarios en cultura."],
                ["CUL-P-16", "Capacitación funcionarios."]
            ],
            "Resultados": [
                ["CUL-R-21", "Patentes concedidas."],
                ["CUL-R-22", "Películas producidas."],
                ["CUL-R-23", "Equipamientos culturales."],
                ["CUL-R-24", "Minorías sin documento identidad."],
                ["CUL-R-25", "Crecimiento asistencia cultural."]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                ["CUL-E-18", "Enfoque diferencial legislación."],
                ["CUL-E-19", "Programas perspectiva poblacional."],
                ["CUL-E-20", "Información desagregada."],
                ["CUL-E-21", "Estrategias poblaciones discriminadas."],
                ["CUL-E-22", "Tenencia tierra indígena."]
            ],
            "Procesos": [
                ["CUL-P-17", "Población beneficiaria vs total."],
                ["CUL-P-18", "Criterios equidad asignación."],
                ["CUL-P-19", "Consultas concertación política."],
                ["CUL-P-20", "Políticas interculturales educación."],
                ["CUL-P-21", "Programas grupos excluidos."]
            ],
            "Resultados": [
                ["CUL-R-26", "Gasto hogares cultura por grupos."],
                ["CUL-R-27", "Crecimiento ingreso quintil 1."],
                ["CUL-R-28", "Concentración geográfica bienes."],
                ["CUL-R-29", "Población hablante lenguas indígenas."],
                ["CUL-R-30", "Representación minorías legislativo."],
                ["CUL-R-31", "Producciones sectores excluidos."]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                ["CUL-E-23", "Sistema preservación inventario."],
                ["CUL-E-24", "Portal estadísticas culturales."],
                ["CUL-E-25", "Mecanismos divulgación oferta."],
                ["CUL-E-26", "Sistema rendición cuentas."]
            ],
            "Procesos": [
                ["CUL-P-22", "Funcionarios preservación."],
                ["CUL-P-23", "Periodicidad boletines."],
                ["CUL-P-24", "Jornadas pedagógicas."]
            ],
            "Resultados": [
                ["CUL-R-32", "Instancias participación."],
                ["CUL-R-33", "Visitas portales."],
                ["CUL-R-34", "Uso indicadores sociedad civil."],
                ["CUL-R-35", "Solicitudes datos."]
            ]
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                ["CUL-E-27", "Recursos jurídicos derechos autor."],
                ["CUL-E-28", "Mecanismos diversidad."],
                ["CUL-E-29", "Justicia tradicional indígena."]
            ],
            "Procesos": [
                ["CUL-P-25", "Casos resueltos."],
                ["CUL-P-26", "Jurisprudencia cultural."],
                ["CUL-P-27", "Garantías procesales."]
            ],
            "Resultados": [
                ["CUL-R-36", "Reducción violencia intergrupal."],
                ["CUL-R-37", "Casos consulta previa."],
                ["CUL-R-38", "Casos resueltos."]
            ]
        }
    },
    "Educación": {
        "Recepción Del Derecho": {
            "Estructurales": [
                ["EDU-E-1", "Ratificación de instrumentos educativos"],
                ["EDU-E-2", "Gratuidad de la educación primaria"],
                ["EDU-E-3", "Legislación específica y/o planes de desarrollo educativo"],
                ["EDU-E-4", "Obligatoriedad escolar"],
                ["EDU-E-5", "Normas que regulan la gratuidad educativa"],
                ["EDU-E-6", "Tipo y características de la cobertura"],
                ["EDU-E-7", "Organizaciones de la sociedad civil en educación"]
            ],
            "Procesos": [
                ["EDU-P-1", "Tasa de matrícula escolar"],
                ["EDU-P-2", "Tasa de deserción escolar"],
                ["EDU-P-3", "Porcentaje de sobreedad"],
                ["EDU-P-4", "Cantidad de días de clase"],
                ["EDU-P-5", "Cobertura de programas para sectores vulnerables"],
                ["EDU-P-6", "Cobertura Primera Infancia y EDJA"],
                ["EDU-P-7", "Encuestas de satisfacción"],
                ["EDU-P-8", "Encuestas programas bilingües"]
            ],
            "Resultados": [
                ["EDU-R-1", "Tasa de alfabetización"],
                ["EDU-R-2", "Años promedio de escolaridad"],
                ["EDU-R-3", "Tasa de conclusión primaria/secundaria"],
                ["EDU-R-4", "Sobreedad/abandono primario"],
                ["EDU-R-5", "Sobreedad/abandono secundario"]
            ]
        },
        "Contexto Financiero Básico Y Compromisos Presupuestarios": {
            "Estructurales": [
                ["EDU-E-8", "Fuentes de financiamiento"],
                ["EDU-E-9", "Leyes financiamiento gratuidad"],
                ["EDU-E-10", "Incentivos sector privado"]
            ],
            "Procesos": [
                ["EDU-P-9", "Porcentaje GPS educación"],
                ["EDU-P-10", "Gasto público por niveles"],
                ["EDU-P-11", "Inversión I+D"],
                ["EDU-P-12", "Gasto por alumno"],
                ["EDU-P-13", "Gasto privado educación"],
                ["EDU-P-14", "Distribución gasto jurisdicciones"],
                ["EDU-P-15", "Docentes sin título"],
                ["EDU-P-16", "Avances gratuidad/universalidad"]
            ],
            "Resultados": [
                ["EDU-R-6", "Alumnos por docente"],
                ["EDU-R-7", "Gasto hogar educación"]
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ["EDU-E-11", "Evaluación calidad educativa"],
                ["EDU-E-12", "Participación sector oficial"],
                ["EDU-E-13", "Cooperación internacional"]
            ],
            "Procesos": [
                ["EDU-P-17", "Oferta establecimientos"],
                ["EDU-P-18", "Bibliotecas escolares"],
                ["EDU-P-19", "Crecimiento escolarización"],
                ["EDU-P-20", "Planes expansión secundaria"]
            ],
            "Resultados": [
                ["EDU-R-8", "Nivel medio educativo"],
                ["EDU-R-9", "Participación 0-6 años"],
                ["EDU-R-10", "Investigadores jornada completa"],
                ["EDU-R-11", "Formación docente continua"],
                ["EDU-R-12", "Capacitación jóvenes/adultos"],
                ["EDU-R-13", "Empleo egresados técnicos"]
            ]
        },
        "Igualdad Y No Discriminación": {
            "Estructurales": [
                ["EDU-E-14", "Marcos legales no discriminación"],
                ["EDU-E-15", "Educación bilingüe intercultural"],
                ["EDU-E-16", "Enfoque género/DDHH currículo"],
                ["EDU-E-17", "Educación sexual"],
                ["EDU-E-18", "Inclusión capacidades especiales"]
            ],
            "Procesos": [
                ["EDU-P-21", "Apoyo familias vulnerables"],
                ["EDU-P-22", "Becas"],
                ["EDU-P-23", "Título educación inicial"],
                ["EDU-P-24", "Matrícula tiempo completo"],
                ["EDU-P-25", "Tiempo educación artística/física"],
                ["EDU-P-26", "Computadores por alumno"],
                ["EDU-P-27", "Cultura escrita"],
                ["EDU-P-28", "Actualización contenidos"]
            ],
            "Resultados": [
                ["EDU-R-14", "Relación niñas/niños"],
                ["EDU-R-15", "Alfabetización mujeres/varones"],
                ["EDU-R-16", "Escolarización minorías"],
                ["EDU-R-17", "Minorías en superior/técnico"],
                ["EDU-R-18", "Necesidades especiales integrados"],
                ["EDU-R-19", "Educación bilingüe pueblos originarios"],
                ["EDU-R-20", "Nivel educativo minorías"]
            ]
        },
        "Acceso A Información Pública Y Participación": {
            "Estructurales": [
                ["EDU-E-19", "Sistema estadístico educativo"],
                ["EDU-E-20", "Campañas difusión derecho"],
                ["EDU-E-21", "Campañas alfabetización"]
            ],
            "Procesos": [
                ["EDU-P-29", "Difusión estadísticas"],
                ["EDU-P-30", "Difusión calidad/metas"],
                ["EDU-P-31", "Proyectos participativos"],
                ["EDU-P-32", "Medios difusión derecho"]
            ],
            "Resultados": []
        },
        "Acceso A La Justicia": {
            "Estructurales": [
                ["EDU-E-22", "Instancias administrativas denuncias"],
                ["EDU-E-23", "Instancias contenciosas"],
                ["EDU-E-24", "Acciones constitucionales"],
                ["EDU-E-25", "Servicios jurídicos gratuitos"],
                ["EDU-E-26", "Oficinas mediación"],
                ["EDU-E-27", "Garantías procesales"]
            ],
            "Procesos": [
                ["EDU-P-33", "Decisiones judiciales garantías"],
                ["EDU-P-34", "Denuncias ante INDH"],
                ["EDU-P-35", "Capacitación jueces/abogados"],
                ["EDU-P-36", "Medios difusión derechos"],
                ["EDU-P-37", "Traducción lenguas indígenas"]
            ],
            "Resultados": []
        }
    }
}