from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
# 가장 핵심, URL을 받아낸다
# 유저가 url을 검색하면 urls에서 path를 통해서 views.??? 로 넘어오게 되는데 이때 POST, GET이 나눠어지고 그 정보를 request로 받아준다.
def index(request):
    print(request.method) # GET
    lottos = GuessNumbers.objects.all()
    
    # 1은 약속, 2는 유저에게 넘겨줄 html, {} 나중에 이 중괄호로 예측된 결과 값을 html에 함께 넣어줄 공간이다
    return render(request, 'lotto/default.html', {'lottos':lottos}) # context-dict라고한다

def post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            
            lotto = form.save(commit=False)
            lotto.generate()
            print(type(lotto)) # <class 'lotto.models.GuessNumbers'>
            print(lotto) # pk None : 최낙현 - 20대
            return redirect('index')
    else:
        # request.method가 GET일때 즉 /lotto/new/ URL로 접속했을 때
        form = PostForm()
    
        return render(request, 'lotto/form.html',{'form':form})


def hello(request):
    
    data = GuessNumbers.objects.all()
    
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

    # index.html
    #<input type='text' name='name'></input>
    #<input type='text' name='text'></input>
    
    # user_input_name = request.POST['name'] # HTML에서 input tag의 name이 'name'인 USER가 입력한 값
    # user_input_text = request.POST['text'] # HTML에서 input tag의 name이 'name'인 USER가 입력한 값
    # new_row = GuessNumbers(name=user_input_name, text=user_input_text)
    # new_row.name = new_row.name.upper()
    # new_row.lottos = [np.randint(1,50) for i in range(6)]
    # new_row.save()
    
    
def detail(request, lottokey):
    
    lotto = GuessNumbers.objects.get(pk=lottokey)
    
    return render(request, 'lotto/detail.html', {'lotto':lotto})
