# Macro to read publication information for CV

import os

pubs = []

f_in = open('INSPIRE-CiteAll.tex', 'r')
data = f_in.read()
for paper in (data.split('\n\n')):
    fields = paper.split('\n')
    author = fields[2]
    title = fields[3][3:][:-3]
    citation = fields[4]
    journal = citation.split(r'\t')[0][:-1]
    if not citation.startswith('[arXiv') and not citation.startswith('doi'):
        pubs.append([title,author,citation,journal])



f = open('writing.tex', 'w')
f.write('\cvsection{Publications}\n\n')
f.write(r'\begin{cventries}')
f.write('\n\n')



for pub in pubs:
    f.write('\cventry\n')
    f.write('\t{%s}\n' % pub[2]) # citation
    f.write('\t{%s}\n' % pub[0]) # title
    f.write('\t{%s}\n' % pub[3]) # journal
    f.write('\t{}\n') # date
    f.write('\t{}\n') # empty
    f.write('\n\n')

f.write('\end{cventries}')
