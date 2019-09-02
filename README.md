# case-report-dataset

XML Dataset with more than 200,000 Abstracts of case report articles from [Pubmed](https://pubmed.gov/).

Date of extraction: 22th of August, 2019.

See used search parameters below:

![alt text](https://github.com/marcelotournier/case-report-dataset/raw/master/parameters.png) 

To unzip using terminal: `cat data.z* > joined.zip && unzip joined.zip`

md5 hash for the `pubmed_result.xml`, when unzipped: `53ec9a259c049142690f0d20fcd1f551`

Known issues: You can see warnings when unzipping the concatenated file. You can safely ignore them, if the file pass a md5 check.
