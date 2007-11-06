#!/usr/bin/python

from re import compile,DOTALL,MULTILINE

enum = compile("static PkEnumMatch enum_([^\]]+)\[\] = {(.*?)};", DOTALL|MULTILINE)
value = compile("PK_([A-Z]+)_ENUM_([A-Z_]+),\s+\"([^\"]+)\"")

inp = open("../libpackagekit/pk-enum.c").read()

names = {}

print "class PackageKitEnum:"
for (name,data) in enum.findall(inp):
	print "\t%s = ("%name,
	for (type,enum,string) in value.findall(data):
		print "\"%s\","%string,
		names["%s_%s"%(type,enum)] = string
	print ")"

print "\n# Constants\n"

for k in sorted(names.keys()):
	print '%s = "%s"'%(k,names[k])

