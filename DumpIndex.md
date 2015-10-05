### Usage ###

```
dumpindex <repository> <command> [ <argument> ]*
These commands retrieve data from the repository: 
    Command              Argument       Description
    term (t)             Term text      Print inverted list for a term
    termpositions (tp)   Term text      Print inverted list for a term, with positions
    fieldpositions (fp)  Field name     Print inverted list for a field, with positions
    expressionlist (e)   Expression     Print inverted list for an Indri expression, with positions
    xcount (x)           Expression     Print count of occurrences of an Indri expression
    documentid (di)      Field, Value   Print the document IDs of documents having a metadata field matching this value
    documentname (dn)    Document ID    Print the text representation of a document ID
    documenttext (dt)    Document ID    Print the text of a document
    documentdata (dd)    Document ID    Print the full representation of a document
    documentvector (dv)  Document ID    Print the document vector of a document
    invlist (il)         None           Print the contents of all inverted lists
    vocabulary (v)       None           Print the vocabulary of the index
    stats (s)                           Print statistics for the Repository
These commands change the data inside the repository:
    compact (c)          None           Compact the repository, releasing space used by deleted documents.
    delete (del)         Document ID    Delete the specified document from the repository.
    merge (m)            Input indexes  Merges a list of Indri repositories together into one repository.
```

### Cookbook recipes ###


Get the text doc for a given trec docno:
```
# Get internal docno based on trec docno:
dumpindex index_focused di "docno" 5160
# Get doc text based on internal docno:
dumpindex index_focused dt 3693
```

Get the text of documents in which a term appears:
```
# Get the internal docnos for the documents in which a term appears:
dumpindex index_focused term "fibrodysplasia"
# For each of the docnos, you should get doc text like this:
dumpindex index_focused dt 3693
```