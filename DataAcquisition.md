#### Main Resources of Rare Diseases Information ####

  * **NORD - National Organization for Rare Disorders** (http://rarediseases.org)
    * database of more than 1,200 diseases
    * <font color='orange'>Sent email asking for access to their database of rare diseases (21 Feb 2011)</font>
  * **Orpha.net** - The portal for rare diseases and orphan drugs (http://www.orpha.net)
    * information about more than 5,000 diseases
    * <font color='orange'>Sent email asking for access to their database of rare diseases (21 Feb 2011)</font>
  * **Orphanet Journal of Rare Diseases** (http://www.ojrd.com/)
    * <font color='green'>retrieved 267 articles (24 Feb 2011)</font>
  * **GARD - Genetic and Rare Diseases Information Center, National Institutes of Health** (http://rarediseases.info.nih.gov/GARD/)
    * contains information for about 7,448 rare and genetic diseases (from 9 March 2011)
    * <font color='green'>retrieved 6,829 articles (extracted links on 24 Feb 2011, retrieved articles on 8 March 2011)</font>
  * **About.com Rare Diseases** (http://rarediseases.about.com/)
    * <font color='green'>retrieved 483 articles stored at rarediseases.about.com, but there are also 134 external links which were not retrieved (24 Feb 2011)</font>
  * **Socialstyrelsen - The Swedish National Board of Health and Welfare** (http://www.socialstyrelsen.se/rarediseases)
    * <font color='green'>retrieved 157 articles (24 Feb 2011)</font>
  * **Madisons Foundation M-Power Rare Pedriatic Disease Database** ([http://www.madisonsfoundation.org/](http://www.madisonsfoundation.org/index.php/component/option,com_mpower/Itemid,49/))
    * 522 diseases with symptoms, available treatments and links to other resources
    * <font color='green'>retrieved 522 articles (9 March 2011)</font>
  * **Genetics Home Reference** - genetic conditions database (http://ghr.nlm.nih.gov/BrowseConditions)
    * more than 550 health condiions, diseases and syndromes
    * <font color='green'>retrieved 605 articles (9 March 2011)</font>
  * **Health on the Net Foundation** - list of rare diseases (http://www.hon.ch/HONselect/RareDiseases/index.html)
    * <font color='green'>retrieved 184 articles (9 March 2011)</font>
  * **OMIM - Online Mendelian Inheritance in Man** (http://www.ncbi.nlm.nih.gov/omim)
    * Downloading OMIM: http://www.ncbi.nlm.nih.gov/Omim/omimfaq.html#download
    * <font color='green'>downloaded through ftp 21,395 articles (11 March 2011)</font>
  * **Wikipedia Category:Rare Diseases** (http://en.wikipedia.org/wiki/Category:Rare_diseases)
    * provides description for around 400 rare diseases
    * Exporting Wikipedia's category on rare diseases to **XML** format:
      * instructions:
        * http://www.mediawiki.org/wiki/API:Query
      * output the list of pages in the category:
        * http://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Rare_diseases&cmlimit=max&cmdir=asc
      * output the content of the pages from the category in a XML file:
        * http://en.wikipedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=Category:Rare_diseases&gcmlimit=max&gcmdir=asc&export&exportnowrap
    * The pages can also be exported in a **PDF** using Wikipedia's Book Creator. See: http://en.wikipedia.org/wiki/Special:Book
  * **Centre for Rare Diseases and Disabilities - CSH** (http://www.csh.dk/)
    * danish description of more than 350 rare diseases (the descriptions are in Danish but contain international links)
  * **rarelink.no** (http://rarelink.no)
    * provides information and organization contact details for 575 rare diseases; the site does not actually store the information on rare diseases, but rather provides links to information sources (disease description and organizations).
    * links to the Danish database of rare diseases from the Centre for Rare Diseases and Disabilities
    * the diagnoses are described primarily in one of the Scandinavian languages, but there are a number of descriptions in English as well
    * a disease can have several names -- a list of these can be found at the end of each disease page

#### Other Resources ####

  * **NCBI** - National Center for Biotechnology Information (http://www.ncbi.nlm.nih.gov/Sitemap/)
    * **PubMed Central Open Access Articles**
      * how to get XML files for all PMC open access articles: http://www.ncbi.nlm.nih.gov/pmc/about/ftp.html#XML_for_Data_Mining
      * http://biostar.stackexchange.com/questions/2077/full-text-retrieval-from-pubmedcentral
      * <font color='green'>downloaded through ftp 236,569 full-text articles in XML format (8 March 2011)</font>
    * **PubMed Central** (http://www.ncbi.nlm.nih.gov/pmc/)
      * "open access", but with traditional copyright
      * around 2,000,000 abstracts?
      * Entrez Programming Utilities: http://eutils.ncbi.nlm.nih.gov/corehtml/query/static/efetchlit_help.html
      * retrieval scripts - run only on weekends or between 2 a.m. and 10 a.m. DK time on weekdays (http://www.ncbi.nlm.nih.gov/entrez/query/static/eutils_help.html)
      * Extract PMC links from [PMC-ids.csv](http://www.ncbi.nlm.nih.gov/pmc/about/ftp.html#Obtaining_DOIs) file
```
# Extract the PMC column
cut -d , -f 9 PMC-ids.csv

# Erase the PMC prefix of every line
cut -c 4- 

# Remove the file header line
sed -i '' '1d' 

# Split the PMC ids into chunks of 1000 ids
split -a 3 -l 1000 pmc_ids pmc_list_

# Replace newline with comma in each file
# Construct the entrez link
# Remove last comma from each file
for f in pmc_list_*; do cat $f | tr '\n' ',' | sed -e 's/^/http\:\/\/eutils\.ncbi\.nlm\.nih\.gov\/entrez\/eutils\/efetch\.fcgi\?db\=pmc\&retmode\=xml\&rettype\=abstract\&id\;s/.$//' >> $f.out; done

# Create a file containing all entrez links
cat *.out >> pmc_links

```
<a href='Hidden comment: 
# Split list into manageable sizes
split -a 1 -l 100000 wget_pmc_link_list pmc_link_list_
# Form the complete entrez link
# http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&retmode=xml&rettype=abstract&id=
sed -e "s/^/http\:\/\/eutils\.ncbi\.nlm\.nih\.gov\/entrez\/eutils\/efetch\.fcgi\?db\=pmc\&retmode\=xml\&rettype\=abstract\&id\=/" wget_list > wget_link_list
'></a>
    * **PubMed / MEDLINE**
      * Baseline Database (19,569,568 records): http://www.nlm.nih.gov/bsd/licensee/2011_stats/baseline_med_filecount.html
      * leasing data - http://www.nlm.nih.gov/databases/leased.html
      * format for XML documents: http://www.nlm.nih.gov/databases/dtd/index.html
    * **Bookshelf** (http://www.ncbi.nlm.nih.gov/books)
      * "collection of freely available, downloadable, on-line versions of selected biomedical books" ([source](http://en.wikipedia.org/wiki/National_Center_for_Biotechnology_Information#NCBI_Bookshelf))
  * **BioMed Central** (http://www.biomedcentral.com/)
    * downloading BioMed Central corpus: http://www.biomedcentral.com/info/about/datamining
    * 88,958 open-access full-text articles
    * however, the articles stored in BioMed Central are part of the PubMed Central Open Access Subset
  * **Human Phenotype Ontology**
    * http://www.human-phenotype-ontology.org/index.php/hpo_home.html
  * **ICD 10**
    * ICD 10 CM: http://www.cdc.gov/nchs/icd/icd10cm.htm
  * **UMLS**

#### Reports ####
  * **Orphanet Report Series** - prevalence of rare diseases ([prevalence\_of\_rare\_diseases\_by\_alphabetical\_list.pdf](http://www.orpha.net/orphacom/cahiers/docs/GB/Prevalence_of_rare_diseases_by_alphabetical_list.pdf))
    * prevalence or reported number of published cases, based on a systematic review of medical literature
  * **Orphanet Thesaurus of clinical signs and symptoms** ([255\_orphanet\_thesaurus\_17.02.10.pdf](http://www.dyscerne.org/dysc/digitalAssets/0/255_orphanet_thesaurus_17.02.10.pdf))

#### Crawling ####

We are using **`HtmlUnit`** and **`wget`** to extract the articles from the resources above. Using **`HtmlUnit`** we have extracted the URLs to articles, saved them in files, and provided them as input to **`wget`** in order to retrieve each URL.

_Example_: <br>
For the resources from Genetics Home Reference, we have saved article URLs in the file articleLinks.GHR.txt<br>
<pre><code>wget --input-file=articleLinks.GHR.txt --wait=2 --random-wait --force-directories<br>
</code></pre>

Usage of <code>wget</code>:<br>
<pre><code>--wait=seconds <br>
--random-wait <br>
--input-file=file <br>
</code></pre>

The URLs extracted for each resource are available in the Downloads section.<br>
<br>
<a href='Hidden comment: 
Other crawlers:
* !VietSpider Web Data Extractor
* !ScraperWiki
'></a><br>
<br>
<a href='Hidden comment: 
====Statistics for Resources====
|| *Resource* || *Number of articles/abstracts/entries* || *Size (compressed/uncompressed)* || Date ||
|| || || || ||
||_*Rare Disease Sites*_ || || || ||
||Orphanet Journal of Rare Diseases || 267 || 5.4 MB || ||
||GARD || 6,829 || 209 MB || ||
||About.com Rare Diseases || 483 || 2.8 MB || ||
||Socialstyrelsen Rare Diseases || 157 || 2.7 MB || ||
||Madisons Foundation Rare Diseases || 522 || ||	||
||HON Rare Diseases || 184 || || ||
||Genetics Home Reference || 605 || || ||
||OMIM || 21,395 || 66250887 / 151221560 bytes|| ||
|| || || ||
||NORD || 1,200 || ||
||Orpha.net || 3,356 || ||
||Wikipedia Category Rare Diseases || 400 || ||
|| || || ||
||_*Other Resources*_ || || ||
||!PubMed Central - Open Access Subset || 236,569 || 2973 MB / 13755 MB ||
||!PubMed Central || 2,250,957 || ||
|| || || ||
||!BioMed Central (BMC) || 88,958 || ||
||!PubMed || 20,000,000 || ||
'></a>