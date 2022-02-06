### Boas Pucker ###
### bpucker@cebitec.uni-bielefeld.de ###
__version__ = "v0.28"	#converted to Python3

__usage__ = """
							python3 collect_best_BLAST_hits.py
							--baits <BAIT_FILE>
							--subject <SUBJECT_FILE>|--subjectdir <FOLDER_WITH_SUBJECT_FILES>
							--out <OUTPUT_FOLDER>
							--number <INT>
							"""

import os, sys, subprocess, glob
from operator import itemgetter

# --- end of imports --- #

def load_best_blast_hits( blast_result_file, number ):
	"""! @brief load best blast hit per query """
	
	# --- initial loading --- #
	best_hits = {}
	with open( blast_result_file, "r" ) as f:
		line = f.readline()
		while line:
			parts = line.strip().split('\t')
			try:
				best_hits[ parts[0] ].append( { 'score': float( parts[-1] ), 'seqID': parts[1] } )
			except:
				best_hits.update( { parts[0]: [ { 'score': float( parts[-1] ), 'seqID': parts[1] } ] } )
			line = f.readline()
	
	selected_hits = []
	for bait in list( best_hits.values() ):
		if len( bait ) > number:
			sorted_hits = list( sorted( bait, key=itemgetter('score') ) )[::-1]
			i = 0
			while i < number:
				selected_hits.append( sorted_hits[i]['seqID'] )
				i += 1
		else:
			for each in bait:
				selected_hits.append( each['seqID'] )
	
	return list( set( selected_hits ) )


def load_sequences( fasta_file ):
	"""! @brief load candidate gene IDs from file """
	
	sequences = {}
	with open( fasta_file ) as f:
		header = f.readline()[1:].strip()
		if " " in header:
			header = header.split(' ')[0]
		seq = []
		line = f.readline()
		while line:
			if line[0] == '>':
					sequences.update( { header: "".join( seq ) } )
					header = line.strip()[1:]
					if " " in header:
						header = header.split(' ')[0]
					seq = []
			else:
				seq.append( line.strip() )
			line = f.readline()
		sequences.update( { header: "".join( seq ) } )	
	return sequences


def main( arguments ):
	
	bait_file = arguments[ arguments.index('--baits')+1 ]
	if "--subject" in arguments:
		subject_files = [ arguments[ arguments.index('--subject')+1 ] ]
	else:
		input_dir = arguments[ arguments.index('--subjectdir')+1 ]
		if input_dir[-1] != "/":
			input_dir += "/"
		subject_files = sorted( glob.glob( input_dir + "*.fasta" ) + glob.glob( input_dir + "*.fa" ) + glob.glob( input_dir + "*.faa" ) + glob.glob( input_dir + "*.FASTA" ) + glob.glob( input_dir + "*.FA" ) + glob.glob( input_dir + "*.FAA" ) )
	general_output_folder = arguments[ arguments.index('--out')+1 ]
	if "--number" in arguments:
		number = int( arguments[ arguments.index('--number')+1 ] )
	else:
		number = 10
	
	cpu = 4
	
	for sidx, subject_file in enumerate( subject_files ):
		try:
			ID = subject_file.split('/')[-1].split('.')[0]
		except:
			ID = str( sidx+1 )
		if len( subject_files ) == 1:
			output_folder = general_output_folder + ""
		else:
			output_folder = general_output_folder + ID + "/"
	
		if not os.path.exists( output_folder ):
			os.makedirs( output_folder )
		
		# --- prepare blastdb --- #
		blastdb = output_folder + "blastdb"
		p = subprocess.Popen( args= " ".join( [ "makeblastdb -in", subject_file, "-out", blastdb, "-dbtype prot" ] ), shell=True )
		p.communicate()
		
		# --- run BLASTp search --- #
		result_file = output_folder + "blast_results.txt"
		if not os.path.isfile( result_file ):
			p = subprocess.Popen( args= " ".join( [ "blastp -query", bait_file, "-db", blastdb, "-out", result_file, "-outfmt 6 -evalue 0.001 -num_threads", str( cpu ) ] ), shell=True )
			p.communicate()
		
		# --- load best BLAST hits per query --- #
		best_blast_hits =  load_best_blast_hits( result_file, number )
		
		# --- collect sequences --- #
		seqs = load_sequences( subject_file )
		output_file = output_folder + "best_hit_sequences.fasta"
		counter = 0
		with open( output_file, "w" ) as out:
			for ID in best_blast_hits:
				try:
					out.write( '>' + ID + "\n" + seqs[ ID ] + "\n" )
					counter += 1
				except KeyError:
					pass
		print ("Number of selected sequences: " + str( counter ) )


if '--baits' in sys.argv and '--subject' in sys.argv and '--out' in sys.argv:
	main( sys.argv )
elif '--baits' in sys.argv and '--subjectdir' in sys.argv and '--out' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )
