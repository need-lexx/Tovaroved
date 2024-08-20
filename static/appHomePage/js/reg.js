$(document).ready(()=>{
    $("#FormReg").submit(function (event){
        event.preventDefault()
        let form = $(this)

        let psw1 = form.find('input[name="password1"]').val()
        let psw2 = form.find('input[name="password2"]').val()

        if (psw1 != psw2) {
            alert("Пароли отличаются")
            return false;
        }

        $.ajax({
            type: "POST",
            data: {
                csrfmiddlewaretoken: form.find("input[name='csrfmiddlewaretoken']").val(),
                username: form.find("input[name='NewLogin']").val(),
                password: psw1,
            },
            success: function(response){
                if (response.status == 'success') {
                    window.location.href = '/auth'
                }
            },
        })
        
    })
})

