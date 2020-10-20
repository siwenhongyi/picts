$(function () {
    $('.col-md-8 input.imgfile').on('change', function () {
        var choose_file = $(this)[0].files[0];
        var reader = new FileReader();
        reader.readAsDataURL(choose_file);
        reader.onload = function () {
            $('.col-md-8 p img.face').attr('src', reader.result);
        };
    });
})