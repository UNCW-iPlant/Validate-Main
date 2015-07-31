"""
Performs functions necessary for GWAS analysis 
"""

from performetrics import *


def gwasWithBeta(data_file, betaColumn, betaTrueFalse, snpTrueFalse, scoreColumn, threshold):
    """
    Performs GWAS analysis with Beta

    :param betaColumn: collected positions
    :param betaTrueFalse: known of the collected positions
    :param snpTrueFalse: true/false data set
    :param scoreColumn: score data set
    :param threshold: significant threshold
    :return: an array of functions and an array of those functions' results
    """
    return {'names': data_file, 'rmse': rmse(betaColumn, betaTrueFalse), 'mae': mae(betaColumn, betaTrueFalse),
            'mattcorr': mattcorr(snpTrueFalse, threshold, scoreColumn), 'auc': auc(snpTrueFalse, scoreColumn),
            'tp': tp(snpTrueFalse, threshold, scoreColumn), 'fp': fp(snpTrueFalse, threshold, scoreColumn),
            'tn': tn(snpTrueFalse, threshold, scoreColumn), 'fn': fn(snpTrueFalse, threshold, scoreColumn),
            'tpr': tpr(snpTrueFalse, threshold, scoreColumn), 'fpr': fpr(snpTrueFalse, threshold, scoreColumn),
            'error': error(snpTrueFalse, threshold, scoreColumn),
            'accuracy': accuracy(snpTrueFalse, threshold, scoreColumn),
            'sens': sens(snpTrueFalse, threshold, scoreColumn), 'spec': spec(snpTrueFalse, threshold, scoreColumn),
            'prec': precision(snpTrueFalse, threshold, scoreColumn), 'fdr': fdr(snpTrueFalse, threshold, scoreColumn),
            'youden': youden(snpTrueFalse, threshold, scoreColumn)}


def gwasWithoutBeta(data_file, snpTrueFalse, scoreColumn, threshold):
    """
    Performs GWAS analysis without Beta

    :param snpTrueFalse: true/false data set
    :param scoreColumn: score data set
    :param threshold: significant threshold
    :return: an array of functions and an array of those functions' results
    """
    return {'names': data_file,  'mattcorr': mattcorr(snpTrueFalse, threshold, scoreColumn),
            'auc': auc(snpTrueFalse, scoreColumn), 'tp': tp(snpTrueFalse, threshold, scoreColumn),
            'fp': fp(snpTrueFalse, threshold, scoreColumn), 'tn': tn(snpTrueFalse, threshold, scoreColumn),
            'fn': fn(snpTrueFalse, threshold, scoreColumn), 'tpr': tpr(snpTrueFalse, threshold, scoreColumn),
            'fpr': fpr(snpTrueFalse, threshold, scoreColumn), 'error': error(snpTrueFalse, threshold, scoreColumn),
            'accuracy': accuracy(snpTrueFalse, threshold, scoreColumn),
            'sens': sens(snpTrueFalse, threshold, scoreColumn), 'spec': spec(snpTrueFalse, threshold, scoreColumn),
            'prec': precision(snpTrueFalse, threshold, scoreColumn), 'fdr': fdr(snpTrueFalse, threshold, scoreColumn),
            'youden': youden(snpTrueFalse, threshold, scoreColumn)}
