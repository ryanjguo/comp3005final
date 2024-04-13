-- COMP 3005 Final Project
-- DDL File to create the database schema
-- Matthew Seto, Ryan Guo

CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50), 
    email VARCHAR(100),
    full_name VARCHAR(100),
    date_of_birth DATE,
    gender VARCHAR(10),
    balance INT
);

CREATE TABLE Trainers (
    trainer_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50), 
    email VARCHAR(100),
    full_name VARCHAR(100)
);

CREATE TABLE AvailabilitySlots (
    slot_id SERIAL PRIMARY KEY,
    trainer_id INT,
    day_of_week VARCHAR(20),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id)
);

CREATE TABLE AdminStaff (
    staff_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50), 
    email VARCHAR(100),
    full_name VARCHAR(100)
);

CREATE TABLE FitnessGoals (
    goal_id SERIAL PRIMARY KEY,
    member_id INT,
    goal_name VARCHAR(100),
    target_weight INT,
    target_time INT,
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE HealthMetrics (
    metric_id SERIAL PRIMARY KEY,
    member_id INT,
    metric_date DATE,
    weight INT,
    steps INT, 
    calories INT,
    height INT,
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE Rooms (
    room_id SERIAL PRIMARY KEY,
    room_name VARCHAR(100)
);

CREATE TABLE Classes (
    class_id SERIAL PRIMARY KEY,
    class_name VARCHAR(100),
    trainer_id INT,
    room_id INT,
    day_of_week VARCHAR(20),
    start_time TIME,
    end_time TIME,
    capacity INT,
    price INT,
    exercise_routine VARCHAR(100),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id)
);

CREATE TABLE ClassMembers (
    class_member_id SERIAL PRIMARY KEY,
    class_id INT,
    member_id INT,
    FOREIGN KEY (class_id) REFERENCES Classes(class_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE Equipment (
    equipment_id SERIAL PRIMARY KEY,
    equipment_name VARCHAR(100),
    room_id INT,
    maintenance_status VARCHAR(20),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);

CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY,
    member_id INT,
    amount INT,
    payment_date DATE,
    payment_status VARCHAR(20),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE PersonalFitnessSessions (
    session_id SERIAL PRIMARY KEY,
    member_id INT,
    trainer_id INT,
    day_of_week VARCHAR(20),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id)
);
