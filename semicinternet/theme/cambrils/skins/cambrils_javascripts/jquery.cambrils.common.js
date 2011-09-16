/**
 * Common Javascript functions for semicinternet.theme.cambrils
 */

$(document).ready(function() {
    $("a.portletGalleryImage").fancybox({'type':'image'});

    // This is only for futbolsalou site, do not merge!
    $("#content-core > .photoAlbumEntry > a").fancybox({'type':'image'});

    $('.menu-shortcuts ul.first li a').click(function(event) {
        if ( $(this).next().css("display") == "block" )
        {
            $(this).next().slideUp('fast', function() {});   
        } else
        {
            $(this).next().slideDown('fast', function() {});
        }
        return false;
        event.preventDefault();
        event.stopPropagation();
    });

}); 
