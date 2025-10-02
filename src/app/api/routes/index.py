from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.get(
	path='/',
	summary='hello',
	description='the main page'
)
def index():
	return {
		'status_code': status.HTTP_200_OK,
		'detaul': 'hello, world!'
	}
