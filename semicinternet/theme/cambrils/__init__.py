# -*- extra stuff goes here -*- 

from zope.i18nmessageid import MessageFactory

GLOBALS = globals()

cambrilsMessageFactory = MessageFactory('semicinternet.theme.cambrils')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
