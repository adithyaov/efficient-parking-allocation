INSERT INTO PLot (name, lat, long, capacity)
	VALUES
		("Lot 1", 0, 0, 3),
		("Lot 2", 2, 3, 2),
		("Lot 3", 1, 4, 3),
		("Lot 4", 6, 2, 1);

INSERT INTO Destinations (id, name, lat, long)
	VALUES
		("Block 1", 0, 0),
		("Block 2", 2, 3),
		("Block 3", 4, 5);

INSERT INTO DistanceGraph (p_lot_id, destination_id, distance)
	VALUES
		(1, 1, 12),
		(1, 2, 4),
		(1, 3, 2),
		(2, 1, 1),
		(2, 2, 0),
		(2, 3, 22),
		(3, 1, 21),
		(3, 2, 34),
		(3, 3, 16),
		(4, 1, 12),
		(4, 2, 27), 
		(4, 3, 79);

INSERT INTO PGroup (id, name)
	VALUES
		("general"),
		("handicappped"),
		("director");

INSERT INTO PSpace (id, name, p_lot_id, group_id)
	VALUES
		("A1", 1, 1),
		("A2", 1, 1),
		("B1", 1, 2),
		("A1", 2, 1),
		("A2", 2, 1),
		("A1", 3, 1),
		("A2", 3, 1),
		("A3", 3, 3),
		("A1", 4, 3);
