[Yahoo! Search BOSS](http://developer.yahoo.com/search/boss/) (Build your Own Search Service) is Yahoo's open search web services platform and can be used to build a custom search solution. Read more about this platform in the review article _[Yahoo Radically Opens Web Search With BOSS](http://techcrunch.com/2008/07/09/yahoo-radically-opens-web-search-with-boss/)_ (July 2008), or get an overview of the services provided by BOSS in [Yahoo! Search BOSS handout](http://ydn.zenfs.com/site/boss/handout-boss-v1.1.pdf).

This page includes the following sections:


---

### Creating a Yahoo BOSS Custom Search ###

Based on BOSS's [documentation](http://developer.yahoo.com/search/boss/boss_guide/index.html) and [this](http://www.brighthub.com/hubfolio/matthew-casperson/articles/54678.aspx) tutorial.

#### Yahoo API Key ####

In order to be able to access the Yahoo search service, you need to sign up for a BOSS App ID.

#### Access to the service ####

Access to the Yahoo search service is done via a REST API.
```
http://boss.yahooapis.com/ysearch/{service}/v1/{query}?appid={yourBOSSappid}[&param1=val1&param2=val2]
```
where {service} can be _web_, _images_, _news_, _se\_inlink_, _se\_pagedata_ or _spelling_. The format of the response can be either XML or JSON (default is JSON). Some characters in the arguments must be escaped, see how [here](http://developer.yahoo.com/search/boss/boss_guide/BOSS_FAQ.html).

#### Customizing the response ####

The BOSS API arguments, described [here](http://developer.yahoo.com/search/boss/boss_guide/overview.html#univer_api_args), are used to configure the response:
  * _count_ - total number of results to be returned (default: 10, maximum: 50)
  * _start_ - position of first result (default: 0, the first position)
  * _format_ - data format of the response: "xml" or "json" (default: "json")
  * _sites_ - restrict search results to a number of predefined sites (multiple sites separated by comma)
  * _style_ - decides whether to add `<b>` tags around the search term in the results (style=raw removes the `<b>` tags)
  * _view_ - used to retrieve additional search data
  * _lang_, _region_, _strictlang_, _callback_
For web search, there are [a few more](http://developer.yahoo.com/search/boss/boss_guide/Web_Search.html#optional_args_web) optional arguments:
  * _filter_ - remove results with adult or hate content
  * _type_ - a comma-separated list which specifies document formats to be included in the search
    * values: html, text, pdf, xl, msword, ppt, msoffice (includes xl, msword, ppt) or nonhtml (includes text, pdf, xl, msword, ppt)
    * can also specify formats to be excluded using the minus opperator
  * _abstract_ - if set to long, it will display an extended abstract (up to 300 characters)
  * _view_ for web search can have one of the values:
    * keyterms (retrieve related words and phrases for each search result), language (identifies the language of the document), searchmonkey\_feed, searchmonkey\_rdf, delicious\_toptags, and delicious\_saves.


#### Querying the web ####

```
http://boss.yahooapis.com/ysearch/web/v1/{query}?appid={yourBOSSappid}&format=xml[&param1=val1&param2=val2]
```

  * **Exact match**: example searching for exact match of the search terms (by using quotation marks):
```
http://boss.yahooapis.com/ysearch/web/v1/"Apple Pie"?appid=xyz&format=xml
```

  * **Excluding keywords** by using the minus operator example:
```
http://boss.yahooapis.com/ysearch/web/v1/Apple -Pie +Recipes?appid=xyz&format=xml
```

  * **Site search**: examples of searching in a specified site, and of excluding a specified site from results:
```
http://boss.yahooapis.com/ysearch/web/v1/Apple Pie -Strawberry +site:epicurious.com?appid=xyz&format=xml
http://boss.yahooapis.com/ysearch/web/v1/Apple Pie -site:epicurious.com?appid=xyz&format=xml
```

#### Response fields ####

The XML response fields returned by the search are the following (as described in [documentation](http://developer.yahoo.com/search/boss/boss_guide/ch02s02.html)):
  * _count_ and _start_, with their default values or the values given in the query URL
  * _totalhits_ and _deephits_
  * _abstract, title, url, clickurl, dispurl, size_ and _date_ - for each result
  * sections corresponding to the view parameter given in the query (e.g. with view=keyterms will include a section named keyterms for each document)

#### Querying for the pages in the Yahoo! index and the sites linking into a site ####

_se\_inlink_
  * displays the pages (from other sites) that link to a given webpage or domain
  * example (from [documentation](http://developer.yahoo.com/search/boss/boss_guide/site_explorer.html)):
```
http://boss.yahooapis.com/ysearch/se_inlink/v1/{site}?appid={yourBOSSappid}&format=xml&count=1
```

_se\_pages_
  * displays the list of subpages belonging to a domain that exist in the Yahoo! index
  * example (from [documentation](http://developer.yahoo.com/search/boss/boss_guide/ch03s02.html)):
```
http://boss.yahooapis.com/ysearch/se_pagedata/v1/{domain}?appid={yourBOSSappid}&format=xml
```

#### Spelling suggestions ####

Spelling suggestions can be retrieved from the spelling database like this:
```
http://boss.yahooapis.com/ysearch/spelling/v1/{query}?appid={yourBOSSappid}&format=xml
```
The result returns a field named suggestion with the actual spelling suggestion as the field's description.
([documentation on retrieving spelling suggestions](http://developer.yahoo.com/search/boss/boss_guide/Spelling_Suggest.html))

#### BOSS Mashup Framework ####

[BOSS Mashup Framework](http://developer.yahoo.com/search/boss/mashup.html) is a Python library that provides developers SQL-like constructs for using the Yahoo! BOSS.


---

### Searching for rare diseases diagnoses with Yahoo! BOSS ###

Running the five symptom queries ([previously described](http://code.google.com/p/raredisss/wiki/GoogleCustomSearch#Five_cases_of_patients_with_a_rare_disease)) on a customized Yahoo! BOSS search (customized by narrowing the search to a selected number of sites with information on rare diseases) returned **no results**. Searches were performed on both the initial queries and the refined queries.

The sites included in the search were the same as [those](http://code.google.com/p/raredisss/wiki/TryCustomSearch#Details_of_the_Search_Engine) listed in our customized Google CSE, with one exception: the category of rare diseases from Wikipedia. Extracting the links from a page (such as a category page from Wikipedia containing multiple links to pages on a specific topic) is a predefined option in Google CSE, while in Yahoo! BOSS it is not.

Unlike Google CSE, BOSS does not have an option to search through the entire web while emphasizing a specific list of sites. The behavior can probably be simulated programmatically after the retrieval of all results, but we did not further investigate this issue.