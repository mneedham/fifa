# FIFA Player of the Year 2015

This is just a little script that scrapes [the PDF with all the votes](http://es.fifa.com/mm/document/ballon-dor/playeroftheyear-men/02/50/58/45/fboaward_menplayer2014_neutral.pdf) which I got from the FIFA website and then creates a CSV file instead.

The CSV file is already checked in but if you want to generate it again just run this:

```
python playerofyear.py
```

## Dependencies

I'm using the [pdfquery](https://pypi.python.org/pypi/pdfquery) library to do the PDF scraping so you'll need to install that with the following command:

```
pip install -r requirements.txt
```
