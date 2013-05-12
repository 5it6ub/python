import unittest
from PIL import Image

class TestPillow(unittest.TestCase):

    def setUp(self):
        self.image = Image.open('lena.tiff')

    def test_open(self):
        """open image"""
        self.assertEqual('TIFF', self.image.format)
        self.assertEqual((512, 512), self.image.size)
        self.assertEqual('RGB', self.image.mode)

    def test_tojpeg(self):
        """resize image & convert to jpg"""
        small = self.image.resize([32, 32])
        small.save('lena_small.jpg', 'JPEG')

if __name__ == '__main__':
    unittest.main()
