CREATE TABLE CAUSANTES (
    nombre VARCHAR(45) NOT NULL,
    run VARCHAR(11) NOT NULL,
    apellido_paterno VARCHAR(45) NOT NULL,
    apellido_materno VARCHAR(48) NOT NULL,
    PRIMARY KEY(run)
);

CREATE TABLE EMPLEADORES (
    rut VARCHAR(45) NOT NULL,
    razon_social VARCHAR(45) NOT NULL,
    PRIMARY KEY (rut)
);

CREATE TABLE CAUSALES (
    codigo_causal INTEGER NOT NULL,
    nombre_causal VARCHAR(250) NOT NULL,
    PRIMARY KEY (codigo_causal)
);

CREATE TABLE REGIONES (
    codigo_region VARCHAR(25) NOT NULL,
    nombre VARCHAR(250) NOT NULL,
    numero_region INTEGER,
    PRIMARY KEY (codigo_region)

);

CREATE TABLE CIUDADES (
    codigo_ciudad VARCHAR(25) NOT NULL,
    nombre VARCHAR(250) NOT NULL,
    regiones_codigo_region VARCHAR(25) NOT NULL,
    PRIMARY KEY (codigo_ciudad),
    FOREIGN KEY (regiones_codigo_region) REFERENCES REGIONES(codigo_region)
);


CREATE TABLE COMUNAS (
    codigo_comuna VARCHAR(100) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    ciudades_codigo_ciudad VARCHAR(25) NOT NULL,
    PRIMARY KEY (codigo_comuna),
    FOREIGN KEY (ciudades_codigo_ciudad) REFERENCES CIUDADES(codigo_ciudad)

);

CREATE TABLE BENEFICIARIOS (
    run VARCHAR(11) NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    apellido_paterno VARCHAR(100) NOT NULL,
    apellido_materno VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(150),
    codigo_tipo_beneficiario VARCHAR(45) NOT NULL,
    calle VARCHAR(45),
    numero_calle VARCHAR(15),
    depto VARCHAR(15),
    benef_comunas_codigo_comuna VARCHAR(100) NOT NULL,
    PRIMARY KEY(run) ,
    FOREIGN KEY (comunas_codigo_comuna) REFERENCES COMUNAS(codigo_comuna)
);

CREATE TABLE SOLICITANTES (
    run VARCHAR(11) NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    apellido_paterno VARCHAR(100) NOT NULL,
    apellido_materno VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(150),
    calle VARCHAR(45),
    numero_calle VARCHAR(15),
    departamento VARCHAR(15),
    solic_comunas_codigo_comuna VARCHAR(100) NOT NULL,
    PRIMARY KEY (run),
    FOREIGN KEY (comunas_codigo_comuna) REFERENCES COMUNAS(codigo_comuna)
);

CREATE TABLE SOLICITUDES (
    firma_solicitante bit NOT NULL,
    codigo_solicitud INTEGER NOT NULL,
    fecha_solicitud DATE NOT NULL,
    firma_recepcion bit NOT NULL,
    timbre_recepcion bit NOT NULL,
    fecha_recepcion DATE NOT NULL,
    beneficiarios_run VARCHAR(11) NOT NULL,
    solicitantes_run VARCHAR(11) NOT NULL,
    empleadores_rut VARCHAR(45) NOT NULL,
    PRIMARY KEY (codigo_solicitud),
    FOREIGN KEY (beneficiarios_run) REFERENCES BENEFICIARIOS(run),
    FOREIGN KEY (solicitantes_run) REFERENCES SOLICITANTES(run),
    FOREIGN KEY (empleadores_rut) REFERENCES EMPLEADORES(rut)        
);

CREATE TABLE SOLICITUDES_CAUSANTES (
    id_solicitud_causante NUMERIC NOT NULL,
    solicitudes_codigo_solicitud INTEGER NOT NULL,
    causantes_run VARCHAR(11) NOT NULL,
    fecha_extincion datetime NOT NULL,
    codigo_extincion INTEGER NOT NULL,
    causales_codigo_causal  INTEGER,
    PRIMARY KEY(id_solicitud_causante),
    FOREIGN KEY (causantes_run) REFERENCES CAUSANTES(run),
    FOREIGN KEY (solicitudes_codigo_solicitud) REFERENCES SOLICITUDES(codigo_solicitud),
    FOREIGN KEY (causales_codigo_causal) REFERENCES CAUSALES(codigo_causal)    
);