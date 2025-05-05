from django.shortcuts import render

# Create your views here.
def calculadora_view(request):
  
  context = {}
   
  if request.POST:
    try:
      expressao = request.POST['expressao']
      resultado = eval(expressao)
      context['calculo'] = f'{expressao} = {resultado}'

    except: 
      context['calculo'] = "expressao inválida" 
  
  return render(request, "calculadora/calculadora.html", context)



# Create your views here.
def calculadora_view(request):
  
  context = {}
   
  if request.POST:
    try:
      expressao = request.POST['expressao']
      resultado = eval(expressao)
      context['calculo'] = f'{expressao} = {resultado}'

    except: 
      context['calculo'] = "expressao inválida" 
  
  return render(request, "calculadora/calculadora.html", context)