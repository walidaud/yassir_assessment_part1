# utils/config.py
BASE_URL = "https://gorest.co.in/public/v2"

''' Access token should not be hardcoded. Use following code instead:
import os
ACCESS_TOKEN = os.getenv("GOREST_TOKEN")

Go to CMD and set token with following line:
set GOREST_TOKEN=your_token_here
'''

ACCESS_TOKEN = "6aa7b70eff16c567746163e837641febc04bceb874345004da31743210c04be9"   #should not be hardcoded



HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}