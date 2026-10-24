import sys, urllib.request
sys.path.insert(0, r'd:\scan1\Face matching\backend')

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/402px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg'
print("Downloading test image...")
urllib.request.urlretrieve(url, 'test_face.jpg')
print("Downloaded.")

from services.landmark_extractor import extract_landmarks

with open('test_face.jpg', 'rb') as f:
    data = f.read()

result = extract_landmarks(data, 'front')
if result:
    lm = result["landmarks"]
    print(f"Face detected! Landmarks shape: {lm.shape}")
    print(f"Image size: {result['image_width']}x{result['image_height']}")
else:
    print("ERROR: No face detected")
