Bingo Card Generator
====================
TL;DR
--------------------

You have two options.

1. Use the script (see instructions below for how to do that)
2. Shrug at the script and load up gh-bingo.html in your browser right from the cloned repo.
   It will display a form where you can enter terms and title and such yourself, or choose
   from one of our handy presets as a starting point. Once you have the values set the way
   you like, click the 'generate' button and the new card is yours!


How to use this script:
----------------------

python3 bingo-generator.py --help will give you a usage message.

Zeroth, save a background image of your choice with the name bg-image.jpg.

First, create a list of short phrases to go in the bingo squares; you need at least 24 of them,
one per line, in a file. See sample_terms.txt or trump_terms.txt for examples.

Second, decide on the title for your bingo card.

Third, decide what color you want the squares to turn when they are clicked; the default
is an annoying shade of orange.

Now run the script:

```shell
python3 bingo-generator.py -t path-to-term-list-file -o name-of-html-file-to-write -h title-of-card -c '#nnnnnn'
```

Load up the html file in a browser.

Clicking on a square marks it for bingo. If you hit the wrong square you can always
click it again to clear it. Nothing spectacular happens when you get bingo unless you jump up and shout
BINGO! yourself and have a drink :-)

Click 'new card' to have it clear any marked squares and reload terms in a different order.

This has drifted pretty far from the original author's intent. Yay open source? :-)
