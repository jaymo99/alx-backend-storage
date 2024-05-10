-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- It computes and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    JOIN (
        SELECT user_id, SUM(score * weight) / SUM(weight) AS w_avg
        FROM (
            SELECT user_id, project_id, score, weight
            FROM corrections
            LEFT JOIN projects
            ON corrections.project_id = projects.id
        ) AS a
        GROUP BY user_id
    ) AS b ON users.id = b.user_id
    SET users.average_score = b.w_avg;
END;
//

DELIMITER ;