from mycroft import MycroftSkill, intent_file_handler


class SubsonicPlayer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('player.subsonic.intent')
    def handle_player_subsonic(self, message):
        self.speak_dialog('player.subsonic')


def create_skill():
    return SubsonicPlayer()

