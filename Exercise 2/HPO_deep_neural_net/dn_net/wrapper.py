#!/usr/bin/env python2.7
# encoding: utf-8

'''
abstractBlackBoxWrapper -- abstract call for black box wrapper; get_value() is not implemented

@author:     Marius Lindauer
@copyright:  2016 ML4AAD. All rights reserved.
@license:    BSD
@contact:    lindauer@informatik.uni-freiburg.de
'''

import sys
import re
import math
import logging

from genericWrapper4AC.generic_wrapper import AbstractWrapper

class AbstractBlackBoxWrapper(AbstractWrapper):
    '''
        Simple wrapper for a SAT solver (Spear)
    '''
    
    def __init__(self):
        AbstractWrapper.__init__(self)
        
        self._return_value = None
    
    def get_command_line_args(self, runargs, config):
        '''
        Returns the command line call string to execute the target algorithm (here: Spear).
        Args:
            runargs: a map of several optional arguments for the execution of the target algorithm.
                    {
                      "instance": <instance>,
                      "specifics" : <extra data associated with the instance>,
                      "cutoff" : <runtime cutoff>,
                      "runlength" : <runlength cutoff>,
                      "seed" : <seed>
                    }
            config: a mapping from parameter name to parameter value
        Returns:
            A command call list to execute the target algorithm.
        '''
        config = dict((name[1:], value) for name, value in config.items()) # remove leading "-" at parameter names
        self._return_value = self.get_value(runargs["instance"],config)
        #NOTE: We cheat here by already evaluating the target function. Therefore, the resource limitation will not work 
        
        return "" # by returning an empty string, the target algorithm call will be skipped
    
    def process_results(self, filepointer, exit_code):
        '''
        Parse a results file to extract the run's status (SUCCESS/CRASHED/etc) and other optional results.
    
        Args:
            filepointer: a pointer to the file containing the solver execution standard out.
            exit_code : exit code of target algorithm
        Returns:
            A map containing the standard AClib run results. The current standard result map as of AClib 2.06 is:
            {
                "status" : <"SAT"/"UNSAT"/"TIMEOUT"/"CRASHED"/"ABORT">,
                "runtime" : <runtime of target algrithm>,
                "quality" : <a domain specific measure of the quality of the solution [optional]>,
                "misc" : <a (comma-less) string that will be associated with the run [optional]>
            }
            ATTENTION: The return values will overwrite the measured results of the runsolver (if runsolver was used). 
        '''
        resultMap = {'status' : 'SUCCESS',
                     'quality' : self._return_value
                     }
        return resultMap

    def get_value(self,instance,config):
        '''
        Returns the command line call string to execute the target algorithm (here: Spear).
        Args:
            config: a mapping from parameter name to parameter value (str)
        Returns:
            the function value
        '''
        raise NotImplementedError()