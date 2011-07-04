#! /bin/sh
# based in: http://maurits.vanrees.org/weblog/archive/2010/10/i18n-plone-4

I18NDOMAIN="semicinternet.plonetheme01"

# Synchronise the templates and scripts with the .pot.
# All on one line normally:
i18ndude rebuild-pot --pot locales/${I18NDOMAIN}.pot \
    --merge locales/manual.pot \
    --create ${I18NDOMAIN} \
   .

# Synchronise the resulting .pot with all .po files
for po in locales/*/LC_MESSAGES/${I18NDOMAIN}.po; do
    i18ndude sync --pot locales/${I18NDOMAIN}.pot $po
done
