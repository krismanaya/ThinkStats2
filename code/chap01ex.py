"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

	This file also contains code for use with "Homework Assignments", 
	by Kris M. Anaya, available at http://www.github.com/krismanay

Copyright 2016 Kris M. Anaya 
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_file = '2002FemResp.dct', 
                dat_file = '2002FemResp.dat.gz'): 
    """Reads the NSFG female respondence data.
    
    dct_file: string in file name
    dat_file: string in file name
    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df

def MakePregMap(df):
    """Make a map from caseid to list of preg indices.

    df: DataFrame

    returns: dict that maps from caseid to list of indices into preg df
    """ 
    return nsfg.MakePregMap(df)

def IntersectPregRespMap(): 
	"""Creates a set that maps from each caseid to a list of indices 

	into the pregnancy DataFrame."""
	
	keys_a = set(MakePregMap(nsfg.ReadFemPreg()).keys())
	keys_b = set(MakePregMap(ReadFemResp()).keys())
	intersection = keys_a & keys_b
	return intersection


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    df = ReadFemResp()
    print(df.shape)
    # print(nsfg.MakePregMap(df))

    assert len(df) == 7643 
    
    assert df.pregnum.value_counts()[0] == 2610
    assert df.pregnum.value_counts()[1] == 1267
    assert df.pregnum.value_counts()[2] == 1432 
    assert df.pregnum.value_counts()[3] == 1110 
    assert df.pregnum.value_counts()[4] == 611
    assert df.pregnum.value_counts()[5] == 305
    assert df.pregnum.value_counts()[6] == 150 
    assert int(df.pregnum.value_counts()[range(7,len(df))].sum()) == 158
 



    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
