-- 1-create_user.sql

-- Créer l'utilisateur user_0d_1 s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorder tous les privilèges à user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Appliquer les changements
FLUSH PRIVILEGES;
