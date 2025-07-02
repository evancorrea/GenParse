from dataclasses import dataclass
from typing import Iterator

@dataclass
class FastaRecord:
    header: str
    sequence: str


def parse_fasta(path: str) -> Iterator[FastaRecord]:
    """Yield FastaRecord objects from a FASTA file."""
    header = None
    seq_lines = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if header is not None:
                    yield FastaRecord(header, ''.join(seq_lines))
                header = line[1:].strip()
                seq_lines = []
            else:
                seq_lines.append(line)
        if header is not None:
            yield FastaRecord(header, ''.join(seq_lines))
