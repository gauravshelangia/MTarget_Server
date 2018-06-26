DROP SCHEMA MTarget CASCADE;
CREATE SCHEMA MTarget;
SET search_path TO MTarget;

-- Table contain the user id i.e. Student ID or cyberoam login id  and student name --image mmay be required later --  ---
CREATE TABLE users (
		userid integer PRIMARY KEY,
		username varchar(15)
);


-- Table contains the graph node number (unique number assigned to each grid of the map), detail of the grid , adjacency list (connected node to a node) --
CREATE TABLE graph (
		node_no integer PRIMARY KEY,
		detail TEXT,
		adj_list integer[]
);

--Store the device mac address, device type and owner of device (referred to userid of Users table) --
CREATE TABLE devices (
		device_id varchar(17) PRIMARY KEY,
		device_type varchar(50),
		userid integer references Users(userid) PRIMARY KEY
);

-- store the time stamp and rssi vector from  graph node --
CREATE TABLE data(
		userid integer references Users(userid),
		device_id varchar(17) references Devices(device_id),
		--device_type varchar(15) references Devices(device_type),
		node_no integer references Graph(node_no),
		timest timestamp,
		rssi2gh integer[], -- initially sizeof rssi is 26 late may change --
		rssi5gh integer[], -- initially sizeof rssi is 26 late may change --
		PRIMARY KEY(userid,device_id,node_no,timest)
);
