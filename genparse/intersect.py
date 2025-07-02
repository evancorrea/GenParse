from dataclasses import dataclass
from typing import List, Iterator

@dataclass
class Interval:
    chrom: str
    start: int
    end: int
    metadata: dict | None = None


def intersect(a: List[Interval], b: List[Interval]) -> Iterator[Interval]:
    """Yield intervals representing the intersection of two interval sets."""
    b_by_chrom = {}
    for iv in b:
        b_by_chrom.setdefault(iv.chrom, []).append(iv)
    for iv in a:
        for other in b_by_chrom.get(iv.chrom, []):
            start = max(iv.start, other.start)
            end = min(iv.end, other.end)
            if start < end:
                yield Interval(iv.chrom, start, end)
