import hug


@hug.get('/')
def hello(request):
    print(request)
    return {"Hello World": 1}
