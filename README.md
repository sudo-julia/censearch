# censearch.py

![Scrutinizer code quality (GitHub/Bitbucket)](https://img.shields.io/scrutinizer/quality/g/sudo-julia/censearch/main?style=flat)
![PyPI - Format](https://img.shields.io/pypi/format/censearch?color=informational)
![GitHub last commit](https://img.shields.io/github/last-commit/sudo-julia/censearch)

Fetch self-censored tweets of a given word, i.e. 'tr*mp'

## Installation

### With Poetry

- Download the repository:
  - `git clone https://github.com/sudo-julia/censearch`
- Enter the repo
  - `cd censearch`
- Install dependencies:
  - `poetry install`
- Run censearch:
  - `poetry run censearch`
    - To avoid typing this every time you want to run the program,
you can alias the above command with: `alias censearch='poetry run censearch'`

### From Source

- Download the repository:
  - `git clone https://github.com/sudo-julia/censearch`
- Enter the repo
  - `cd censearch`
- Build the package:
  - `python3 setup.py sdist bdist_wheel`
- Install from the local build
  - `pip install --user -U .`
- Run censearch:
  - `censearch`
  - Please note that running from a local build may not set up the entry point
correctly, resulting in: `bash: command not found: censearch`. In this case, simply
run `alias censearch='python3 -m censearch'`.
This sets up `censearch` to be run as
a module when `censearch` is typed, which solves the entry point problem.
You can add the `alias` command to the bottom of your shell's configuration file
for it to be set automatically at your terminal's initialization.

## Configuration

- Register for a developer account on
[developer.twitter.com](https://developer.twitter.com)
- Once your account is approved, navigate to the [dashboard](https://developer.twitter.com/en/portal/dashboard)
- Create a new app in the [overview section](https://developer.twitter.com/en/portal/projects-and-apps)
  - Optional: Name the app "censearch"
- Copy the: consumer public and private keys to somewhere secure, be it a file
or note
  - If storing the key values in a text file, make sure that the file contains
nothing but the string of text.
- Open [config.ini](./config.ini) and set the `ConsumerKey` and `ConsumerSecret`
keys to their appropriate values
  - The values can be:
    1. Paths to files containing the keys, which will be read
    2. The values of the keys (**unquoted** text)
    3. A combination of the above two
- Run `censearch -s [your_search_term]`

## Requirements

- Python ^3.7
- TwitterAPI ^2.6.9
- A twitter *developer* account with API Keys

## Bugs

Please report any bugs to this repo's [issues](https://github.com/sudo-julia/censearch/issues)

Linux is guaranteed support, but OSX and Windows testers would be appreciated :)
