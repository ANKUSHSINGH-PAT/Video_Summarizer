from fastapi import FastAPI
from langserve import add_routes
from translation_chain import translation_chain

app = FastAPI()

add_routes(app, translation_chain, path="/translate")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
