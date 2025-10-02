from fastapi import APIRouter, HTTPException, status

import datetime as dt
import typing as tp
import uuid

from app.api.models.requests import *
from app.api.models.responses import *


router = APIRouter()


@router.post(
	path='/text',
	response_model=TextGenerationResponse,
	summary='text gen route',
	description='text generation route'
)
def generate_text(request: TextGenerationRequest):
	try:
		pass

	except Exception as ex:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail=f'error of gen text'
		)
