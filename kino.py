import urllib2
import json
import datetime

cur_date=datetime.datetime.now()


def compare_lists(l1,l2):
  p=0
  for i in l1:
    if i in l2:
      p+=1
  return p

numbers=[]
megistoi=[]
epanalipsi=[]
mera=[]
print "Give 10 numbers"
numbers = raw_input()
lista = map(int, numbers.split())
for i in range (31):
  cur_date= cur_date - datetime.timedelta(days=1)
  date_str= cur_date.strftime("%d-%m-%Y")
  url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
  req= urllib2.Request(url)
  response = urllib2.urlopen(req)
  data = response.read()
  data = json.loads(data)
  klhrwseis= data['draws']['draw']
  r=[]
  for k in klhrwseis:
    temp=k["results"]
    r.append (compare_lists(lista,temp))
  if max(r)>4:
      megistoi.append(max(r))
      epanalipsi.append(r.count(max(r)))
      mera.append(date_str)
thesi = []
for i in range(31):
    if megistoi[i] == max(megistoi):
        thesi.append(i)
temp2 = epanalipsi[0]
for i in thesi:
    if epanalipsi[i] > temp2 :
        temp2 = epanalipsi[i]
print " "        
print "Your lucky day(s) :"
for i in thesi:
    print mera[i]
