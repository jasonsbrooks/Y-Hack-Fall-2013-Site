$(document).ready(function(){


    document.querySelector('#fileSelect').addEventListener('click', function(e) {
        document.querySelector('#fileElem').click();
    }, false);

    $('#fileElem').change(function() {
        $('#myForm').submit();
    });
    $("#myForm").ajaxForm({url: '/photo_upload/', type: 'post',
        beforeSubmit: function(){
            $('#original').attr('src', 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==');
            $('#new').attr('src', 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==');
        },
        success: function(data){
            $('#original').attr("src", data);
            dataObj = {newLink: data};
            $.ajax({
                type: 'GET',
                url: '/process_photo',
                data: dataObj,
                success: function(data){
                    $( "#new" ).attr("src", data );
                }
            });
    }});
});