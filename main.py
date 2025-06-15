from fastapi import FastAPI
from langserve import add_routes
from pydantic import BaseModel

from translation_chain import translation_chain

app = FastAPI()



class TranslationRequest(BaseModel):
    input: str

class TranslationResponse(BaseModel):
    output: str

add_routes(app, translation_chain, path="/translate",
           input_type=TranslationRequest, output_type=TranslationResponse)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
