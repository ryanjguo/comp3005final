CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50), 
    email VARCHAR(100),
    full_name VARCHAR(100),
    date_of_birth DATE,
    gender VARCHAR(10),
    bill INT
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
    full_name VARCHAR(100),
    role VARCHAR(100)
);

CREATE TABLE FitnessGoals (
    goal_id SERIAL PRIMARY KEY,
    member_id INT,
    goal_name VARCHAR(100),
    target_weight DECIMAL(5,2),
    target_time INT,
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

CREATE TABLE HealthMetrics (
    metric_id SERIAL PRIMARY KEY,
    member_id INT,
    metric_date DATE,
    weight DECIMAL(5,2), 
    steps DECIMAL(5,2), 
    calories DECIMAL(5,2),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
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
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id)
);

CREATE TABLE Rooms (
    room_id SERIAL PRIMARY KEY,
    room_name VARCHAR(100),
    capacity INT
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
    amount DECIMAL(10,2),
    payment_date DATE,
    payment_method VARCHAR(50),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);
