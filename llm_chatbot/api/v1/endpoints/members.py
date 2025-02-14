from fastapi import APIRouter, Request

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{member_no}")
def get_user(member_no: str):
    return f"{member_no} 회원번호를 조회하였습니다. 이름 : 홍길동"


@router.post("/")
def create_user(request: Request):
    return f"회원가입이 완료 되었습니다. : {request.json()}"


@router.put("/{member_no}")
def update_user(request: Request):
    return f"회원 수정 완료 : {request.json()}"


@router.delete("/{member_no}/")
def delete_user(member_no: int):
    return f"회원 탈퇴 완료 : {member_no}"
