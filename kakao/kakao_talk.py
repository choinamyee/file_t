from kakao.kakao_user import kakao_user

class kakao_talk(kakao_user):
    친구 = ""
    def __init__(self,_id,_password,_name, _친구) -> None:
        super().set_id(_id)
        super().set_password(_password)
        super().set_name(_name)
        self.친구 = _친구
        pass