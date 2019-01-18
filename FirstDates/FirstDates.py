'''
Algorithm for matching dates on Carnival Rag's First Dates event 2019.

Take a CSV file from Google forms and assign each individual their top N matches.

The team will then go through these manually and judge by eye whether they would be a good match or not.

Form: https://docs.google.com/forms/d/1L4QRRU_kHX13MysTP7Rp42pZZKQXEAa2OX_6z0HVrYs

TODO Do I need to defend against duplicate names?
Probably- do this later.
TODO Remove everyone who is "other" on "I am a..."

Iterate through each person and match them by:
0. Sexuality
1. Available dates
2. Things in spare time
3. Personality
4. Ideal date

@author Ed Wong
@date Jan 2019
'''

import csv
from collections import defaultdict

filename = "test.csv"

def printDict(dict):
	for ind in dict:
		print(str(ind)+": " + str(dict[ind]))


# Returns a dictionary of people where the key is each persons name and the values are
# their relevant responses.
def getPeople():
	def transpose(people):
		# Transpose the data
		# At the moment we finish with a name dict, q1 a dict, q2 a dict etc... is this the best way?
		newdict = {}
		for k in people:
			for v in people[k]:
				newdict.setdefault(v, []).append(k)

		return newdict

	people = {}

	# Fill in information
	with open(filename, newline='') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			people[row["Full Name"]] =\
				row["I am a..."],\
				row["Please select all the days you are available for your date:"],\
				row["What 4 things do you most enjoy in your spare time?"],\
				row["What 4 personality traits describe yourself?"],\
				row["Whats your ideal date?"]


	return people


def writeToFile(completeCandidateList):
	with open('output.csv', 'w', newline='') as csvfile:
		fieldnames = ["Full Name", "Candidate 1", "Candidate 2", "Candidate 3"]
		writer = csv.DictWriter(csvfile, fieldnames)
		writer.writerows(completeCandidateList)


# Get sexuality preference.
def getSexualPref(sexuality):	
	MW = "Man looking for a woman"
	MM = "Man looking for a man"
	WM = "Woman looking for a man"
	WW = "Woman looking for a woman"
	MB = "Man looking for man or woman"
	WB = "Woman looking for man or woman"

	if sexuality == MW:
		return [WM, WB]
	elif sexuality == WM:
		return [MW, MB]
	elif sexuality == WW:
		return [WW, WB]
	elif sexuality == MM:
		return [MM, MB]
	elif sexuality == MB:
		return [WM, MM, WB, MB]
	elif sexuality == WB:
		return [MW, WW, MB, WB]
	else:
		raise Exception("You fucked up the sexuality: " + str(sexuality))


def matchMaking():
	people = getPeople()
	# printDict(people)

	completeCandidateList = {}

	for person in people:
		candidates = []
		sexuality = people[person][0]
		eligibile = getSexualPref(sexuality)
		possibleDates = people[person][1].split(",")

		# Gather candidates by sexuality and available dates first.
		for candidate in {i:people[i] for i in people if i!=person}:
			theirPossibleDates = people[candidate][1].split(",")
			if people[candidate][0] in eligibile and bool(set(possibleDates).intersection(theirPossibleDates)):
				candidates.append(candidate)

		# TODO gather top 3 eligible candidates

		completeCandidateList[person] = candidates

	# write to the csv with the top three matches appended at the end
	writeToFile(completeCandidateList)

if __name__ == "__main__":
	matchMaking()