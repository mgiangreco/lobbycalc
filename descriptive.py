#!/usr/bin/env python
import sys
import os
import glob
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

def csv_reader (file_name) : 
	return pd.read_csv(file_name)

def full_name(lobbyists_frame, name_parts) :
	result = ''
	zero = name_parts[0]
	Last_Name = lobbyists_frame[zero]
	one = name_parts[1]
	First_Name = lobbyists_frame[one]
	two = name_parts[2]
	Middle = lobbyists_frame[two]
	return Last_Name+First_Name+Middle

def currency_sum(arr):
    widget = 0 
    result = 0

    for word in arr: 
    	word = word.replace("$", "")
    	word = word.replace(",", "")
    	my_float = float(word)
    	result = result + my_float
    return result

def aggregate_by_compensation_sum(frame, key_field, sum_field) :
	groups = frame.groupby(frame[key_field])[sum_field]
	return groups.agg(currency_sum)

def aggregate_by_compensation_sum_new(frame, key_field, sum_field) :
	groups = frame.groupby(frame[key_field])[sum_field]
	return groups.agg(currency_sum)


def top_n(frame, n) :
	frame.sort_values(ascending=False, inplace=True)
	return frame.head(n)
	
if __name__ == '__main__':
	lobbyists_frame = csv_reader(sys.argv[1])
	lobbyists_frame['full_name'] = full_name(lobbyists_frame, ['LAST NAME','FIRST NAME','LOBBYIST MIDDLE INITIAL'])

	lobbyist_totals = aggregate_by_compensation_sum(lobbyists_frame, 'full_name', 'COMPENSATION')
	print lobbyist_totals.ix['KASPERMICHAELJ']
	print top_n(lobbyist_totals, 20)
