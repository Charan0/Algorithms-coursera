import random
import urllib.request

def downloadImage(urlImage):
    name = random.randrange(1, 1000)
    fullName = str(name) + ".jpg"
    urllib.request.urlretrieve(urlImage, fullName)

url = input("Enter the url: ")
downloadImage(url)