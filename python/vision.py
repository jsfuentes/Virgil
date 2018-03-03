import requests

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
vision_analyze_url = vision_base_url + "analyze"
image_url = "http://onpointfresh.com/wp-content/uploads/2016/03/95559ca9a79f7da23522cb702e5eb2e8.jpg"

headers  = {'Ocp-Apim-Subscription-Key': '0727313b6afe4e82ad687fbd28c98345' }
params   = {'visualFeatures': 'Description,Tags,Faces'}
data     = {'url': image_url}
response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()
analysis = response.json()

print(analysis)
image_caption = analysis["description"]["captions"][0]["text"].capitalize()
print(image_caption)
