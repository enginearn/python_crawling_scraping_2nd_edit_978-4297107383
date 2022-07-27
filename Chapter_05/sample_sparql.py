#!/usr/bin/env python3
from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper(endpoint='http://ja.dbpedia.org/sparql', returnFormat='json')
sparql.setQuery("""
    PREFIX dbpj: <http://ja.dbpedia.org/resource/>
    PREFIX dbp-owl: <http://dbpedia.org/ontology/>
    PREFIX dbp-prop: <http://ja.dbpedia.org/property/>

    SELECT ?p, ?o
    WHERE {
        dbpj:日本 ?p ?o
        FILTER REGEX (?o, "オリンピック")
    }
""")
results = sparql.query().convert()
for result in results['results']['bindings']:
    print(result['p']['value'], result['o']['value'])