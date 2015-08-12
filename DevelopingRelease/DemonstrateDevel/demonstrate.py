from commandline import initialize_graphics, check_args
import rpy2.robjects as robjects
import os


class Demonstrate:
    def __init__(self, args):
        self.args = args
        self.r_args = {"dir": self.args["dir"]}
        self.load_r()
        if self.args["mode"] == "demo":
            self.demonstrate_one()
        elif self.args["mode"] == "demo2":
            self.demonstrate_two()

    def load_r(self):
        mode = self.args["mode"]
        if mode == "demo":
            with open(os.getcwd()+"/DemoMPlot/R/Demonstrate.R") as f:
                dem = f.read()
            robjects.r(dem)
        elif mode == "demo2":
            with open(os.getcwd()+"/DemoMPlot/R/Demonstrate2.R") as f:
                dem2 = f.read()
            robjects.r(dem2)

    def demonstrate_one(self):
        r_dem = robjects.globalenv['Demonstrate']
        self.args["auct"] = add_pdf_extension(self.args["auct"])
        self.args["maet"] = add_pdf_extension(self.args["maet"])
        r_dem(self.args["dir"], check_for_null(self.args["settings"]), self.args["auc"], self.args["auct"],
              self.args["mae"], self.args["maet"]+".pdf", self.args["heritstring"], self.args["heritvalue"],
              self.args["structstring"], self.args["structvalue"])

    def demonstrate_two(self):
        r_dem2 = robjects.globalenv['Demonstrate2']


def check_for_null(entry):
    if entry is None:
        return robjects.NULL
    else:
        return entry


def add_pdf_extension(s):
    if ".pdf" not in s:
        return s + ".pdf"


def initialize():
    initialize_graphics()
    return check_args()


def main():
    args = initialize()
    print args
    demon = Demonstrate(args)



if __name__ == "__main__":
    main()
