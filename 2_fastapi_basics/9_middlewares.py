'''
Allow to intercept and modify requests and responses before they reach the endpoint. 
They are useful for logging, authentication, CORS handling, response transformation, and more.

A middleware is a function that executes before and after every request in your FastAPI application.

🔹 How Middleware Works
A client sends a request.

The middleware processes the request (e.g., authentication, logging, modifying headers).

The request reaches the FastAPI route handler.

The response is processed by the middleware again (e.g., adding headers, modifying response format).

The response is sent back to the client.

'''

# Middleware for logging request details.
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(f"Incoming request: {request.method} {request.url}")
        response = await call_next(request)
        print(f"Response status: {response.status_code}")
        return response

app.add_middleware(LoggingMiddleware)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# dispatch() - entry point for processing every HTTP request before it reaches the actual endpoint.
# call_next() - Executes the route function i.e forwards the requests to actual routes.