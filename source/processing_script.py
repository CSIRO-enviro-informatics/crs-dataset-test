import rdflib


# to pretty-print the agency-functions
g = rdflib.Graph().parse('agency-functions-raw.ttl', format='turtle')
with open('agency-functions.ttl', 'w') as f:
    f.write(g.serialize(format='turtle').decode('utf-8'))
