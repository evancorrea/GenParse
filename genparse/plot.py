from typing import Iterable

import matplotlib.pyplot as plt


def plot_length_distribution(lengths: Iterable[int], title: str = "Sequence Lengths") -> None:
    """Plot a histogram of sequence lengths."""
    plt.figure(figsize=(8, 4))
    plt.hist(list(lengths), bins=20, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel('Length')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
