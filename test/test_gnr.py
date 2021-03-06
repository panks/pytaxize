"""Tests for GNR module of pytaxize"""

import os
import pytaxize

# expected results
exp1 = {
 u'canonical_form': u'Helianthus annus',
 u'classification_path': u'',
 u'classification_path_ids': u'',
 u'classification_path_ranks': u'',
 u'data_source_id': 12,
 u'data_source_title': u'EOL',
 u'edit_distance': 0,
 u'gni_uuid': u'f5674e32-00cc-57e3-b632-6a0b89fa4df4',
 u'local_id': u'468106',
 u'match_type': 1,
 u'name_string': u'Helianthus annus',
 u'prescore': u'3|0|0',
 u'score': 0.988,
 u'taxon_id': u's_5106367',
 u'url': u'http://eol.org/pages/468106/names/synonyms'
}

def test_gnr_resolve():
    """Basic test of of gnr_resolve"""
    assert exp1 == pytaxize.gnr_resolve('Helianthus annus')[0][0]
