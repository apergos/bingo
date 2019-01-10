Bingo Card Generator
====================
Use of bingo.html:
Put the background image of your choice into bg-image.jpg, edit the title in the html file to whatever
you like, add more or different trumpisms in the html file by extending the list 'trumpisms', and load
up into your browser. Clicking on a square marks it for bingo. If you hit the wrong square you can always
click it again to clear it. Nothing spectacular happens when you get bingo unless you jump up and shout
BINGO! yourself and have a drink :-)

Use of python script:

Make sure you put the background image of your choice into bg-image.jpg and edit template.html to use
the title (in h1 tags) you prefer. Then run the script with python3.

Once you've run the script and viewed the html in your browser, resize the browser and printscreen the
area you want for the card, for a cheap quick image. I've repurposed it with the intent to produce one
card, with title, for the web. If you wanted something else, the original fork is still there...

Original text from source follows:

Some terrible old code I wrote that belongs on the Internet.

Just dump your potential bingo terms into a text file, each on its own line, run the program, and print out the resulting HTML. Pagebreaks, etc. *should* be handled gracefully.

Usage:
------

```shell
bingo-generator.py  [file of terms] [output file] [# of cards]
```

Example:
--------

```shell
python bingo-generator.py bingo_terms.txt bingo.html 20
```


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/hrs/bingo/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

