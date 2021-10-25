from urllib.request import urlretrieve
link = input("Enter your link : ")
fileName = input ("Enter Your File Name : ")

urlretrieve(link,'images/'+ fileName + '.jpg')
