This Quick Guide to Creating Customized Searches with the Google Custom Search Engine is based on the information presented in the [documentation of the Google Custom Search](http://code.google.com/intl/en/apis/customsearch/docs/start.html) and describes some of the options that could be used to improve search results.

[Official website](http://www.google.com/cse/) of Google Custom Search

[Help forum](http://www.google.com/support/forum/p/customsearch?hl=en) for Google Custom Search

[Blog](http://googlecustomsearch.blogspot.com/) for Google Custom Search

**Contents**

This page includes the following sections:



---

### Basic CSE Options in the Control Panel ###
#### Selecting where to search ####

You can specify the sites (URLs) to be included in the search, as well as the sites to be excluded from the search.
  * a maximum of 5000 sites is allowed (per account, for all custom search engines)
  * more about specifying the sites to be included in the search and about the URLs: [here](http://code.google.com/intl/en/apis/customsearch/docs/start.html#sites)
  * _Control Panel -> Sites_

The customized engine can search:
  * only through a specified list of sites, or
  * the entire web but emphasize the specified sites.
  * _Control Panel -> Basics_

Indexing:
  * can view the approximate number of pages (not on-demand pages) indexed
  * on-demand indexing (max 100 pages per search engine)
    * by adding sitemaps or URLs
  * _Control Panel -> Indexing_

#### Improving user queries and search results ####
##### Refinements #####

  * refinement labels (categories of search results) appear at the top of the search results page ([details](http://code.google.com/intl/en/apis/customsearch/docs/refinements.html))
    * the refinement labels can have three modes determining what happens when the user clicks the refinement link:
      * boost (sites tagged with the label are prioritized over other results),
      * filter (only sites tagged with the label are shown),
      * eliminate (sites tagged with the label are excluded entirely).
    * for boost and filter labels, weights can be attributed (values between -1.0 and 1.0, with the default of 0.7)
  * the refinement labels are applied on the sites from the annotations file (sites can be tagged in XML or TSV file formats)
  * refinements can be used for appending search terms to user queries and redirecting users to another website or search engine
  * the refinement labels can be added in the control panel (_Control Panel -> Refinements_) or in the XML context file

##### Synonyms #####

  * Google already has a large body of synonyms for terms that are common to the general public
  * upload a XML file for other synonyms that the custom search should include ([details](http://code.google.com/intl/en/apis/customsearch/docs/queries.html#synonyms))
    * maximum number of variants for each query term: 10
    * maximum number of variants per search engine: 500
    * maximum number of synonyms files: <4mb (one file size < 500kb)
  * _Control Panel -> Indexing_

##### Autocompletions #####

  * by default, autocompletions are disabled
  * autocompletion is a list of optional queries that appear as the user types in the query
    * the list is derived partly from the contents of the website and the popularity of the search term ([details](http://code.google.com/intl/en/apis/customsearch/docs/queries.html#auto))
  * can add or remove individual terms in the control panel (_Control Panel -> Autocompletions_) or by uploading an autocompletions XML file. Regular expressions can be used. The terms added through the XML file will appear above the algorithmically generated terms.

#### Preview ####

  * you can visit the search engine's homepage and get the generated code for the search box for placing it on a website (_Control Panel -> Preview_ and _Control Panel -> Get Code_)
  * the style of the search box can be extended with CSS and Javascript (_Control Panel -> Look and feel_)
  * statistics for the custom search engine (_Control Panel -> Statistics_):
    * reports per day/week/month/overall
    * graph with distinct queries per day
    * list of popular queries

#### Collaboration ####

  * limited access for collaborators (can only add sites and apply existing refinement labels)
  * _Control Panel -> Collaboration_


---

### More Advanced CSE Options ###

#### Context and annotations ####

A custom search engine consists of annotations and a context. These two main components are housed in XML files. These give you a greater level of control over your search engine.

**Context** - Describes the search engine. It specifies the global settings of the search engine.
  * in the control panel, these settings are defined in the Basics, Refinements, Look and feel, Collaboration, and Make money tabs.
  * each search engine has its own context file
  * can upload and download the XML context file (_Control Panel -> Advanced_)

**Annotations** - Specify which sites are included in the search engine (like an index of the search engine). It contains information about which sites should be covered and how they should be ranked in the results.
  * in the control panel, the sites are defined in the Sites tab. Each site and its associated information is called an annotation.
  * an annotations file is simply a list of annotations; each annotation has two components: the site and its associated labels.
    * the label tells Custom Search how to handle a site; that is, whether a site should be included, excluded, promoted, or demoted.
  * maximum of 5000 annotations for all custom search engines (and a maximum of 2000 annotations per annotations file)
  * can upload and download annotations file, or add them as feeds (_Control Panel -> Advanced_)
  * annotations files can be in any of the following formats:
    * Outline Processor Markup Language (OPML)
    * Text files with tab-separated values (TSV)
    * Custom Search XML -> the most powerful format, can take advantage of all the features available in the Custom Search API

**Context files with inline annotations** - a single file, with the annotations section right after the context specification
  * can only be used if the file is hosted on a website
  * [more details](http://code.google.com/intl/en/apis/customsearch/docs/annotations.html)

#### Auxiliary files ####

In addition to these main components, a search engine can also have the following auxiliary files:
  * Promotions
  * Synonyms
  * Autocompletions

#### Changing the ranking of the search results ####

Custom Search lets you tune results by three means:
  * keywords
  * weighted labels
  * scores
    * keywords and weights are defined in the context file, while scores are defined in the annotations file
    * weights in labels and scores have values that range from -1.0 to +1.0

**Keywords**
  * webpages that contain the keyword are promoted in the results page
    * webpages that contain most of the keywords are promoted even more
  * can use series of words enclosed within quotation marks
  * defined through the Basics tab in the control panel, or in the context file
  * [more](http://code.google.com/intl/en/apis/customsearch/docs/ranking.html#keywords)

**Labels**
  * two kinds of labels:
    * search engine labels
      * determine which sites should be covered by the search engine
      * are invisible to the users and run in the background
    * refinement labels
      * are visible to the users and show up as links
      * are labels that you apply to sites to categorize them
    * modes, weights, and scores operate in the same way in both search engine and refinement labels
  * search engine labels have modes, which determine how the sites should be treated; one of them is exclusive (mode="ELIMINATE"), and the other one is inclusive (either mode="FILTER" or mode="BOOST")

#### Programaticaly customize result snippets ####

You can create your own snippets (small samples of content that gives search users an idea of what's in a webpage) with image thumbnails, summaries, dates, ratings. [More](http://code.google.com/intl/en/apis/customsearch/docs/snippets.html)


---

### Google Site Search ###

With [Google Site Search](http://www.google.com/sitesearch/) you can:
  * retrieve search results in XML format
  * display ads-free results
  * Google branding is optional
Prices start from 100$ per year.