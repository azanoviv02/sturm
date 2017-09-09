$(document).ready(function () {

    //== Helper function defenitions ===

    function switchToStatus(switchValue) {
        switch (switchValue) {
            case true:
                return "yes"
            case false:
            default:
                return "no"
        }
    }

    function statusToSwitch(statusValue) {
        switch (statusValue) {
            case "yes":
                return true
            case "no":
            default:
                return false
        }
    }

    function oppositeSwitch(switchValue) {
        if (switchValue == "on") {
            return "off"
        } else {
            return "on"
        }
    }

    //==================================

    $('select').material_select();

    (function () {
        $('.book-status-switch').each(function (index) {
            var bookStatus = $(this).find(".book-status-source").text()
            var input = $(this).find("input")
            input.prop('checked', statusToSwitch(bookStatus))
        })
    })();

    $('.book-status-switch label input').on('click', function (event) {
        var input = $(this)
        sendBookStatus(input.parent().parent());
    });

    function sendBookStatus(statusSwitch) {

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                function getCookie(name) {
                    var cookieValue = null;
                    if (document.cookie && document.cookie != '') {
                        var cookies = document.cookie.split(';');
                        for (var i = 0; i < cookies.length; i++) {
                            var cookie = jQuery.trim(cookies[i]);
                            // Does this cookie string begin with the name we want?
                            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }

                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    // Only send the token to relative URLs i.e. locally.
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            }
        });

        console.log("sending values:")
        console.log("book id:")
        console.log(statusSwitch.find(".book-id-source").text())
        console.log("status:")
        console.log(statusSwitch.find("input").val())

        $.ajax({
            url: "rest/status/update/", // the endpoint
            type: "POST", // http method
            data: {
                book_id: statusSwitch.find(".book-id-source").text(),
                new_status: switchToStatus(statusSwitch.find("input").prop('checked')), // data sent with the post request
            },

            // handle a successful response
            success: function (json) {
                // $('form.status-post-form').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
            },

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                // $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                //     " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };

    // function create_post() {
    //     console.log("create post is working!") // sanity check
    //     var $inputs = $('#status-post-form :input');
    //     var values = {};
    //     $inputs.each(function () {
    //         values[this.name] = $(this).val();
    //     })
    //     console.log(values)
    // };

    // $('#selector-form').on('submit', function (event) {
    //     event.preventDefault();
    //     console.log("seach form submitted!")  // sanity check
    //     create_post_search();
    // });
    //
    // function create_post_search() {
    //     console.log("create search post is working!") // sanity check
    //     // console.log($('#selector-form').val())
    //     var $inputs = $('#selector-form :input');
    //     var values = {};
    //     $inputs.each(function () {
    //         values[this.name] = $(this).val();
    //     })
    //     console.log(values)
    // }
});

$(document).ready(function () {
    $('.collapsible').collapsible();
});

// $(document).ready(function () {
//     $('.block-video').addClass('video-container')
//     $('.block-image').find('img').addClass('responsive-img')
// });