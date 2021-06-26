# We will need to make use of the HttpResponse in order to be able to formulate a response to a request
from django.http import HttpResponse
# View will be needed in order to construct our class based view
from django.views import View
# Now from the chatbot_logic we will make use of the talk function in order to communicate with the chatbot
from qa_chat.chatbot_logic import talk
# We will make the this particulat view csrf exempt as this is a learning exercise
from django.views.decorators.csrf import csrf_exempt
# In order to achive this we will need a method decorator
from django.utils.decorators import method_decorator

# This is our class based view that only works with post requests where the post request can be received and then data extracted from it
# The data that we extract will be passed to the talk function which will return us an answer from chatbot and that will be our response.
@method_decorator(csrf_exempt, name='dispatch')
class QuestionView(View):
    def post(self, request, *args, **kwargs):
        response = talk(request.POST['question'])

        return HttpResponse(response, 200)
