# ECE1747-A1-SimMud

1. BUILDING THE GAME FROM SOURCES

Make sure all the needed libraries are installed:
	- SDL - http://www.libsdl.org/
	- SDL_net - http://www.libsdl.org/projects/SDL_net/
	- OpenGL

The script "sdl-config" must be present and return the valid path to the SDL header and libraries. Otherwise manually edit the CXXFLAGS and LDFLAGS in parameters in the Makefile. Also change the compiler name in the makefile if it is not g++.

Build:	make
Clean:	make clean

Run server:		./server <config_file> <server_port>
Run client:		./client [--gui] <server_ip:server_port>

2. CONFIGURATION FILE

The relevant settings that can be specified in the configuration file and their meaning follow:


[Server]

server.number_of_threads = 4				//	number of threads used by the server
server.regular_update_interval = 50			//	number of milliseconds between 2 consecutive updates of the world (form server to clients)

server.balance = static						//	algorithm used for load balancing
server.load_balance_limit = 10				//	number of seconds between 2 consecutive load re-distributions of regions to threads

[Map]

map.width = 16								//	size of the map ( in number of client-areas-of-interest )
map.height = 16

map.region_min_width = 4					//	size of a region ( in number of client-areas-of-interest )
map.region_min_height = 4

map.blocks = 50								//	number of blocks on the map for every 1000 cells
map.resources = 30							//	number of resources on the map for every 1000 cells

map.min_res = 1								//	min/max value of a resource at initialization
map.max_res = 10



[Player]

player.min_life = 20						//	min/max value of a players life at initialization
player.max_life = 60

[Quest]

quest.bonus = 10							//	bonus given to the players that have reached the quest area

quest.between = 20							//	time between quests

quest.min = 40								//	min/max duration of a quest (seconds)
quest.max = 90

3. Testing it
We are using four different configuration files for each different scenario:
 - config/config_static_nquest.ini: Used for running static load management with no quests
 - config/config_static_quest.ini: Used for running static load management with quests
 - config/config_lightest_nquest.ini: Used for running lightest load management with no quests
 - config/config_lightest_quest.ini: Used for running lightest load management with quests

An example of using the automated test script for lightest load management with quests, on port 8080, writing to logfile logs/lightest_quest.log, and with 500 clients
tools/create_log.py ./server ./client configs/config_lightest_quest.ini 8080 logs/lightest_quest.log 500

An example of using the log plotter:
tools/parse_log.py logs/lightest_quest.log
