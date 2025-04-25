from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AddressCompareSerializer
from compare_app.gemini import generate

# Create your views here.
class CompareView(APIView):
    def get(self, request):
        return Response({"message":"Use POST to compare addresses"})
    
    def post(self, request):
        serializer = AddressCompareSerializer(data = request.data)

        if serializer.is_valid():
            address1 = serializer.validated_data['address1']
            address2 = serializer.validated_data['address2']

            try:
                comparison_result = generate(address1, address2)
                print("Gemini Response:\n", comparison_result)

                return Response({"Comparison":comparison_result})
            except Exception as e:
                print("Error while calling Gemini:", e)
                return Response({"error":str(e)}, status=500)
        return Response(serializer.errors, status=400)

