-- This SQL script creates an index named 'idx_name_first' on the 'name' column of the 'names' table.
-- The index is created on the first character of the 'name' column to optimize queries that filter by the initial character of names.
CREATE INDEX idx_name_first ON names(name(1));