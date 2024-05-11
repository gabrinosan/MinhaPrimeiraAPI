from fastapi import FastAPI
from primeira_api.router import api_router

app = FastAPI(title='primeira_api')

app.include_router(api_router)

if __name__ == 'main':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)

# uvicorn primeira_api.main:app --reload
#   executar no terminal  #