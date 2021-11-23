import os
import json
import glob
from multiprocessing import Pool
import pubmed_parser as pp

def process_pubmed_file(filename):
	dicts_out = pp.parse_medline_xml(filename,
                                 year_info_only=False,
                                 nlm_category=False,
                                 author_list=False,
                                 reference_list=False)
                                 
	articles_with_nct = [d for d in dicts_out if d['NCTs']]
	output_file = filename.split('.')[-3].split('/')[-1] + '.json'
	output_file = os.path.join(output_dir, output_file)
	with open(output_file, 'w') as fp:
		for d in articles_with_nct:
			json.dump(d, fp)
			fp.write('\n')

output_dir = './output'
if not os.path.exists(output_dir):
	os.makedirs(output_dir)
baselines = glob.glob('*.xml.gz')
dailies = glob.glob('./daily/*.xml.gz')
all_dumps = baselines + dailies

p = Pool(4)
p.map(process_pubmed_file, all_dumps)




