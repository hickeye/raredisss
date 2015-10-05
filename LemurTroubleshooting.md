The purpose of this page is to provide information that does not appear, is not clear, or is hard to find on the official site of The Lemur Project. The material provided in what follows resulted from our experiments with the product(s) on a medical IR database - the OHSUMED document collection. The code produced during our experiments with this database is available in the Source tab.




---

## General ##

Lemur, Indri, The Lemur Toolkit, or The Lemur Project?

> The biggest question of all: _What is Lemur and what is Indri?_ You have installed The Lemur Toolkit, however you are running IndriBuildIndex to use it. So are you actually using Lemur or Indri? `TO-DO: explain and add links to sources`


---

## Indexing ##

  * If you are trying to generate a file of the TRECTEXT format by converting it from another format for the purpose of indexing it with Lemur, make sure that the `<DOC>` tags are on separate lines. Also, the file should terminate with a newline.
  * If you are using fields, make sure that you write their names in lowercase in the parameter file for indexing.


---

## Retrieval ##


---

## Evaluation ##

  * If you are using trec\_eval, make sure the query identifiers from your query parameter file and those from the relevance judgements files have the same names. To name your queries, use the `<number>` tag for each `<query>` tag in the query parameter file. The "number" does not necessarily need to be a number, contrary to your naive assumptions.

  * Interpreting the [trec\_eval](http://trecvid.nist.gov/trecvid.tools/trec_eval_video/README) evaluation results:
|num\_ret        	|Total number of documents retrieved over all queries|
|:----------------|:---------------------------------------------------|
|num\_rel        	|Total number of relevant documents over all queries |
|num\_rel\_ret    	|Total number of relevant documents retrieved over all queries|
|map            	 |Mean Average Precision (MAP) <br> <a href='http://en.wikipedia.org/wiki/Information_retrieval#Mean_average_precision'>http://en.wikipedia.org/wiki/Information_retrieval#Mean_average_precision</a>
<tr><td>gm_ap          	 </td><td>Average Precision. Geometric Mean, q_score=log(MAX(map,.00001)) <br><a href='http://en.wikipedia.org/wiki/Information_retrieval#Average_precision'>http://en.wikipedia.org/wiki/Information_retrieval#Average_precision</a></td></tr>
<tr><td>R-prec         	 </td><td>R-Precision (Precision after R (= num-rel for topic) documents retrieved)</td></tr>
<tr><td>bpref          	 </td><td>Binary Preference, top R judged nonrel <br>DOI: 10.1145/1277741.1277756 </td></tr>
<tr><td>recip_rank     	 </td><td>Reciprical rank of top relevant document<br><a href='http://en.wikipedia.org/wiki/Mean_reciprocal_rank'>http://en.wikipedia.org/wiki/Mean_reciprocal_rank</a> </td></tr>
<tr><td>ircl_prn.<code>&lt;t&gt;</code>  	</td><td>Interpolated Recall - Precision Averages at <code>&lt;t&gt;</code> recall <br>Measures precision (percent of retrieved documents that are relevant) at various recall levels (after a certain percentage of all the relevant documents for that query have been retrieved). 'Interpolated' means that, for example, precision at recall 0.10 (ie, after 10% of rel docs for a query have been retrieved) is taken to be MAXIMUM of precision at all recall points >= 0.10. (<a href='http://trecvid.nist.gov/trecvid.tools/trec_eval_video/README'>source</a>)</td></tr>
<tr><td>P<code>&lt;nr&gt;</code>             	</td><td>Precision after <code>&lt;nr&gt;</code> docs retrieved <br><a href='http://en.wikipedia.org/wiki/Information_retrieval#Precision'>http://en.wikipedia.org/wiki/Information_retrieval#Precision</a></td></tr></li></ul></tbody></table>

More: <a href='http://en.wikipedia.org/wiki/Information_retrieval#Performance_measures'>http://en.wikipedia.org/wiki/Information_retrieval#Performance_measures</a>