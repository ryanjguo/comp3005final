-- COMP 3005 Final Project
-- DML File
-- Matthew Seto, Ryan Guo

-- Note that some tables do not have sample data as our application does not require them to be populated initially
-- For example, health metrics and fitness goals are added by the user through the application optionally

-- Sample data for Members table
INSERT INTO Members (username, password, email, full_name, date_of_birth, gender, balance)
VALUES
    ('john', 'password', 'john@gmail.com', 'John Doe', '1990-05-15', 'Male', 0),
    ('jane', 'pass', 'jane@yahoo.com', 'Jane Smith', '1985-09-20', 'Female', 0),
    ('bob', 'bobpass', 'bob@example.com', 'Bob Jones', '1988-03-10', 'Male', 0);

-- Sample data for Trainers table
INSERT INTO Trainers (username, password, email, full_name)
VALUES
    ('tim', 'timmytim', 'timothy@bigbrothersgym.com', 'Timothy Himothy'),
    ('terry', 'terryhu123', 'terryh@bigbrothersgym.com', 'Terry Hu');

-- Sample data for AdminStaff table
INSERT INTO AdminStaff (username, password, email, full_name)
VALUES
    ('admin1', 'adminpass1', 'admin1@bigbrothersgym.com', 'Admin 1'),
    ('admin2', 'adminpass2', 'admin2@bigbrothersgym.com', 'Admin 2');
	
-- Sample data for AvailabilitySlots table
INSERT INTO AvailabilitySlots (trainer_id, day_of_week, start_time, end_time)
VALUES
    (1, 'Monday', '08:00:00', '12:00:00'),
    (1, 'Wednesday', '10:00:00', '14:00:00'),
    (2, 'Tuesday', '09:00:00', '13:00:00');
	
-- Sample data for Rooms table
INSERT INTO Rooms (room_name)
VALUES
    ('Studio 1'),
    ('Cycling Room'),
    ('Weight Room');

-- Sample data for Classes table
INSERT INTO Classes (class_name, trainer_id, room_id, day_of_week, start_time, end_time, capacity, price, exercise_routine)
VALUES
    ('Yoga', 1, 1, 'Monday', '10:00:00', '11:30:00', 20, 10, 'Hatha Yoga'),
    ('Spin Class', 2, 2, 'Wednesday', '09:00:00', '10:00:00', 15, 15, 'Indoor Cycling');

-- Sample data for Equipment table
INSERT INTO Equipment (equipment_name, room_id, maintenance_status)
VALUES
    ('Yoga Mats', 1, 'Good Condition'),
    ('Stationary Bikes', 2, 'Needs Maintenance');
