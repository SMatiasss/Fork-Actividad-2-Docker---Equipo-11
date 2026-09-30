CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

INSERT INTO usuarios (nombre, email) VALUES
('Juan Perez', 'juan@example.com'),
('Maria Gomez', 'maria@example.com'),
('Carlos Lopez', 'carlos@example.com');