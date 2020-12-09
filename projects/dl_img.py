import urllib.request

def download_img(url,filepath,filename):
	fullpath=filepath+filename+'.jpg'
	urllib.request.urlretrieve(url,fullpath)

url=input('Enter the image url: ')
filename=input('Enter the download name: ')

download_img(url,'images/',filename)


