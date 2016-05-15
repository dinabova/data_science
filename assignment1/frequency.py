import sys
import json
import re


def hw(tweet_file):
    calc_terms_frequencies(tweet_file, debug_print=1)


def calc_terms_frequencies(tweet_file, debug_print=0):
    frequency_dict = {}
    total_words_count = 0
    for line in tweet_file:
        words = get_words_for_single_tweet_line(line)
        for word in words:
            if len(word) < 2:
                continue
            if not frequency_dict.has_key(word):
                frequency_dict[word] = 0.0
            frequency_dict[word] += 1.0
            total_words_count += 1

    if total_words_count == 0:
        return frequency_dict

    for term in frequency_dict.keys():
        frequency_dict[term] /= total_words_count
        if debug_print:
            print term, round(frequency_dict[term], 4)

    return frequency_dict


def get_words_for_single_tweet_line(line):
    words = []
    try:
        tweet_data = json.loads(line.strip())
    except:
        return words
    if tweet_data.has_key('text'):
        tweet_text = tweet_data["text"]
        tweet_text = tweet_text.strip()
        if tweet_text != '':
            words = re.split('[^a-z]+', tweet_text.lower())
    return words


def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

    tweet_file.close()


if __name__ == '__main__':
    main()
