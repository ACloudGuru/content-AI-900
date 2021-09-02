from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os
cog_endpoint = os.environ.get('azurecognitiveservicesendpoint')
cog_key = os.environ.get('azurecognitiveserviceskey')


# Change the URL between the quotes below to run your own images!
image_to_analyze = "https://raw.githubusercontent.com/ACloudGuru/content-AI-900/main/images/image-analysis/1-computervision-couple.jpg"


computervision_client = ComputerVisionClient(cog_endpoint, CognitiveServicesCredentials(cog_key))

image_analysis = computervision_client.analyze_image(image_to_analyze,visual_features=[VisualFeatureTypes.description,
 VisualFeatureTypes.tags, VisualFeatureTypes.faces])

print("\n-----Image Description-----")
for caption in image_analysis.description.captions:
    print("Confidence: " + str(caption.confidence))
    print("Description: " + caption.text)
print("----------\n")


input("Press Enter to continue to image tags...\n")


print("-----Image Tags-----")
for tag in image_analysis.tags:
    print(tag)
print("----------\n")


input("Press Enter to continue to face detection...\n")


print("-----Face Detection-----")
for face in image_analysis.faces:
    print("detected age: " + str(face.age))
    print("detected gender: " + face.gender)
print("----------")

input("\nPress Enter to Exit...")
