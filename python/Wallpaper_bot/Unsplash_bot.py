
import requests
import urllib.request as url

# Index variable to increment images in loop
index =0

# Using get method to fetch images from unpslash site using api.
# Follow below URL to create a developer account on unsplash and READ documentation
# Create your app, make a note of client ID.
# Follow the heirarchy of path
#URL/search/photos?query= "category of photos" &page= "number of pages" & perpage = "no of photos" & client ID (replace asteriks with your client ID
requestdump = requests.get('https://api.unsplash.com/search/photos?query=wallpaper&page=1&perpage=30&client_id= ***********************')

#try block to check exceptions
try:
    requestdump.raise_for_status()
except Exception as exc:
    print('There was a problem... ' + exc)

#converting to json dat
data = requestdump.json()
#Run below print statement to unleash a gigantic mumbo jumbo which reveals the 'keys' in data(keys are repeated for every image in data)
#print(data)

# For loop using 'results' key in data
for img_data in data['results']:

    # Assigning image ID as the name of the file
    file_name = str(img_data["alt_description"])[:4]+ ".jpg"
    # Assiging URL of raw format image, there are other formats named , full, regular, small.(Self explanatory unlike Starbucks)
    img_url = img_data['urls']['raw']
    url.urlretrieve(img_url, file_name)
    # Incrementing index value to fetch next one
    index +=1
    print("image downloaded" + str(index))
    
    




