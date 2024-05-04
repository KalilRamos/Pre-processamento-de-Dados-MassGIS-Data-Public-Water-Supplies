SELECT *
FROM public_water_supplies
LIMIT 5;


DESCRIBE public_water_supplies;

SELECT COUNT(*)
FROM public_water_supplies
WHERE coluna_a_verificar IS NULL;

UPDATE public_water_supplies
SET coluna_valores_ausentes = (
    SELECT AVG(coluna_valores_ausentes)
    FROM public_water_supplies
    WHERE coluna_valores_ausentes IS NOT NULL
)
WHERE coluna_valores_ausentes IS NULL;

SELECT *
FROM public_water_supplies
WHERE região = 'região_de_interesse';
