# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from work.models import Ocp_Artwork_Type, Ocp_Skill_Type, Ocp_Unit_Type, Ocp_Record_Type

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

def insertArtworkTypes(apps, schema_editor):
    keys = (
        "artwork_type_id",
        "context_agent_id",
        "facet_id",
        "facet_value_id",
        "material_type_id",
        "nonmaterial_type_id",
        "resource_type_id",
        "unit_type_id",
    )

    rows = (
        (9,None,1,None,None,None,None,None),
        (10,None,3,None,None,None,None,None),
        (49,None,None,17,None,None,None,None),
        (50,None,None,None,None,None,None,None),
        (51,None,None,22,None,None,None,None),
        (52,None,None,None,None,None,None,None),
        (53,None,None,None,None,None,None,None),
        (54,None,None,None,None,None,None,None),
        (55,None,None,None,None,None,None,None),
        (56,None,None,None,None,None,None,None),
        (57,None,None,None,None,None,60,None),
        (65,None,None,None,None,None,None,None),
        (71,None,None,19,None,None,None,None),
        (72,None,None,None,None,None,None,None),
        (73,None,None,None,None,None,None,None),
        (74,None,None,None,None,None,None,None),
        (75,None,None,None,None,None,59,None),
        (76,None,None,None,None,None,None,None),
        (77,None,None,None,None,None,None,None),
        (78,None,None,None,None,None,None,None),
        (79,None,None,None,None,None,None,None),
        (80,None,None,None,None,None,None,None),
        (81,None,None,None,None,None,None,None),
        (82,None,None,None,None,None,None,None),
        (83,None,None,None,None,None,None,None),
        (84,None,None,None,None,None,None,None),
        (85,None,None,None,None,None,None,None),
        (86,None,None,None,None,None,None,None),
        (87,None,None,None,None,None,None,None),
        (88,None,None,9,None,None,None,None),
        (89,None,None,10,None,None,None,None),
        (90,None,None,None,None,None,None,None),
        (91,None,None,None,None,None,None,None),
        (92,None,None,None,None,None,None,None),
        (93,None,None,None,None,None,None,None),
        (94,None,None,None,None,None,None,None),
        (95,None,None,None,None,None,None,None),
        (96,None,None,None,None,None,None,None),
        (97,None,None,None,None,None,None,None),
        (98,None,None,None,None,None,None,None),
        (149,None,None,16,None,None,None,None),
        (151,None,None,None,None,None,None,None),
        (152,None,None,None,None,None,36,None),
        (153,None,None,None,None,None,6,None),
        (155,None,None,24,None,None,None,None),
        (156,None,None,26,None,None,46,237),
        (157,None,None,27,None,None,54,249),
        (158,None,None,24,None,None,None,None),
        (159,None,None,27,None,None,47,249),
        (160,None,None,21,None,None,None,None),
        (161,None,None,8,None,None,None,None),
        (162,None,None,None,None,None,31,None),
        (163,None,None,None,None,None,33,None),
        (164,None,None,None,None,None,17,None),
        (165,None,None,None,None,None,37,None),
        (166,None,None,None,None,None,32,None),
        (167,None,None,None,None,None,44,None),
        (168,None,None,None,None,None,28,None),
        (169,None,None,None,None,None,None,None),
        (170,None,None,None,None,None,24,None),
        (171,None,None,None,None,None,15,None),
        (172,None,None,None,None,None,14,None),
        (175,None,None,None,None,None,29,None),
        (177,None,None,None,None,None,None,None),
        (178,None,None,None,None,None,48,None),
        (179,None,None,None,None,None,27,None),
        (250,None,None,None,None,None,51,None),
        (261,None,None,None,None,None,52,None),
        (262,None,None,None,None,None,55,None), # :TODO: is missing valueaccounting_economicresourcetypes
        (264,None,None,None,None,None,56,None),
        (265,None,None,None,None,None,57,None),
        (271,None,None,None,161,None,58,None),
    )

    ensureRows(Ocp_Artwork_Type, keys, rows)

