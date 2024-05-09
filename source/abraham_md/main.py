"""main.py: Called when the package is run as a script."""

from .config.dialogue import Dialogue
from .interface.command_line import fetch_input_path, intro_text
from .logs.setup_logging import setup_logging

main_logger = setup_logging()

"""
TEMPORARY RAMBLINGS:
--------------------

TODO: PROJECT FLOW
PDF -> MD -> Abstraction -> Elaboration -> MD (-> APKG, PDF)

TODO: FETCH REQUIRED DATA
module name
module coordinator name
module coordinator email
assessment weighting percentages
learning outcomes
module outline
recommended reading

TODO: ARGUMENT PARSING
input as arguments, e.g. abraham_md --input <path> --output <path>
instructions for usage as argument, e.g. abraham_md --help
no arguments, e.g. abraham_md, return error message prompting user to use --help
optional arguments, e.g. verbosity level (--verbose), log file (--log), etc.
allow single letter arguments, e.g. -i, -o, -h, -v, -l, etc.

TODO: GUI
when ported to gui, use kivy/kivyMD and file choosers/checkboxes for input: the
gui should replace command line interface, not run alongside it - but keep optional
argument parsing for verbosity, log file, etc.
"""


def main() -> None:
    """
    Main function for the application.

    Notes
    -----
    This function is the entry point for the application.
    """
    try:
        intro_text()
        input_path = fetch_input_path()
        print(input_path)
    except KeyboardInterrupt:
        print("\n")
        main_logger.info(Dialogue.EXIT_TEXT)


if __name__ == "__main__":
    main()
