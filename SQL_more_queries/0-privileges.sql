-- 0-privileges.sql

-- Créer les utilisateurs si nécessaire
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Accorder tous les privilèges pour les besoins de la démonstration
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- Afficher les privilèges de user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Afficher les privilèges de user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
