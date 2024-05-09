"""structures.py: Contains data structures for the application."""


class Structures:
    """
    Data structures for the application.

    Notes
    -----
    This class contains data structures used throughout the application.
    By storing data structures in a single location, it is easier to
    manage and update them. Data structures should be defined as class
    attributes and should be named in uppercase with underscores
    separating words.
    """

    # Directory structure
    DIRECTORY_STRUCTURE_REGEX = {
        "module": r"^[A-Z]{3}\d{4} [A-Za-z]+(?:\s+[A-Za-z]+)*$",  # e.g. "MTH1001 Calculus"
        "handbook": r"^Module Specification.pdf$",  # e.g. "Module Specification.pdf"
        "lectures": r"^\d{1,2}.pdf$",  # e.g. "1.pdf"
        "papers": r"^(202\d{1}|MOCK\d{1}).pdf$",  # e.g. "2021.pdf"
        "practicals": r"^\d+.pdf$",  # e.g. "1.pdf"
        "tutorials": r"^\d+.pdf$",  # e.g. "1.pdf"
    }
