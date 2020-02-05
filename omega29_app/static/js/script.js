
$(document).ready(function () {
    scroll_to_top();
    add_anchors();
    copy_to_clipboard();
    toc_height();
    search_focus();
});


function scroll_to_top() {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });
}


function add_anchors() {
    // anchors.options.visible = 'always';
    // anchors.options.icon = '§';
    // anchors.options.placement = 'left';

    anchors.add();
}


function copy_to_clipboard() {
    // clipboard
    var clipboard = new ClipboardJS('.btn-clipboard', {
        target: function (trigger) {
            return trigger.nextElementSibling;
        }
    });

    clipboard.on('success', function (e) {
        e.clearSelection();
    });


    // tooltips
    $('.btn-clipboard').click(function () {
        $(this).attr('data-original-title', "Copied!").tooltip('show');
    });

    $('.btn-clipboard').mouseleave(function () {
        $(this).attr('data-original-title', "").tooltip('hide');
    });
}


function toc_height() {

    function setTocHeight() {
        var el = document.getElementById('toc-scroll');
        if (el) {
            var h = window.innerHeight - el.getBoundingClientRect().top - 24;
            el.style.maxHeight = '' + h + 'px';
        }
    }

    if ($( window ).width() > 991) {
        setTocHeight();
        $(window).scroll(setTocHeight);
        $(window).resize(setTocHeight);
    }

}


function search_focus() {
    $( "#search input" ).focus(function() {
        $( "#search" ).css("border-color", "rgb(29, 161, 242)");
        $( "#search" ).css("background-color", "#ffffff");
        $( "#search svg" ).css("fill", "rgb(29, 161, 242)");
    });

    $( "#search input" ).focusout(function() {
        $( "#search" ).css("border-color", "rgb(230, 236, 240)");
        $( "#search" ).css("background-color", "rgb(230, 236, 240)");
        $( "#search svg" ).css("fill", "rgb(101, 119, 134)");
    });
}
