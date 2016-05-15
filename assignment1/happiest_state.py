import sys
import json
import re


def hw(sent_file, tweet_file, us_states_shortnames_dict):
    sentiments_scores_dict = read_sentiments_scores(sent_file)
    state = calc_happiest_state(tweet_file, sentiments_scores_dict, us_states_shortnames_dict)
    print state


def lines(fp):
    print(str(len(fp.readlines())))


def read_sentiments_scores(sent_file):
    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores


def calc_happiest_state(tweet_file, sentiments_scores_dict, us_states_shortnames_dict):
    states_scores = {}
    for line in tweet_file:
        try:
            tweet_data = json.loads(line.strip())
        except:
            continue

        us_state = get_single_tweet_us_state(tweet_data, us_states_shortnames_dict)
        if us_state != '':
            tweet_score, words = calc_sentiment_score_for_single_tweet_data(tweet_data, sentiments_scores_dict)
            if not states_scores.has_key(us_state):
                states_scores[us_state] = [0.0, 0.0]
            state_data = states_scores[us_state]
            state_data[0] += tweet_score
            state_data[1] += 1.0

    max_score = -1000
    max_score_state = ''
    for state in states_scores.keys():
        state_score_sum, count = states_scores[state]
        state_score = round(state_score_sum / count, 5)
        states_scores[state] = state_score
        if state_score > max_score:
            max_score = state_score
            max_score_state = state

    return max_score_state



def calc_sentiment_score_for_single_tweet_data(tweet_data, sentiments_scores_dict):
    tweet_score_sum = 0
    num_sentiment_words = 0
    words = []
    if tweet_data.has_key('text'):
        tweet_text = tweet_data["text"]
        tweet_text = tweet_text.strip()
        if tweet_text != '':
            words = re.split('[^a-z]+', tweet_text.lower())
            for word in words:
                if len(word) < 2:
                    continue
                if sentiments_scores_dict.has_key(word):
                    tweet_score_sum += sentiments_scores_dict[word]
                    num_sentiment_words += 1
    tweet_score = float(tweet_score_sum) / max(num_sentiment_words, 1)
    return tweet_score, words


def get_single_tweet_us_state(tweet_data, us_states_shortnames_dict):
    us_state = ''
    location = get_single_tweet_location(tweet_data)
    if location != '':
        us_state = get_us_state_shortname(location, us_states_shortnames_dict)
    return us_state


def get_single_tweet_location(tweet_data):
    if tweet_data.has_key("place"):
        place_data = tweet_data["place"]
        if place_data and place_data.has_key("full_name"):
            place_name = place_data["full_name"]
            if place_name:
                place_name = place_name.encode('utf-8')
                return place_name

    if tweet_data.has_key("user"):
        user_data = tweet_data["user"]
        if user_data and user_data.has_key("location"):
            location_name = user_data["location"]
            if location_name:
                location_name = location_name.encode('utf-8')
                return location_name

    return ''


def get_us_state_shortname(location_name, us_states_shortnames_dict):
    location_name = location_name.lower().strip()
    location_name_words = re.split('[^a-z]+', location_name)

    states_dict = us_states_shortnames_dict
    for word in location_name_words:
        if states_dict.has_key(word):
            item = states_dict[word]
            if isinstance(item, str):
                return item
            states_dict = item

    return ''




states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

def states_shortnames(states_dict):
    states_shortnames = {}
    for shortname in states_dict.keys():
        fullname = states_dict[shortname].lower()

        fullname_splitted = fullname.split(' ')
        if len(fullname_splitted) > 1:
            cur_dict = states_shortnames
            for word in fullname_splitted[0:-1]:
                if cur_dict.has_key(word):
                    cur_dict = cur_dict[word]
                    continue
                cur_dict[word] = dict()
                cur_dict = cur_dict[word]

            last_word = fullname_splitted[-1]
            cur_dict[last_word] = shortname
        else:
            states_shortnames[fullname] = shortname

        #states_shortnames[shortname.lower()] = shortname

    return states_shortnames



def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    us_states_shortnames_dict = states_shortnames(states)

    hw(sent_file, tweet_file, us_states_shortnames_dict)

    tweet_file.close()
    sent_file.close()


if __name__ == '__main__':
    main()
