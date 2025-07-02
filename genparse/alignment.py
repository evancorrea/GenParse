from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class AlignmentResult:
    score: int
    aligned_seq1: str
    aligned_seq2: str


def needleman_wunsch(seq1: str, seq2: str, match: int = 1, mismatch: int = -1, gap: int = -1) -> AlignmentResult:
    """Simple global alignment using Needleman-Wunsch."""
    n = len(seq1)
    m = len(seq2)
    score_matrix: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        score_matrix[i][0] = i * gap
    for j in range(1, m + 1):
        score_matrix[0][j] = j * gap
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = score_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            delete = score_matrix[i - 1][j] + gap
            insert = score_matrix[i][j - 1] + gap
            score_matrix[i][j] = max(diag, delete, insert)
    aligned_seq1 = []
    aligned_seq2 = []
    i, j = n, m
    while i > 0 or j > 0:
        current_score = score_matrix[i][j]
        if i > 0 and j > 0 and current_score == score_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and current_score == score_matrix[i - 1][j] + gap:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append('-')
            i -= 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j - 1])
            j -= 1
    return AlignmentResult(
        score=score_matrix[n][m],
        aligned_seq1=''.join(reversed(aligned_seq1)),
        aligned_seq2=''.join(reversed(aligned_seq2)),
    )
