import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('CNN','Peter Polle','The tech scene in Africa-Is it the next big thing?','A look at various tech hubs in Africa and the impact they have on the worlds economy','techie.com','techie.com/7643t94.jpg','2018-04-11T07:57:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'CNN')
        self.assertEquals(self.new_article.author,'Peter Polle')
        self.assertEquals(self.new_article.title,'The tech scene in Africa-Is it the next big thing?')
        self.assertEquals(self.new_article.description,'A look at various tech hubs in Africa and the impact they have on the worlds economy')
        self.assertEquals(self.new_article.url,'techie.com')
        self.assertEquals(self.new_article.image,'techie.com/7643t94.jpg')
        self.assertEquals(self.new_article.date,'2018-04-11T07:57:16Z')

# class ArticlesTest(unittest.TestCase):
#     '''
#     Test Class to test the behaviour of the News class
#     '''

#     def setUp(self):
#         '''
#         Set up method that will run before every Test
#         '''
#         self.new_article = Articles('CNN','David Goldman','What is Dogecoin? How a joke became hotter than bitcoin','cnn.com','https://cdn.cnn.com/cnnnext/dam/assets/210107104229-03-bitcoin---stock-super-tease.jpg','2021-4-17')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_article,Articles))

#     def test_to_check_instance_variables(self):
#         self.assertEquals(self.new_article.id,'CNN')
#         self.assertEquals(self.new_article.author,'David Goldman')
#         self.assertEquals(self.new_article.title,'What is Dogecoin? How a joke became hotter than bitcoin')
#         self.assertEquals(self.new_article.description,'a look at crypto ')
#         self.assertEquals(self.new_article.url,'https://edition.cnn.com/2021/04/17/investing/what-is-dogecoin/index.html')
#         self.assertEquals(self.new_article.image,'https://cdn.cnn.com/cnnnext/dam/assets/210107104229-03-bitcoin---stock-super-tease.jpg')
#         self.assertEquals(self.new_article.date,'2021-4-17')