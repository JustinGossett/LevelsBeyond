README.txt

ReachEngine at LevelsBeyond Coding Assessment by Justin Gossett

Part 1:
Note: This was implemented in C# and it is assumed that Visual Studio is installed on the system (WINDOWS or MAC).

Locate and open ./Part1/REST_API/REST_API.sln.
Build solution and run NotesApi.

This should open a web page at address http://localhost:5000/api/notes displaying an automatically generated sample note.
If it is using a port other than 5000, then adjust the following commands accordingly.

Open a terminal window and try the following command:
	curl -i -H "Content-Type: application/json" -X POST -d '{"body" : "Pick up milk!"}' http://localhost:5000/api/notes 
	
Refresh your web browser at http://localhost:5000/api/notes and you should see both notes displayed.

Now try the command:
	curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/api/notes/2
	
This should return the "Pick up milk!" note you previously posted.

Now try the command:
	curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/api/notes?query=milk 
	
This should also return the "Pick up milk!" note again and nothing else (unless you posted other notes with "milk" in them).

Try creating and retrieving (ane even updating or deleting if you wish) some more notes.




Part 2:
Note: This was implemented with a python script and it is assumed Python is installed on the system.

Navigate to ./Part2/ and run the command:
	python part2.py
	
This should query the Angular github repo for all issues updated in the last 7 days.
A results.html file will be generated and opened.
This web page will display each issue's Title, User Login, Assignee Login, and body.