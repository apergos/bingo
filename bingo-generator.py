#!/usr/bin/env python3
import random
import sys


def generate_table(terms, pagebreak=True):
    '''Generates an HTML table representation of the bingo card for terms'''
    terms_and_space = terms[:12] + ["FREE SPACE"] + terms[12:24]
    if pagebreak:
        res = "<table class=\"newpage\">\n"
    else:
        res = "<table>\n"
    for i, term in enumerate(terms_and_space):
        if i % 5 == 0:
            res += "\t<tr>\n"
        if i == 12:
            # center square
            res += "\t\t<td bgcolor=\"#ffcc99\">" + term + "</td>\n"
        else:
            res += "\t\t<td>" + term + "</td>\n"
        if i % 5 == 4:
            res += "\t</tr>\n"
    res += "</table>\n"
    return res


def do_main():
    '''entry point'''

    # check for the right # of args
    if len(sys.argv) != 4:
        print("USAGE: " + sys.argv[0], " [file of terms] [output file] [# of cards]")
        print("Example: " + sys.argv[0] + " bingo_terms.txt bingo.html 20")
        sys.exit(1)

    # read in the bingo terms
    in_file = open(sys.argv[1], 'r')
    terms = [line.strip() for line in in_file.readlines()]
    terms = list(filter(lambda x: x != "", terms))
    in_file.close()

    html_template = open("html_template.txt", "r").read()
    out_file = open(sys.argv[2], 'w')
    out_file.write(html_template)
    cards = int(sys.argv[3])
    for i in range(cards):
        random.shuffle(terms)
        if i != cards - 1:
            out_file.write(generate_table(terms))
        else:
            out_file.write(generate_table(terms, False))
    out_file.write("</body></html>")

    out_file.close()


if __name__ == '__main__':
    do_main()
