#!/usr/bin/python3

import cgi, subprocess as sp

print("content-type: text/html")
print()


clientData = cgi.FieldStorage()
x = clientData.getvalue("cmd")
clientcmd = "sudo {}".format(x)
#print("testing")

output = sp.getstatusoutput(clientcmd)
status = output[0]
result = output[1]
if status == 0:
   print(f" {result} ")
else:
   print(f"There is some problem, {stauts} ")


