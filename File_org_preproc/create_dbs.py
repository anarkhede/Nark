# Checks if Study.db exist an then runs through study folder creating a new entry if it doesent exist in the db.
# Adds fields: Study, SubjID, Seqs, Analysis: Name, Maual Corrections, Post Manual Corrections, Result.

function create_db:
  import csv
  import json
  import pandas as pd
  import sys, getopt, pprint
  from pymongo import MongoClient
  
  #TXT to JSON Conversion
 
