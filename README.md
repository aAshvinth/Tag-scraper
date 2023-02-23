 [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-yellow.svg)](https://www.buymeacoffee.com/Ashvinth)
# Tag-scraper
Get Video Tags 🎬🔍

This is a simple Python program that scrapes the keywords/tags for a given YouTube video URL and saves them to a file.

### How it Works 🤔

The program uses the requests and beautifulsoup4 libraries to send a request to the specified URL and parse the HTML response. It then looks for the meta tags with name="keywords" and property="og:title" attributes to extract the video's tags and title, respectively. The program then writes the tags and title to a file called Tags.txt, along with a timestamp.

### How to Use 🛠️

To use the program, simply enter the URL of the YouTube video you want to scrape tags for and click the "Fetch" button. If the program successfully scrapes the tags, they will be displayed in the window and also saved to Tags.txt in the same directory as the program.

![image](https://user-images.githubusercontent.com/106897514/218933100-36adbd04-8b40-44d3-80b1-9dc84e2dcf80.png)



### Download 💾

## windows:

You can <a href="https://github.com/aAshvinth/Tag-scraper/raw/main/Tag%20scraper%20-%20aAshvinth.zip">download</a> the program for windows as the compressed .rar file.

## Other operating systems:

### Requirements 📦

    Python 3.x
    requests library
    beautifulsoup4 library
    tkinter library (usually included with Python)

### Usage

    Download the program files.
    Install the required libraries using pip:
    
    pip install requests beautifulsoup4 tkinter
    
    Run the program using Python:
    
    python video_tags_scraper.py


### Notes

This program was tested on Python 3.9.7 and Windows 10. It should work on other operating systems as well, but this is not guaranteed.



### License 📄

This program is licensed under the GNU General Public License v3.0.
