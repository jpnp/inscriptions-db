
from flask import render_template, current_app
import pysolr

from . import index

fields = index.solr_fields

def show(id):
    corename = current_app.config["SOLR_CORE"]

    solr = pysolr.Solr(corename)
    results = solr.search('id:'+id)

    return render_template('show.html', item=results.docs[0], fields=fields)
