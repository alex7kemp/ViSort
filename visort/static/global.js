$('#file-upload').change(function () {
    var file = $('#file-upload')[0].files[0].name;
    $('#browse').val(file);
});