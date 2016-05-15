import sys
import json
import re


def hw(sent_file, tweet_file):
    sentiments_scores_dict = read_sentiments_scores(sent_file)
    read_tweet_data_and_calc_scores(tweet_file, sentiments_scores_dict)


def lines(fp):
    print(str(len(fp.readlines())))


def read_sentiments_scores(sent_file):
    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores


def read_tweet_data_and_calc_scores(tweet_file, sentiments_scores_dict):
    tweet_scores = []
    for line in tweet_file:
        tweet_score, words = calc_sentiment_score_for_single_tweet_line(line, sentiments_scores_dict)
        tweet_scores.append(tweet_score)
        print tweet_score

    return tweet_scores


def calc_sentiment_score_for_single_tweet_line(line, sentiments_scores_dict):
    try:
        tweet_data = json.loads(line.strip())
    except:
        return 0, []
    return calc_sentiment_score_for_single_tweet_data(tweet_data, sentiments_scores_dict)


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


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    hw(sent_file, tweet_file)

    #lines(sent_file)
    #lines(tweet_file)

    tweet_file.close()
    sent_file.close()


if __name__ == '__main__':
    main()
