CREATE TABLE ESPECIALIDADES 
    (
     cod INTEGER NOT NULL , 
     nombre VARCHAR2 (50) NOT NULL , 
     descripcion VARCHAR2 (200) 
    );

CREATE TABLE MEDICOS 
    (
     cod INTEGER NOT NULL , 
     nombre VARCHAR2 (20) NOT NULL , 
     apellido_paterno VARCHAR2 (30) NOT NULL , 
     apellido_materno VARCHAR2 (30) NOT NULL , 
     telefono INTEGER NOT NULL , 
     ESPECIALIDADES_cod INTEGER NOT NULL,
     PRIMARY KEY (cod)
