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
       [--header <string>] [--color <#nnnnnn>]
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
 --color   (-c):  color to turn a square when it's been clicked
                  Default: #ffcc99
 --help    (-H):  show this help message

Example:

python3 bingo-generator.py -t trump_terms.txt -o trump_bingo.html -h "Presidential Border Bingo"
"""
    sys.stderr.write(usage_message)
    sys.exit(1)


def get_default_opts():
    '''
    initialize args with default values and return them
    '''
    args = {'output': None, 'heading': 'Bingo Card', 'color': '#ffcc99'}
    return args


def process_opts():
    '''
    get command-line args and values, falling back to defaults
    where needed, whining about bad args
    '''
    try:
        (options, remainder) = getopt.gnu_getopt(
            sys.argv[1:], "t:o:h:c:H", ["terms=", "output=", "heading=", 'color=', "help"])

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

    html_template = open("html_template.txt", "r").read()
    for argname in ['phrases', 'color', 'heading']:
        html_template = html_template.replace('{{' + argname + '}}', args[argname], 1)

    if args['output']:
        out_file = open(args['output'], 'w')
        out_file.write(html_template)
        out_file.close()
    else:
        sys.stdout.write(html_template)


if __name__ == '__main__':
    do_main()
