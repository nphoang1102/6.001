# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Hoang Nguyen
# Time: 4:00

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# General class to store the news story retrieved from rss url
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link

        # This special snowflake...
        self.pubdate = pubdate.replace(tzinfo=pytz.timezone("EST"))

    # Basic getters here, self explanatory
    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

    # Another special snowflake here...
    def __equal__(self, other):
        return (self.description == other.description) and (self.title == other.title)



#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# Super class phrase trigger, with helper function to cleanup
# an input string
class PhraseTrigger(Trigger):
    # Take a string and strip off all punctutations and
    # excessive space
    def clean_up_text(self, input):
        
        # Clean up the input by converting to lower case first
        lower = input.lower()

        # First convert all punctuations to spaces
        converted_to_space = ''
        for char in lower:
            if char in string.punctuation:
                converted_to_space += ' '
            else:
                converted_to_space += char

        # Next remove excessive space
        cleaned = ''
        last_char = ''
        for char in converted_to_space:
            if ((char == ' ') and (last_char != ' ') and (last_char != '')) or (char != ' '):
                cleaned += char
            last_char = char

        # Return cleaned string and termintate
        return cleaned

    # Check if input is valid
    def is_phrase_valid(self, input):

        # Some storage variables
        cleaned = ''
        last_char = ''

        # Convert the input to all lower case first,
        # then check for excessive space and punctuations
        lower = input.lower()
        for char in lower:
            cond = char == ' ' and last_char == ' '
            if (char in string.punctuation) or (cond):
                return False
            last_char = char

        # Terminate and return true if we have not yet terminated
        return True



# Trigger whenever a title match a certain phrase
class TitleTrigger(PhraseTrigger):

    # Class constructor, store the user's desired trigger phrase
    def __init__(self, phrase):
        self.phrase = phrase

    # Evaluation to trigger, override the super class
    def evaluate(self, story):

        # First thing first, return false immediately
        # if we have a bad input
        if not self.is_phrase_valid(self.phrase):
            return False

        # Okay, phrase is good, proceed to clean up
        title = self.clean_up_text(story.get_title())
        phrase = self.phrase.lower()

        # Check if the phrase is in the title
        # then evaluate accordingly and terminate
        if phrase in title:
            if (title.index(phrase) + len(phrase)) > len(title) - 1:
                return True
            elif title[title.index(phrase) + len(phrase)] not in string.ascii_lowercase:
                return True
        else:
            return False



# Trigger whenever a description match a certain phrase
class DescriptionTrigger(PhraseTrigger):

    # Class constructor, store the user's desired trigger phrase
    def __init__(self, phrase):
        self.phrase = phrase

    # Evaluation to trigger, override the super class
    def evaluate(self, story):

        # First thing first, return false immediately
        # if we have a bad input
        if not self.is_phrase_valid(self.phrase):
            return False

        # Okay, phrase is good, proceed to clean up
        description = self.clean_up_text(story.get_description())
        phrase = self.phrase.lower()

        # Check if the phrase is in the description
        # then evaluate accordingly and terminate
        if phrase in description:
            if (description.index(phrase) + len(phrase)) > len(description) - 1:
                return True
            elif description[description.index(phrase) + len(phrase)] not in string.ascii_lowercase:
                return True
        else:
            return False


# Trigger based on time of article
class TimeTrigger(Trigger):

    # Class constructor
    def __init__(self, time):

        # Setup the standard time format
        time_format = "%d %b %Y %H:%M:%S"

        # Add exceptions here in case of erronous strings
        try:
            self.time = datetime.strptime(time, time_format)

            # Replace with EST timezone
            self.time = self.time.replace(tzinfo=pytz.timezone("EST"))
        except ValueError:
            print('Invalid input, please try again')



# Trigger anything happened before the set date
class BeforeTrigger(TimeTrigger):

    # Class constructor, inherit from super class
    def __init__(self, time):
        TimeTrigger.__init__(self, time)

    # Override super class evaluate function, return
    # true if the event is before the set date
    def evaluate(self, story):
        if self.time > story.pubdate:
            return True
        return False


# Trigger anything happened after the set date
class AfterTrigger(TimeTrigger):

    # Class constructor, inherit from super class
    def __init__(self, time):
        TimeTrigger.__init__(self, time)

    # Override super class evaluate function, return
    # true if the event is after the set date
    def evaluate(self, story):
        if self.time < story.pubdate:
            return True
        return False


# Composite NOT trigger
class NotTrigger(Trigger):

    # Class constructor, take a trigger
    def __init__(self, trigger):
        self.trigger = trigger

    # Override the superclass evaluate function,
    # invert the output of trigger evaluate function
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# Composite AND trigger
class AndTrigger(Trigger):

    # Class constructor, take 2 triggers
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2

    # Override the superclass evaluate function,
    # take the and logic of the two input triggers
    def evaluate(self, story):
        return self.trig1.evaluate(story) and self.trig2.evaluate(story)


# Composite OR trigger
class OrTrigger(Trigger):

    # Class constructor, take 2 triggers
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2

    # Override the superclass evaluate function,
    # take the or logic of the two input triggers
    def evaluate(self, story):
        return self.trig1.evaluate(story) or self.trig2.evaluate(story)


#======================
# Filtering
#======================

# Filter out stories that matches one trigger in the
# intput list of triggers 
def filter_stories(stories, triggerlist):

    # Making an emtpy list for filter here
    filtered = []

    # Start sorting our stories
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filtered.append(story)
                break

    # Finish and terminate
    return filtered



#======================
# User-Specified Triggers
#======================
# Generate a list of triggers based on the input triggers.txt
def read_trigger_config(filename):

    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # Dictionary to convert all string input to actual trigger class
    dict_conv = {
        'TITLE': TitleTrigger,
        'DESCRIPTION': DescriptionTrigger,
        'AFTER': AfterTrigger,
        'NOT': NotTrigger,
        'AND': AndTrigger,
        'OR': OrTrigger,
    }

    # Variable for return the list of triggers
    triggerlist = []

    # Iterating through chunks in our lines
    for chunk in lines:
        # Seperate based on the comma and assumed all trigger has custom name
        process = chunk.split(',')
        hasName = False

        # If we do manage to get a process, meaning there is
        # no trigger name
        if dict_conv.get(process[0], 0):
            hasName = True
        
        # Very manual way of inputting all elements into trigger objects,
        # let's leave it here now until I can find a better way
        if (hasName):
            triggerlist.append(dict_conv[process[0]](*process[1:]))
        else:
            process[0] = dict_conv[process[1]](*process[2:])
            triggerlist.append(process[0])
        
    # Return and terminate function
    return triggerlist



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # Import the trigger configuration file
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
