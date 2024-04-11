-- Populate Members Table
INSERT INTO Members (username, password, email, full_name, date_of_birth, gender)
VALUES 
('johndoe', '513', 'johndoe@gmail.com', 'John Doe', 2000-10-14, "male"),
('georgewell', '123', 'georgewell@gmail.com', 'George Well', 1980-8-12, "male"),
('janeausten', '718', 'janeausten@gmail.com', 'Jane Austen', 1999-10-13, 'female'),
('wallishillary', '192', 'wallishillary@gmail.com', 'Wallis Hillary', 2004-12-14, 'female');

-- Populate Trainers Table
INSERT INTO Trainers (username, password, email, full_name)
VALUES 
('johnsmith', '548', 'johnsmith@gmail.com', 'John Smith'),
('emilyjohnson', '279', 'emilyjohnson@gmail.com', 'Emily Johnson'),
('michaelbrown', '713', 'michaelbrown@gmail.com', 'Michael Brown'),
('jessicadavis', '926', 'jessicadavis@gmail.com', 'Jessica Davis'),
('williammiller', '405', 'williammiller@gmail.com', 'William Miller'),
('sophiawilson', '832', 'sophiawilson@gmail.com', 'Sophia Wilson'),
('alexandertaylor', '147', 'alexandertaylor@gmail.com', 'Alexander Taylor'),
('oliviamartinez', '659', 'oliviamartinez@gmail.com', 'Olivia Martinez'),
('jamesanderson', '382', 'jamesanderson@gmail.com', 'James Anderson'),
('emmagarcia', '571', 'emmagarcia@gmail.com', 'Emma Garcia');

INSERT INTO Rooms (room_name, capacity)
VALUES
('512', 10),
('145', 14),
('518', 10)