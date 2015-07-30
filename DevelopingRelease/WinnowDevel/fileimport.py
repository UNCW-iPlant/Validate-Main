"""
Functions to handle importing class and results files as well as exporting output
"""

import csv

def trueFalse(currentSnp, ktSnps):
    """
    Defines the known truth list

    :param currentSnp: current SNP
    :param ktSnps: known-truth SNPs
    :return: True is the current SNP is in the known-truth SNPs
    """
    if currentSnp in ktSnps:
        return True
    else:
        return False


def writeCSV(filename, keepToWrite, method="wb", exportDelimiter=","):
    """
    Writes the Winnow output file once analysis is complete

    :param filename: file name to save as
    :param keepToWrite: data to write
    :param method: writing method
    :param exportDelimiter: how data is separated
    """
    with open(filename + ".txt", method) as openFile:
        openFileWriter = csv.writer(openFile, delimiter=exportDelimiter)
        if method == "wb":
            openFileWriter.writerow(keepToWrite[0])
        currentRow = list()
        for item in keepToWrite[1]:
            currentRow.append(item)
        openFileWriter.writerow(currentRow)


def writeSettings(winnowargs):
    """
    Saves a settings file with parameters used in Winnow

    :param winnowargs: dictionary of runtime arguments used in Winnow
    :return: saves a txt file with the given filename that is appended with _settings containing the list of data files,
    the truth and results file, the type of analysis, the type of known truth, and the threshold.
    """
    a = winnowargs['analysis']
    if winnowargs['beta'] is not None:
        a += 'WithBeta'
    else:
        a += 'WithoutBeta'
    with open(winnowargs['filename'] + "_parameters.txt", 'wb') as openFile:
        openFileWriter = csv.writer(openFile, delimiter='\t')
        openFileWriter.writerow(('Analysis Type: ', a))
        openFileWriter.writerow(('KT Type: ', winnowargs['kt_type']))
        openFileWriter.writerow(('Threshold: ', winnowargs['threshold']))
        if winnowargs['pvaladjust'] is not None and 'pvaladjust' in winnowargs.keys():
            openFileWriter.writerow(('Adjustment:', winnowargs['pvaladjust']))
