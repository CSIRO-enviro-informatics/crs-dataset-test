# CRS Dataset - test
This is data from the CRS Database, formulated according to the CRS Ontology, and formatted in RDF (turtle).

Data in this repository is a formulation of several table's worth of data from the [National Archives of Australia](http://www.naa.gov.au)'s *Commonwealth Record Series* database according to the [CRS Ontology](http://linked.data.gov.au/def/crs) developed within the [Longitudinal Spine of Government Functions](https://longspine.cat) project. The data is formatted in [RDF](https://www.w3.org/RDF/)'s [Turtle serialisation](https://www.w3.org/TR/turtle/).

This dataset is considered a *test* because it is a static, one-off 'dump' of data from the internal CRS database and will not be updated. It is just for data demonstration purposes.

The URI for this dataset is a text URI, i.e. not one that is guaranteed to persist or work. It is:

* **<http://test.linked.data.gov.au/dataset/crs>**


## Data
* [data/agency-functions.ttl](data/agency-functions.ttl) - Commonwealth Agencies's association with [CRS Thesuarus](http://linked.data.gov.au/def/crs-th) functions
* [data/ca.ttl](data/ca.ttl) - Commonwealth Agencies
* [data/co.ttl](data/co.ttl) - Commonwealth Organisations
* [data/cp.ttl](data/cp.ttl) - Commonwealth Persons
* [data/CA1889.ttl](data/CA1889.ttl) - An extended formulation of longitudinal (temporal) information about the Commonwealth Agency 1889 - *Department of Northern Australia, Central Office*
* [data/CP665.ttl](data/CP665.ttl) - An extended formulation of longitudinal (temporal) information about the Commonwealth Person 665 - *Paul Keating*

The [source/](source/) folder contains raw data from the CRS database (in Excel) and intermediate files and scripts used to process it to created the files listed above.


## Rights and License
All the contents of this repository are derived from NAA source data and thus the rights to that data reside with the NAA.

All work done on the NAA data for its presentation here was undertaken by [CSIRO](https://www.csiro.au).

This data and other content in this repository are licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) (local copy of deed: [LICENSE](LICENSE)).


## Contacts
Creator:  
**Nicholas Car**  
*Senior Experimental Scientist*  
CSIRO Land & Water, Brisbane, Australia  
<nicholas.car@csiro.au>  
<http://orcid.org/0000-0002-8742-7730>  

Data provisioning:  
**National Archives of Australia**  

