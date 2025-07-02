"""GenParse: simple genomic parsing and analysis framework."""

from .fasta import FastaRecord, parse_fasta
from .fastq import FastqRecord, parse_fastq
from .gff import GFFFeature, parse_gff
from .stats import gc_content, sequence_lengths
from .alignment import AlignmentResult, needleman_wunsch
from .intersect import Interval, intersect

try:
    from .plot import plot_length_distribution
except Exception:  # matplotlib may not be installed
    plot_length_distribution = None

__all__ = [
    'FastaRecord', 'parse_fasta',
    'FastqRecord', 'parse_fastq',
    'GFFFeature', 'parse_gff',
    'gc_content', 'sequence_lengths',
    'AlignmentResult', 'needleman_wunsch',
    'Interval', 'intersect',
    'plot_length_distribution',
]
