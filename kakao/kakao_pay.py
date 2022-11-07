from kakao.kakao_user import kakao_user
class kakao_pay(kakao_user):
    계좌_번호 = ""
    돈 = 0
    def __init__(self,_id,_password,_name, _계좌_번호, _돈) -> None:
        super().set_id(_id)
        super().set_password(_password)
        super().set_name(_name)
        self.계좌_번호 = _계좌_번호
        self.돈 = _돈
        pass