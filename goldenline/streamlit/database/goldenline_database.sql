-- Database: goldenline_database

-- DROP DATABASE IF EXISTS goldenline_database;

CREATE DATABASE goldenline_database
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_France.1252'
    LC_CTYPE = 'French_France.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
	-- creation table collecte
	CREATE TABLE collecte(
		user_id SERIAL PRIMARY KEY,
		sweater NUMERIC(10,2),
    	pant NUMERIC(10,2),
    	t_shirt NUMERIC(10,2),
    	underwear NUMERIC(10,2),
    	jacket NUMERIC(10,2)
		);
	SELECT * FROM collecte;
	
		-- Créer la table "goldenline_client"
	CREATE TABLE goldenline_client(
		user_id SERIAL PRIMARY KEY,
   	 	social_categorie VARCHAR(100),
    	nb_children INT,
		total_price NUMERIC(10,2),
    	date_of_sale TIMESTAMP);
	
	SELECT * FROM goldenline_client;
	
	
	--creation table utilisateur
	CREATE TABLE utilisateur(
		user_id SERIAL PRIMARY KEY,
		email VARCHAR(100),
		prenom VARCHAR(100),
		nom VARCHAR(100),
		mot_de_passe VARCHAR(200),
		admins BOOL);
		
	
	INSERT INTO collecte(sweater, pant, t_shirt, underwear, jacket)
SELECT 
    floor(random() * (80 - 20 + 1) + 20)::numeric(10,2), -- génère un nombre aléatoire entre 20 et 80 pour la colonne sweater
    floor(random() * (100 - 20 + 1) + 20)::numeric(10,2), -- génère un nombre aléatoire entre 20 et 100 pour la colonne pant
    floor(random() * (20 - 7 + 1) + 7)::numeric(10,2), -- génère un nombre aléatoire entre 7 et 20 pour la colonne t_shirt
    floor(random() * (20 - 5 + 1) + 5)::numeric(10,2), -- génère un nombre aléatoire entre 5 et 20 pour la colonne underwear
    floor(random() * (150 - 50 + 1) + 50)::numeric(10,2) -- génère un nombre aléatoire entre 50 et 150 pour la colonne jacket
FROM generate_series(1, 1000);

INSERT INTO goldenline_client (social_categorie, nb_children, total_price, date_of_sale)
SELECT 
    CASE ROUND(RANDOM()*11)::INT 
        WHEN 0 THEN 'agriculteurs exploitants'
        WHEN 1 THEN 'artisans'
        WHEN 2 THEN 'cadre'
        WHEN 3 THEN 'ouvrier'
        WHEN 4 THEN 'retraiter'
        WHEN 5 THEN 'sans activité professionnelle'
        WHEN 6 THEN 'Profession intellectuelles supérieures'
        WHEN 7 THEN 'Profession intermédiaire'
        WHEN 8 THEN 'technicien'
        WHEN 9 THEN 'employer'
        WHEN 10 THEN 'chef entreprise'
        WHEN 11 THEN 'commerçant'
    END AS social_categorie,
    ROUND(RANDOM()*4)::INT AS nb_children,
    (SELECT SUM(sweater+pant+t_shirt+underwear+jacket) FROM collecte WHERE user_id = c.user_id) AS total_price,
    TIMESTAMP '2020-01-01 00:00:00' + (RANDOM() * (TIMESTAMP '2023-12-31 00:00:00' - TIMESTAMP '2020-01-01 00:00:00')) AS date_of_sale
FROM collecte c
LIMIT 1000;


