# loy-lunar-lexicon

A lexicon that focuses on Mina Loy's 1923 Lunar Baedeker--the first published collection of her poems.

The files are divided up generally into three main folders: the programs used to scrape data and text (and also generate plaintext files for later use), the file resources that we scraped and cleaned themselves, and the program that makes lexicon entries on our site using calls to the Wordpress API.   

## Getting Started

Our project started simply with a plaintext file of Loy's 1923 Lunar Baedeker, from which we compiled a list of words and definitions pulled from the 1907 [Webster's International Dictionary of the English Language](https://catalog.hathitrust.org/Record/100598138). We chose to use Python to scrape, clean, and post the information from these resources due to prior experience with the language.

### Prerequisites

The starting resource files (and the generated ones on the whole) are simple .txt or .tsv files, so they can be viewed and modified with any word processor. For the file processing Python programs, you'll need: [Python 3.x.x](https://www.python.org/downloads/). Additionally, for the Wordpress, integration you'll need the [python-wordpress-xmlrpc](https://python-wordpress-xmlrpc.readthedocs.io/en/latest/index.html) library. Finally, for the initial work in computerized textual analysis, you'll need [Voyant](https://voyant-tools.org/).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Dr. Suzanne Churchill of Davidson College and her work with [Mina Loy: Navigating the Avant-Garde](https://mina-loy.com/)
* Our inspiration -- the wonderful lexicon at [Emily Dickinson Archive](http://www.edickinson.org/words)
* [Voyant](https://voyant-tools.org/) -- as NLP was a little beyond the scope of our project
* [HathiTrust](https://www.hathitrust.org/) and their extensive digital library

## Fair Use Act Disclaimer

This project and the accompanying site were made for educational purposes only.
