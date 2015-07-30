# -*- coding: utf-8 -*-
""" 
Functions for indentifying and using the command-line to execute Winnow for Python
"""


# Dependencies
import argparse


# Functions to be used later in the software
def initializeGraphics():
    """Prints introduction graphics for every time the software is run"""

    print "###################################################################"
    print "###                                                            ####"
    print "###      Winnow for Python!                                    ####"
    print "###      By Dustin A. Landers                                  ####"
    print "###      Contact: (770) 289-8830 -- dustin.landers@gmail.com   ####"
    print "###                                                            ####"
    print "###################################################################"


def usage():
    """Prints all possible command-line arguments to the screen; also ends the execution of the software"""

    print "\n\n\n"
    print "Command-line usage help menu.\n"
    print "--verbose or -v for verbose mode"
    print "--analysis or -a to specify either 'GWAS' or 'prediction' (if blank, Winnow assumes GWAS)"
    print "--folder or -F to input folder of box results (required)"
    print "--class or -C to specify the known-truth file for used simulation (required)"
    print "--snp or -S to specify a string for the name of the SNP column in results file (required)"
    print "--score or -P to specify a string for the name of the scoring column in results file (e.g., p-value; required)"
    print "--beta or -b to specify a string for the name of the estimated SNP effect column in results file"
    print "--filename or -f to specify the desired filename for the Winnow output file"
    print "--threshold ir -t to specify a desired threshold for classification performetrics where necessary"
    print "--seper or -s to specify either whitespace or comma"
    print "--kttype or -k to specify the type of known-truth file for --class (either OTE or FGS)"
    print "--kttypeseper or -r to specify delimination in known-truth file"
    print "--pvaladjust or -p to specify the type of P-value adjustment"
    print "--savep or -o to save P-values"
    print "--help or -h to see help menu\n\n"


def checkArgs():
    """Checks for arguments at beginning of the execution of the main function"""
    parser = argparse.ArgumentParser(description="Winnow command line arguments")
    parser.add_argument("-v", "--verbose", help="Trigger verbose mode", action="store_true")
    parser.add_argument("-a", "--analysis", nargs='?',
                        help="The type of analysis for Winnow to perform (currently, only GWAS is supported)",
                        default="GWAS", type=str, choices=["GWAS"])
    parser.add_argument("-F", "--folder", required=True, type=str, help="The input folder of box results")
    parser.add_argument("-C", "--class", required=True, type=str, help="The known-truth file for used simulation")
    parser.add_argument("-S", "--snp", required=True, type=str, help="The name of the SNP column in results file")
    parser.add_argument("-P", "--score", required=True, type=str,
                        help="The name of the scoring column in results file (e.g. p-value)")
    parser.add_argument("-b", "--beta", type=str, help="Name of the estimated SNP effect column in results file")
    parser.add_argument("-f", "--filename", type=str, default="Results",
                        help="The desired filename for the Winnow output file")
    parser.add_argument("-t", "--threshold", type=float, default=0.05,
                        help="A desired threshold for classification performetrics where necessary")
    parser.add_argument("-s", "--seper", type=str, choices=["comma", "whitespace", "tab"], default="whitespace",
                        help="Delimiter for box results")
    parser.add_argument("-k", "--kttype", type=str, required=True, choices=["OTE", "FGS"], default="OTE",
                        help="The type of known-truth file for --Class")
    parser.add_argument("-r", "--kttypeseper", choices=["comma", "whitespace", "tab"], nargs='?', default="whitespace",
                        help="Specify delimitation in known-truth file")
    parser.add_argument("-y", "--severity", type=float, default=None, nargs='?',
                        help="Severity ratio used in the h-measure calculation (currently not available, can leave blank)")
    parser.add_argument("-p", "--pvaladjust", default=None, nargs='?', choices=["BH"],
                        help="Specify the type of p-value adjustment")
    parser.add_argument("-o", "--savep", default=False, action="store_true",
                        help="Saves P-values in a text file if specified")
    args = parser.parse_args()

    """Change command line arguments into variables to pass along to the rest of the program"""
    verbose = args.verbose
    folder = args.Folder
    analysis = args.analysis
    truth = args.Class
    snp = args.Snp
    score = args.Score
    beta = args.beta
    filename = args.filename
    threshold = args.threshold
    seper = args.seper
    kttype = args.kttype
    kttypeseper = args.kttypeseper
    severity = args.severity
    pvaladjust = args.pvaladjust
    savep = args.savep
    if verbose:
        print "\nVerbose mode"
        print "Analysis method for being validated is specified as", analysis
        print "Folder of results files for validation is located in", folder
        print "Truth file is", truth
        print "SNP column name in results files is specified as", snp
        print "Scoring Column name (e.g. p-vale column) in results files is specified as", score
        print "Estimated SNP weight column name (e.g. regression betas) in results files is specified as", beta
        print "Filename specified as", filename
        print "Threshold is set at", threshold
        print "Delimination of results files is set as", seper
        print "Known-truth data format is set as", kttype
        print "Known-truth delimiter is set as", kttypeseper
        print "Severity ratio is specified at", severity
        print "P-value adjustment is set as", pvaladjust
        if savep:
            print "Saving p-values"

    if pvaladjust not in ["BH"] and pvaladjust is not None:
        print 'Currently only BH (Benjamini-Hochberg) is supported, the original P-values will be used'

    return folder, analysis, truth, snp, score, beta, filename, \
           threshold, seper, kttype, kttypeseper, severity, pvaladjust, savep


if __name__ == "__main__":
    import doctest

    doctest.testmod()
