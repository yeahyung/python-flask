class first:
    def __init__(self, text):
        ## _ => private
        self._name = text

    @property
    ## @property 를 통해 외부에서도 접근 가능하게 해줌
    def name(self):
        return self._name

    @name.setter
    def name(self, text):
        self._name = text
