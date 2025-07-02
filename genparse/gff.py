from dataclasses import dataclass
from typing import Iterator, Optional

@dataclass
class GFFFeature:
    seqid: str
    source: str
    type: str
    start: int
    end: int
    score: Optional[str]
    strand: str
    phase: Optional[str]
    attributes: str


def parse_gff(path: str) -> Iterator[GFFFeature]:
    """Yield GFFFeature objects from a GFF/GTF file."""
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) < 9:
                continue
            yield GFFFeature(
                seqid=parts[0],
                source=parts[1],
                type=parts[2],
                start=int(parts[3]),
                end=int(parts[4]),
                score=parts[5] if parts[5] != '.' else None,
                strand=parts[6],
                phase=parts[7] if parts[7] != '.' else None,
                attributes=parts[8]
            )
