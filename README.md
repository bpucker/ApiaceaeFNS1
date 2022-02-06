# ApiaceaeFNS1
These scripts were applied to study the evolution of FNS I in the Apiaceae. Please cite the corresponding publication when using these scripts.


## Collect best BLAST hits
This script performs an automatic collection of sequences with some similarity to the bait sequences. Since BLAST does not allow the reliable identification of orthologs, a following validation through a phylogenetic analysis is necessary for most applications.


```
Usage:
  python collect_best_BLAST_hits.py --baits <FILE> --out <DIR> [--subject <FILE>|--subjectdir <DIR>]

Mandatory (option1):
  --baits      STR         A multiple FASTA file. 
  --out        STR         Directory for temporary and output files.
  --subject    STR         Subject sequence file.

Mandatory (option2):
  --baits      STR         A multiple FASTA file. 
  --out        STR         Directory for temporary and output files.
  --subjectdir STR         Folder containing subject sequence files.

Optional:
    --number STR        Number of BLAST hits to consider.
```

`--baits` FASTA file containing the bait sequences.

`--out` is the output folder. The folder will be created if it does not exist already.

`--subject` is the subject file for the BLAST search. Candidates will be identified in this collection of sequences.

`--subjectdir` is a folder containig the subject files. This option allows the automatic collection of sequences from multiple different species. This option prevents the need to run the analysis multiple times with different subject files.


## Extract sequences of highlighted clade
Extract the sequences belonging to IDs that are highlighted in a phylogenetic tree. This scripts enables to selection of specific clades after inspecting a tree.

```
Usage:
  python extract_red.py --tree <FILE> --out <FILE> --seq <FILE>

Mandatory:
  --tree    STR   Tree file. 
  --out     STR   Sequence ouptut file.
  --seq     STR   Sequence input file.

Optional:
    --taxon STR   Taxon file.
    --color STR   Color of highlighted clade.[#ff0000]
```

`--tree` phylogenetic tree file. One clade is highlighted by a color (clade needs to be highlighted via FigTree). The color string attached to the sequence names is used for the extraction of the IDs of interest and used for the collection of these sequences in a new file.

`--out` output FASTA file contains the sequences of the highlighted IDs.

`--seq` FASTA input file contains all sequences that were used for the phylogenetic tree construction. A subset of these sequences will be written into the output file.

`--taxon` this taxon file allows to connect IDs in the tree file to different IDs in the FASTA input file. This is necessary if sequence IDs were replaced by sequence names.

`--color` color that was used to highlight one clade in the tree file. Default color is red (#ff0000).





## TBLASTN-based check of genes missing in annotation



## References