def insertSkillTypes(apps, schema_editor):
    keys = (
        "job_id",
        "facet_value_id",
        "resource_type_id",
        "ocp_artwork_type_id",
        "facet_id",
    )

    rows = (
        (1,None,None,None,None),
        (2,None,None,None,None),
        (3,None,None,None,None),
        (4,25,None,None,None),
        (5,None,None,None,None),
        (6,None,None,None,None),
        (7,14,None,None,None),
        (8,None,None,None,None),
        (9,None,None,None,None),
        (10,None,None,None,None),
        (11,None,None,None,None),
        (12,None,None,None,None),
        (13,None,None,None,None),
        (14,None,None,None,None),
        (15,13,None,None,None),
        (16,None,None,None,None),
        (17,None,None,None,None),
        (18,None,None,None,None),
        (19,None,None,None,None),
        (20,None,None,None,None),
        (21,None,None,None,None),
        (22,None,None,None,None),
        (25,None,None,None,2),
        (26,None,None,None,None),
        (27,12,None,None,None),
        (28,None,None,None,None),
        (29,None,None,None,None),
    )

    ensureRows(Ocp_Skill_Type, keys, rows)

def insertUnitTypes(apps, schema_editor):
    keys = (
        "unit_type_id",
        "ocp_unit_id",
        "unit_id",
    )

    rows = (
        (34,None,None),
        (35,None,11),
        (36,None,None),
        (37,None,None),
        (38,None,None),
        (48,None,None),
        (67,None,None),
        (68,None,None),
        (232,None,None),
        (233,None,5),
        (234,None,8),
        (235,None,9),
        (236,None,None),
        (237,None,7),
        (238,None,14),
        (240,None,None),
        (241,None,1),
        (242,None,3),
        (243,None,4),
        (244,None,None),
        (245,None,15),
        (246,None,10),
        (247,None,12),
        (248,None,13),
        (249,None,2),
    )

    ensureRows(Ocp_Unit_Type, keys, rows)

def insertRecordTypes(apps, schema_editor):
    keys = (
        "record_type_id",
        "exchange_type_id",
        "ocp_artwork_type_id",
        "ocp_skill_type_id",
    )

    rows = (
        (125,None,None,None),
        (126,None,None,None),
        (127,None,None,None),
        (128,None,None,None),
        (129,None,None,None),
        (130,None,None,None),
        (131,None,9,None),
        (132,None,10,None),
        (133,None,None,25),
        (134,None,9,None),
        (135,None,10,None),
        (136,None,None,25),
        (137,None,9,None),
        (138,None,9,None),
        (139,None,10,None),
        (140,None,10,None),
        (141,None,None,None),
        (142,None,None,None),
        (143,None,9,None),
        (144,None,10,None),
        (145,None,None,25),
        (146,None,9,None),
        (147,None,10,None),
        (148,None,None,25),
        (181,None,None,None),
        (182,None,None,None),
        (183,None,None,None),
        (184,None,161,None),
        (185,None,None,None),
        (186,None,None,None),
        (187,None,None,None),
        (214,None,None,None),
        (215,None,None,None),
        (217,None,None,None),
        (218,None,None,None),
        (219,None,None,None),
        (220,None,None,None),
        (221,None,None,None),
        (222,None,None,None),
        (223,None,None,None),
        (224,None,None,None),
        (225,None,None,None),
        (226,None,None,None),
        (227,None,None,None),
        (228,None,None,None),
        (229,None,None,None),
        (230,None,None,None),
        (231,None,161,None),
        (251,None,156,None),
        (252,None,None,None),
        (253,None,None,None),
        (254,None,156,None),
        (256,None,None,18),
        (257,None,160,None),
        (258,None,None,15),
        (259,None,89,None),
        (260,None,89,None),
        (263,None,262,None),
        (266,None,9,None),
        (267,None,10,None),
        (269,None,89,None),
        (270,None,87,None),
        (274,None,152,None),
        (275,None,75,None),
        (276,None,271,None),
        (277,None,161,None),
    )

    ensureRows(Ocp_Record_Type, keys, rows)


# Migration interface

class Migration(migrations.Migration):

    dependencies = [
        ('work', '0018_ocp_material_type_ocp_nonmaterial_type_ocp_record_type'),
        ('work', '0019_auto_20161207_1438'),
        ('work', '0020_ocp_skill_type'),
        ('work', '0021_ocp_artwork_type'),
        ('work', '0023_auto_20170121_0004'),
        ('work', '0025_ocp_skill_type_facet'),
        ('work', '0024_ocp_unit_type'),
        ('work', '0025_ocp_skill_type_facet'),
        ('work', '0026_ocp_record_type_ocp_skill_type'),
        ('work', '0027_ocp_artwork_type_unit_type'),
    ]

    operations = [
        migrations.RunPython(insertArtworkTypes),
        migrations.RunPython(insertSkillTypes),
        migrations.RunPython(insertUnitTypes),
        migrations.RunPython(insertRecordTypes)
    ]
