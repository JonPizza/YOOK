# YOOK!!!

Yook is a micro framework for Python web scraping.

Example:

```
get https://jon.network becomes jon
soupify jon becomes soup

python:
# from here onwards it is just plain python with soup defined
print(soup.title.string)
```

Output:

```
Jon's Network: For Programmers
```
