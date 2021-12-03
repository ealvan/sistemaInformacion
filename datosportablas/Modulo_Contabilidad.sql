-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 03-12-2021 a las 00:44:30
-- Versión del servidor: 5.7.36-0ubuntu0.18.04.1
-- Versión de PHP: 7.2.24-0ubuntu0.18.04.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Modulo_Contabilidad`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `LIB`
--

CREATE TABLE `LIB` (
  `ID_LIB` int(2) NOT NULL,
  `LIB` char(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Libro_Cabecera`
--

CREATE TABLE `Libro_Cabecera` (
  `ID_LIB_CAB` int(10) NOT NULL,
  `PERI` varchar(6) NOT NULL,
  `GLO` char(255) DEFAULT NULL,
  `NROASI` int(3) NOT NULL,
  `ID_LIB` int(2) NOT NULL,
  `FECASI` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Libro_Detalle`
--

CREATE TABLE `Libro_Detalle` (
  `ID_LIB_DET` int(10) NOT NULL,
  `ID_LIB_CAB` int(10) DEFAULT NULL,
  `CODCTA` varchar(8) DEFAULT NULL,
  `NRODOC` varchar(20) DEFAULT NULL,
  `MONMN` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `PLAN`
--

CREATE TABLE `PLAN` (
  `CODCTA` varchar(8) NOT NULL,
  `DESCRIP` char(255) DEFAULT NULL,
  `BALANCE` tinyint(1) NOT NULL,
  `EPGNATU` tinyint(1) NOT NULL,
  `EPGFUNCI` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `RESUMEN`
--

CREATE TABLE `RESUMEN` (
  `ID_RESUMEN` int(10) NOT NULL,
  `PERIODO` year(4) NOT NULL,
  `CODCTA` varchar(8) NOT NULL,
  `DEBE00` int(10) DEFAULT NULL,
  `HABER00` int(10) DEFAULT NULL,
  `DEBE01` int(10) DEFAULT NULL,
  `HABER01` int(10) DEFAULT NULL,
  `DEBE02` int(10) DEFAULT NULL,
  `HABER02` int(10) DEFAULT NULL,
  `DEBE03` int(10) DEFAULT NULL,
  `HABER03` int(10) DEFAULT NULL,
  `DEBE04` int(10) DEFAULT NULL,
  `HABER04` int(10) DEFAULT NULL,
  `DEBE05` int(10) DEFAULT NULL,
  `HABER05` int(10) DEFAULT NULL,
  `DEBE06` int(10) DEFAULT NULL,
  `HABER06` int(10) DEFAULT NULL,
  `DEBE07` int(10) DEFAULT NULL,
  `HABER07` int(10) DEFAULT NULL,
  `DEBE08` int(10) DEFAULT NULL,
  `HABER08` int(10) DEFAULT NULL,
  `DEBE09` int(10) DEFAULT NULL,
  `HABER09` int(10) DEFAULT NULL,
  `DEBE10` int(10) DEFAULT NULL,
  `HABER10` int(10) DEFAULT NULL,
  `DEBE11` int(10) DEFAULT NULL,
  `HABER11` int(10) DEFAULT NULL,
  `DEBE12` int(10) DEFAULT NULL,
  `HABER12` int(10) DEFAULT NULL,
  `DEBE13` int(10) DEFAULT NULL,
  `HABER13` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `LIB`
--
ALTER TABLE `LIB`
  ADD PRIMARY KEY (`ID_LIB`);

--
-- Indices de la tabla `Libro_Cabecera`
--
ALTER TABLE `Libro_Cabecera`
  ADD PRIMARY KEY (`ID_LIB_CAB`),
  ADD KEY `IX_Relationship19` (`ID_LIB`);

--
-- Indices de la tabla `Libro_Detalle`
--
ALTER TABLE `Libro_Detalle`
  ADD PRIMARY KEY (`ID_LIB_DET`),
  ADD KEY `IX_Relationship23` (`ID_LIB_CAB`),
  ADD KEY `IX_Relationship24` (`CODCTA`);

--
-- Indices de la tabla `PLAN`
--
ALTER TABLE `PLAN`
  ADD PRIMARY KEY (`CODCTA`);

--
-- Indices de la tabla `RESUMEN`
--
ALTER TABLE `RESUMEN`
  ADD PRIMARY KEY (`ID_RESUMEN`),
  ADD KEY `IX_Relationship18` (`CODCTA`);

ALTER TABLE `RESUMEN` CHANGE `ID_RESUMEN` `ID_RESUMEN` INT(10) NOT NULL AUTO_INCREMENT;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Libro_Cabecera`
--
ALTER TABLE `Libro_Cabecera`
  ADD CONSTRAINT `Relationship19` FOREIGN KEY (`ID_LIB`) REFERENCES `LIB` (`ID_LIB`);

--
-- Filtros para la tabla `Libro_Detalle`
--
ALTER TABLE `Libro_Detalle`
  ADD CONSTRAINT `Relationship23` FOREIGN KEY (`ID_LIB_CAB`) REFERENCES `Libro_Cabecera` (`ID_LIB_CAB`),
  ADD CONSTRAINT `Relationship24` FOREIGN KEY (`CODCTA`) REFERENCES `PLAN` (`CODCTA`);

--
-- Filtros para la tabla `RESUMEN`
--
ALTER TABLE `RESUMEN`
  ADD CONSTRAINT `Relationship18` FOREIGN KEY (`CODCTA`) REFERENCES `PLAN` (`CODCTA`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
