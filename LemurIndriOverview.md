## Resources ##

**General**

Lemur Project and Indri Search Engine Wiki:
> http://sourceforge.net/apps/trac/lemur/

Quick start guide and overview:
> http://sourceforge.net/apps/trac/lemur/wiki/Quick%20Start

Lemur Forum:
> http://sourceforge.net/projects/lemur/forums

**More specific**

Manipulating retrieval:
> http://ciir.cs.umass.edu/~strohman/indri/

Dumpindex and dumpterm:
> http://sourceforge.net/apps/trac/lemur/wiki/dumpdoc,%20dumpterm,%20and%20dumpindex<br>
<blockquote><a href='http://www.lemurproject.org/docs/index.php/Dumpdoc,_dumpterm,_and_dumpindex'>http://www.lemurproject.org/docs/index.php/Dumpdoc,_dumpterm,_and_dumpindex</a></blockquote>

Transform simple keyword queries into more complex Indri formulations:<br>
<blockquote><a href='http://ciir.cs.umass.edu/~strohman/code/xform.py'>http://ciir.cs.umass.edu/~strohman/code/xform.py</a> <br>
and other stuff: <a href='http://ciir.cs.umass.edu/~strohman/code'>http://ciir.cs.umass.edu/~strohman/code</a></blockquote>

<hr />

<h2>INDEXING</h2>

Files:<br>
<ul><li><b>Input data files</b>
<ul><li>formats: TRECTEXT or TRECWEB<br>
</li><li>indexer file formats: <a href='http://sourceforge.net/apps/trac/lemur/wiki/Indexer%20File%20Formats'>http://sourceforge.net/apps/trac/lemur/wiki/Indexer%20File%20Formats</a> - includes PDF, xml, html, doc, ppt, txt, trecweb and trectext<br>
</li><li>annotations, tagger: <a href='http://sourceforge.net/apps/trac/lemur/wiki/Inline%20and%20Offset%20Annotations'>http://sourceforge.net/apps/trac/lemur/wiki/Inline%20and%20Offset%20Annotations</a></li></ul></li></ul>

<pre><code># Example of TRECTEXT file:<br>
&lt;DOC&gt; <br>
&lt;DOCNO&gt; 18921 &lt;/DOCNO&gt; <br>
&lt;TEXT&gt; <br>
&lt;TITLE&gt;Alstrom syndrome&lt;/TITLE&gt;<br>
&lt;DESCRIPTION&gt;Alstrom syndrome is a rare disorder charcterized by ...&lt;/DESCRIPTION&gt;<br>
&lt;/TEXT&gt; <br>
&lt;/DOC&gt;<br>
</code></pre>

<ul><li><b>Output directory</b>
<ul><li>must be empty or does not exist</li></ul></li></ul>

<ul><li><b>Parameter files for indexing</b>
<ul><li>well-formed XML documents that must be wrapped in <code>&lt;parameter&gt;&lt;/parameter&gt;</code> tags<br>
</li><li>one or more parameter files<br>
</li><li><a href='http://sourceforge.net/apps/trac/lemur/wiki/IndriBuildIndex%20Parameters'>http://sourceforge.net/apps/trac/lemur/wiki/IndriBuildIndex%20Parameters</a></li></ul></li></ul>

Usage:<br>
<pre><code>&gt; IndriBuildIndex &lt;parameter_file&gt; [&lt;parameter_file_2&gt; ... &lt;parameter_file_n&gt;] -index=&lt;path_to_index&gt;<br>
</code></pre>

<b>Accepted parameters:</b> <a href='http://sourceforge.net/apps/trac/lemur/wiki/IndriBuildIndex%20Parameters'>http://sourceforge.net/apps/trac/lemur/wiki/IndriBuildIndex%20Parameters</a>

<b>Troubleshooting:</b>
<ul><li>If you are trying to generate a file of the TRECTEXT format by converting it from another format for the purpose of indexing it with Lemur, make sure that the <code>&lt;DOC&gt;</code> tags are on separate lines. Also, the file should terminate with a newline.<br>
</li><li>If you are using fields, make sure that you write their names in lowercase in the parameter file for indexing.<br>
<hr /></li></ul>

<h2>RETRIEVAL</h2>

Files:<br>
<ul><li><b>Query parameter files</b></li></ul>

Usage example:<br>
<pre><code>&gt; IndriRunQuery &lt;query_parameter_file&gt; [&lt;query_parameter_file_2&gt; ... &lt;query_parameter_file_n&gt;] -index=&lt;path_to_index&gt; &gt; &lt;result_file&gt;<br>
</code></pre>

<b>Accepted parameters:</b> <a href='http://lemur.sourceforge.net/indri/IndriRunQuery.html'>http://lemur.sourceforge.net/indri/IndriRunQuery.html</a>

Formatting the query, interpreting retrieval results: <a href='http://sourceforge.net/apps/trac/lemur/wiki/IndriRunQuery'>http://sourceforge.net/apps/trac/lemur/wiki/IndriRunQuery</a>

The Indri query language:<br>
<a href='http://sourceforge.net/apps/trac/lemur/wiki/The%20Indri%20Query%20Language'>http://sourceforge.net/apps/trac/lemur/wiki/The%20Indri%20Query%20Language</a>
<a href='http://sourceforge.net/apps/trac/lemur/wiki/Indri%20Query%20Language%20Reference'>http://sourceforge.net/apps/trac/lemur/wiki/Indri%20Query%20Language%20Reference</a>

<b>Troubleshooting:</b>

