"""constants.py: Constants for the application."""

from dotenv import load_dotenv
from os import getenv


class Constants:
    """
    Constants for the application.

    Notes
    -----
    This class contains constants used throughout the application.
    By storing constants in a single location, it is easier to
    manage and update them. Constants should be defined as class
    attributes and should be named in uppercase with underscores
    separating words.
    """

    load_dotenv()

    # Logging constants
    LOGGING_LEVEL_DEFAULT = "INFO"
    LOGGING_FORMAT = "%(message)s"
    LOGGING_DATE_FORMAT = "[%X]"
    LOGGING_TRACEBACKS = True

    # Conversion constants
    TO_CONVERT_EXTENSION = ".pdf"  # TODO: Add support for other input file types
    MATHPIX_APP_ID = getenv("MATHPIX_APP_ID")
    MATHPIX_APP_KEY = getenv("MATHPIX_APP_KEY")
    MATHPIX_CONVERSION_SUFFIX = ".md"
    MATHPIX_ENDPOINT = "https://api.mathpix.com/v3/pdf"
    MATHPIX_OPTIONS = {
        "math_inline_delimiters": ["$", "$"],
        "math_display_delimiters": ["$$", "$$"],
        "idomatic_eqn_arrays": True,
        "numbers_default_to_math": True,
        "enable_spell_check": True,
    }
