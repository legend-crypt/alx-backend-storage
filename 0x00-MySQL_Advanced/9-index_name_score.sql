
-- This SQL script creates an index named 'idx_name_first_score' on the 'names' table.
-- The index is created on the first character of the 'name' column and the entire 'score' column.
-- Indexes can improve the performance of queries that filter or sort by these columns.
CREATE INDEX idx_name_first_score on names(name(1), score);