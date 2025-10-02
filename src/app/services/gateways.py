import requests

import time
import typing as tp

from app.api.models.requests import *

headers = {
	'Authorization': f'Bearer {}',
	'Content-Type': 'application/json'
}


def generate_text_service(request: TextGenerationRequest) -> tp.Dict[str, tp.Any]:
	start_time = time.time()

	data = {
		'model': request.model,
		'messages': [{'role': 'user', 'content': request.prompt}],
		'stream': False
	}

	response = requests.post(request.url, headers=headers, json=data)
	result = {}

	result['generated_text'] = response #
	result['tokens_used'] = len(response)
	result['processing_time'] = time.time() - start_time

	return result

