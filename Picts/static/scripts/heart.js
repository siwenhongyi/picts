function add_like_num() {
    $('body').on("click", '.heart', function () {
        var father = $(this).attr("data-id");
        var like_num = parseInt(document.getElementById(father).innerText)
        $(this).css("background-position", "")
        var status = $(this).attr("rel");
        like_num += status == "like" ? 1 : -1;
        if (status === 'like') {
            $("#" + father).html(like_num);
            $(this).addClass("heartAnimation").attr("rel", "unlike");
        } else {
            $("#" + father).html(like_num);
            $(this).removeClass("heartAnimation").attr("rel", "like");
            $(this).css("background-position", "left");
        }
    });
}

function checkoutclass(a,user_id) {
    $(a).toggleClass('cs');
    var pict_id = $(a).attr('data-id');
    $.ajax({
        "url":"/like_heart",
        "type":"POST",
        "data":{"user":user_id,"pict_id":pict_id,"status":$(a).hasClass("cs") ? "add" : "delete"},
    });
}