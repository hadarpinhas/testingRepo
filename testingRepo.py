
import unittest
import time
import tensorflow as tf


class TestingRepo(unittest.TestCase):
	def setUp(self):
		self.startTime = time.time()

	def tearDown(self):
		t = time.time() - self.startTime
		print('%s: %.5f minutes' % (self.id(), (t/60)))

	def testOne(self):

		print('-'*100 + '\n' + ' '*50 + 'running TestingRepo\n' + '-'*100)
		


	#--------------------------------------------------------------------

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestingRepo)
	unittest.TextTestRunner(verbosity=0).run(suite)
