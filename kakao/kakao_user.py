class kakao_user:
    id = ""
    password =""
    name =""
    def __init__(self,_id,_password,_name) -> None:
        self.id=_id
        self.password=_password
        self.name=_name
        pass
    
    def set_name(self,_name):
        self.name = _name
        
    def set_id(self,_id):
        self.id = _id

    def set_password(self,_password):
        self.password = _password
