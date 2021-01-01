from django.http import request
from django.shortcuts import render
import json
from . import gensudoku


def handler404(request):
    response = render(
        request,
        "404.html",
    )
    return response


def home(request):
    return render(request, "index.html")

def get_list(request):
    tasks = request.POST.get("array", False)
    print(tasks)
    return render(request,"index.html")



def easy(request):

    qs, ans = gensudoku.all()

    arr = []
    for i in range(9):
        for j in range(9):
            arr.append(qs[i][j])

    json_list = json.dumps(arr)
    return render(request, "sudoku.html", {"list": json_list})


def medium(request):
    print("selected medium level")

    return render(request, "sudoku.html")
