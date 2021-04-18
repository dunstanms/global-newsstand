import unittest
from app.models import Sources,Articles

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('CNN','CNN News','Cable News Newtork that is a leader in providing news worldwide','cnn.com','general','U.S.A','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'CNN')
        self.assertEquals(self.new_source.name,'CNN News')
        self.assertEquals(self.new_source.description,'Cable News Newtork that is a leader in providing news worldwide')
        self.assertEquals(self.new_source.url,'cnn.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'U.S.A')
        self.assertEquals(self.new_source.language,'en')

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('CNN','David Goldman','What is Dogecoin? How a joke became hotter than bitcoin','cnn.com','https://cdn.cnn.com/cnnnext/dam/assets/210107104229-03-bitcoin---stock-super-tease.jpg',' April 17, 2021')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'CNN')
        self.assertEquals(self.new_article.author,'David Goldman')
        self.assertEquals(self.new_article.title,'What is Dogecoin? How a joke became hotter than bitcoin')
        self.assertEquals(self.new_article.description,'a look at crypto ')
        self.assertEquals(self.new_article.url,'https://edition.cnn.com/2021/04/17/investing/what-is-dogecoin/index.html')
        self.assertEquals(self.new_article.image,'https://cdn.cnn.com/cnnnext/dam/assets/210107104229-03-bitcoin---stock-super-tease.jpg')
        self.assertEquals(self.new_article.date,'April 17, 2021')