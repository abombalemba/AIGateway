from fastapi import APIRouter, HTTPException, status

import datetime as dt
import typing as tp
import uuid

from app.api.models.requests import *
from app.api.models.responses import *

from app.services.gateways import *

router = APIRouter()


@router.post(
	path='/text',
	response_model=TextGenerationResponse,
	summary='text gen route',
	description='text generation route'
)
def generate_text(request: TextGenerationRequest):
	try:
		result = text_generation_service(request)

		return TextGenerationResponse(
			success=True,
			message='ok',
			timestamp=dt.now(),
			generated_text=result['generated_text'],
			tokens_used=result['tokens_used'],
			processing_time=result['processing_time']
		)

	except Exception as ex:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail=f'error of gen text'
		)
