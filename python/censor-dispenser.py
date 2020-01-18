#Objective: You’ve recently gotten a job working in the IT department at one of Silicon Valley’s hottest new startups, AirWeb. The company is developing a state-of-the-art artificial intelligence engine designed to help provide a new perspective on the world’s problems. Interestingly, very few people know the details of AirWeb ‘s work and the company is very secretive about its technology, even to its own investors.

#You report directly to the Head of Product, a person named Mr. Cloudy, and he has a very important task for you. You see, every month, the head researchers down in the lab send an email to the board of investors to tell them about the status of the project. Cloudy wants you to intercept these emails and censor any “proprietary information” included in them.

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("/Users/tbohmert/Google Drive/developmentProjects/portfolio-projects/resources/censor_dispenser_emails/email_one.txt", "r").read()
email_two = open("/Users/tbohmert/Google Drive/developmentProjects/portfolio-projects/resources/censor_dispenser_emails/email_two.txt", "r").read()
email_three = open("/Users/tbohmert/Google Drive/developmentProjects/portfolio-projects/resources/censor_dispenser_emails/email_three.txt", "r").read()
email_four = open("/Users/tbohmert/Google Drive/developmentProjects/portfolio-projects/resources/censor_dispenser_emails/email_four.txt", "r").read()

#function to censor 'learning alogrithms' from email_one and capitalized versions
#Write a function that can censor a specific word or phrase from a body of text, and then return the text.
#Mr. Cloudy has asked you to use the function to censor all instances of the phrase learning algorithms from the first email, email_one. Mr. Cloudy doesn’t care how you censor it, he just wants it done.
def censor_learn(email):
	email = email.replace('learning algorithms', 'software')
	email = email.replace('learning algorithms'.capitalize(), 'software'.capitalize())
	return email

print(censor_learn(email_one))

#function to censor list of proprietary terms and capitalized versions.
#Write a function that can censor not just a specific word or phrase from a body of text, but a whole list of words and phrases, and then return the text.
#Mr. Cloudy has asked that you censor all words and phrases from the following list in email_two.
proprietary_terms = ['she', 'personality matrix', 'sense of self', 'self-preservation', 'learning algorithm', 'her', 'herself']

replacement_prop_terms = ['The computer', 'database', 'update', 'protection', 'software', "the program's", 'the program itself']

def censor_prop_list(email):
	for index in range(len(proprietary_terms)):
		email = email.replace(proprietary_terms[index], replacement_prop_terms[index])
		email = email.replace(proprietary_terms[index].capitalize(), replacement_prop_terms[index].capitalize())
	return email

#print(censor_prop_list(email_two))


#function to censor proprietary words and censor negative terms.
#The most recent email update has concerned Mr. Cloudy, but not for the reasons you might think. He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the negative language and remove unnecessary instances of ‘negative words.’”
#Write a function that can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three.

negative_words = [["concerned", 'interested'], ["behind", 'catching up to'], ["danger", ''], ["dangerous", 'safe'], ["alarming", 'raising interest'], ["alarmed", 'intrigued'], ["out of control", 'getting put in control'], ["help", 'to continue working'], ["unhappy", 'content'], ["bad", 'improving'], ["upset", 'happy'], ["awful", 'great'], ["broken", 'repaired'], ["damage", 'repair'], ["damaging", 'repairing'], ["dismal", 'layoff'], ["distressed", 'motivated'], ["concerning", 'interesting'], ["horrible", 'average'], ["horribly", 'moderately'], ["questionable", 'unique']]


def censor_neg_list(email):

	#block to change proprietaary terms to replacement words
	censored_email = censor_prop_list(email)

	#block to change the negative words to replacement words
	neg_word_count = 0

	for words in negative_words:

		if neg_word_count < 2:
			neg_word_count += censored_email.count(words[0] + '') + censored_email.count(words[0].capitalize() + '')

		else:
			censored_email = censored_email.replace(words[0], words[1])
			censored_email = censored_email.replace(words[0].capitalize(), words[1].capitalize())

	return censored_email

print(censor_neg_list(email_three))


#This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He tells you, “our company would be ruined! Censor it! Censor it all!”
#Write a function that censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words in email_four that come before AND after a term from those two lists.

replacement_neg_words = ['interested', 'catching up to', '', 'safe', 'raising interest', 'intrigued', 'getting put in control', 'to continue working', 'content', 'improving', 'happy', 'great', 'repaired', 'repair', 'repairing', 'layoff', 'motivated', 'interesting', 'average', 'moderately', 'unique']

email_four = open("/Users/tbohmert/Google Drive/developmentProjects/portfolio-projects/resources/censor_dispenser_emails/email_four.txt", "r").read()

proprietary_terms = ['she', 'personality matrix', 'sense of self', 'self-preservation', 'learning algorithm', 'her', 'herself']

neg_words = ['concerned', 'behind', 'danger', 'dangerous', 'alarming', 'alarmed', 'out of control', 'help', 'unhappy', 'bad', 'upset', 'awful', 'broken', 'damage', 'damaging', 'dismal', 'distressed', 'concerning', 'horrible', 'horribly', 'questionable']

#function to normalize items in a list
def	normalize_item(item):
	item = item.strip('.')
	item = item.strip('!')
	item = item.lower()
	return item

def censor_all(email):
	#put email words into list with '' as delimiter
	email_list = email.split()



	#block to remove proprietary term +/-
	for index in range(len(email_list)):
		if normalize_item(email_list[index]) in neg_words or normalize_item(email_list[index]) in proprietary_terms:
			if email_list[index] == email_list[-1]:
				email_list[index] = 'bop'
				email_list[index - 1] = 'beep'
			else:
				email_list[index] = 'bop'
				email_list[index - 1] = 'beep'
				email_list[index + 1] = 'boop'				

	#join email_list into string
	big_censor_email = ' '.join(email_list)
	
	return big_censor_email

print(censor_all(email_four))




