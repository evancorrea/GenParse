from typing import Iterable, Iterator
import random


def simulate_sequences(lengths: Iterable[int] | int, alphabet: str = "ACGT") -> Iterator[str]:
    """Yield random DNA sequences for each length in ``lengths``.

    Parameters
    ----------
    lengths:
        Either a single integer length or an iterable of lengths specifying
        the length of each simulated sequence.
    alphabet:
        String of characters to sample from when generating sequences.
        Defaults to ``"ACGT"``.
    """
    if isinstance(lengths, int):
        lengths = [lengths]
    for length in lengths:
        yield "".join(random.choices(alphabet, k=length))
