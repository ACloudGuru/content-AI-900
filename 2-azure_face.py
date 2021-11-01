import requests
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
import os

os.system("color")
class colors:
    green = '\033[92m'
    blue = '\033[94m'
    red = '\033[31m'
    yellow = '\033[33m'
    reset = '\033[0m'

cog_endpoint = os.environ.get('azurecognitiveservicesendpoint')
cog_key = os.environ.get('azurecognitiveserviceskey')


# Change the URL between the quotes below to run your own faces through the Azure Face Service!
face_to_analyze = "https://raw.githubusercontent.com/ACloudGuru/content-AI-900/main/images/image-analysis/2-azureface-family.jpg"


face_client = FaceClient(cog_endpoint, CognitiveServicesCredentials(cog_key))

detected_faces = face_client.face.detect_with_url(url=face_to_analyze, detection_model='detection_01', 
return_face_attributes=list(['age','gender','headPose','smile','facialHair','glasses','emotion'
,'hair','makeup','accessories','blur','exposure','noise']), 
return_face_landmarks=True)
if not detected_faces:
    print("No faces were found in the image! Please try another image!")
    input("Press Enter to exit")
    quit()

print("\n-----Facial Attributes-----")
for count, face in enumerate(detected_faces):
    print()
    print(f"{colors.green}\nPerson Number: {colors.reset}" + str(count))
    print(f"{colors.yellow}\nAge: {colors.reset}" + str(face.face_attributes.age))
    print(f"{colors.red}\nDetected Gender: {colors.reset}" + str(face.face_attributes.gender))
    print(f"{colors.blue}\nEmotions: {colors.reset}" + str(face.face_attributes.emotion))
    print(f"{colors.green}\nFacial Hair: {colors.reset}" + str(face.face_attributes.facial_hair))
    print(f"{colors.yellow}\nGlasses: {colors.reset}" + str(face.face_attributes.glasses))
    print(f"{colors.red}\nSmile: {colors.reset}" + str(face.face_attributes.smile))
    print(f"{colors.blue}\nMakeup: {colors.reset}" + str(face.face_attributes.makeup))
    for hair in face.face_attributes.hair.hair_color:
        print(f"{colors.green}\nHair: {colors.reset}" + str(hair.color))
        break
    print("\n----------\n")

input("Press Enter to continue to displaying face frames...\n")

print("\n-----Face Frames-----")

# Convert width height to a point in a rectangle
def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height
    
    return ((left, top), (right, bottom))

def drawFaceRectangles() :
    # Download the image from the url
    response = requests.get(face_to_analyze)
    img = Image.open(BytesIO(response.content))

    # For each face returned use the face rectangle and draw a red box.
    print('Drawing rectangle around face... ')
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        draw.rectangle(getRectangle(face), outline='red')

    # Display the image in the default image browser.
    img.show()

drawFaceRectangles()

input("\nPress Enter to Exit...")
