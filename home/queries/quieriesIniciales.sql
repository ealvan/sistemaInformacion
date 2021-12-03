-- PARA EL DEBE !!
-- debes cambiar el el periodo que quieres
USE sisinfo;
SELECT 
table1.DEBE
FROM
(
SELECT
 distinct(home_diario.codcta),
 ifnull(haber01.DEBE,0) AS DEBE

FROM home_diario
LEFT JOIN (
SELECT 
	codcta, 
	ROUND(ABS(sum(monmn)),2) as DEBE 
FROM home_diario
WHERE monmn > 0 AND fecasi LIKE "%-03-%"  -- <-aqui
GROUP BY codcta
) haber01
ON haber01.codcta = home_diario.codcta
ORDER BY home_diario.codcta

) table1
-- ----------------------------------------------------------------
-- debes cambiar el el periodo que quieres
USE sisinfo;
-- HABER!!
SELECT 
table1.HABER
FROM
(
SELECT
 distinct(home_diario.codcta),
 ifnull(haber01.HABER,0) AS HABER

FROM home_diario
LEFT JOIN (
SELECT 
	codcta, 
	ROUND(ABS(sum(monmn)),2) as HABER 
FROM home_diario
WHERE monmn < 0 AND fecasi LIKE "%-01-%"  -- <-aqui
GROUP BY codcta
) haber01
ON haber01.codcta = home_diario.codcta
ORDER BY home_diario.codcta

) table1
-- ------------------------------------------------------
-- despues de comprobar que funciona ahora debes
-- hacer los templates
-- eso haces para cada debe y haber 01,02,03,04
USE sisinfo;
CREATE OR REPLACE VIEW debe01 AS
SELECT 
table1.DEBE
FROM
(
SELECT
 distinct(home_diario.codcta),
 ifnull(haber01.DEBE,0) AS DEBE

FROM home_diario
LEFT JOIN (
SELECT 
	codcta, 
	ROUND(ABS(sum(monmn)),2) as DEBE 
FROM home_diario
WHERE monmn > 0 AND fecasi LIKE "%-01-%"  -- <-aqui
GROUP BY codcta
) haber01
ON haber01.codcta = home_diario.codcta
ORDER BY home_diario.codcta
) table1
-- ----------------------------------------------------------------
-- Luego de crear las views , aahora debemos unirlas con innner join
-- y colocarlas en una sola tabla
USE sisinfo;

DELIMITER //
CREATE PROCEDURE getTablaSaldos()
BEGIN
	SELECT 
		d01.DEBE01,    h01.HABER_01,
		d02.DEBE02,    h02.HABER_02,
		d03.DEBE03,    h03.HABER_03,
		d04.DEBE04,    h04.HABER_04
		
	FROM
	(

	SELECT 
		d01.DEBE01,
		@rn1 := @rn1 + 1 AS iterator
	 FROM sisinfo.debe_01 d01, (SELECT @rn1 := 0) foo

	) AS d01
	INNER JOIN
	(
	SELECT 
		d02.DEBE02,
		@rn2 := @rn2 + 1 AS iterator
	 FROM sisinfo.debe_02 d02, (SELECT @rn2 := 0) foo
	) AS d02
	ON d02.iterator = d01.iterator

	INNER JOIN
	(
		
	SELECT 
		d03.DEBE03,
		@rn3 := @rn3 + 1 AS iterator
	 FROM sisinfo.debe_03 d03, (SELECT @rn3 := 0) foo
	) AS d03
	ON d03.iterator = d02.iterator


	INNER JOIN
	(
		
	SELECT 
		d04.DEBE04,
		@rn4 := @rn4 + 1 AS iterator
	 FROM sisinfo.debe_04 d04, (SELECT @rn4 := 0) foo
	) AS d04
	ON d04.iterator = d03.iterator

	INNER JOIN
	(
	SELECT 
		h01.HABER_01,
		@rn_1 := @rn_1 + 1 AS iterator
	 FROM sisinfo.haber_01 h01, (SELECT @rn_1 := 0) foo
	) AS h01
	ON h01.iterator = d04.iterator

	INNER JOIN
	(
	SELECT 
		h02.HABER_02,
		@rn_2 := @rn_2 + 1 AS iterator
	 FROM sisinfo.haber_02 h02, (SELECT @rn_2 := 0) foo
	) AS h02
	ON h02.iterator = d04.iterator

	INNER JOIN
	(
	SELECT 
		h03.HABER_03,
		@rn_3 := @rn_3 + 1 AS iterator
	 FROM sisinfo.haber_03 h03, (SELECT @rn_3 := 0) foo
	) AS h03
	ON h03.iterator = d04.iterator

	INNER JOIN
	(
	SELECT 
		h04.HABER_04,
		@rn_4 := @rn_4 + 1 AS iterator
	 FROM sisinfo.haber_04 h04, (SELECT @rn_4 := 0) foo
	) AS h04
	ON h04.iterator = d04.iterator;

