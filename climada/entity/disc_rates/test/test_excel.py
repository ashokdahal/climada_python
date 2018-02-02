"""
Test DiscRatesExcel class.
"""

import unittest
import numpy

from climada.entity.disc_rates.source_excel import DiscRatesExcel
from climada.util.constants import ENT_DEMO_XLS, ENT_TEMPLATE_XLS

class TestReader(unittest.TestCase):
    """Test reader functionality of the DiscRatesExcel class"""

    def test_demo_file_pass(self):
        """ Read demo excel file."""
        # Read demo excel file
        disc_rate = DiscRatesExcel()
        description = 'One single file.'
        disc_rate.read(ENT_DEMO_XLS, description)

        # Check results
        n_rates = 51

        self.assertEqual(type(disc_rate.years[0]), numpy.int64)
        self.assertEqual(disc_rate.years.shape, (n_rates,))
        self.assertEqual(disc_rate.years[0], 2000)
        self.assertEqual(disc_rate.years[n_rates-1], 2050)

        self.assertEqual(type(disc_rate.rates[0]), numpy.float64)
        self.assertEqual(disc_rate.rates.shape, (n_rates,))
        self.assertEqual(disc_rate.rates.min(), 0.02)
        self.assertEqual(disc_rate.rates.max(), 0.02)

        self.assertEqual(disc_rate.tag.file_name, ENT_DEMO_XLS)
        self.assertEqual(disc_rate.tag.description, description)

    def test_template_file_pass(self):
        """ Read demo excel file."""
        # Read demo excel file
        disc_rate = DiscRatesExcel()
        disc_rate.read(ENT_TEMPLATE_XLS)

        # Check results
        n_rates = 102

        self.assertEqual(type(disc_rate.years[0]), numpy.int64)
        self.assertEqual(disc_rate.years.shape, (n_rates,))
        self.assertEqual(disc_rate.years[0], 2000)
        self.assertEqual(disc_rate.years[n_rates-1], 2101)

        self.assertEqual(type(disc_rate.rates[0]), numpy.float64)
        self.assertEqual(disc_rate.rates.shape, (n_rates,))
        self.assertEqual(disc_rate.rates.min(), 0.02)
        self.assertEqual(disc_rate.rates.max(), 0.02)

        self.assertEqual(disc_rate.tag.file_name, ENT_TEMPLATE_XLS)
        self.assertEqual(disc_rate.tag.description, '')

    def test_wrong_file_fail(self):
        """ Read file without year column, fail."""
        # Read demo excel file
        disc_rate = DiscRatesExcel()
        disc_rate.col_names['year'] = 'wrong col'
        with self.assertRaises(KeyError):
            disc_rate.read(ENT_DEMO_XLS)

# Execute Tests
TESTS = unittest.TestLoader().loadTestsFromTestCase(TestReader)
unittest.TextTestRunner(verbosity=2).run(TESTS)