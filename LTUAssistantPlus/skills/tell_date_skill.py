#!/usr/bin/python3

import calendardb

from nlp.universal_dependencies import ParsedUniversalDependencies
from user_interface.user_interaction_service_base import UserInteractionServiceBase
from .skill import SkillInput, Skill

class TellDateSkill(Skill):
    """Lets the assistant tell the user the current date."""

    def __init__(self):
        """Initializes a new instance of the TellDateSkill class."""
        self._cmd_list = ['what is', 'tell']

    def matches_command(self, skill_input: SkillInput) -> bool:
        """Returns a Boolean value indicating whether this skill can be used to handle the given command."""
        verb = (skill_input.verb or None) and skill_input.verb.lower()
        verb_object = (skill_input.verb_object or None) and skill_input.verb_object.lower()
        return verb in self._cmd_list and (verb_object == "date" or verb_object == "day")
    
    def execute_for_command(self, skill_input: SkillInput, user_interaction_service: UserInteractionServiceBase):
        """Executes this skill on the given command input."""
        user_interaction_service.speak(f"It is currently {calendardb.get_current_date()}.", True)