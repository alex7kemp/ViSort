$('#file-upload').change(function () {
    var file = $('#file-upload')[0].files[0].name;
    $('#browse').val(file);
});

function myFunction(unique_id) {
    var popup = document.getElementById(unique_id);
    popup.classList.toggle("show");
}

function checkboxes(benchmark) {
    var count = $(".checkbox:checked").length;
    if (count >= 2) {
        $('#benchmark_check').prop('checked', true);
    } else if (count < 2 && benchmark == false) {
        $('#benchmark_check').prop('checked', false);
    }
}