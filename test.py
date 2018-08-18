from textblob import TextBlob

positiveTweets = []
neutralTweets = []
negativeTweets = []

numberOfTweets = 0
myfile = open("DataFile.txt", "r")

for line in myfile:
	numberOfTweets = numberOfTweets + 1
	analysis = Textblob(line)

	if ( analysis.sentiment.polarity > 0 ):
		positiveTweets.append(analysis.sentiment.polarity)

	elif ( analysis.sentiment.polarity == 0 ):
		neutralTweets.append(analysis.sentiment.polarity)

	else:
		negativeTweets.append(analysis.sentiment.polarity)

print(positiveTweets)
print(neutralTweets)
print(negativeTweets)
myfile.close()