import requests
from secret import VISION_API_KEY

#TODO: Can get face box, maybe go to clothing box
def getSubjectByUrl(image_url, debug=False):
    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
    vision_analyze_url = vision_base_url + "analyze"

    headers  = {'Ocp-Apim-Subscription-Key': VISION_API_KEY }
    params   = {'visualFeatures': 'Description,Tags,Faces'}
    data     = {'url': image_url}
    response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
    response.raise_for_status()
    analysis = response.json()

    topSubject = analysis['tags'][0]['name']
    print(topSubject)
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    print(image_caption)
    return topSubject

def getSubjectByImage(binaryImg, debug=False):
    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
    vision_analyze_url = vision_base_url + "analyze"

    headers  = {'Ocp-Apim-Subscription-Key': VISION_API_KEY,
                'Content-Type': 'application/octet-stream'}
    params   = {'visualFeatures': 'Description,Tags,Faces'}

    response = requests.post(vision_analyze_url, headers=headers, params=params, data=binaryImg)
    response.raise_for_status()
    analysis = response.json()

    try:
        topSubject = analysis['tags'][0]['name']
    except:
        topSubject = None

    if not topSubject:
        topSubject = analysis["description"]["captions"][0]["text"].capitalize()
    print(topSubject)
    return topSubject

if __name__ == "__main__":
    image_url = "http://onpointfresh.com/wp-content/uploads/2016/03/95559ca9a79f7da23522cb702e5eb2e8.jpg"
    image_url2 = "https://www.fatrabbitcreative.com/images/blog/red.jpg"
    getSubject(image_url)
