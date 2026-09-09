from fastapi import FastAPI

# Create the API application
app = FastAPI(
    title="ProcureFlow AI",
    description="Procurement and operations automation API",
    version="0.1.0",
)


# Basic endpoint to confirm the API is running
@app.get("/")
def root():
    return {"message": "ProcureFlow AI API is running"}