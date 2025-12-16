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

# --- 2. CATÁLOGO MAESTRO DE INDICADORES (EXPANDIDO) ---

CATALOGO_INDICADORES = {
    
    # ==============================================================================
    # 1. DERECHO A LA SEGURIDAD SOCIAL
    # ==============================================================================
    "Seguridad Social": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("001", "Ratificación del Pacto Internacional de Derechos Económicos, Sociales y Culturales (PIDESC)"),
                ("002", "Ratificación del Protocolo de San Salvador"),
                ("003", "Ratificación del Convenio 102 de la OIT (Norma mínima de Seguridad Social)"),
                ("004", "Ratificación de la CEDAW"),
                ("005", "Ratificación de la Convención sobre el Estatuto de los Refugiados"),
                ("006", "Incorporación explícita en la Constitución del derecho a la seguridad social"),
                ("007", "Existencia de Código de Seguridad Social o Ley Marco"),
                ("008", "Reconocimiento normativo de pensiones contributivas"),
                ("009", "Reconocimiento normativo de pensiones no contributivas")
            ],
            "Procesos": [
                ("010", "Tiempo promedio de reconocimiento del derecho a pensiones"),
                ("011", "Porcentaje de la población asegurada por sistemas contributivos"),
                ("012", "Porcentaje de la población cubierta por sistemas no contributivos"),
                ("013", "Porcentaje de población afiliada a regímenes especiales"),
                ("014", "Cobertura de programas de atención a la vejez (>65 años)")
            ],
            "Resultados": [
                ("015", "Tasa de población económicamente activa (PEA) con cobertura"),
                ("016", "Población cubierta por jubilación (desagregado)"),
                ("017", "Número de afiliados cotizantes activos"),
                ("018", "Total de subsidios al desempleo otorgados"),
                ("019", "Nivel de satisfacción de usuarios con la cobertura")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("020", "Definición legal de fuentes de financiamiento (Aportes/Impuestos)"),
                ("021", "Normativa sobre administración privada de fondos (AFPs/Otros)"),
                ("022", "Normativa sobre uso de fondos de reserva")
            ],
            "Procesos": [
                ("023", "% del Presupuesto Nacional asignado a Seguridad Social"),
                ("024", "Sostenibilidad financiera del sistema (Ingresos vs Egresos)"),
                ("025", "Frecuencia de actualización de montos de pensiones")
            ],
            "Resultados": [
                ("026", "Déficit/Superávit del sistema previsional"),
                ("027", "Costo fiscal de reformas previsionales")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("028", "Existencia de entidad rectora de Seguridad Social"),
                ("029", "Autonomía administrativa de la entidad rectora")
            ],
            "Procesos": [
                ("030", "Número de pensiones de invalidez otorgadas"),
                ("031", "Eficiencia en la recaudación de cotizaciones"),
                ("032", "Tasa de cobertura efectiva de riesgos laborales")
            ],
            "Resultados": [
                ("033", "Tasa de informalidad laboral (sin cobertura SS)"),
                ("034", "Población excluida del sistema de seguridad social"),
                ("035", "Tasa de siniestralidad laboral")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("036", "Normativa de inclusión para trabajadores domésticos"),
                ("037", "Normativa de inclusión para trabajadores rurales"),
                ("038", "Reconocimiento del trabajo de cuidado no remunerado en el sistema"),
                ("039", "Edad de jubilación diferenciada o igualitaria por género")
            ],
            "Resultados": [
                ("040", "Brecha de cobertura pensional entre hombres y mujeres"),
                ("041", "Cobertura de seguridad social en población indígena"),
                ("042", "Cobertura de seguridad social en población migrante")
            ]
        },
        "Acceso a Información Pública y Participación": {
            "Estructurales": [
                ("043", "Existencia de sistema estadístico de seguridad social"),
                ("044", "Publicación periódica de balances actuariales")
            ],
            "Resultados": [
                ("045", "Campañas de información sobre derechos pensionales")
            ]
        },
        "Acceso a la Justicia": {
            "Estructurales": [
                ("046", "Mecanismos administrativos de reclamo"),
                ("047", "Gratuidad en litigios de seguridad social")
            ],
            "Resultados": [
                ("048", "Número de amparos/tutelas por negación de pensión"),
                ("049", "Sentencias favorables en materia previsional")
            ]
        }
    },

    # ==============================================================================
    # 2. DERECHO A LA SALUD (EXPANDIDO)
    # ==============================================================================
    "Salud": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("060", "Ratificación PIDESC (Salud)"),
                ("061", "Ratificación Convención Derechos del Niño (Salud)"),
                ("062", "Consagración constitucional del derecho a la salud"),
                ("063", "Ley General o Marco de Salud"),
                ("064", "Existencia de Plan Nacional de Salud vigente")
            ],
            "Procesos": [
                ("065", "Cobertura de programas de vacunación"),
                ("066", "Cobertura de atención prenatal"),
                ("067", "Porcentaje de partos institucionales"),
                ("068", "Disponibilidad de medicamentos esenciales")
            ],
            "Resultados": [
                ("069", "Tasa de mortalidad materna"),
                ("070", "Tasa de mortalidad infantil"),
                ("071", "Tasa de mortalidad neonatal"),
                ("072", "Esperanza de vida al nacer"),
                ("073", "Tasa de incidencia de VIH/SIDA"),
                ("074", "Tasa de incidencia de Tuberculosis"),
                ("075", "Tasa de incidencia de Malaria/Dengue"),
                ("076", "% Acceso a agua potable"),
                ("077", "% Acceso a saneamiento básico")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Procesos": [
                ("078", "Gasto público en salud como % del PIB"),
                ("079", "Gasto público en salud como % del Gasto Total"),
                ("080", "Gasto de bolsillo en salud de los hogares")
            ],
            "Resultados": [
                ("081", "Distribución equitativa del presupuesto de salud por regiones")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("082", "Existencia de sistema de atención primaria en salud (APS)"),
                ("083", "Política de medicamentos genéricos")
            ],
            "Procesos": [
                ("084", "Camas hospitalarias por 1.000 habitantes"),
                ("085", "Médicos por 10.000 habitantes"),
                ("086", "Enfermeras por 10.000 habitantes"),
                ("087", "Centros de salud nivel 1 por habitantes")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("088", "Legislación sobre salud sexual y reproductiva"),
                ("089", "Legislación sobre salud intercultural"),
                ("090", "Protocolos de atención para personas con discapacidad"),
                ("091", "Marco legal sobre interrupción del embarazo")
            ],
            "Resultados": [
                ("092", "Uso de anticonceptivos modernos"),
                ("093", "Necesidad insatisfecha de planificación familiar"),
                ("094", "Embarazo adolescente (Tasa)")
            ]
        },
        "Acceso a la Justicia": {
            "Resultados": [
                ("095", "Tutelas/Amparos por falta de medicamentos"),
                ("096", "Denuncias por mala praxis médica")
            ]
        }
    },

    # ==============================================================================
    # 3. DERECHO A LA EDUCACIÓN (EXPANDIDO)
    # ==============================================================================
    "Educación": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("100", "Ratificación Convención contra Discriminación en la Enseñanza"),
                ("101", "Garantía constitucional de gratuidad (Primaria)"),
                ("102", "Garantía constitucional de gratuidad (Secundaria)"),
                ("103", "Garantía constitucional de gratuidad (Universitaria)"),
                ("104", "Obligatoriedad escolar (Años)")
            ],
            "Procesos": [
                ("105", "Tasa de matrícula neta en primaria"),
                ("106", "Tasa de matrícula neta en secundaria"),
                ("107", "Tasa de asistencia escolar")
            ],
            "Resultados": [
                ("108", "Tasa de alfabetismo adultos"),
                ("109", "Tasa de alfabetismo juvenil"),
                ("110", "Tasa de deserción escolar (Primaria)"),
                ("111", "Tasa de deserción escolar (Secundaria)"),
                ("112", "Tasa de repitencia"),
                ("113", "Años promedio de escolaridad")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Procesos": [
                ("114", "Gasto público en educación como % del PIB"),
                ("115", "Gasto público en educación como % del Gasto Total"),
                ("116", "Inversión por alumno (Primaria)"),
                ("117", "Inversión por alumno (Secundaria)")
            ]
        },
        "Capacidades Estatales": {
            "Procesos": [
                ("118", "Ratio alumnos/docente (Primaria)"),
                ("119", "Ratio alumnos/docente (Secundaria)"),
                ("120", "% Docentes con titulación certificada"),
                ("121", "% Escuelas con acceso a Internet"),
                ("122", "% Escuelas con acceso a agua potable y saneamiento")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("123", "Educación bilingüe intercultural reconocida"),
                ("124", "Programas de integración para discapacitados")
            ],
            "Resultados": [
                ("125", "Paridad de género en educación primaria"),
                ("126", "Paridad de género en educación secundaria"),
                ("127", "Tasa de escolaridad en población indígena vs no indígena")
            ]
        }
    },

    # ==============================================================================
    # 4. DERECHO AL TRABAJO (DESGLOSE COMPLETO SEGÚN MATRIZ)
    # ==============================================================================
    "Trabajo": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("200", "Consagración constitucional: Condiciones dignas, justas y satisfactorias"),
                ("201", "Consagración constitucional: Salario mínimo y móvil"),
                ("202", "Consagración constitucional: Estabilidad en el empleo"),
                ("203", "Consagración constitucional: Capacitación"),
                ("204", "Consagración constitucional: Seguridad en el trabajo"),
                ("205", "Consagración constitucional: Promoción del pleno empleo"),
                ("206", "Consagración constitucional: No discriminación laboral"),
                ("207", "Consagración constitucional: Protección trabajo infantil"),
                ("208", "Ratificación C29 OIT (Trabajo Forzoso)"),
                ("209", "Ratificación C105 OIT (Abolición Trabajo Forzoso)"),
                ("210", "Ratificación C138 OIT (Edad Mínima)"),
                ("211", "Ratificación C182 OIT (Peores Formas Trabajo Infantil)"),
                ("212", "Ratificación C100 OIT (Igualdad Remuneración)"),
                ("213", "Ratificación C111 OIT (Discriminación Empleo)"),
                ("214", "Ratificación Convención Protección Trabajadores Migratorios"),
                ("215", "Legislación sobre indemnizaciones por despido")
            ],
            "Procesos": [
                ("216", "Existencia de Programa: Eliminación del trabajo forzoso"),
                ("217", "Existencia de Programa: Eliminación del trabajo infantil"),
                ("218", "Existencia de Programa: Anti-discriminación (etnia/género/discapacidad)"),
                ("219", "Existencia de Programa: Regularización migrantes"),
                ("220", "Existencia de Programa: Prevención accidentes ocupacionales"),
                ("221", "Existencia de mecanismos tripartitos (diálogo social)")
            ],
            "Resultados": [
                ("222", "Tasa de trabajo Infantil (5-17 años)"),
                ("223", "Tasa de desempleo total"),
                ("224", "Tasa de desempleo juvenil"),
                ("225", "Tasa de desempleo femenino"),
                ("226", "% Asalariados sobre ocupados"),
                ("227", "Tasa de informalidad laboral"),
                ("228", "Proporción de empleo precario"),
                ("229", "Proporción de mujeres en empleo no agrícola"),
                ("230", "Tasa de accidentes ocupacionales"),
                ("231", "% Mujeres en funcionariado público (jerarquía)"),
                ("232", "Participación económica personas con discapacidad")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("233", "Existencia de subsidios al empleo")
            ],
            "Procesos": [
                ("234", "% Presupuesto Ministerio Trabajo"),
                ("235", "% Presupuesto para políticas de grupos vulnerables"),
                ("236", "Ejecución presupuestaria programas laborales"),
                ("237", "% Inversión en seguridad laboral")
            ],
            "Resultados": [
                ("238", "Masa salarial como % del PIB")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("239", "Cobertura regional del Ministerio de Trabajo")
            ],
            "Procesos": [
                ("240", "Inspectores laborales por 100.000 trabajadores"),
                ("241", "Funcionarios MinTrabajo vs Población Ocupada"),
                ("242", "Empleos creados por programas gubernamentales"),
                ("243", "Avance metas Plan de Desarrollo (Trabajo)")
            ],
            "Resultados": [
                ("244", "Cobertura seguro desempleo"),
                ("245", "Tiempo promedio desempleo"),
                ("246", "Desempleo larga duración"),
                ("247", "Contratos colectivos suscritos"),
                ("248", "Adolescentes trabajadores registrados")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("249", "Sanciones por discriminación laboral"),
                ("250", "Mecanismos contra acoso laboral"),
                ("251", "Cuotas laborales (género/discapacidad/etnia)")
            ],
            "Procesos": [
                ("252", "Programas conciliación vida laboral-familiar"),
                ("253", "Programas inserción laboral vulnerables")
            ],
            "Resultados": [
                ("254", "% Casos discriminación resueltos"),
                ("255", "Cumplimiento cuotas en sector público"),
                ("256", "Brecha salarial de género")
            ]
        },
        "Acceso a la Justicia": {
            "Estructurales": [
                ("257", "Jueces laborales por 10.000 hab"),
                ("258", "Justicia gratuita laboral")
            ],
            "Resultados": [
                ("259", "Tasa de resolución causas laborales"),
                ("260", "Duración promedio juicios laborales")
            ]
        }
    },

    # ==============================================================================
    # 5. DERECHOS SINDICALES (DESGLOSE COMPLETO)
    # ==============================================================================
    "Derechos Sindicales": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("270", "Ratificación C87 OIT (Libertad Sindical)"),
                ("271", "Ratificación C98 OIT (Sindicación y Negociación)"),
                ("272", "Ratificación C135 OIT (Representantes trabajadores)"),
                ("273", "Ratificación C141 OIT (Trabajadores rurales)"),
                ("274", "Ratificación C151 OIT (Servidores públicos)"),
                ("275", "Ratificación C154 OIT (Negociación colectiva)"),
                ("276", "Ratificación C144 OIT (Consultas tripartitas)"),
                ("277", "Garantía Constitucional: Derecho de asociación"),
                ("278", "Garantía Constitucional: Derecho de reunión"),
                ("279", "Garantía Constitucional: Derecho a huelga"),
                ("280", "Garantía Constitucional: Negociación colectiva"),
                ("281", "Regulación huelga servicios esenciales")
            ],
            "Procesos": [
                ("282", "Política de promoción de la sindicalización"),
                ("283", "Política de eliminación de prácticas anti-sindicales"),
                ("284", "Monitoreo de negociación colectiva")
            ],
            "Resultados": [
                ("285", "Tasa de sindicalización"),
                ("286", "Cobertura negociación colectiva"),
                ("287", "% Solicitudes sindicatos rechazadas"),
                ("288", "Días no laborados por huelga"),
                ("289", "Denuncias ante Comité Libertad Sindical")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Procesos": [
                ("290", "Recursos para jurisdicción laboral"),
                ("291", "Recursos para protección libertad sindical")
            ],
            "Resultados": [
                ("292", "Atomización sindical (% sindicatos pequeños)")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("293", "Instancia diálogo social nacional"),
                ("294", "Tipificación penal violación libertad sindical")
            ],
            "Resultados": [
                ("295", "Contratos colectivos anuales"),
                ("296", "Nuevos sindicatos registrados"),
                ("297", "Negociaciones apoyadas por Estado")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("298", "Fuero sindical"),
                ("299", "Derechos sindicales trabajadores tercerizados")
            ],
            "Resultados": [
                ("300", "Sindicalización en grupos vulnerables"),
                ("301", "Mujeres en dirigencia sindical")
            ]
        }
    },

    # ==============================================================================
    # 6. DERECHO A LA ALIMENTACIÓN (DESGLOSE COMPLETO)
    # ==============================================================================
    "Alimentación": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("310", "Ratificación PIDESC (Alimentación)"),
                ("311", "Ratificación CEDAW (Alimentación)"),
                ("312", "Ratificación CDN (Alimentación)"),
                ("313", "Adopción Directrices Voluntarias FAO"),
                ("314", "Consagración constitucional derecho alimentación"),
                ("315", "Legislación calidad alimentos programas públicos")
            ],
            "Procesos": [
                ("316", "Política pública: Erradicación del hambre"),
                ("317", "Política pública: Erradicación desnutrición infantil"),
                ("318", "Política pública: Erradicación desnutrición materna"),
                ("319", "Política pública: Acceso agua potable"),
                ("320", "Política pública: Eliminar grasas trans"),
                ("321", "Política pública: Disminuir sodio/sal"),
                ("322", "Política pública: Reducir azúcares libres"),
                ("323", "Política pública: Alimentación escolar saludable"),
                ("324", "Política pública: Prevención desabastecimiento")
            ],
            "Resultados": [
                ("325", "Tasa mortalidad por malnutrición"),
                ("326", "% Inseguridad alimentaria"),
                ("327", "% Población bajo consumo mínimo energía"),
                ("328", "% Hogares sin saneamiento"),
                ("329", "% Indigencia"),
                ("330", "Desnutrición infantil global"),
                ("331", "Desnutrición crónica"),
                ("332", "Anemia en mujeres gestantes"),
                ("333", "Anemia en niños"),
                ("334", "Prevalencia sobrepeso/obesidad"),
                ("335", "Prevalencia diabetes"),
                ("336", "Prevalencia hipertensión")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("337", "Prioridad constitucional sector rural")
            ],
            "Procesos": [
                ("338", "% Presupuesto Agricultura/Desarrollo Rural"),
                ("339", "Ruralidad vs Transferencias per cápita")
            ],
            "Resultados": [
                ("340", "PIB Agropecuario vs PIB Nacional")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("341", "Ministerio de Agricultura (cobertura)"),
                ("342", "Autoridad control alimentos")
            ],
            "Procesos": [
                ("343", "Censo Agropecuario (periodicidad)"),
                ("344", "Programa: Fomento producción campesina"),
                ("345", "Programa: Abastecimiento emergencia"),
                ("346", "Programa: Transferencia tecnológica agro"),
                ("347", "Programa: Acceso fuentes hídricas"),
                ("348", "Programa: Sustitución cultivos"),
                ("349", "Programa: Control precios alimentos"),
                ("350", "Programa: Mitigación cambio climático agro"),
                ("351", "Estándares uso pesticidas")
            ],
            "Resultados": [
                ("352", "Intoxicaciones alimentarias"),
                ("353", "Cobertura programas nutrición suplementaria")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("354", "Enfoque diferencial derecho alimentación"),
                ("355", "Protección tierras comunidades étnicas")
            ],
            "Procesos": [
                ("356", "Incentivos mujeres campesinas"),
                ("357", "Estímulo lactancia materna")
            ],
            "Resultados": [
                ("358", "Gasto en alimentos por quintiles")
            ]
        },
        "Acceso a Información Pública y Participación": {
            "Estructurales": [
                ("359", "Encuesta Nacional Nutricional"),
                ("360", "Sistema información precios/clima"),
                ("361", "Regulación publicidad comida chatarra")
            ]
        }
    },

    # ==============================================================================
    # 7. DERECHO AL MEDIO AMBIENTE (DESGLOSE COMPLETO)
    # ==============================================================================
    "Medio Ambiente": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("370", "Ratificación Convenio Basilea (Desechos)"),
                ("371", "Ratificación Protocolo Cartagena (Biotecnología)"),
                ("372", "Ratificación Convenio Diversidad Biológica"),
                ("373", "Ratificación CITES (Especies amenazadas)"),
                ("374", "Ratificación Convenio Especies Migratorias"),
                ("375", "Ratificación Protocolo Kioto (Cambio climático)"),
                ("376", "Ratificación Protocolo Montreal (Capa Ozono)"),
                ("377", "Ratificación Convención Ramsar (Humedales)"),
                ("378", "Ratificación Convenio Rotterdam (Químicos)"),
                ("379", "Ratificación Convenio Estocolmo (COPs)"),
                ("380", "Ratificación Convención Lucha Desertificación"),
                ("381", "Ratificación Convención Derecho del Mar"),
                ("382", "Ratificación Convención Marco Cambio Climático"),
                ("383", "Consagración constitucional medio ambiente sano"),
                ("384", "Política ambiental nacional aprobada")
            ],
            "Procesos": [
                ("385", "Programa: Consumo mínimo agua potable"),
                ("386", "Programa: Saneamiento hídrico"),
                ("387", "Programa: Sustitución energética"),
                ("388", "Programa: Manejo residuos peligrosos"),
                ("389", "Programa: Educación ambiental")
            ],
            "Resultados": [
                ("390", "Acceso agua potable (Urbano/Rural)"),
                ("391", "Acceso saneamiento (Urbano/Rural)"),
                ("392", "Superficie cubierta por bosques"),
                ("393", "Áreas degradadas/desertificadas"),
                ("394", "Áreas protegidas vs superficie total"),
                ("395", "Eficiencia energética (PIB por unidad energía)"),
                ("396", "Emisiones CO2 per cápita"),
                ("397", "Consumo sustancias agotan ozono"),
                ("398", "Población usa combustibles sólidos"),
                ("399", "Mortalidad infantil enf. respiratorias"),
                ("400", "Concentración contaminantes aire")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("401", "Incentivos tributarios ambientales"),
                ("402", "Fondos áreas protegidas")
            ],
            "Procesos": [
                ("403", "% Presupuesto Medio Ambiente"),
                ("404", "Efectividad gasto ambiental")
            ],
            "Resultados": [
                ("405", "Inversión en energías limpias")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("406", "Entidades análisis técnico ambiental"),
                ("407", "Mapas de riesgo ambiental")
            ],
            "Procesos": [
                ("408", "Evaluación recursos hídricos"),
                ("409", "Evaluación calidad del aire"),
                ("410", "Medición residuos tóxicos"),
                ("411", "Conservación áreas protegidas"),
                ("412", "Estrategias conservación especies amenazadas")
            ],
            "Resultados": [
                ("413", "Tasa de reciclaje"),
                ("414", "Generación residuos per cápita")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("415", "Reconocimiento saberes indígenas"),
                ("416", "Mecanismo consulta previa ambiental")
            ],
            "Resultados": [
                ("417", "Proyectos con consulta previa realizada"),
                ("418", "Acceso servicios públicos grupos vulnerables")
            ]
        },
        "Acceso a Información Pública y Participación": {
            "Estructurales": [
                ("419", "Garantía acceso información ambiental"),
                ("420", "Portal indicadores ambientales")
            ]
        },
        "Acceso a la Justicia": {
            "Estructurales": [
                ("421", "Tribunales ambientales especializados"),
                ("422", "Medidas cautelares ambientales")
            ],
            "Resultados": [
                ("423", "Denuncias penales delitos ambientales"),
                ("424", "Protección defensores ambientales"),
                ("425", "Sentencias ambientales ejecutadas")
            ]
        }
    },

    # ==============================================================================
    # 8. DERECHOS CULTURALES (DESGLOSE COMPLETO)
    # ==============================================================================
    "Cultura": {
        "Recepción del Derecho": {
            "Estructurales": [
                ("430", "Ratificación PIDESC (Cultura)"),
                ("431", "Ratificación Convención Diversidad Cultural (UNESCO)"),
                ("432", "Ratificación Convención Patrimonio Inmaterial (UNESCO)"),
                ("433", "Ratificación Convención Patrimonio Mundial (UNESCO)"),
                ("434", "Ratificación Convención Eliminación Discriminación Racial"),
                ("435", "Apoyo Declaración Derechos Pueblos Indígenas"),
                ("436", "Consagración constitucional derechos culturales"),
                ("437", "Traducción normas a lenguas indígenas"),
                ("438", "Legislación derechos de autor (Morales/Materiales)"),
                ("439", "Legislación protección minorías")
            ],
            "Procesos": [
                ("440", "Campañas promoción derechos culturales"),
                ("441", "Plan Nacional de Cultura"),
                ("442", "Fondos concursables cultura"),
                ("443", "Adecuación espacios culturales discapacidad")
            ],
            "Resultados": [
                ("444", "Tasa de alfabetismo"),
                ("445", "Tasa alfabetismo lenguas originarias"),
                ("446", "Museos por 100.000 hab"),
                ("447", "Bibliotecas por 100.000 hab"),
                ("448", "Teatros por 100.000 hab"),
                ("449", "% Acceso a internet"),
                ("450", "Asistencia espectáculos culturales"),
                ("451", "Tiempo promedio disfrute cultura"),
                ("452", "Producción películas anuales"),
                ("453", "Publicaciones artísticas/académicas")
            ]
        },
        "Contexto Financiero y Compromiso Presupuestario": {
            "Estructurales": [
                ("454", "Prioridad constitucional gasto cultura/ciencia"),
                ("455", "Incentivos fiscales cultura")
            ],
            "Procesos": [
                ("456", "% Presupuesto MinCultura"),
                ("457", "% Presupuesto Ciencia y Tecnología"),
                ("458", "Ejecución recursos cultura")
            ],
            "Resultados": [
                ("459", "PIB Cultural"),
                ("460", "Gasto público per cápita cultura"),
                ("461", "Gasto hogares en cultura")
            ]
        },
        "Capacidades Estatales": {
            "Estructurales": [
                ("462", "Existencia Ministerio Cultura"),
                ("463", "Inventario riqueza cultural")
            ],
            "Procesos": [
                ("464", "Divulgación oferta cultural"),
                ("465", "Festivales financiados (Música)"),
                ("466", "Festivales financiados (Cine)"),
                ("467", "Festivales financiados (Teatro)"),
                ("468", "Comunicación estado-minorías (Lenguas)")
            ],
            "Resultados": [
                ("469", "Patentes concedidas"),
                ("470", "Equipamientos culturales")
            ]
        },
        "Igualdad y No Discriminación": {
            "Estructurales": [
                ("471", "Enfoque diferencial legislación cultural"),
                ("472", "Reconocimiento tenencia tierra indígena")
            ],
            "Resultados": [
                ("473", "Equidad regional bienes culturales"),
                ("474", "Política intercultural educación"),
                ("475", "Gasto hogares cultura por deciles"),
                ("476", "Hablantes lenguas indígenas (Crecimiento)")
            ]
        },
        "Acceso a Información Pública y Participación": {
            "Estructurales": [
                ("477", "Portal estadísticas culturales"),
                ("478", "Veeduría ciudadana cultura")
            ]
        },
        "Acceso a la Justicia": {
            "Estructurales": [
                ("479", "Recursos jurídicos derechos autor"),
                ("480", "Justicia tradicional indígena reconocida")
            ],
            "Resultados": [
                ("481", "Casos resueltos derechos culturales"),
                ("482", "Reducción violencia inter-grupal")
            ]
        }
    }
}