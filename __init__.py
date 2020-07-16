from mycroft import MycroftSkill, intent_file_handler


class Xinchao(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('xinchao.intent')
    def handle_xinchao(self, message):
        self.speak_dialog('xinchao')


def create_skill():
    return Xinchao()