END //
    
DELIMITER ;
--- ---------------------------
-- sino te funciona debe haber un error, 
-- puedes ejecutar por separado
-- este select, para ver que esta mal, talves te falta un ttemplate
-- o algo asi

SELECT 
	d01.DEBE01,    h01.HABER_01,
    d02.DEBE02,    h02.HABER_02,
    d03.DEBE03,    h03.HABER_03,
    d04.DEBE04,    h04.HABER_04
    
FROM
(

SELECT 
	d01.DEBE01,
    @rn1 := @rn1 + 1 AS iterator
 FROM sisinfo.debe_01 d01, (SELECT @rn1 := 0) foo

) AS d01
INNER JOIN
(
SELECT 
	d02.DEBE02,
    @rn2 := @rn2 + 1 AS iterator
 FROM sisinfo.debe_02 d02, (SELECT @rn2 := 0) foo
) AS d02
ON d02.iterator = d01.iterator

INNER JOIN
(
	
SELECT 
	d03.DEBE03,
    @rn3 := @rn3 + 1 AS iterator
 FROM sisinfo.debe_03 d03, (SELECT @rn3 := 0) foo
) AS d03
ON d03.iterator = d02.iterator


INNER JOIN
(
	
SELECT 
	d04.DEBE04,
    @rn4 := @rn4 + 1 AS iterator
 FROM sisinfo.debe_04 d04, (SELECT @rn4 := 0) foo
) AS d04
ON d04.iterator = d03.iterator

INNER JOIN
(
SELECT 
	h01.HABER_01,
    @rn_1 := @rn_1 + 1 AS iterator
 FROM sisinfo.haber_01 h01, (SELECT @rn_1 := 0) foo
) AS h01
ON h01.iterator = d04.iterator

INNER JOIN
(
SELECT 
	h02.HABER_02,
    @rn_2 := @rn_2 + 1 AS iterator
 FROM sisinfo.haber_02 h02, (SELECT @rn_2 := 0) foo
) AS h02
ON h02.iterator = d04.iterator

INNER JOIN
(
SELECT 
	h03.HABER_03,
    @rn_3 := @rn_3 + 1 AS iterator
 FROM sisinfo.haber_03 h03, (SELECT @rn_3 := 0) foo
) AS h03
ON h03.iterator = d04.iterator

INNER JOIN
(
SELECT 
	h04.HABER_04,
    @rn_4 := @rn_4 + 1 AS iterator
 FROM sisinfo.haber_04 h04, (SELECT @rn_4 := 0) foo
) AS h04
ON h04.iterator = d04.iterator
-- --------------------------
-- la sigte querie nos da el codta distinc osea
-- no se repite
use sisinfo;
SELECT 
	d04.codcta,
    @rn8 := @rn8 + 1 AS iterator
    
 FROM
(
SELECT 
	distinct codcta
 FROM sisinfo.home_diario d04
ORDER BY codcta
) AS d04, (SELECT @rn8 := 0) foo