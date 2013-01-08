github-wiki-edit-page
=====================

Provides an optimised workflow for editing GitHub wiki pages using a local repo.

Example
-------

Lets use this repository as an example and make a local copy of the GitHub Wiki
associated with it.

```sh
git clone git@github.com:CalumJEadie/github-wiki-edit-page.wiki.git
```

Now, we'll make a change to the Home page using vanilla git commands.

```sh
git pull
vim Home.md
git add Home.md
git commit -m "Update Home" Home.md
git push
```

This can be quite a hassle when making a lot of small changes!

Instead we'll do the same using `github-wiki-edit-page.py`.

```sh
github-wiki-edit-page.py Home.md
```

Simple!