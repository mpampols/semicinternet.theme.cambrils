Introduction
============

How to add images to the header slideshow
-----------------------------------------
For slideshow to work you must create a new folder with he id: "slideshow" in
the site root, and then upload some 960x238 images.

If you need to change the name of the slideshow container folder, you must edit:
semicinternet.theme.cambrils/semicinternet/theme/cambrils/browser/templates/global_sections.pt

changing the function value slideshow from:
hp_view.getSlideshowImageItems('slideshow')
and:
hp_view.getSlideshowImages('slideshow')


