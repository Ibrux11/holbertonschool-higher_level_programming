-- 2-create_read_user.sql

-- Créer la base de données hbtn_0d_2 si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Créer l'utilisateur user_0d_2 s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Accorder le privilège SELECT à user_0d_2 pour la base de données hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Appliquer les changements
FLUSH PRIVILEGES;
