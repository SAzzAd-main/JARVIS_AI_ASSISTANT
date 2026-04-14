import google.generativeai as genai
apiKey = "GOOGLE_API_KEY"
genai.configure(api_key=apiKey)

for m in genai.list_models():
    print(m.name)
    

