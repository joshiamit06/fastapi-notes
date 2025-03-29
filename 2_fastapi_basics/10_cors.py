'''
CORS (Cross-Origin Resource Sharing) is a security mechanism that controls how resources
on a web server can be requested from another domain.

By default, browsers block cross-origin requests for security reasons. 
CORS allows us to specify which origins, methods, and headers are permitted.

Imagine you have a FastAPI backend running at http://api.example.com and 
a frontend React app running at http://frontend.example.com. 
If your frontend tries to fetch data from the backend, 
the browser blocks the request because the frontend and backend are on different origins.

'''

# enable/use CORS

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins, methods, and headers (Not recommended for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    # allow_origins["https://frontend.example.com"] - # Allow only this frontend
    allow_credentials=True, # If your frontend sends authentication credentials (e.g., JWT, session cookies), set allow_credentials=True.
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
    # allow_headers=["Content-Type", "Authorization"],  # Allow only specific header

)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
