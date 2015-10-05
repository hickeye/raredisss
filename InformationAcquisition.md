#### Main Resources of Rare Diseases Information ####

  * **NORD - National Organization for Rare Disorders** (http://rarediseases.org)
    * database of more than 1,200 diseases
    * <font color='orange'>Sent emails asking for access to their database of rare diseases (21 Feb 2011, 8 Mar 2011, 6 Apr 2011)</font>
    * <font color='green'>extracted links and retrieved 1,240 articles (6 Apr 2011)</font>
  * **Orpha.net** - The portal for rare diseases and orphan drugs (http://www.orpha.net)
    * information about more than 5,000 diseases (some entries include only disease name, with no description, and some entries include link to the article used in the description of the disease)
    * <font color='orange'>Sent email asking for access to their database of rare diseases (21 Feb 2011); Registered - waiting for data (23 March 2011)</font>
  * **Orphanet Journal of Rare Diseases** (http://www.ojrd.com/)
    * <font color='green'>retrieved 267 articles (24 Feb 2011)</font>
  * **GARD - Genetic and Rare Diseases Information Center, National Institutes of Health** (http://rarediseases.info.nih.gov/GARD/)
    * contains information for about 7,448 rare and genetic diseases (from 9 March 2011)
    * <font color='green'>retrieved 6,829 articles (extracted links on 24 Feb 2011, retrieved articles on 8 March 2011)</font> 15 files deleted
  * **About.com Rare Diseases** (http://rarediseases.about.com/)
    * <font color='green'>extracted 483 links and saved 360 articles stored at rarediseases.about.com, but there are also 134 external links which were not retrieved (24 Feb 2011)</font>
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
    * Downloading OMIM / Description of files: http://www.ncbi.nlm.nih.gov/Omim/omimfaq.html#download
      * [new filepath](ftp://ftp.ncbi.nih.gov/repository/OMIM/ARCHIVE/)
    * <font color='green'>downloaded through ftp 21,395 articles (11 March 2011)</font>
    * <font color='green'>downloaded html with genes to MIM codes mapping (26 March 2011)</font>
  * **Wikipedia**
    * **Category:Rare Diseases** (http://en.wikipedia.org/wiki/Category:Rare_diseases)
      * provides description for around 400 rare diseases
      * Exporting Wikipedia's category on rare diseases to **XML** format:
        * instructions: http://www.mediawiki.org/wiki/API:Query
        * to get more than 500 use `&cmcontinue=` and the code at the end of the xml file (under the `<query-continue>` tag)
        * output the list of pages in the category: http://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Rare_diseases&cmlimit=max&cmdir=asc
        * output the content of the pages from the category in a XML file: http://en.wikipedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=Category:Rare_diseases&gcmlimit=max&gcmdir=asc&export&exportnowrap
      * The pages can also be exported in a **PDF** using Wikipedia's Book Creator. See: http://en.wikipedia.org/wiki/Special:Book
    * **Category:Syndromes** (http://en.wikipedia.org/wiki/Category:Syndromes)
      * provides description for around 500 syndromes
    * Search query: rare disease -incategory:"Rare Diseases"
    * <font color='green'>added around 150 existing Wikipedia pages to the category of Rare Diseases (23 March 2011), downloaded 529 pages from category RD, and 492 pages from category Syndromes in XML format (23 March 2011)</font>
  * **Centre for Rare Diseases and Disabilities - CSH** (http://www.csh.dk/)
    * danish description of more than 350 rare diseases (the descriptions are in Danish but contain international links)
  * **rarelink.no** (http://rarelink.no)
    * provides information and organization contact details for 575 rare diseases; the site does not actually store the information on rare diseases, but rather provides links to information sources (disease description and organizations).
    * links to the Danish database of rare diseases from the Centre for Rare Diseases and Disabilities
    * the diagnoses are described primarily in one of the Scandinavian languages, but there are a number of descriptions in English as well
    * a disease can have several names -- a list of these can be found at the end of each disease page

#### Other Resources ####

  * **NCBI** - National Center for Biotechnology Information (http://www.ncbi.nlm.nih.gov/Sitemap/)
    * **PubMed Central Open Access Subset**
      * how to get XML files for all PMC open access articles: http://www.ncbi.nlm.nih.gov/pmc/about/ftp.html#XML_for_Data_Mining
      * http://biostar.stackexchange.com/questions/2077/full-text-retrieval-from-pubmedcentral
      * <font color='green'>downloaded through ftp 236,569 full-text articles in XML format (8 March 2011)</font>
      * **BioMed Central** (http://www.biomedcentral.com/)
        * downloading BioMed Central corpus: http://www.biomedcentral.com/info/about/datamining
        * around 89,000 open-access full-text articles
        * the articles stored in BioMed Central are part of the PubMed Central Open Access Subset
      * **PLoS** (http://www.plos.org/)
        * open-access journals (http://en.wikipedia.org/wiki/Plos)
        * Fetch PLoS XML Papers: http://www.neurogems.org/fetchplos/
        * included in PubMed Central OAS
    * **PubMed Central** (http://www.ncbi.nlm.nih.gov/pmc/)
      * "open access", but with traditional copyright
      * around 2,000,000 abstracts
      * Entrez Programming Utilities: http://eutils.ncbi.nlm.nih.gov/corehtml/query/static/efetchlit_help.html
      * retrieval scripts - run only on weekends or between 2 a.m. and 10 a.m. DK time on weekdays (http://www.ncbi.nlm.nih.gov/entrez/query/static/eutils_help.html)
      * Extract PMC links from [PMC-ids.csv](http://www.ncbi.nlm.nih.gov/pmc/about/ftp.html#Obtaining_DOIs) file
```
# Remove comma from inside quotes (around 368 entries are affected)
#sed 's/\(\".*\),\(.*\"\)/\1;\2/' PMC-ids.csv > safe_PMC_ids.csv
sed 's/\(\".*\"\)/"-"/' PMC-ids.csv > safe_PMC_ids.csv

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
for f in pmc_list_*; do cat $f | tr '\n' ',' | sed -e 's/^/http\:\/\/eutils\.ncbi\.nlm\.nih\.gov\/entrez\/eutils\/efetch\.fcgi\?db\=pmc\&retmode\=xml\&rettype\=abstract\&id\=/;s/.$//' >> $f.test; done

# Create a file containing all entrez links
cat *.out >> pmc_links

```
      * <font color='green'>extracted PMCIDs from FTP (18 March 2011), finished downloading 2,250,957 records (20 March 2011)</font>
      * <font color='green'>extracted 2,252,158 PMCIDs from FTP (21 March 2011)</font>
    * **Bookshelf** (http://www.ncbi.nlm.nih.gov/books)
      * "collection of freely available, downloadable, on-line versions of selected biomedical books" ([source](http://en.wikipedia.org/wiki/National_Center_for_Biotechnology_Information#NCBI_Bookshelf))
      * 844 articles
      * range 201 - 53477
  * **PubMed / MEDLINE**
    * Baseline Database (19,569,568 records): http://www.nlm.nih.gov/bsd/licensee/2011_stats/baseline_med_filecount.html
    * format for XML documents: http://www.nlm.nih.gov/databases/dtd/index.html
    * difference between MEDLINE and PubMed: http://www.nlm.nih.gov/pubs/factsheets/dif_med_pub.html
    * <font color='green'>agreed to license - waiting for approval (19 March 2011) approval received (21 March 2011)</font>
    * access instructions: http://www.nlm.nih.gov/bsd/licensee/access/
      * the baseline files are available all hours seven days per week
      * access to the ftp based on IPs provided when requesting the license
    * <font color='green'>downloaded 19,569,568 records in 653 files through ftp (23 March 2011)</font>
  * List of open access journals:
    * http://en.wikipedia.org/wiki/Category:Open_access_journals
  * NLM Databases:
    * http://www.nlm.nih.gov/databases/
  * **DECIPHER** (http://decipher.sanger.ac.uk/)
    * Wikipedia article: http://en.wikipedia.org/wiki/DECIPHER
  * EBI Databases:
    * http://www.ebi.ac.uk/Information/databases_sitemap.html

#### Classifications. Ontologies. Thesaurus ####

  * **Human Phenotype Ontology** (http://www.human-phenotype-ontology.org/index.php/hpo_home.html)
    * more than 56,000 annotations to more than 5,000 OMIM-entries
    * documentation for the database: [hpo\_docu.html](http://www.human-phenotype-ontology.org/index.php/hpo_docu.html)
    * explore HPO terms:
      * url: http://www.human-phenotype-ontology.org/hpoweb/showterm?id=HP:0000127
      * explorer: http://www.human-phenotype-ontology.org/PhenExplorer/PhenExplorer.html
    * <font color='green'>downloaded 56,439 records through svn (14 March 2011)</font>
    * data in OWL format: http://www.berkeleybop.org/ontologies/owl/HP <font color='green'>downloaded (24 March 2011)</font>
  * **UTS** - UMLS Terminology Services (https://uts.nlm.nih.gov/home.html)
    * **NLM UMLS Metathesaurus - Unified Medical Language System** (http://www.nlm.nih.gov/research/umls/)
      * ~ 2,300,000 concepts - 8,500,000 unique concept names - 158 source vocabularies ([statistics.html](http://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/statistics.html))
      * <font color='green'>agreed to license - waiting for approval (21 March 2011); approval received (21 March 2011)</font>
      * <font color='green'>downloaded international release (23 March 2011)</font>
    * **SNOMED-CT** (http://www.nlm.nih.gov/research/umls/Snomed/snomed_main.html)
      * SNOMED CT Releases: [snomedctfiles.html](http://www.nlm.nih.gov/research/umls/licensedcontent/snomedctfiles.html)
      * SNOMED CT Snapshot: the latest release; SNOMED CT Delta: modifications since last release
      * <font color='green'>downloaded SNOMED CT (23 March 2011)</font>
    * **SNOMED-CT CORE** (http://www.nlm.nih.gov/research/umls/Snomed/core_subset.html)
      * <font color='green'>downloaded 5,815 records (21 March 2011)</font>
  * **ICD 10 CM** (http://www.cdc.gov/nchs/icd/icd10cm.htm)
    * International Classification of Diseases, Tenth Revision, Clinical Modification
    * <font color='green'>downloaded the 2011 release with 57,611 codes for diseases and injuries (23 March 2011)</font>
  * **MeSH - Medical Subject Headings** (http://www.nlm.nih.gov/mesh/)
    * files available to download: http://www.nlm.nih.gov/mesh/filelist.html
    * over 25,000 headings
    * browser:
      * NLM MeSH Browser: http://www.nlm.nih.gov/mesh/MBrowser.html
      * Wikipedia.org: http://en.wikipedia.org/wiki/List_of_MeSH_codes
    * <font color='green'>downloaded MeSH 2011 - 26,142 headings (21 March 2011)</font>
  * bioportal.bioontology.org

#### Reports ####

  * **Orphanet Report Series** - prevalence of rare diseases ([prevalence\_of\_rare\_diseases\_by\_alphabetical\_list.pdf](http://www.orpha.net/orphacom/cahiers/docs/GB/Prevalence_of_rare_diseases_by_alphabetical_list.pdf))
    * prevalence or reported number of published cases, based on a systematic review of medical literature
    * preliminary report: http://ec.europa.eu/health/archive/ph_threats/non_com/docs/rdnumbers.pdf
  * **Orphanet Thesaurus of clinical signs and symptoms** ([255\_orphanet\_thesaurus\_17.02.10.pdf](http://www.dyscerne.org/dysc/digitalAssets/0/255_orphanet_thesaurus_17.02.10.pdf))
  * **List of features and definitions from the Winter-Baraitser Dysmorphology Database** ([253\_LDDB\_ALL\_21.01.10\_SGCHPG.pdf](http://www.dyscerne.org/dysc/digitalAssets/0/253_LDDB_ALL_21.01.10_SGCHPG.pdf))

#### Crawling ####

We are using **`HtmlUnit`** and **`wget`** to extract the articles from some of the resources above (those that do not provide their data for downloading). Using **`HtmlUnit`** we have extracted the URLs to articles, saved them in files, and provided them as input to **`wget`** in order to retrieve each URL.

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
This can be used to download all of the URLs lists:<br>
<pre><code>wget -q -O - 'code.google.com/p/raredisss/downloads/list' | grep -i 'http:.*articleLinks\..*\.txt' | sed 's/^.*http\(.*\)\.txt.*/http\1.txt/' &gt; articleLinks<br>
<br>
wget -q -P wgetlinks -i articleLinks<br>
<br>
for i in wgetlinks/*.txt; do <br>
    mv $i  ${i%\.txt}; <br>
done<br>
<br>
for f in wgetlinks/articleLinks.*; do <br>
    wget -b -a logfile -i $f -w 0.5 -x --save-headers -P ${f#wgetlinks/articleLinks.}-data &gt;&gt; pids<br>
    echo ${f#wgetlinks/articleLinks.}.py &gt;&gt; py-scripts;<br>
done<br>
<br>
sed -i 's/[^0-9]*//g' pids<br>
<br>
python process-downloads.py<br>
</code></pre>


Scripts Cookbook:<br>
<pre><code># Delete .DS_Store files from current directory (recursive):<br>
find . -type f -name ".DS_Store" | xargs rm<br>
# Flatten the directory:<br>
find . -type f -exec mv {} ../temp \;<br>
</code></pre>

<a href='Hidden comment: 
Other crawlers:
* !VietSpider Web Data Extractor
* !ScraperWiki
'></a>