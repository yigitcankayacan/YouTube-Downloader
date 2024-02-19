import pytube

url= input("enter video url: ")

path="C:\YouTube_Python"

pytube.YouTube(url).streams.get_highest_resolution().download(path)