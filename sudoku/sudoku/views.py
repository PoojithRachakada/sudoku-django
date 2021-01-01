from django.http import request
from django.shortcuts import render
import json
from . import gensudoku

storing_ans = []


def get_list(request):
    tasks = request.POST.get("array", True)
    n = len(tasks)
    timer = ""
    c = 0
    rem = ""
    for i in range(n - 1, -1, -1):
        if c == 2 and tasks[i] == "|":
            timer = tasks[i + 1 :]
            rem = tasks[:i]
            break
        if tasks[i] == "|":
            c += 1

    response_got = []

    timer = timer.split("|")
    sending = {}
    sending["h"] = timer[0]
    sending["m"] = timer[1]
    sending["s"] = timer[2]

    poi = 0
    for i in range(9):
        b = []
        for j in range(9):
            b.append(rem[poi])
            poi += 1
        response_got.append(b)

    if gensudoku.valid(response_got):
        return render(request, "winner.html", sending)

    else:
        arr = []
        for i in range(9):
            for j in range(9):
                arr.append(storing_ans[i][j])
        json_list = json.dumps(arr)
        return render(request, "loser.html", {"list": json_list})


def show_solution(request):
    arr = []
    for i in range(9):
        for j in range(9):
            arr.append(storing_ans[i][j])
    json_list = json.dumps(arr)
    return render(request, "loser.html", {"list": json_list})


def handler404(request):
    response = render(
        request,
        "404.html",
    )
    return response


def home(request):
    return render(request, "index.html")


def easy(request):

    qs, ans = gensudoku.all()

    for ele in ans:
         print(ele)

    global storing_ans
    storing_ans = ans[:]
    arr = []
    for i in range(9):
        for j in range(9):
            arr.append(qs[i][j])

    json_list = json.dumps(arr)
    return render(request, "sudoku.html", {"list": json_list})


def medium(request):
    qs, ans = gensudoku.all()
    global storing_ans
    storing_ans = ans[:]
    arr = []
    for i in range(9):
        for j in range(9):
            arr.append(qs[i][j])

    json_list = json.dumps(arr)
    return render(request, "msudoku.html", {"list": json_list})


def hard(request):
    qs, ans = gensudoku.all()
    global storing_ans
    storing_ans = ans[:]
    arr = []
    for i in range(9):
        for j in range(9):
            arr.append(qs[i][j])

    json_list = json.dumps(arr)
    return render(request, "hsudoku.html", {"list": json_list})
