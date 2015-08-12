"""
Functions for identifying and using the command-line to execute Demonstrate through Python
"""

import argparse


def initialize_graphics():
    """ Prints introduction graphics for every time the software runs """

    print "###################################################################"
    print "###                                                            ####"
    print "###                Demonstrate Through Python!                 ####"
    print "###                                                            ####"
    print "###################################################################"


def usage():
    """ Prints all possible command-line arguments to the screen """
    print "\n\n\n"
    print "Command-line usage help menu"
    print "--help or -h to see the help menu"
    print "--verbose or -v for verbose mode"
    print "--dir or -d to specify the directory containing the input files (required)"
    print "--settingsfile or -s to specify the settings file from Winnow"
    print "--mode or -o to specify either Demonstrate or Demonstrate2 (required)"
    print "Demonstrate Arguments"
    print "\t--auc or -a to include the AUC plot"
    print "\t--auctitle or -t to specify the AUC plot title"
    print "\t--mae or -m to include the MAE plot"
    print "\t--maetitle or -y to specify the MAE plot title"
    print "\t--heritstring or -r to specify the strings representing heritability found in the data files (required)"
    print "\t--heritvalue or -l to specify the heritability values (required)"
    print "\t--structstring or -u to specify the strings representing the structure found in the data files (required)"
    print "\t--structvalue or -p to specify the value of structure (TRUE or FALSE, required)"
    print "Demonstrate2 Arguments"
    print "\t--pos or -q to include the TP by FP plot"
    print "\t--postitle or -i to specify the TP by FP title"
    print "\t--error or -e to include the Error plot"
    print "\t--errortitle or -w to specify the Error plot title"
    print "\t--extraplots or -x to not include extra plots"
    print "\t--aucmin or -z to specify the minimum for the AUC axis"
    print "\t--aucmax or -b to specify the maximum for the AUC axis"
    print "\t--maemin or -n to specify the minimum for the MAE axis"
    print "\t--maemax or -c to specify the maximum for the MAE axis\n\n"


def check_args():
    """ Checks for arguments at beginning of the execution of the main function """

    parser = argparse.ArgumentParser(description="Demonstrate command-line arguments")
    parser.add_argument("-v", "--verbose", help="Trigger verbose mode", action="store_true", default=False)
    parser.add_argument("-d", "--dir", required=True, type=str, help="The input folder")
    parser.add_argument("-s", "--settingsfile", type=str, help="The .param file from winnow", default=None)
    parser.add_argument("-o", "--mode", type=str, required=True, choices=["demo", "demo2"],
                        help="Graphics mode (demo or demo2")
    parser.add_argument("-a", "--auc", action="store_false", default=True,
                        help="To include the AUC plot")
    parser.add_argument("-t", "--auctitle", type=str, default="Mean AUC By Population Structure and Heritability",
                        help="AUC plot title")
    parser.add_argument("-m", "--mae", action="store_false", default=True,
                        help="To include the MAE plot")
    parser.add_argument("-y", "--maetitle", type=str, default="Mean MAE By Population Structure and Heritability",
                        help="MAE plot title")
    parser.add_argument("-r", "--heritstring", type=str, default=["_03_", "_04_", "_06_"],
                        help="Heritability string from input data")
    parser.add_argument("-l", "--heritvalue", type=float, default=[0.3, 0.4, 0.6],
                        help="Heritability value from input data")
    parser.add_argument("-u", "--structstring", type=str, default=["PheHasStruct", "PheNPStruct"],
                        help="Structure string from input data")
    parser.add_argument("-p", "--structvalue", type=bool, default=[True, False],
                        help="Structure value from input data")
    parser.add_argument("-q", "--pos", action="store_false", default=True,
                        help="To include the TP by FP plot")
    parser.add_argument("-i", "--postitle", type=str, default="True Positives by False Positives",
                        help="TP by FP plot title")
    parser.add_argument("-e", "--error", action="store_false", default=True,
                        help="To include the error plot")
    parser.add_argument("-w", "--errortitle", type=str, default="Plot of AUC by MAE",
                        help="The error plot title")
    parser.add_argument("-x", "--extraplots", action="store_false", default=True,
                        help="To include extra plots")
    parser.add_argument("-z", "--aucmin", type=float, default=0,
                        help="Minimum auc axis value")
    parser.add_argument("-b", "--aucmax", type=float, default=1.0,
                        help="Maximum auc axis value")
    parser.add_argument("-n", "--maemin", type=float, default=0,
                        help="Minimum mae axis value")
    parser.add_argument("-c", "--maemax", type=float, default=2.0,
                        help="Maximum mae axis value")
    parser = parser.parse_args()
    if parser.verbose:
        print "\nVerbose Mode"
        print "Input directory is specified as", parser.dir
        if parser.settingsfile is not None:
            print "Settings file is specified as", parser.settingsfile
        print "Demonstrate mode is set to", parser.mode
        if parser.mode == "demo":
            if parser.auc:
                print "AUC plot not included"
            else:
                print "AUC plot included"
                print "AUC plot title specified as", parser.auctitle
            if parser.mae:
                print "MAE plot not included"
            else:
                print "MAE plot included"
                print "MAE plot title specified as", parser.maetitle
            print "Heritability strings specified as", parser.heritstring
            print "Heritability values specified as", parser.heritvalue
            print "Structure strings specified as", parser.structstring
            print "Structure values specified as", parser.structvalue
        elif parser.mode == "demo2":
            if parser.pos:
                print "TP by FP plot not included"
            else:
                print "TP by FP plot included"
                print "TP by FP plot title specified as", parser.postitle
            if parser.error:
                print "Error plot not included"
            else:
                print "Error plot included"
                print "Error plot title specified as", parser.errortitle
            if parser.extraplots:
                print "Extra plots not included"
            print "AUC axis minimum specified as", parser.aucmin
            print "AUC axis maximum specified as", parser.aucmax
            print "MAE axis minimum specified as", parser.maemin
            print "MAE axis maximum specified as", parser.maemax
    if parser.mode == "demo":
        return {"dir": parser.dir, "settings": parser.settingsfile, "mode": parser.mode, "auc": parser.auc,
                "auct": parser.auctitle, "mae": parser.mae, "maet": parser.maetitle, "heritstring": parser.heritstring,
                "heritvalue": parser.heritvalue, "structstring": parser.structstring, "structvalue": parser.structvalue}
    elif parser.mode == "demo2":
        return {"dir": parser.dir, "settings": parser.settingsfile, "mode": parser.mode, "pos": parser.pos,
                "post": parser.postitle, "error": parser.error, "errort": parser.errortitle, "extra": parser.extraplots,
                "aucmin": parser.aucmin, "aucmax": parser.aucmax, "maemin": parser.maemin, "maemax": parser.maemax}


if __name__ == "__main__":
    initialize_graphics()
    usage()
    print check_args()