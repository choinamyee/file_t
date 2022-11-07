# 카카오 서비스
# 카카오 택시 , 카카오 톡, 카카오 페이
# 카카오 로그인 (id, password, name)
# 택시 (내위치 , 목적지)
# 카카오톡 (친구 ) 
# 카카오 페이 (계좌_번호 , 돈)

from kakao.kakao_pay import kakao_pay
from kakao.kakao_talk import kakao_talk
from kakao.kakao_taxi import kakao_taxi
from kakao.kakao_user import kakao_user
from kakao.kakao_services import kakao_services
user = kakao_user("id","pw","kim")
services = kakao_services(user)
print(services)
a = kakao_taxi(user, "서울","부산")
services.append_service(a)
a = kakao_taxi(user, "서울","인천")
services.append_service(a)
print(services.service_list[0].목적지)
print(services.service_list[1].목적지)
# b = kakao_talk("id","pw", "kim", "친구")
# print(b.친구)
# c = kakao_pay("id","pw", "kim", "123-123-123",100000)
# print(c.계좌_번호)


