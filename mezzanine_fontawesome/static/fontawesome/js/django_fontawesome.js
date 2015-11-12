if (!$) {
    var $ = jQuery = django.jQuery;
}

$(document).ready(function() {
    function formatState(state) {
        if (!state.id) { return state.text; }
        var icon_name = $(state.element).data("icon-name");
        return '<i class="fa fa-' + icon_name + '"></i> ' + state.text;
    }

    function matchStart(params, data) {
        // Always return the object if there is nothing to compare
        if ($.trim(params.term) === '') {
          return data;
        }

        var filters = data.text.toUpperCase();
        var synonyms = data.element.dataset.iconFilter;
        if (synonyms !== undefined) {
            filters = filters + " " + synonyms.toUpperCase();
        }
        if (filters.indexOf(params.term.toUpperCase()) > -1) {
            return data;
        }

        return null;
    }

    $('.fontawesome-select').select2({
        width: 'element',
        templateResult: formatState,
        templateSelection: formatState,
        matcher: matchStart,
        escapeMarkup: function(m) {return m;}
    });
});
