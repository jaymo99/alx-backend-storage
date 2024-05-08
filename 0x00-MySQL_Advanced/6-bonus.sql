-- Creates a stored procedure AddBonus
-- The procedure adds a new correction for a student
DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER //
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE proj_id INT;

    IF NOT EXISTS (SELECT name FROM projects WHERE name = project_name) THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    SELECT id INTO proj_id FROM projects WHERE name = project_name;
    INSERT INTO corrections (corrections.user_id, project_id, score)
    VALUES (user_id, proj_id, score);
END;
//

DELIMITER ;