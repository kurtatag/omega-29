
$(document).ready(function () {
    scroll_to_top();
    add_anchors();
    copy_to_clipboard();
    toc_tooltips();
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
    anchors.options.visible = 'always';
    anchors.options.icon = '§';

    if ($( window ).width() > 600) {
        anchors.options.placement = 'left';
    }

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
    $('[data-toggle="tooltip"]').tooltip({trigger: 'hover'});

    $('.btn-clipboard').click(function () {
        $(this).attr('data-original-title', "Copied!").tooltip('show');
    });

    $('.btn-clipboard').mouseleave(function () {
        $(this).attr('data-original-title', "Copy to clipboard").tooltip('hide');
    });
}


function toc_tooltips() {
    var elements = document.querySelectorAll('#toc a');
    console.log(elements);
    elements.forEach(function (el, index) {
        $el = $(el);
        if (el.clientWidth < el.scrollWidth && !$el.attr('title')) {
            console.log(el);
            $el.tooltip({
                boundary: 'window',
                title: $el.text(),
                placement: "right",
                trigger: 'hover',
                delay: { "show": 500, "hide": 1 }
            });
        }
    });

    $('#toc a').click(function () {
        $(this).tooltip('hide');
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
