import sys
from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper(endpoint="http://dbpedia.org/sparql", returnFormat="json")
sparql.setQuery(
    r"""
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX owl: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select * where {
  ?link a owl:Museum;
  rdfs:label ?title;
  prop-ja:所在地 ?address;
  geo:lat ?lat;
  geo:long ?long .
FILTER REGEX(?address, "^\\p{Han}{2,3}[都道府県]")
} ORDER BY ?title;
"""
)

response = sparql.query().convert()
print(response)
# for result in response["results"]["bindings"]:
#     print(result["s"]["value"], result["address"]["value"])
