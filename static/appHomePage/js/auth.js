$(document).ready(()=>{
    $("#FormAuth").submit(function (event){
        event.preventDefault()
        let form = $(this)

        $.ajax({
            type: "POST",
            data: {
                csrfmiddlewaretoken: form.find("input[name='csrfmiddlewaretoken']").val(),
                login: form.find("input[name='login']").val(),
                password: form.find("input[name='password']").val(),
            },
            success: function(response){
                if (response.status == 'success') {
                    window.location.href = '/'
                }
            },
        })
    })
})

