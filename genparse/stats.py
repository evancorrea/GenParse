from typing import Iterable


def gc_content(seq: str) -> float:
    gc = sum(1 for base in seq.upper() if base in 'GC')
    return gc / len(seq) * 100 if seq else 0.0


def sequence_lengths(seqs: Iterable[str]) -> list[int]:
    return [len(s) for s in seqs]
