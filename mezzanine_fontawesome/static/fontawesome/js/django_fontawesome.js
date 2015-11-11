if (!$) {
    var $ = jQuery = django.jQuery;
}

$(document).ready(function() {
    function formatState(state) {
        if (!state.id) { return state.text; }
        var icon_name = $(state.element).data("icon-name");
        return '<i class="fa fa-' + icon_name + '"></i> ' + state.text;
    }

    $('.fontawesome-select').select2({
        width: 'element',
        templateResult: formatState,
        templateSelection: formatState,
        escapeMarkup: function(m) {return m;}
    });
});
