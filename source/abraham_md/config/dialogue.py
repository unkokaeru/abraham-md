"""dialogue.py: Dialogue for the application."""


class Dialogue:
    """
    Dialogue for the application.

    Notes
    -----
    This class contains dialogue used throughout the application.
    By storing dialogue in a single location, it is easier to
    manage and update it. Dialogue should be defined as class
    attributes and should be named in uppercase with underscores
    separating words.
    """

    # Text
    INTRO_TEXT = "Welcome to Abraham!"
    EXIT_TEXT = "Exiting Abraham..."
    SETUP_TEXT = """Please enter the input directory path:"""

    # Validation messages
    VALID_PATH_MESSAGE = "Valid path."

    # Error messages
    INVALID_PATH_ERROR = "Invalid path. Please try again."
    MISSING_DIRECTORY_ERROR = "Missing directory: {}"
    INVALID_STRUCTURE_ERROR = "Invalid directory structure. Please try again."
    DIRECTORY_NAMING_ERROR = "Invalid directory name: {}"
    MISSING_FILE_ERROR = "Missing file: {}"
    MESSY_DIRECTORY_ERROR = (
        "Messy directory: {}. Please ensure all files are in the correct directories."
    )

    PROCEED_TEXT = "Would you like to proceed anyway? [y/n]:"  # TODO: Add "proceed anyway" option
