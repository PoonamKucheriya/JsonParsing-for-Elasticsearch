import json
import os
fh = open("movies.json")
jdata = json.loads(fh.read())
outfile = open("movies_parsed.json","w")
for i in range(len(jdata)):
   	outfile.write(json.dumps({'index':{'_id': '%s' %i,'_index':'test','_type':'type1'}}))
   	outfile.write("\n")
   	outfile.write(json.dumps(jdata[i]))
   	outfile.write("\n")
	outfile.close()	