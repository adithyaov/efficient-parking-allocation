CREATE TABLE PLot (id INT PRIMARY KEY, 
	name TEXT, 
	lat REAL, 
	long REAL, 
	capacity INT);

CREATE TABLE Destinations (id INT PRIMARY KEY, 
	name TEXT, 
	lat REAL, 
	long REAL);

CREATE TABLE DistanceGraph (p_lot_id INT, 
	destination_id INT, 
	distance INT,
	CONSTRAINT UNQPD UNIQUE (p_lot_id, destination_id));

CREATE TABLE PSpace (id INT PRIMARY KEY, 
	name TEXT, 
	p_lot_id INT, 
	group_id INT);

CREATE TABLE PGroup (id INT PRIMARY KEY, 
	name TEXT);

CREATE TABLE TempReserves (p_space_id INT, 
	till_timestamp INT);

CREATE TABLE Allocations (p_space_id INT PRIMARY KEY, 
	reserved BOOL);

CREATE TABLE CurrentCapacity (p_lot_id INT, 
	group_id INT, 
	capacity INT, 
	CONSTRAINT UNQIDF UNIQUE (p_lot_id, group_id));
