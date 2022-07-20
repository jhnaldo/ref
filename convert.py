import bibtexparser

with open('ref.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

print(bib_database.entries)
