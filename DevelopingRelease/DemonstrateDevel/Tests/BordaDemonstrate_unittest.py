import os
import unittest
import rpy2.robjects as robjects

class BordaDemonstrateTest(unittest.TestCase):
    testdir = os.getcwd()+"/BordaTestFiles"
    
    def test_directory(self):
        self.assertTrue(os.path.isdir(self.testdir))
        
    def test_function(self):
        if os.path.isfile(self.testdir + '/Bordatest.pdf'):
            os.remove(self.testdir + '/Bordatest.pdf')
        if os.path.isfile(self.testdir + '/Canberratest.pdf'):
            os.remove(self.testdir + '/Canberratest.pdf')
        self.load_r()
        r_bordademo = robjects.globalenv['BordaPlot']
        r_bordademo(self.testdir)
        r_canberrademo = robjects.globalenv['CanberraPlot']
        r_canberrademo(self.testdir)
        self.assertTrue(os.path.isfile(self.testdir + '/Bordatest.pdf'))
        self.assertTrue(os.path.isfile(self.testdir + '/Canberratest.pdf'))
        self.assertTrue(os.path.getsize(self.testdir + '/Bordatest.pdf') > 0)
        self.assertTrue(os.path.getsize(self.testdir + '/Canberratest.pdf') > 0)
        
    def load_r(self):
        with open(os.getcwd()[:os.getcwd().index('Tests')]+'Borda_Demonstrate.R') as f:
            borda = f.read()
            canberra = f.read()
        robjects.r(borda)
        
def get_test_suite():
    return unittest.TestLoader().loadTestsFromTestCase(MPlotTest)

if __name__ == "__main__":
    unittest.main()

            
            
            
        
    
    