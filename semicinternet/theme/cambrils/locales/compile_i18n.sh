#! /bin/sh
# based in: http://maurits.vanrees.org/weblog/archive/2010/10/i18n-plone-4
for po in $(find . -path '*/LC_MESSAGES/*.po'); do
    msgfmt -o ${po/%po/mo} $po;
done
echo "done."
