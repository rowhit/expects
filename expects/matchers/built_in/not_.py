# -*- coding: utf-8 -*

from .. import Matcher


class not_(Matcher):
    def __init__(self, matcher):
        self._matcher = matcher

    def _match(self, subject):
        result, _ = self._matcher._match(subject)
        return not result, []

    def _description(self, subject):
        return 'not ' + self._matcher._description(subject)
