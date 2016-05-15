import sys
import json



def hw(tweet_file):
    sorted_hashtags = get_sorted_hashtags_by_appearances(tweet_file, debug_print=0)
    max_num = min(len(sorted_hashtags), 10)

    for i in range(max_num):
        count, hashtag = sorted_hashtags[i]
        print hashtag, count




def get_sorted_hashtags_by_appearances(tweet_file, debug_print=0):
    appearances_dict = calc_hashtags_appearances(tweet_file, debug_print=debug_print)

    hashtags = []
    for hashtag in appearances_dict:
        count = appearances_dict[hashtag]
        hashtags.append((count, hashtag))

    return sorted(hashtags, reverse=True)



def calc_hashtags_appearances(tweet_file, debug_print=0):
    appearances_dict = {}

    for line in tweet_file:
        try:
            tweet_data = json.loads(line.strip())
        except:
            continue
        hashtags = get_single_tweet_hashtags(tweet_data)
        for hashtag in hashtags:
            if not appearances_dict.has_key(hashtag):
                appearances_dict[hashtag] = 0
            appearances_dict[hashtag] += 1

    return appearances_dict





def get_single_tweet_hashtags(tweet_data):
    hashtags_items_list = []
    if tweet_data.has_key("entities"):
        entity_data = tweet_data["entities"]
        if entity_data and entity_data.has_key("hashtags"):
            hashtags_items_list = entity_data["hashtags"]

    if len(hashtags_items_list)==0 and tweet_data.has_key("user"):
        user_data = tweet_data["user"]
        if user_data and user_data.has_key("hashtags"):
            hashtags_items_list = user_data["hashtags"]

    hashtags_list = []
    for hashtag_item_dict in hashtags_items_list:
        if hashtag_item_dict.has_key('text'):
            hashtag = hashtag_item_dict['text']
            hashtags_list.append(hashtag.encode('utf-8'))

    return hashtags_list





def main():
    tweet_file = open(sys.argv[1])

    hw(tweet_file)

    tweet_file.close()


if __name__ == '__main__':
    main()
