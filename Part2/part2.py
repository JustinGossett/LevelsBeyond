import datetime
import commands
import json

# Find the date from 7 days ago
date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")

# Generate command
command = 'curl -i -H "Content-Type: application/json" -X GET https://api.github.com/repos/angular/angular/issues?since=' + date

# Get results in JSON
output = commands.getoutput(command)
json_data = output[output.find('['):]

numIssues = 0
title = []
userLogin = []
assignLogin = []
body = []

# Parse JSON and populate values for title, user login, assignee login, and body
while len(json_data) > 0 and json_data.find('"title": "') <> -1:
	# Find the issue's title
	json_data = json_data[json_data.find('"title": "') + len('"title": "'):]
	index = json_data.find('",\n')
	title.append(json_data[:index])
	json_data = json_data[index + len('",\n'):]
	
	# Find the issue's user login
	json_data = json_data[json_data.find('"login": "') + len('"login": "'):]
	index = json_data.find('",\n')
	userLogin.append(json_data[:index])
	json_data = json_data[index + len('",\n'):]

	# Find the issue's assignee login
	json_data = json_data[json_data.find('"assignee": ') + len('"assignee": '):]
	index = json_data.find(',')
	assignLogin.append(json_data[:index])
	if assignLogin[-1] == "null":
		json_data = json_data[index + len(','):]
	else:
		# If the assignee is not null, then we look for the next login value
		json_data = json_data[json_data.find('"login": "') + len('"login": "'):]
		index = json_data.find('",\n')
		assignLogin[-1] = json_data[:index]
		json_data = json_data[index + len('",\n'):]

	# Find the issue's body
	json_data = json_data[json_data.find('"body": "') + len('"body": "'):]
	index = json_data.find('"')
	# Ensure that the found " is not escaped by a previous \ character
	while len(json_data) > 0 and json_data[index-1] == '\\':
		index = json_data.find('"',index+1)
	body.append(json_data[:index])
	json_data = json_data[index + len('"'):]
	
	numIssues = numIssues + 1
	
# Create html page with the results
with open('results.html', 'w') as results:
	results.write('<html>\n\t<head>\n\t\t<style>\n\t\t\ttable {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}\n\t\t\tth {border: 4px solid #000000;text-align: left;padding: 8px;width: 10%}\n\t\t\ttd {border: 4px solid #000000;text-align: left;padding: 8px;width: 90%}\n\t\t</style>\n\t\t<title>Issues of the last 7 days</title>\n\t</head>\n\t<body>\n\t\t<h1>Issues of the last 7 days</h1>\n')
	
	for i in range(0, numIssues-1):
		results.write('\t\t<table>\n')
		results.write('\t\t\t<tr>\n\t\t\t\t<th>Title</th>\n\t\t\t\t<td>' + title[i] + '</td>\n\t\t\t</tr>\n')
		results.write('\t\t\t<tr>\n\t\t\t\t<th>User Login</th>\n\t\t\t\t<td>' + userLogin[i] + '</td>\n\t\t\t</tr>\n')
		results.write('\t\t\t<tr>\n\t\t\t\t<th>Assignee Login</th>\n\t\t\t\t<td>' + assignLogin[i] + '</td>\n\t\t\t</tr>\n')
		results.write('\t\t\t<tr>\n\t\t\t\t<th>Body</th>\n\t\t\t\t<td>' + body[i] + '</td>\n\t\t\t</tr>\n')
		results.write('\t\t</table>\n\t\t<br>\n')
	
	results.write('\t</body>\n</html>')

# Open html page
commands.getoutput('open ./results.html')

