#!/usr/bin/env python

"""
Provides an optimised workflow for editing GitHub wiki pages using a local repo.
"""

__author__ = "Calum J. Eadie"
__license__ = "MIT License"
__contact__ = "https://github.com/CalumJEadie/github-wiki-edit-page"

import sys
import argparse
import subprocess
import os.path

COMMIT_MESSAGE = "Updated %s"

class GithubWikiEditPageError(Exception):
    """Base class for all exceptions."""
    pass

class EditorError(GithubWikiEditPageError):
    pass

class GitError(GithubWikiEditPageError):
    pass

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("page", help="local path of page")
    parser.add_argument("-k","--skip-pull", action="store_true", help="skip git pull at start")
    args = parser.parse_args(sys.argv[1:])

    # Get normalised absolute path to page.
    page = os.path.abspath(args.page)

    # Automate single page editing workflow.
    # Pull by default for safety.
    if not args.skip_pull:
        # Call pull to avoid merge conflicts.
        print "> pull"
        pull(page)
        raw_input("> enter to continue...")
    else:
        print "> skipped pull"
    print "> edit"
    edit(page)
    print "> add"
    add(page)
    print "> commit"
    commit(page)
    print "> push"
    push(page)

def pull(page):
    try:
        dirname = os.path.dirname(page)
        subprocess.check_call(["git","pull"],cwd=dirname)
    except subprocess.CalledProcessError as e:
        raise GitError(e)

def edit(page):
    editor = os.environ.get('EDITOR','vim')
    try:
        subprocess.check_call([editor,page])
    except subprocess.CalledProcessError as e:
        raise EditorError(e)

def add(page):
    try:
        dirname = os.path.dirname(page)
        subprocess.check_call(["git","add",page],cwd=dirname)
    except subprocess.CalledProcessError as e:
        raise GitError(e)

def commit(page):
    commit_message = COMMIT_MESSAGE % os.path.basename(page)
    try:
        dirname = os.path.dirname(page)
        subprocess.check_call(["git","commit","-m",commit_message,page],cwd=dirname)
    except subprocess.CalledProcessError as e:
        raise GitError(e)

def push(page):
    try:
        dirname = os.path.dirname(page)
        subprocess.check_call(["git","push"],cwd=dirname,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise GitError(e)

if __name__ == "__main__":
    main()
