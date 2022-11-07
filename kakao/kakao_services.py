# kakao_services.py
from kakao.kakao_user import kakao_user

class kakao_services():
    kakao_user_info = None
    service_list = []

    def __init__(self,_kakao_user) -> None:
        self.kakao_user_info = _kakao_user
        pass

    def append_service(self,any_service):
        self.service_list.append(any_service)

    def __str__(self) -> str:
        answer = f"""id : {self.kakao_user_info.id} 
        ,password : {self.kakao_user_info.password}
        ,service_list : {self.service_list}"""
        return answer