#!/usr/bin/python

import json, mymodule_091620

class job():
  jobtitle = 'Job Title Very Important'
  jobpay = 'Job Pay Very Important too'

  def __init__(self, title, location):
    self.title = title
    self.location = location

  def maintool(self, tool):
    print('Engineer like ' + self.title + ' Mainly work with ' + tool + ' every day ') 

  def cloudtype(self, types):
    print('Engineer title like {} usually loves cloud type such as {}'.format(self.title,types))

j1 = job('Infrastructure Engineer', 'Dublin')
print(j1.title)
print(j1.jobtitle)

j1.maintool('Terraform')

j1.cloudtype('Amazon AWS')

# class inherence

class job2(job):
  pass

j2 = job2('SRE', 'SF')
j2.maintool('Kubernetes')

thisdict = {
  "Mon": "One",
  "Tue": "Two",
  "Wed": "Three"
}

for a in thisdict:
  print(a)

for b in thisdict:
  print(thisdict[b])

thisdict["Thurs"] = "Four"
print(thisdict)

thatlist = ["a", "b", "c", "d"]

for c in thatlist:
  print(c)

thatlist.append('e')

print(thatlist)


d = '{"mon":"one", "tue":"two", "wed":"three"}'
e = json.loads(d)
print(e['mon'])

day = 'Wed'

if day == 'Wed':
  print('Today is Wed')
else:
  print('Today is NOT Wed')

grade = 6

print('You are at grade ' + str(grade) + ' now ')

while grade < 12:
  grade += 1
  print('You will be grade ' +str(grade) + ' next year ')
 
print('After finish above grades you will be entering college !!!')  

weeekday = 'Wed'

try:
  print(weekday)
except:
  print('weekday is NOT defined')

# how to add two lists together

first = ['a', 'b', 'c']
second = ['d', 'e', 'f']

for f in second:
  first.append(f)

print(first) 
  
g = open('list', 'ro')
print(g.read())

mymodule_091620.greeting('Jordan')

h = {
  "one": "mon",
  "two": "tue",
  "three": "wed"
}

i = json.dumps(h)
print(i)
