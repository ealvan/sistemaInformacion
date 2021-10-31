-- Create tables section -------------------------------------------------
-- Este es nuestro modelo para poner la BD
-- debemos ingresar todos los datos desde la DIARIOD.csv
-- deben copiar este modelo para su base de datos creada
-- Table DIARIO

CREATE TABLE `DIARIO`
(
  `LIB` Varchar(20)
  COMMENT 'ES LE LIB DEL CSV',
  `NROASI` Int NOT NULL
  COMMENT 'NRO DE ASIENTO',
  `NRODOC` Varchar(20),
  `CODCTA` Varchar(20)
  COMMENT 'CODGIO DE CUENTA',
  `MONMN` Double NOT NULL
  COMMENT 'MONMN',
  `ID` Int NOT NULL
)
;

ALTER TABLE `DIARIO` ADD PRIMARY KEY (`ID`)
;