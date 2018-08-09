import pickle,requests
dic={"main":[]}
r=requests.get("http://127.0.0.1:8000/media/documents/Http_Proxies.txt")
data=r.text
temp=data.split("\n")
for a in temp:
    print (a)
##f=open('proxies.txt','r')
##f1=open('new','wb')
##dic["main"]=f.readlines()
##print(type(dic))
##pickle.dump(dic,f1)
##f1=open('new','rb')
##for a in pickle.load(f1)["main"]:
##    print(a)
##for a in f1.readlines()[main]
