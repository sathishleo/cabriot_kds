class Displaysection:
    VEGETABLE = 'vegetable'
    MAIN = 'main'
    BREAD = 'bread'
    key_vegetable="VEGETABLE"
    key_main="MAIN"
    key_bread="BREAD"

    def get_displaysection(self,section):
        if Displaysection.VEGETABLE == section:
            return Displaysection.key_vegetable
        elif Displaysection.MAIN == section:
            return Displaysection.key_main
        elif Displaysection.BREAD == section:
            return Displaysection.key_bread
        else:
            return " "