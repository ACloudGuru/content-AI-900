from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os

os.system("color")
class colors:
    green = '\033[92m'
    blue = '\033[94m'
    red = '\033[31m'
    yellow = '\033[33m'
    reset = '\033[0m'

cog_endpoint = os.environ.get('azurecognitiveservicesendpoint')
cog_key = AzureKeyCredential(os.environ.get('azurecognitiveserviceskey'))
text_analytics_client = TextAnalyticsClient(endpoint=cog_endpoint, credential=cog_key)


# Change the lines below in quotes to try your own sentence! 
review = ["This was a great meal, I would eat here anytime!"]

key_phrase = ["We should make a run for it! We don't want to be caught out in a thunderstorm!"]

entities = ["Clint is going to Europe next week. He'll be there from 12-15th of August. \
    There is 90% chance you can find him in a World War 2 Museum at some point"]




sentiment_analysis = text_analytics_client.analyze_sentiment(documents=review)
print("\n-----Sentiment Analysis-----")
print(f"{colors.blue}The sentence to analyze: {colors.reset}" + str(review))
for result in sentiment_analysis:
    print(f"{colors.green}Sentiment: {colors.reset}" + result.sentiment)
    print(f"{colors.green}Confidence: {colors.reset}" + str(result.confidence_scores))
print("----------\n")

input("Press Enter to continue to key phrases...\n")

print("\n-----Key Phrases-----")
print(f"{colors.blue}The sentence to analyze:  {colors.reset}" + str(key_phrase))
key_phrase_analysis = text_analytics_client.extract_key_phrases(documents=key_phrase)
for result in key_phrase_analysis:
    print(f"{colors.green}Key Phrases: {colors.reset}" + str(result.key_phrases))
print("----------\n")

input("Press Enter to continue to entities...\n")

print("\n-----Entities-----")
print(f"{colors.blue}The sentence to analyze:  {colors.reset}" + str(entities))
entity_analysis = text_analytics_client.recognize_entities(documents=entities)
for result in entity_analysis:
    for entity in result.entities:
        print(f"{colors.green}Entity:{colors.reset} {entity.text:<30}", 
        f" {colors.yellow}Category:{colors.reset} {entity.category:<15}", 
        f" {colors.red}Confidence:{colors.reset} {entity.confidence_score:<4}")
print("----------\n")


input("Press Enter to exit...\n")