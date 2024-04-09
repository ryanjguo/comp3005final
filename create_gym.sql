-- Members table
CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50), 
    email VARCHAR(100),
    full_name VARCHAR(100),
    date_of_birth DATE,
    gender VARCHAR(10),
    fitness_goal VARCHAR(100)
    -- Other relevant fields for member information
);

-- Trainers table
CREATE TABLE Trainers (
    trainer_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50), 
    email VARCHAR(100),
    full_name VARCHAR(100),
    expertise_area VARCHAR(100)
    -- Other relevant fields for trainer information
);

-- Administrative Staff table
CREATE TABLE AdminStaff (
    staff_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50), 
    email VARCHAR(100),
    full_name VARCHAR(100),
    role VARCHAR(100)
    -- Other relevant fields for administrative staff information
);

-- Fitness Goals table
CREATE TABLE FitnessGoals (
    goal_id SERIAL PRIMARY KEY,
    member_id INT,
    goal_name VARCHAR(100),
    target_weight DECIMAL(5,2), -- Assuming weight in kilograms
    target_time INT, -- Assuming time in months
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- Health Metrics table
CREATE TABLE HealthMetrics (
    metric_id SERIAL PRIMARY KEY,
    member_id INT,
    metric_date DATE,
    weight DECIMAL(5,2), -- Assuming weight in kilograms
    height DECIMAL(5,2) -- Assuming height in meters
    -- Other relevant health metrics
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- Schedules table (for personal training sessions and group fitness classes)
CREATE TABLE Schedules (
    schedule_id SERIAL PRIMARY KEY,
    member_id INT, -- For personal training sessions
    trainer_id INT, -- For personal training sessions
    class_id INT, -- For group fitness classes
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    status VARCHAR(20), -- Booked, cancelled, etc.
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id)
    -- Add foreign key for class_id if needed
);

-- Classes table
CREATE TABLE Classes (
    class_id SERIAL PRIMARY KEY,
    class_name VARCHAR(100),
    trainer_id INT,
    schedule VARCHAR(100), -- Schedule details
    capacity INT,
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id)
);

-- Rooms table
CREATE TABLE Rooms (
    room_id SERIAL PRIMARY KEY,
    room_name VARCHAR(100),
    capacity INT
);

-- Equipment table
CREATE TABLE Equipment (
    equipment_id SERIAL PRIMARY KEY,
    equipment_name VARCHAR(100),
    room_id INT,
    maintenance_status VARCHAR(20), -- In maintenance, working, etc.
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);

-- Payments table
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY,
    member_id INT,
    amount DECIMAL(10,2),
    payment_date DATE,
    payment_method VARCHAR(50) -- Credit card, cash, etc.
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);
