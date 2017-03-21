# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from valuenetwork.valueaccounting.models import Facet, FacetValue

# helper for performing checks & inserts

def ensureRows(model, keys, rows):
    for row in rows:
        fields = zip(keys, row)
        lookup = dict(zip((fields[0][0],), (fields[0][1],)))

        if (model.objects.filter(**lookup).count() > 0):
            print "%s record already exists, skipping" % model.__name__
        else:
            model.objects.create(**dict(fields))
            print "created new %s record (id %d)" % (model.__name__, row[0])

# data inserts

def insertFacects(apps, schema_editor):
    keys = (
        "id",
        "name",
        "description",
        "clas"
    )

    rows = (
        (1,'Material','This is a set of material resource types or facet values, in coordination with the General common tree of Material Artwork Types (physical items). This facet relates a General model class which manages the subtypes as a tree.','Material_Type'),
        (2,'Types of Work','This is a set of Skill resource types or facet values, in coordination with the General common tree of Jobs (arts, verbs). This facet relates a Work model class which manages the subtypes as a tree.','Skill_Type'),
        (3,'Non-material','This is a set of non-material resource types or facet values, in coordination with the General common tree of Non-material Artwork Types (physical items). This facet relates a General model class which manages the subtypes as a tree.','Nonmaterial_Type'),
        (4,'Currency','This facet is to group types of currencies, so a resource type can act as a currency of certain type if wears any of this values','Currency_Type'),
    )

    ensureRows(Facet, keys, rows)

def insertFacetValues(apps, schema_editor):
    keys = (
        "id",
        "value",
        "description",
        "facet_id",
    )

    rows = (
        (1,'Product','',1),
        (8,'Space','',1),
        (9,'Raw material','',1),
        (10,'Tool','',1),
        (12,'Making','',2),
        (13,'Communicating','',2),
        (14,'LifeCareing','',2),
        (16,'Visual','',3),
        (17,'Formation','',3),
        (18,'Sound','',3),
        (19,'Text','',3),
        (21,'Food\'n\'Drinks','',1),
        (22,'Digital','',3),
        (23,'Service','',3),
        (24,'Money','',3),
        (25,'Transporting','',2),
        (26,'Fair currency','',4),
        (27,'Fiat currency','',4),
        (28,'Social currency','',4),
        (29,'Crypto currency','',4),
    )

    FacetValue(Facet, keys, rows)



# Migration interface

class Migration(migrations.Migration):

    dependencies = [
        ('valueaccounting', '0008_auto_20170319_1333'),
    ]

    operations = [
        migrations.RunPython(insertFacects),
        migrations.RunPython(insertFacetValues),
    ]
