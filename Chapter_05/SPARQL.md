
[SPARQL Query Editor](https://ja.dbpedia.org/sparql)

[SPARQL sample](http://uedayou.net/sparql-examples/)

`Default Data Set Name (Graph IRI): http://ja.dbpedia.org`

<details>
<summary>sample 1</summary>


``` SPARQL
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

select * where {
  ?link a dbpedia-owl:Station;
  rdfs:label ?title;
  geo:lat ?lat;
  geo:long ?long.
}

```

</details>

<details>
<summary>sample 2</summary>

``` SPARQL
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
}
LIMIT 100

```

</details>
