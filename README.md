# GenParse

GenParse is a lightweight Python framework for working with common genomic file formats.
It includes parsers for FASTA, FASTQ, and GFF/GTF files, utilities for computing basic
sequence statistics, simple global sequence alignment, genomic feature intersection, and
helpers for plotting statistics.

## Installation

```
pip install matplotlib
```

Clone this repository and use the modules directly or install as a package.

## Example Usage

```python
from genparse import parse_fasta, gc_content, sequence_lengths, plot_length_distribution

records = list(parse_fasta('example.fa'))
lengths = sequence_lengths(r.sequence for r in records)
print('GC%:', gc_content(records[0].sequence))
plot_length_distribution(lengths)
```

## Simulating Sequences

Generate random sequences of specified lengths using `simulate_sequences`:

```python
from genparse import simulate_sequences

for seq in simulate_sequences([50, 75, 100]):
    print(seq)
```

