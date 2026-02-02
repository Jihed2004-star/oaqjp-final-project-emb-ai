import unittest
from EmotionDetection.emotion_detection import *
class test_emotion_detection(unittest.TestCase):
    def testJoy(self):
        self.assertEquals(emotion_detector('I am glad this happened')['dominant_emotion'],'joy')
    def testAnger(self):
        self.assertEquals(emotion_detector('I am really mad about this')['dominant_emotion'],'anger')
    def testDisgust(self):
        self.assertEquals(emotion_detector('I feel disgusted just hearing about this')['dominant_emotion'],'disgust')
    def testSadness(self):
        self.assertEquals(emotion_detector('I am so sad about this')['dominant_emotion'],'sadness')
    def testFear(self):
        self.assertEquals(emotion_detector('I am really afraid that this will happen')['dominant_emotion'],'fear')

unittest.main()