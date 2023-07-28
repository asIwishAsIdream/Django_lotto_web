from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected number')
        g.generate()
        
        print(g.update_date) # 시간 찍기
        print(g.lottos)
        
        self.assertTrue(len(g.lottos) > 20)  # 주어진 값이 True인지 확인해봐라, OK라고 나면 된거임
        
        