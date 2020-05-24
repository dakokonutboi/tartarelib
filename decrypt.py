import rsa
import sys

priv = eval("rsa."+str(sys.argv[1]))
msg = eval(str(sys.argv[2]).replace("[GUI]",'"').replace("[ASL]","\\"))

print(str(rsa.decrypt(msg,priv).decode('utf8')))
