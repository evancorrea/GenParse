from dataclasses import dataclass
from typing import Iterator

@dataclass
class FastqRecord:
    header: str
    sequence: str
    plus: str
    quality: str


def parse_fastq(path: str) -> Iterator[FastqRecord]:
    """Yield FastqRecord objects from a FASTQ file."""
    with open(path) as fh:
        while True:
            header = fh.readline().rstrip()
            if not header:
                break
            seq = fh.readline().rstrip()
            plus = fh.readline().rstrip()
            qual = fh.readline().rstrip()
            if not qual:
                break
            yield FastqRecord(header[1:], seq, plus, qual)
