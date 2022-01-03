from django.shortcuts import render

class RequestCheck:
    def __init__(self, view):
        self.view=view

    def __call__(self, request, *args, **kwargs):
        resp = self.view(request, *args, **kwargs)
        if resp.status_code == 500:
            return render(request, "500.html")
        return resp

class LogRequest:
    def __init__(self, view):
        self.view=view

    def __call__(self, request, *args, **kwargs):
        # write a model(request, resp columns)
        #
        resp = self.view(request, *args, **kwargs)
        #LogRequestModel(request=str(request.__dict__),
        #resp=str(resp.__dict__))
        #LogRequestModel.save()
        return resp
