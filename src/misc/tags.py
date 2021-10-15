EVENT_TAG_PROP_NAME = "_eventTag"

class EventTagger():
    def __init__(self):
        self.registredEvents = {}
    
    def __call__(self, name):
        if name not in self.registredEvents:
            self.registredEvents[name] = []

        def eventDecorator(function):
            if not callable(function): return

            self.registredEvents[name].append(function)
            setattr(function, EVENT_TAG_PROP_NAME, name)

            return function

        return eventDecorator