<ul><li>Setting up Java for running the queries:<br>
<pre><code>cp /usr/local/lib/libindri_jni.so .<br>
cp /usr/local/share/indri/indri.jar .<br>
javac -cp '.:indri.jar' RunQuery.java <br>
java -cp '.:indri.jar' -Djava.library.path='.' RunQuery<br>
</code></pre></li></ul>

<hr />

<h2>EVALUATION</h2>

<ul><li><i>trec_eval</i>
<ul><li>per query evaluation and summary over all queries<br>
</li><li><a href='http://trecvid.nist.gov/trecvid.tools/trec_eval_video/README'>http://trecvid.nist.gov/trecvid.tools/trec_eval_video/README</a>
</li></ul><blockquote><code>&gt; trec_eval -q QREL_file Retrieval_Results &gt; eval_output </code>
</blockquote></li><li><i>ireval</i>
<ul><li>statistical tests comparing results<br>
</li><li><a href='http://sourceforge.net/apps/trac/lemur/wiki/ireval'>http://sourceforge.net/apps/trac/lemur/wiki/ireval</a>
</li></ul><blockquote><code>&gt; java -jar lemur/ireval/src/ireval.jar baseline_result testrun_result QREL_file &gt; comparison_output</code></blockquote></li></ul>

<b>Troubleshooting:</b>
<ul><li>If you are using trec_eval, make sure the query identifiers from your query parameter file and those from the relevance judgements files have the same names. To name your queries, use the <code>&lt;number&gt;</code> tag for each <code>&lt;query&gt;</code> tag in the query parameter file. The "number" does not necessarily need to be a number, contrary to your naive assumptions.</li></ul>

<hr />
<h2>Programming</h2>

<ul><li>Changing the retrieval model can <a href='http://sourceforge.net/projects/lemur/forums/forum/836442/topic/2545629'>only</a> be done by implementing a new retrieval method in C++.<br>
</li></ul><blockquote><a href='http://www.lemurproject.org/lemur/progexamples.php#exam-newmethod'>http://www.lemurproject.org/lemur/progexamples.php#exam-newmethod</a></blockquote>

<ul><li>Lemur API Programming Examples: <a href='http://www.lemurproject.org/lemur/progexamples.php'>http://www.lemurproject.org/lemur/progexamples.php</a></li></ul>

<hr />
Medical IR datasets that could be useful for novice users in testing Lemur's performance and capabilities on medical data:<br>
<br>
<ul><li>The OHSUMED document collection<br>
<ul><li>readme file: <a href='http://trec.nist.gov/data/filtering/README.t9.filtering'>http://trec.nist.gov/data/filtering/README.t9.filtering</a>
</li><li>download data: <a href='http://trec.nist.gov/data/t9_filtering.html'>http://trec.nist.gov/data/t9_filtering.html</a></li></ul></li></ul>

<hr />
<h3>Eval results</h3>
<ul><li>Interpreting the <a href='http://trecvid.nist.gov/trecvid.tools/trec_eval_video/README'>trec_eval</a> evaluation results:<br>
<table><thead><th>num_ret        	</th><th>Total number of documents retrieved over all queries</th></thead><tbody>
<tr><td>num_rel        	</td><td>Total number of relevant documents over all queries </td></tr>
<tr><td>num_rel_ret    	</td><td>Total number of relevant documents retrieved over all queries</td></tr>
<tr><td>map            	</td><td>Mean Average Precision (MAP) <br> <a href='http://en.wikipedia.org/wiki/Information_retrieval#Mean_average_precision'>http://en.wikipedia.org/wiki/Information_retrieval#Mean_average_precision</a></td></tr>
<tr><td>gm_ap          	</td><td>Average Precision. Geometric Mean, q_score=log(MAX(map,.00001)) <br><a href='http://en.wikipedia.org/wiki/Information_retrieval#Average_precision'>http://en.wikipedia.org/wiki/Information_retrieval#Average_precision</a></td></tr>
<tr><td>R-prec         	</td><td>R-Precision (Precision after R (= num-rel for topic) documents retrieved)</td></tr>
<tr><td>bpref          	</td><td>Binary Preference, top R judged nonrel <br>DOI: 10.1145/1277741.1277756 </td></tr>
<tr><td>recip_rank     	</td><td>Reciprical rank of top relevant document<br><a href='http://en.wikipedia.org/wiki/Mean_reciprocal_rank'>http://en.wikipedia.org/wiki/Mean_reciprocal_rank</a> </td></tr>
<tr><td>ircl_prn.<code>&lt;t&gt;</code>  	</td><td>Interpolated Recall - Precision Averages at <code>&lt;t&gt;</code> recall <br>Measures precision (percent of retrieved documents that are relevant) at various recall levels (after a certain percentage of all the relevant documents for that query have been retrieved). 'Interpolated' means that, for example, precision at recall 0.10 (ie, after 10% of rel docs for a query have been retrieved) is taken to be MAXIMUM of precision at all recall points >= 0.10. (<a href='http://trecvid.nist.gov/trecvid.tools/trec_eval_video/README'>source</a>)</td></tr>
<tr><td>P<code>&lt;nr&gt;</code>             	</td><td>Precision after <code>&lt;nr&gt;</code> docs retrieved <br><a href='http://en.wikipedia.org/wiki/Information_retrieval#Precision'>http://en.wikipedia.org/wiki/Information_retrieval#Precision</a></td></tr></li></ul></tbody></table>

More: <a href='http://en.wikipedia.org/wiki/Information_retrieval#Performance_measures'>http://en.wikipedia.org/wiki/Information_retrieval#Performance_measures</a>