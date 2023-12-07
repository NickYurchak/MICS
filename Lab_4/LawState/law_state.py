class LawState(object):
    """ Базовий клас, що відображає стани законодавчого процесу """
    name = "state"
    allowed = []

    def switch(self, state):
        """ Перехід у новий стан """
        if state.name in self.allowed:
            print('Поточний стан:', self, ' => перехід до нового стану', state.name)
            self.__class__ = state
        else:
            print('Поточний стан:', self, ' => перехід до', state.name, 'неможливий.')

    def __str__(self):
        return self.name
