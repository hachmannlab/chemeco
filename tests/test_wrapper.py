import unittest
import os
import shutil, tempfile
import pkg_resources

from chemeco import ChemEcoRun

CONFIG_PATH = pkg_resources.resource_filename('chemeco', os.path.join('tests', 'configfiles'))


class Testwrapper(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_template1(self):
        from chemeco.notebooks.templates import template1
        script =  template1()
        ChemEcoRun(script,os.path.join(self.test_dir,'test.out'))

    def test_template2(self):
        from chemeco.notebooks.templates import template2
        script = template2()
        ChemEcoRun(script, os.path.join(self.test_dir,'test.out'))

    def test_template3(self):
        from chemeco.notebooks.templates import template3
        script = template3()
        # require rdkit
        # wrapperRUN(script, os.path.join(self.test_dir,'test.out'))
    
    def test_template4(self):
        from chemeco.notebooks.templates import template4
        script = template4()
        # require Dragon
        #wrapperRUN(script, os.path.join(self.test_dir,'test.out'))
    
    def test_template5(self):
        from chemeco.notebooks.templates import template5
        script = template5()
        ChemEcoRun(script, os.path.join(self.test_dir,'test.out'))
    
    def test_template6(self):
        from chemeco.notebooks.templates import template6
        script = template6()
        # runs slow
        #wrapperRUN(script, os.path.join(self.test_dir,'test.out'))
    
    def test_template7(self):
        from chemeco.notebooks.templates import template7
        script = template7()
        ChemEcoRun(script, os.path.join(self.test_dir,'test.out'))
    
    def test_template8(self):
        from chemeco.notebooks.templates import template8
        script = template8()
        ChemEcoRun(script, os.path.join(self.test_dir,'test.out'))
    
    def test_template9(self):
        from chemeco.notebooks.templates import template9
        script = template9()
        ChemEcoRun(script, os.path.join(self.test_dir,'test.out'))
    

    def test_template11(self):
        from chemeco.notebooks.templates import template11
        script = template11()
        ChemEcoRun(script, os.path.join(self.test_dir,'test.out'))

    def test_template12(self):
        from chemeco.notebooks.templates import template12
        script = template12()
        ChemEcoRun(script, os.path.join(self.test_dir,'test.out'))

    def test_test1(self):
        ChemEcoRun(os.path.join(CONFIG_PATH,'test1.txt'), os.path.join(self.test_dir,'test.out'))


if __name__== '__main__':
    unittest.main()



