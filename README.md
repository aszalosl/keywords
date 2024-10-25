# keywords

Generate list of keywords for completion.

There is a plugin for the [vis](https://github.com/martanne/vis) editor that can be used to complete the typed letters into words/identifiers. Although Python has only a few keywords, in the case of a larger project there are a lot of classes and variables that are boring to type their names over and over again, and for readable code we use long identifiers that are easy to mistype.

That's why this little routine was created to go through the source files of the current project and collect the words in them. Perhaps well-known is the one-line [solution](https://unix.stackexchange.com/questions/41479/find-n-most-frequent-words-in-a-file) that combines Unix commands and finds the 10 most frequently occurring words of a given file.

On the other hand, I wanted to leave out the rarely occurring words - which probably only appear in one or two comments - as well as the short words that we can easily type. Since Python is case-sensitive, make everything lowercase was out of the question here, which is essential for frequency calculations.

The source to be processed conservatively uses only ASCII characters, so we do not have to consider UTF-8 characters.

I probably could have formulated the solution in bash as well, but since I found half-finished solutions in other languages, I developed one of them further.
