
#!/bin/python2.7

import re
from sys import argv

dna = re.compile("[ATCG]+")
cons = False
i = 1
with open(argv[1]) as fin:
	for line in fin.readlines():
		if line.startswith("Consensus pattern"):
			outfile = argv[1].replace(".html", ".%i.cons.fa" %i)
			fout = open(outfile, "w")
			fout.write(">%s-%i repeat unit consensus\n" %(argv[1].split(".")[0], i))
			cons = True
			continue
		elif cons and line.strip() == "":
			cons = False
			try:	
				fout.write("\n")
				fout.close()
			except:
				pass				
			i += 1
			continue
		elif line.startswith("Done"):
			cons = False
			break
		
		if cons:
			fout.write(line.strip())
	

	try:	
		fout.write("\n")
		fout.close()
	except:
		pass				
