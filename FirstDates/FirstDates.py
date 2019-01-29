'''
Algorithm for matching dates on Carnival Rag's First Dates event 2019.
Take a CSV file from Google forms and assign each individual their top N matches.
The cupids will then go through these manually and judge by eye whether they would be a good match or not.
We then allow for multiple iterations if needed.

Form: https://docs.google.com/forms/d/1L4QRRU_kHX13MysTP7Rp42pZZKQXEAa2OX_6z0HVrYs

PRECONDITION: This only sorts straight people, the rest shall be done by hand.

Iterate through each person and match them by:
0. Sexuality
1. Available dates
2. Things in spare time
3. Personality
4. Drinking habits and Ideal date

@author Ed Wong
@date Jan 2019
'''

import csv

# VARIABLES
filename = "Carnival RAG's First Dates.csv"
output = 'output.csv'
numberOfMatches = 3


def printDict(dict):
	for ind in dict:
		print(str(ind)+": " + str(dict[ind]))


# Returns a dictionary of people where the key is each persons name and the values are
# their relevant responses.
def getPeople():
	people = {}
	# Fill in information
	with open(filename, newline='') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			# If someone has the same name then we append the time stamp.
			if row["Full Name "] in people:
				person = row["Full Name "] + row["Timestamp"]
			else:
				person = row["Full Name "]
			people[person] =\
				row["I am a..."],\
				row["Please select all the days you are available for your date:"],\
				row["What 4 things do you most enjoy in your spare time? "],\
				row["What 4 personality traits describe yourself?"],\
				row["How much do you drink"],\
				row["Whats your ideal date?"],\
				row["Year of Study"]#\
				# row["Skip these candidates."]

	return people


def writeToFile(completeCandidateList):
	with open(output, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(["Full Name ", "Candidate 1", "Candidate 2", "Candidate 3"])
		writer.writerows(completeCandidateList)


# Get sexuality preference. NOTE: Cupids will sort anyone who is not heterosexual by hand.
def getSexualPref(sexuality):	
	MW = "Man looking for a woman"
	WM = "Woman looking for a man"
	if sexuality == MW:
		return [WM]
	elif sexuality == WM:
		return [MW]
	else:
		raise Exception("Other sexuality: " + str(sexuality) + ". Please remove and sort by hand.")

def yearOfStudyCheck(person, candidate):
	if person == "1st" and (candidate == "PHD" or candidate == "Masters"):
		return False
	elif candidate == "1st" and (person == "PHD" or person == "Masters"):
		return False
	else:
		return True

def matchMaking():
	people = getPeople()

	completeCandidateList = {}

	for person in people:

		candidates = []
		sexuality = people[person][0]
		eligibile = getSexualPref(sexuality)
		possibleDates = people[person][1].split(";")
		personYoS = people[person][6]

		# Gather candidates by sexuality and available dates first.
		for candidate in {i:people[i] for i in people if i!=person}:
			theirPossibleDates = people[candidate][1].split(";")
			if people[candidate][0] in eligibile and bool(set(possibleDates).intersection(theirPossibleDates)):
				if yearOfStudyCheck(personYoS,people[candidate][6]):
					# Checking if candidate is in ignore list (or vice versa) THIS IS FOR THE NEXT ITERATION
					# if candidate not in people[person][6].split(",") and person not in people[candidate][6].split(","):
					candidates.append(candidate)

		# convert candidates to a dictionary with values as their scores
		if len(candidates) > numberOfMatches:
			candidateDict = dict(zip(candidates, [0] * len(candidates)))

			for candidate in candidates:
				# Score the spare time question (with relevant weighting)
				score = len(set(people[candidate][2].split(";")).intersection(people[person][2].split(";")))
				candidateDict[candidate] += 4 * score

				# Score the personality question (with relevant weighting)
				score = len(set(people[candidate][3].split(";")).intersection(people[person][3].split(";")))
				candidateDict[candidate] += 3 * score

				# Score the drinking question (with relevant weighting)
				score = len(set(people[candidate][4].split(";")).intersection(people[person][4].split(";")))
				candidateDict[candidate] += 2 * score

				# Score the ideal date question (with relevant weighting)
				score = len(set(people[candidate][5].split(";")).intersection(people[person][5].split(";")))
				candidateDict[candidate] += 2 * score

			# sort the candidates and put them into the candidates array
			candidates = [k for k in sorted(candidateDict, key=candidateDict.get, reverse=True)]

		# take the top N
		candidates = candidates[0:numberOfMatches]
		completeCandidateList[person] = candidates

	result = []

	for key, value in completeCandidateList.items():
		result.append([key] + value)

	# write to the csv with the top three matches appended at the end
	writeToFile(result)

if __name__ == "__main__":
	matchMaking()