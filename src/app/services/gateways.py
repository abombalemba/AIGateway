import requests
import dotenv

import typing as tp
import time
import os

from app.api.models.requests import *
from app.api.models.responses import *


def text_generation_service(
	request: TextGenerationRequest,
	model: str
) -> TextGenerationResponse:
	text_generation_response = TextGenerationResponse(
		success=False,
		message='...',
		timestamp=time.time(),
		generated_text='',
		tokens_used=0,
		processing_time=0.0
	)

	model_name, model_url, token = get_model_configuration(model)

	if not all([model_name, model_url, token]):
		text_generation_response.success = False
		text_generation_response.message = 'missing ai model configuration'
		return text_generation_response

	headers = {
		'Authorization': f'Bearer {token}',
		'Content-Type': 'application/json'
	}

	start_time = time.time()

	data = {
		'model': model_name,
		'messages': [{'role': 'user', 'content': request.prompt}],
		'stream': False
	}

	response = requests.post(model_url, headers=headers, json=data, timeout=10)
	if response.status_code != 200:
		text_generation_response.succes = False
		text_generation_response.message = f'{response.status_code} {response.text}'
		return text_generation_response

	content = response.json()['choices'][0]['message']['content']

	tokens_used = len(request.prompt.split()) + len(content.split())

	text_generation_response.success = True
	text_generation_response.message = 'ok'
	text_generation_response.generated_text = content
	text_generation_response.tokens_used = tokens_used
	text_generation_response.processing_time = time.time() - start_time

	return text_generation_response



def get_model_configuration(model: str) -> tp.Tuple[str]:
	config = dotenv.dotenv_values(dotenv_path=f'./models/{model}.env')

	model_name: str = config.get('MODEL_NAME')
	model_url: str = config.get('MODEL_URL')
	token: str = config.get('TOKEN')

	return model_name, model_url, token

