-- This SQL script creates a view named 'need_meeting' that selects the names of students
-- from the 'students' table who have a score less than 80 and either have never had a meeting
-- or had their last meeting more than 30 days ago.
CREATE VIEW need_meeting AS SELECT name FROM students
WHERE score < 80 AND (last_meeting IS NULL OR last_meeting < CURDATE() - 30)