create table Plot (id int, name text, lat real, long real, capacity int);
create table Destinations (id int, name text, lat real, long real);
create table DistanceGraph (parking_id int, destination_id int, distance int);
create table PSpace (id int, name text, p_lot_id int, group_id int);
create table PGroup (id int, name text);

create table TempReserves (p_space_id int, till_timestamp int);
create table Allocations (p_space_id int, reserved bool);
create table CurrentCapacity (p_lot_id int, group_id int, capacity int);
