CREATE TABLE PLot (id INTEGER PRIMARY KEY AUTOINCREMENT, 
	name TEXT, 
	lat REAL, 
	long REAL, 
	capacity INTEGER);

CREATE TABLE Destinations (id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT, 
	lat REAL, 
	long REAL);

CREATE TABLE DistanceGraph (p_lot_id INTEGER, 
	destination_id INTEGER, 
	distance INTEGER,
	CONSTRAINT UNQPD UNIQUE (p_lot_id, destination_id));

CREATE TABLE PSpace (id INTEGER PRIMARY KEY AUTOINCREMENT, 
	name TEXT, 
	p_lot_id INTEGER, 
	group_id INTEGER);

CREATE TABLE PGroup (id INTEGER PRIMARY KEY AUTOINCREMENT, 
	name TEXT);

CREATE TABLE TempReserves (p_space_id INTEGER, 
	till_timestamp INTEGER);

CREATE TABLE Allocations (p_space_id INTEGER PRIMARY KEY, 
	reserved BOOL);

CREATE TABLE CurrentCapacity (p_lot_id INTEGER, 
	group_id INTEGER, 
	capacity INTEGER, 
	CONSTRAINT UNQIDF UNIQUE (p_lot_id, group_id));
