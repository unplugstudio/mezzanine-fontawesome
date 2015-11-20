if (!$) {
    var $ = jQuery = django.jQuery;
}

$(document).ready(function() {
    function formatState(state) {
        if (!state.id) { return state.text; }
        state_id = state.id.split(",")[0];
        return "<i class='fa fa-" + state_id + "'></i> " + state.text;
    }

    $(".select2-widget").select2({
        width: "element"
    });

    $(".fontawesome-select").select2({
        width: "element",
        templateResult: formatState,
        templateSelection: formatState,
        escapeMarkup: function(m) {return m;},
        ajax: {
            url: "/static/fontawesome/js/icons.json",
            dataType: "json",
            delay: 250,
            data: function (params) {
                return {
                    q: params.term, // search term
                    page: params.page
                };
            },
            processResults: function (data, params) {
                // parse the results into the format expected by Select2
                // since we are using custom formatting functions we do not need to
                // alter the remote JSON data, except to indicate that infinite
                // scrolling can be used
                params.page = params.page || 0;
                params.term = $.trim(params.term);
                var icons = data.icons;
                var ICONS_PER_PAGE = 30;

                // Always return the object if there is nothing to compare
                if (params.term !== "") {
                    var data_icons = icons;
                    icons = [];
                    for (var i=0; i < data_icons.length; i++) {
                        var synonyms = data_icons[i].id.toUpperCase();
                        var filters = data_icons[i].filter;
                        if (filters) {
                            synonyms = synonyms + " " + filters.join(" ").toUpperCase()
                        }
                        if (synonyms.indexOf(params.term.toUpperCase()) > -1) {
                            icons.push(data_icons[i]);
                        }
                    }
                }

                result = [];
                for (i in icons) {
                    icons[i].id = icons[i].id + ", " + icons[i].text;
                }

                var icons_original = icons.slice(0);
                while(icons.length) {
                    result.push(icons.splice(0, ICONS_PER_PAGE));
                }
                icons = icons_original;

                return {
                    results: result[params.page],
                    pagination: {
                        more: (params.page * ICONS_PER_PAGE) < icons.length
                    }
                };
            },
            cache: false
        }
    });
});
