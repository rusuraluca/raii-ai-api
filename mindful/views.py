import openai
from rest_framework.views import APIView
from rest_framework.response import Response

class MindfulView(APIView):
    def post(self, request):
        received = request.data
        user_input = received['input']

        # Call the function to send a request to the GPT API
        response_from_gpt = self.send_request(user_input)

        # Prepare the response data
        response_data = {'response': response_from_gpt}
        return Response(response_data)

    def send_request(self, text):
        openai.api_key = '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'

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo-0301",
                messages=[
                    {"role": "system", "content": "You are a therapist offering counseling."},
                    {"role": "user", "content": text}
                ]
            )
            return response

        except Exception as e:
            return str(e)
