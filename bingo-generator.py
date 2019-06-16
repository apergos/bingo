#!/usr/bin/env python3
import sys
import getopt


def usage(message=None):
    '''
    display a nice usage message along with an optional message
    describing an error
    '''
    if message:
        sys.stderr.write(message + "\n")
    usage_message = """Usage: python3 bingo-generator.py --terms <path> [--output <path>]
       [--header <string>] [--color <#nnnnnn>] [--free <string>]
or: python3 bingo-generator.py --help

Reads a list of phrases from a file, fills in an html template,
and writes the result, possibly with a title, to stdout or
optionally to a file.

Arguments:

 --terms   (-t):  path to file containing list of terms, one per line;
                  there should be 24 of them at least
 --output  (-o):  path to file into which to write the html
                  Default: written to stdout
 --heading (-h):  what to call the bingo card (goes in the <h1> header)
                  Default: Bingo Card
 --free    (-f):  what to put in the free space
                  Default: FREE SPACE
 --bgimage (-b):  what image to use for the background image
                  Default: bg-image.jpg (if missing, white)
 --color   (-c):  color to turn a square when it's been clicked
                  Default: #ffcc99
 --help    (-H):  show this help message

Examples:

python3 bingo-generator.py \\
  -t trump_terms.txt -o trump_bingo.html -h "Presidential Border Bingo" -b trump_bg.jpg
python3 bingo-generator.py \\
  -t nice_terms.txt -o nice.html -h "A Nice Day" -f "Punch a Nazi" -b nice_bg.jpg
python3 bingo-generator.py \\
  -t impeach_terms.txt -o impeach_bingo.html -h "Impeachment Bingo" -b trump_bg.jpg -f 'WITCH HUNT!'
python3 bingo-generator.py \\
  -t corpbuzz_terms.txt -o corpbuzz_bingo.html -h "Corporate Buzzword Bingo" -b corpbuzz_bg.jpg -f 'IDEATE!' --color '#EBA5D5'
"""
    sys.stderr.write(usage_message)
    sys.exit(1)


def get_default_opts():
    '''
    initialize args with default values and return them
    '''
    args = {'output': None, 'heading': 'Bingo Card', 'color': '#ffcc99',
            'free': 'Free Space', 'bgimage': 'bg-image.jpg'}
    return args


def process_opts():
    '''
    get command-line args and values, falling back to defaults
    where needed, whining about bad args
    '''
    try:
        (options, remainder) = getopt.gnu_getopt(
            sys.argv[1:], "t:o:h:c:f:b:H", ["terms=", "output=", "heading=",
                                            "color=", "free=", 'bgimage=',"help"])

    except getopt.GetoptError as err:
        usage("Unknown option specified: " + str(err))

    args = get_default_opts()

    for (opt, val) in options:
        if opt in ["-t", "--terms"]:
            args['terms'] = val
        elif opt in ["-o", "--output"]:
            args['output'] = val
        elif opt in ["-h", "--heading"]:
            args['heading'] = val
        elif opt in ["-c", "--color"]:
            args['color'] = val
        elif opt in ["-f", "--free"]:
            args['free'] = val
        elif opt in ["-b", "--bgimage"]:
            args['bgimage'] = val
        elif opt in ["-H", "--help"]:
            usage('Help for this script\n')
        else:
            usage("Unknown option specified: <%s>" % opt)

    if remainder:
        usage("Unknown option(s) specified: {opt}".format(opt=remainder[0]))

    check_opts(args)
    return args


def check_opts(args):
    '''
    whine if mandatory args not supplied
    '''
    for name in ['terms']:
        if name not in args or not args[name]:
            usage("Mandatory argument {name} not specified".format(name=name))


def hex_to_rgb(hexcolor, alpha):
    '''
    pass in desired transparency and the hex string for the color
    get back the rgba() string suitable for css
    '''

    # if we got a shorthand color, 'fill in' the missing hex digits
    if len(hexcolor[1:]) == 3:
        hexcolor = '#' + hexcolor[1]*2 + hexcolor[2]*2 + hexcolor[3]*2
    red = int(hexcolor[1:3], 16)
    green = int(hexcolor[3:5], 16)
    blue = int(hexcolor[5:7], 16)
    return 'rgba({r},{g},{b},{a})'.format(r=red, g=green, b=blue, a=alpha)


def do_main():
    '''entry point'''

    args = process_opts()

    # read in the bingo terms
    in_file = open(args['terms'], 'r')
    terms = [line.strip() for line in in_file.readlines()]
    in_file.close()
    terms = list(filter(lambda x: x != "", terms))
    terms = ['"' + term + '"' for term in terms]
    terms = ",".join(terms)
    args['phrases'] = terms
    # make the cells a bit transparent
    args['color'] = hex_to_rgb(args['color'], '0.4')

    html_template = open("html_template.txt", "r").read()
    for argname in ['phrases', 'color', 'heading', 'free', 'bgimage']:
        html_template = html_template.replace('{{' + argname + '}}', args[argname])

    if args['output']:
        out_file = open(args['output'], 'w')
        out_file.write(html_template)
        out_file.close()
    else:
        sys.stdout.write(html_template)


if __name__ == '__main__':
    do_main()
