-- Creates and index on the table `names`.
-- Indexes the first letter of `name` and `score`

CREATE INDEX idx_name_first_score ON names (name(1), score);
