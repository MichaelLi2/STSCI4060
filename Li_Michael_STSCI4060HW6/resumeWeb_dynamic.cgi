#!/usr/bin/env python

'''Prompt user for resume info and displays a web page with their resume.'''
import scipy as sp
import cgi

def main():
  form=cgi.FieldStorage()
  firstName=form.getfirst('firstName','')
  lastName=form.getfirst('lastName','')
  address=form.getfirst('address','')
  phone=form.getfirst('phone','')
  email=form.getfirst('email','')
  uMajor=form.getfirst('umajor','')
  uSchool=form.getfirst('uschool','')
  uAddress=form.getfirst('uschoolAddress','')
  cMajor=form.getfirst('cmajor','')
  cSchool=form.getfirst('cschool','')
  cAddress=form.getfirst('cschoolAddress','')
  career=form.getfirst('career','')
  skills=form.getfirst('skills','')
  #print form
  print makePage('resumeTemplate.html', (firstName, lastName, phone, email, address, career, cSchool, cAddress, cMajor, uSchool, uAddress, uMajor, skills))

def filetoStr(fileName):
  '''Return a string containing the contents of the named file.'''
  fin = open(fileName);
  contents = fin.read();
  fin.close()
  return contents

def makePage(templateFileName, subsitutions):
  template = filetoStr(templateFileName)
  return template % subsitutions

#Don't think I actually need these functions????
#def strToFile(text, filename):
#  output = file(filename, 'w')
#  output.write(text)
#  output.close()

#def browseLocal(webpageText, filename):
#  strToFile(webpageText, filename)
#  import webbrowser
#  webbrowser.open(filename)


try:
  print "Content-type: text/html\n\n"
  main()
except:
  cgi.print_exception()
