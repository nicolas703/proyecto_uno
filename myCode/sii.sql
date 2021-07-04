CREATE TABLE actividades (
    codigo                             INTEGER NOT NULL,
    descripcion                        VARCHAR2(250 CHAR) NOT NULL,
    tipo                               VARCHAR2(100 CHAR) NOT NULL, 
    clasificacion_actividades_codigo   INTEGER NOT NULL,
    PRIMARY KEY(codigo),
    FOREIGN KEY (clasificacion_actividades_codigo) REFERENCES CLASIFICACION_ACTIVIDADES(codigo)

);

CREATE TABLE ciudades (
    codigo            VARCHAR2(150 CHAR) NOT NULL,
    nombre            VARCHAR2(150 CHAR) NOT NULL,
    regiones_codigo   VARCHAR2(150 CHAR) NOT NULL,
    PRIMARY KEY(codigo) ,
    FOREIGN KEY (regiones_codigo) REFERENCES REGIONES(codigo)
);

CREATE TABLE clasificacion_actividades (
    codigo        INTEGER NOT NULL,
    descripcion   VARCHAR2(500 CHAR) NOT NULL,
    PRIMARY KEY(codigo)
);

CREATE TABLE comunas (
    codigo            VARCHAR2(150 CHAR) NOT NULL,
    nombre            VARCHAR2(150 CHAR) NOT NULL,
    ciudades_codigo   VARCHAR2(150 CHAR) NOT NULL,    
    PRIMARY KEY(codigo) ,
    FOREIGN KEY (ciudades_codigo) REFERENCES CIUDADES(codigo)
);

CREATE TABLE condiciones (
    codigo        INTEGER NOT NULL,
    descripcion   VARCHAR2(500 CHAR) NOT NULL,
    PRIMARY KEY(codigo)
);

CREATE TABLE condiciones_declaraciones (
    codigo                         INTEGER NOT NULL,
    seleccionado                   CHAR(1) NOT NULL,
    declaraciones_juradas_codigo   INTEGER NOT NULL,
    condiciones_codigo             INTEGER NOT NULL,
    PRIMARY KEY(codigo) ,
    FOREIGN KEY (condiciones_codigo) REFERENCES CONDICIONES(codigo)
);

CREATE TABLE declaraciones_juradas (
    codigo                INTEGER NOT NULL,
    capital_inicial       NUMBER NOT NULL,
    numero_trabajadores   INTEGER NOT NULL,
    formularios_codigo    INTEGER NOT NULL,
    PRIMARY KEY(codigo) ,
    FOREIGN KEY (formularios_codigo) REFERENCES FORMULARIOS(codigo)
);

CREATE TABLE detalles (
    codigo         INTEGER NOT NULL,
    tipo_detalle   VARCHAR2(500 CHAR) NOT NULL,
    PRIMARY KEY(codigo) ,

);

CREATE TABLE detalles_formularios (
    codigo               INTEGER NOT NULL,
    seleccionado         CHAR(1) NOT NULL,
    formularios_codigo   INTEGER NOT NULL,
    detalles_codigo      INTEGER NOT NULL,
    PRIMARY KEY(codigo) ,
    FOREIGN KEY (formularios_codigo) REFERENCES FORMULARIOS(codigo)
    FOREIGN KEY (detalles_codigo) REFERENCES DETALLES(codigo)
);

CREATE TABLE domicilios (
    codigo              INTEGER NOT NULL,
    poblacion           VARCHAR2(150 CHAR),
    calle               VARCHAR2(150) NOT NULL,
    numero_calle        VARCHAR2(100 CHAR) NOT NULL,
    bloque               VARCHAR2(150 CHAR),
    depto_local         VARCHAR2(150 CHAR),
    rol_avaluo_fiscal   VARCHAR2(150 CHAR) NOT NULL,
    comunas_codigo      VARCHAR2(150 CHAR) NOT NULL,
    PRIMARY KEY(codigo),
    FOREIGN KEY (comunas_codigo) REFERENCES COMUNAS(codigo)
);

CREATE TABLE formularios (
    codigo                       INTEGER NOT NULL,
    rol_patente                  INTEGER NOT NULL,
    decreto_numero               INTEGER,
    fecha                        DATE,
    folio_rentas                 INTEGER DEFAULT "0",
    firma_empresario             CHAR(1),
    firma_timbre_municipalidad   CHAR(1),
    firma_timbre_sii             CHAR(1),
    personas_rut                 VARCHAR2(11 CHAR) NOT NULL,
    actividades_codigo           INTEGER NOT NULL,
    declaraciones_juradas_codigo INTEGER
    PRIMARY KEY(codigo),
    FOREIGN KEY (actividades_codigo) REFERENCES ACTIVIDADES(codigo),
    FOREIGN KEY (personas_rut) REFERENCES PERSONAS(codigo),
    FOREIGN KEY (declaraciones_juradas_codigo) REFERENCES DECLARACIONES_JURADAS(codigo)
);

CREATE TABLE personas (
    rut                  VARCHAR2(11 CHAR) NOT NULL,
    nombre_apellidos     VARCHAR2(100 CHAR) NOT NULL,
    sexo                 CHAR(1) NOT NULL,
    edad                 INTEGER NOT NULL,
    jefe_hogar           CHAR(1),
    profesion_oficio     VARCHAR2(250 CHAR) NOT NULL,
    telefono             INTEGER NOT NULL,
    celular              INTEGER NOT NULL,
    fax                  INTEGER NOT NULL,
    codigo_actividad_1   VARCHAR2(150 CHAR) NOT NULL,
    codigo_actividad_2   VARCHAR2(150 CHAR),
    domicilios_codigo    INTEGER NOT NULL,
    PRIMARY KEY(rut),
    FOREIGN KEY (domicilios_codigo) REFERENCES DOMICILIOS(codigo),

);

CREATE TABLE propagandas (
    codigo               INTEGER NOT NULL,
    tipo                 VARCHAR2(150 CHAR) NOT NULL,
    metros               NUMBER,
    ubicacion            VARCHAR2(500 CHAR),
    formularios_codigo   INTEGER NOT NULL,
    PRIMARY KEY(codigo),
    FOREIGN KEY (formularios_codigo) REFERENCES FORMULARIOS(codigo)

);

CREATE TABLE regiones (
    codigo   VARCHAR2(150 CHAR) NOT NULL,
    nombre   VARCHAR2(150 CHAR) NOT NULL,
    PRIMARY KEY(codigo)
);
