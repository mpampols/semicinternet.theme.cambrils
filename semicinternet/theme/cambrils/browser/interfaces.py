from z3c.form import interfaces
from z3c.form.browser import checkbox

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

from semicinternet.theme.cambrils import cambrilsMessageFactory as _

from plone.app.vocabularies.catalog import SearchableTextSourceBinder

from plone.portlets.interfaces import IPortletDataProvider
from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
	"""Marker interface that defines a Zope 3 browser layer.
	   If you need to register a viewlet only for the
	   "SEMIC Internet Cambrils Theme" theme, this interface must be its layer
	   (in theme/cambrils/viewlets/configure.zcml).
	"""

class IGalleryPortlet(IPortletDataProvider):
	image_count = schema.Int(title=_(u'Number of images to display'),
									 description=_(u'How many images to list.'),
							 required=True,
							 default=5)

	image_root_folder = schema.Choice(title=_(u"label_navigation_root_path", default=u"Root node for image gallery"),
									  description=_(u'help_navigation_root',
										default=u"You may search for and choose a folder "
												  "to act as the root of the image gallery."
												  "Leave blank to use the Plone site root."),
									  required=False,
									  source=SearchableTextSourceBinder({'is_folderish' : True},
										default_query='path:'))

	path_depth = schema.Int(title=_(u'Path depth'),
									description=_(u'How many depth to search inside the root folder.'),
							required=True,
							default=1)

class IHomepage(Interface):
	"""Browser view for homepage logic"""

	def getDropDownMenuLevels():
		"""Returns the number of levels to show in the dropbox menu
		"""

	def getDropdownMenu():
		"""Returns the number of images inside the slideshow folder
		"""

	def getSlideshowImages():
		"""Returns the number of images inside the slideshow folder
		"""

	def getSlideshowFolder():
		"""Returns the id of the folder containing the slide images.
		"""
	
	def getCompanyName():
		"""Returns a string containing the company name, this is part of the copyright shown at the bottom right part.
		"""
	
	def getCompanyAboutLine1():
		"""Returns a string containing an optional line to be shown at the bottom right part (address, etc...)
		"""
	
	def getCompanyAboutLine2():
		"""Returns a string containing an optional line to be shown at the bottom right part (address, etc...)
		"""
	
	def getCompanyAboutLine3():
		"""Returns a string containing an optional line to be shown at the bottom right part (address, etc...)
		"""

	def getCompanyAboutLine4():
		"""Returns a string containing an optional line to be shown at the bottom right part (address, etc...)
		"""
	
	def getAuthorName():
		"""Returns a string containing the website author name to be shown at the bottom left part.
		"""
	
	def getAuthorUrl():
		"""Returns a string containing the url address of the author's website.
		"""
	
	def showSocialIcons():
		"""Returns True if any social URL is set
		"""

	def getFacebookFanpage():
		"""Returns a string containing the url of the facebook fan page
		"""

	def getFlickrPage():
		"""Returns a string containing the url of the flickr page
		"""

	def getTwitterStream():
		"""Returns a string containing the url of the twitter stream page
		"""

	def getYoutubeChannel():
		"""Returns a string containing the url of the youtube channel page
		"""

class ICambrilsSettings(Interface):
	"""Global cambrils settings. This describes records stored in the configuration 
	   registry and otainable via plone.registry."""

	dropdown_menu_level = schema.Choice(title = _(u'Number of levels in dropdown menu'),
									 	description = _(u'help_dropdown_menu_levels',
									 		default = u"Select the number of levels, 0 to disable the dropdown effect"),
									 	required = True,
									 	values = ['0','1','2']
									 	)

	slideshow_folder = schema.TextLine(title=_(u"Slideshow folder"),
									   description=_(u"help_slideshow_folder",
									   		default=u"Name of the folder containing the slideshow images."),
									   required=True,
									   default=u'slideshow',)

	company_name = schema.TextLine(title=_(u"Company name"),
									   description=_(u"help_company_name",
									   default=u"Name of the website owner."),
								   required=False,
								   default=u'Company name',)

	company_about_line1 = schema.TextLine(title=_(u"Company about line 1"),
											  description=_(u"help_company_about_line1",
											  default=u"Address or other information (line 1)."),
										  required=False,
										  default=u'Company about line 1',)

	company_about_line2 = schema.TextLine(title=_(u"Company about line 2"),
											  description=_(u"help_company_about_line2",
											  default=u"Address or other information (line 2)."),
										  required=False,
										  default=u'Company about line 2',)

	company_about_line3 = schema.TextLine(title=_(u"Company about line 3"),
											  description=_(u"help_company_about_line3",
											  default=u"Address or other information (line 3)."),
										  required=False,
										  default=u'Company about line 3',)

	company_about_line4 = schema.TextLine(title=_(u"Company about line 4"),
											  description=_(u"help_company_about_line4",
											  default=u"Address or other information (line 4)."),
										  required=False,
										  default=u'Company about line 4',)

	author_name = schema.TextLine(title=_(u"Website author name"),
									 description=_(u"help_author_name",
									 default=u"Name of your company, or website creator."),
								 required=False,
								 default=u'SEMIC Internet',)

	author_url = schema.TextLine(title=_(u"Website author URL"),
									description=_(u"help_author_url",
									default=u"Website URL of your company or website creator."),
								required=False,
								default=u'http://www.semicinternet.com',)

	facebook_fanpage = schema.TextLine(title=_(u"Facebook Fanpage URL"),
											   description=_(u"help_facebook_fanpage",
											   default=u"The url of your facebook fan page"),
									   required=False,
									   default=u'',)

	flickr_page = schema.TextLine(title=_(u"Flickr Account URL"),
										  description=_(u"help_flickr_page",
										  default=u"The url of your flickr account page"),
								  required=False,
								  default=u'',)

	twitter_stream = schema.TextLine(title=_(u"Twitter Stream URL"),
											 description=_(u"help_twitter_stream",
											 default=u"The url of your twitter stream page."),
									 required=False,
									 default=u'',)

	youtube_channel = schema.TextLine(title=_(u"YouTube Channel URL"),
											  description=_(u"help_youtube_channel",
											  default=u"The url of your youtube channel page"),
									  required=False,
									  default=u'',)
