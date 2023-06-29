import requests
import wget
import zipfile
import os
print("Downloading latest Chrome Driver")
# get the latest chrome driver version number
url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
response = requests.get(url)
version_number = response.text
print("Latest Chrome Driver version is: " + version_number)

# build the donwload url
download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

# download the zip file using the url built above
latest_driver_zip = wget.download(download_url,'chromedriver.zip')
print("Latest Chrome Driver downloaded is: " + latest_driver_zip)

# extract the zip file
with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
    zip_ref.extractall() # you can specify the destination folder path here
# delete the zip file downloaded above

print("Deleting the zip file downloaded")
os.remove(latest_driver_zip)

print("Latest Chrome Driver path is: " + os.getcwd() + "\chromedriver.exe")

# add the chromedriver.exe to the path for linux and mac
os.environ["PATH"] += os.pathsep + os.getcwd()
