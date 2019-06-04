#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
from echo.echo import create_parser

# Your test case class goes here
class test_shit(unittest.TestCase):
    def test_help(self):
        """Running the program without arguments should show usage."""

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo/echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        """Running the program with -u should uppercase the word
        as well as appear in the namespace"""
        parser = create_parser()
        args = parser.parse_args(["-u", "hello"])

        process = subprocess.Popen(
        ["python", "./echo/echo.py", "-u", "hello"],
        stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(args.upper, True)
        self.assertEquals(stdout[:len(stdout) - 1], 'HELLO')

    def test_lower(self):
        """Running the program with -l should lowercase the word
        as well as appear in the namespace"""
        parser = create_parser()
        args = parser.parse_args(["-l", "HELLO"])

        process = subprocess.Popen(
        ["python", "./echo/echo.py", "-l", "HELLO"],
        stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(args.lower, True)
        self.assertEquals(stdout[:len(stdout) - 1], 'hello')

    def test_title(self):
        """Running the program with -t should titlecase the word
        as well as appear in the namespace"""
        parser = create_parser()
        args = parser.parse_args(["-t", "hello there"])

        process = subprocess.Popen(
        ["python", "./echo/echo.py", "-t", "hello there"],
        stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(args.title, True)
        self.assertEquals(stdout[:len(stdout) - 1], 'Hello There')

    def test_empty(self):
        """Running the program with no arguments should return the word
        the original word"""
        parser = create_parser()
        args = parser.parse_args(["hello there"])

        process = subprocess.Popen(
        ["python", "./echo/echo.py", "hello there"],
        stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(stdout[:len(stdout) - 1], 'hello there')

    def test_all(self):
        """Running the program with all arguments should run the commands
        in the order they appear under the usage info"""
        parser = create_parser()
        args = parser.parse_args(["-tul","heLLo!"])

        process = subprocess.Popen(
        ["python", "./echo/echo.py", "-tul", "heLLo!"],
        stdout=subprocess.PIPE)
        stdout, _ = process.communicate()

        self.assertEquals(stdout[:len(stdout) - 1], 'Hello!')

    
    
        



        

        





if __name__ == '__main__':
    unittest.main()
