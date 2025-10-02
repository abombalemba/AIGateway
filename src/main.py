from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api.routes import index, ai

app = FastAPI(
	title='AIGateway',
	description='microservice for ai'
)


app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=True,
	allow_methods=['GET', 'POST'],
	allow_headers=['*']
)

app.include_router(index.router, prefix='')
app.include_router(ai.router, prefix='/api/v1')

if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=5010)

