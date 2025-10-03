from fastapi import APIRouter, Query, HTTPException, status

import datetime as dt

from app.api.models.requests import *
from app.api.models.responses import *

from app.services.gateways import *

router = APIRouter()


@router.post(
	path='/text',
	response_model=TextGenerationResponse,
	summary='text generation route',
	description='text generation route'
)
def generate_text(
	request: TextGenerationRequest,
	model: str = Query(..., description='ai model title')
):
	try:
		response = text_generation_service(request, model)
		return response

	except Exception as ex:
		return TextGenerationResponse(
			success=False,
			message=f'{ex}',
			timestamp=dt.datetime.now(),
			generated_text='',
			tokens_used=0,
			processing_time=0.0
		)

