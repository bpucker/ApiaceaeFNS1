[![DOI](https://zenodo.org/badge/456032863.svg)](https://zenodo.org/badge/latestdoi/456032863)

# Apiaceae FNS I
These scripts were applied to study the evolution of _FNS I_ in the Apiaceae. Please cite the corresponding publication when using these scripts.


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
    --number STR        Number of BLAST hits to consider.[10]
```

`--baits` FASTA file containing the bait sequences.

`--out` is the output folder. The folder will be created if it does not exist already.

`--subject` is the subject file for the screen via BLAST. Candidates will be identified in this collection of sequences.

`--subjectdir` is a folder containig the subject files. This option allows the automatic collection of sequences from multiple different species. This option prevents the need to run the analysis multiple times with different subject files.

`--number` defines how many different BLAST hits will be considered per query. A non-redundant set of sequences will be collected per subject sequence. Increasing this number make the search more sensitive, but also computationally more expensive. Default: 10.


## Extract sequences of highlighted clade
Extract the sequences belonging to IDs that are highlighted in a phylogenetic tree. This script enables the selection of specific clades after inspecting a tree in FigTree. It is important that the "Clade" is selected and colored in red (R=255, G=0,B=0; default) or any other color of choice. The color needs to be specified if it is not red.

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

`--tree` phylogenetic tree file. One clade is highlighted by a color ('clade' needs to be highlighted via FigTree). The color string attached to the sequence names is used for the extraction of the IDs of interest and used for the collection of these sequences in a new file.

`--out` output FASTA file contains the sequences of the highlighted IDs.

`--seq` FASTA input file contains all sequences that were used for the phylogenetic tree construction. A subset of these sequences will be written into the output file.

`--taxon` this taxon file allows to connect IDs in the tree file to different IDs in the FASTA input file. This is necessary if sequence IDs were replaced by sequence names after constructing the tree. If possible, the need for this option should be avoided.

`--color` color that was used to highlight one clade in the tree file. Default color is red (#ff0000). FigTree provides an option to set the color. The default red is R=255, G=0, and B=0.





## TBLASTN-based check of genes missing in annotation
This scripts performs a search for genes that were missed in the annotation process. The results of a TBLASTN are processed and hits are compared against the annotated genes in a GFF3 file. If a gene is bit by BLAST, the ID is returned in the output file. The genomic position of a BLAST hit is returned if no gene is hit. This enables a phylogenetic evaluation of the candidates.


```
Usage:
  python3 TBLASTN_check.py --in <FILE> --out <FILE> --ref <FILE> --gff <FILE>

Mandatory:
  --in    STR   FASTA file. 
  --out   STR   Ouptut folder.
  --ref   STR   Reference FASTA file.
  --gff   STR   Annotation file.
```

`--in` FASTA input file containing the bait sequence(s).

`--out` output folder for temporary and final output files. This folder will be created if it does not exist already.

`--ref` genome sequence FASTA file.

`--gff` annotation file (GFF3) corresponding to the genome sequence FASTA file.



## References



