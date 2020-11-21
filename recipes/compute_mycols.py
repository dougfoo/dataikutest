# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
hokkaido_covid19_patients = dataiku.Dataset("010006_hokkaido_covid19_patients")
hokkaido_covid19_patients_df = hokkaido_covid19_patients.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

mycols_df = hokkaido_covid19_patients_df[3]
# For this sample code, simply copy input to output


# Write recipe outputs
mycols = dataiku.Dataset("mycols")
mycols.write_with_schema(mycols_df)
