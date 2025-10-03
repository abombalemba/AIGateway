from fastapi import APIRouter, status

import os

router = APIRouter()


@router.get(
	path='/',
	summary='hello',
	description='the main page'
)
def index():
	return {
		'status_code': status.HTTP_200_OK,
		'detail': 'hello, world!'
	}


@router.get(
	'/models',
	summary='ai models',
	description='list of available ai models'
)
def models():
	return {
		'status_code': status.HTTP_200_OK,
		'detail': os.listdir(os.getcwd() + '/models')
	}

