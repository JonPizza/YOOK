#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import sys

class YookSyntaxError(Exception):
    pass


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def tokenize(code):
    lines = []
    line_is_python = False
    pycode = ''

    for line in code.split('\n'):
        if line_is_python:
            pycode += line + '\n'
            continue
        elif line == '':
            continue
        elif line.replace(' ', '') == 'python:':
            line_is_python = True
        
        lines.append(line.split(' '))
    
    return lines, pycode


def get(url, becomes_keyword, name):
    if becomes_keyword != 'becomes':
        raise YookSyntaxError('did you mean "becomes"?')
    response = requests.get(url).content.decode('utf-8')
    exec(f'global {name}; {name} = """{response}"""')


def soupify(html, becomes_keyword, name):
    if becomes_keyword != 'becomes':
        raise YookSyntaxError('did you mean "becomes"?')
    exec(f'global {name}; {name} = BeautifulSoup({html}, features="lxml")')


def run(lines, python):
    for line in lines:
        if line[0] == 'get':
            get(line[1], line[2], line[3])
        elif line[0] == 'soupify':
            soupify(line[1], line[2], line[3])
        elif line[0] == 'python:':
            exec(python)

def main():
    contents = read_file(sys.argv[1])
    lines, python = tokenize(contents)
    run(lines, python)

main()