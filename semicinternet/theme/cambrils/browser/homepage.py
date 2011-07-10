from zope.interface import implements
from Acquisition import aq_inner

from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView

from Products.ATContentTypes.interface.folder import IATFolder

from semicinternet.theme.cambrils.browser.interfaces import IHomepage

from zope.component import getUtility 
from plone.registry.interfaces import IRegistry 
from semicinternet.theme.cambrils.browser.interfaces import ICambrilsSettings

from plone.registry.fieldfactory import persistentFieldAdapter

DEFAULT_NUMBER_OF_ITEMS = 10

class Homepage(BrowserView):
    
    implements(IHomepage)

    def __init__(self, context, request):
        super(Homepage, self).__init__(context, request)
        self.portal = getToolByName(self.context, "portal_url").getPortalObject()

    def getSlideshowImages(self,
                           num_items=DEFAULT_NUMBER_OF_ITEMS):
        urltool = getToolByName(self, 'portal_url')
        catalog = getToolByName(self, 'portal_catalog')
        section_path = urltool.getPortalPath() + '/' + self.getSlideshowFolder()

        query_result = catalog({'Type':{'query':['Image','ATImage']},
                                'path':{'query':section_path,'level':0},
                              })[:num_items]

        if query_result:
            return [brain.getObject() for brain in query_result]
        else:
            return False

    def getSlideshowImageItems(self):
        urltool = getToolByName(self, 'portal_url')
        catalog = getToolByName(self, 'portal_catalog')
        section_path = urltool.getPortalPath() + '/' + self.getSlideshowFolder()
        query_result = catalog({'Type':{'query':['Image','ATImage']},
                                'path':{'query':section_path,'level':0},
                              })
        if query_result:
            return len(query_result)
        else:
            return False

    def getSlideshowFolder(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        return settings.slideshow_folder

    def getCompanyName(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        return settings.company_name

    def getCompanyAboutLine1(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        return settings.company_about_line1

    def getCompanyAboutLine2(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        return settings.company_about_line2

    def getCompanyAboutLine3(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        return settings.company_about_line3

    def getCompanyAboutLine4(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        return settings.company_about_line4

    def getAuthorName(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        return settings.author_name

    def getAuthorUrl(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        return settings.author_url

    def showSocialIcons(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        if (settings.facebook_fanpage or
            settings.flickr_page or
            settings.twitter_stream or
            settings.youtube_channel):
            return True
        else:
            return False

    def getFacebookFanpage(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        return settings.facebook_fanpage

    def getFlickrPage(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        return settings.flickr_page

    def getTwitterStream(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        return settings.twitter_stream

    def getYoutubeChannel(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICambrilsSettings)
        return settings.youtube_channel
