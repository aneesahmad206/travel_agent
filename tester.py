#MsCr_EafVvZEQWhFl9JAL5orVYLq3qOhx_KyPqHFerRP

from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

# Replace with your credentials
WATSONX_API_KEY = "MsCr_EafVvZEQWhFl9JAL5orVYLq3qOhx_KyPqHFerRP"
WATSONX_URL = "https://us-south.ml.cloud.ibm.com"
PROJECT_ID = "2e0aa627-23e6-4396-a484-7fd8f6e9ea20"  # get this from your Watsonx.ai space/project

# Set up client
creds = Credentials(url=WATSONX_URL, api_key=WATSONX_API_KEY)
client = APIClient(credentials=creds)

# Pick a supported model
model = ModelInference(
    model_id="ibm/granite-3-2-8b-instruct",  # <-- supported
    api_client=client,
    project_id=PROJECT_ID,
    params={"max_new_tokens": 50}
)

# Test prompt
prompt = "Hello, Watsonx! Can you give me a short greeting message?"

try:
    result = model.generate(prompt)
    print("Watsonx response:")
    print(result)
except Exception as e:
    print("Error:", e)
