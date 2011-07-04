from plone.app.registry.browser import controlpanel

from semicinternet.theme.cambrils.browser.interfaces import ICambrilsSettings, _

class CambrilsSettingsEditForm(controlpanel.RegistryEditForm):

    schema = ICambrilsSettings
    label = _(u"Cambrils settings")
    description = _(u"""""")

    def updateFields(self):
        super(CambrilsSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(CambrilsSettingsEditForm, self).updateWidgets()

class CambrilsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = CambrilsSettingsEditForm

