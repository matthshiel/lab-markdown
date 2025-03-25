

import json
import matplotlib.pyplot as plt
files = [
    r'C:\Users\ma386\CS40 projects\data\trump_tweet_data_archive-master\master_2009.json\master_2009.json', 
    r'C:\Users\ma386\CS40 projects\data\trump_tweet_data_archive-master\master_2010.json\master_2010.json',
    r'C:\Users\ma386\CS40 projects\data\trump_tweet_data_archive-master\master_2011.json\master_2011.json',
    r'C:\Users\ma386\CS40 projects\data\trump_tweet_data_archive-master\master_2012.json\master_2012.json',
    r'C:\Users\ma386\CS40 projects\data\trump_tweet_data_archive-master\master_2013.json\master_2013.json',
    r'C:\Users\ma386\CS40 projects\data\trump_tweet_data_archive-master\master_2014.json\master_2014.json',
    r'C:\Users\ma386\CS40 projects\data\trump_tweet_data_archive-master\master_2015.json\master_2015.json',
    r'C:\Users\ma386\CS40 projects\data\trump_tweet_data_archive-master\master_2016.json\master_2016.json',
    r'C:\Users\ma386\CS40 projects\data\trump_tweet_data_archive-master\master_2017.json\master_2017.json',
    r'C:\Users\ma386\CS40 projects\data\trump_tweet_data_archive-master\master_2018.json\condensed_2018.json'
    
]
all_tweets = []
for master in files:
    with open(master, encoding='utf-8') as f:
        text = f.read()
        data = json.loads(text)
        all_tweets.extend(data)



keywords = ['Obama', 'Trump', 'Mexico', 'Russia', 'Fake News', 'Illegal', 'Crooked', 'Weak']
keywords = sorted(['Obama', 'Trump', 'Mexico', 'Russia', 'Fake News', 'Illegal', 'Crooked', 'Weak'])
counts = {keyword.lower(): 0 for keyword in keywords}

for tweet in all_tweets:
    if 'text' in tweet:
        text = tweet['text'].lower()
        for keyword in keywords:
            if keyword.lower() in text:
                counts[keyword.lower()] += 1


print(f"counts= {counts}")

total_tweets = len(all_tweets)
percentages = {keyword.lower(): (count / total_tweets) * 100 for keyword, count in counts.items()}

for keyword, percentage in percentages.items():
    print(f"{keyword}: {percentage:.2f}%")


print("| {:>10} | {:>10} |".format("Keyword", "Percentage"))
print("|------------|------------|")
for keyword, percentage in percentages.items():
    print("| {:>10} | {:>05.2f} |".format(keyword, percentage))


keywords = list(counts.keys())
values = list(counts.values())

plt.figure(figsize=(10, 5))
plt.bar(keywords, values, color='blue')
plt.xlabel('Keywords')
plt.ylabel('Counts')
plt.title('Trumps famous diction')
plt.show()



quote_tweet_count = 0
original_tweet_count = 0

for tweet in all_tweets:
    if 'is_quote_status' in tweet:
        if tweet['is_quote_status']:
            quote_tweet_count += 1
        else:
            original_tweet_count += 1

print(f"Quote tweets: {quote_tweet_count}")
print(f"Original tweets: {original_tweet_count}")

labels = ['Quote Tweets', 'Original Tweets']
counts = [quote_tweet_count, original_tweet_count]

plt.figure(figsize=(10, 5))
plt.bar(labels, counts, color=['Purple', 'gold'])
plt.xlabel('Tweet Types')
plt.ylabel('Counts')
plt.title('Quote Tweets Or Original Tweets?')
plt.show()
