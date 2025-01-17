#!/usr/bin/python3

import calendardb

from nlp.universal_dependencies import ParsedUniversalDependencies
from user_interface.user_interaction_service_base import UserInteractionServiceBase
from .skill import SkillInput, Skill

class AddCalendarEventSkill(Skill):
    """Lets the assistant schedule a calendar event for the user."""

    def __init__(self):
        """Initializes a new instance of the AddCalendarEventSkill class."""
        self._cmd_list = ['schedule', 'remind', 'remind about', 'plan']

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (skill_input.verb or None) and skill_input.verb.lower()
        return verb in self._cmd_list
    
    def execute_for_command(self, skill_input: SkillInput, user_interaction_service: UserInteractionServiceBase):
        """Executes this skill on the given command input."""
        verb_object = skill_input.noun
        event_str = verb_object
        if event_str == 'event':
            event_sentence = user_interaction_service.ask_question('Okay, what is the event called?', skill_input.verbose)
            day_sentence = user_interaction_service.ask_question('What day will this be on?', skill_input.verbose)
            time_sentence = user_interaction_service.ask_question('What time will this start at?', skill_input.verbose)
            cal_event = calendardb.CalendarEvent(event_sentence, day_sentence, time_sentence, '')
            calendardb.add_event(cal_event)
            feedback_sentence = 'Alright, I\'m putting down ' + str(cal_event) + '.'
            user_interaction_service.speak(feedback_sentence, skill_input.verbose)
        else:
            user_interaction_service.speak('Sorry, I am unable to help you schedule this right now.', skill_input.verbose)