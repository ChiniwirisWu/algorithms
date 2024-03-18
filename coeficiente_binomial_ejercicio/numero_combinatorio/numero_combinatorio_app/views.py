from inspect import getinnerframes
from itertools import combinations
from math import comb
from django.shortcuts import render
import random

# Create your views here.

def index(request, amount_letters=4):
    if(request.POST.get('amount') != None):
        amount_letters = int(request.POST.get('amount'))
        bc = binomial_coef(amount_letters, 2)
        combinations, answer = create_combinations(amount_letters, bc)
        return render(request, 'index.html', context={'combinations':combinations, 'amount_letters':amount_letters, 'bc':bc, 'correct_answer':answer})
    bc = binomial_coef(amount_letters, 2)
    combinations, answer = create_combinations(amount_letters, bc)
    return render(request, 'index.html', context={'combinations':combinations, 'amount_letters':amount_letters, 'bc':bc, 'correct_answer':answer})

def result(request):
    correct_ans = request.POST.get('correct_ans', 'default_value')
    ans_attempt = request.POST.get('answer_attempt', 'default_value')
    if(int(correct_ans) == int(ans_attempt)):
        return render(request, 'result.html', context={'state':'correct', 'message':'Felicidades, respuesta correcta!', 'image': get_image(True)}) 
    return render(request, 'result.html', context={'state':'incorrect', 'message': 'Respuesta incorrecta, intente denuevo :(', 'image': get_image(False)}) 
    

#functions
def get_image(answer:bool):
    images = {
        'feliz': ['alpaca','castor','chica'],
        'triste': ['duende','luis','mario']
    }
    if answer:
        return "feliz/" + images['feliz'][random.randint(0, len(images['feliz']) - 1)] + "_feliz.jpg"
    return "triste/" + images['triste'][random.randint(0, len(images['triste']) - 1)] + "_triste.jpg"
    

def binomial_coef(n:int, k:int):
    if(k == 0 or n == k):
        return 1
    return binomial_coef(n - 1, k - 1) + binomial_coef(n - 1, k)
 
def create_combinations(amount_letters:int, bc:int):
    letters:list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    r = random.randint(0, bc)
    letters = letters[r:r +amount_letters]
    combinations:list = []
    combinations_inverse:list = []

    for a1 in letters:
        for a2 in letters:
            if(a1 == a2): 
                continue
            if([a1, a2] in combinations or [a2, a1] in combinations_inverse): 
                continue
            combinations.append([a1,a2])
            combinations_inverse.append([a2,a1])

    r = random.randint(0, bc)
    return combinations[r: r + bc], random.randint(0, bc - 1)





    
