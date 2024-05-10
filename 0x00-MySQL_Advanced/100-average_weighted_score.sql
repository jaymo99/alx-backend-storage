-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- It computes and store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    UPDATE users
    SET users.average_score = (
        SELECT SUM(score * weight) / SUM(weight)
        FROM (
            SELECT project_id, score, weight
            FROM corrections
            LEFT JOIN projects
            ON corrections.project_id = projects.id
            WHERE corrections.user_id = user_id
        ) AS a
    )
    WHERE users.id = user_id;
END;
//

DELIMITER ;