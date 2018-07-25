import os
import flasker
import unittest
import tempfile

class FlaskerTestCase(unittest.TestCase):
	"""docstring for FlaskerTestCase"""
	def setUp(self):
		self.db_fd,flasker.app.config['DATABASE'] = tempfile.mkstemp()
		flasker.app.config['TESTING'] = True
		self.app = flasker.app.test_client()
		flasker.init_db()

	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(flasker.app.config['DATABASE'])

if __name__ == '__main__':
	unittest.main()
		