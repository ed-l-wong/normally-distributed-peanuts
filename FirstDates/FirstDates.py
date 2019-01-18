'''
Algorithm for matching dates on Carnival Rag's First Dates event 2019.

Take a CSV file from Google forms and assign each individual their top N matches.

The team will then go through these manually and judge by eye whether they would be a good match or not.

@author Ed Wong
@date Jan 2019
'''

import csv

filename = "test.csv"


def topThree(names, emails):
	return "hi", "hi", "hi"


def getData():
	emails = []
	names = []
	bestmatches = []

	# Fill in information
	with open(filename, newline='') as csvfile:
		spamreader = csv.DictReader(csvfile)
		for row in spamreader:
			names.append(row["Name"])
			emails.append(row["Email"])

	return emails, names, bestmatches


def writeToFile(bestmatches):
	with open('output.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		writer.writerows(bestmatches)


def matchMaking():
	# Get the data and ds
	emails, names, bestmatches = getData()

	'''
	Iterate through each person and match them by:
	1. Sexuality
	2. Available dates
	3. Things in spare time
	4. Personality
	5. Ideal date
	'''
	for ind in names:
		bestmatches.append(topThree(names, emails))

	# write to the csv with the top three matches appended at the end
	writeToFile(bestmatches)


if __name__ == "__main__":
	matchMaking()
