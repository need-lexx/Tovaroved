$(document).ready(()=>{
    $("#FormAuth").submit(function (event){
        event.preventDefault()
        let form = $(this)

        $.ajax({
            type: "POST",
            data: {
                params: 'auth',
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
    $('#FormContact').submit(function (event) {
        event.preventDefault();
        let form = $(this);
        $.ajax({
            type: "POST",
            data: {
                params: 'contact',
                csrfmiddlewaretoken: form.find("input[name='csrfmiddlewaretoken']").val(),
                name: form.find("input[name='name']").val(),
                email: form.find("input[name='email']").val(),
                phone: form.find("input[name='phone']").val(),
                comment: form.find("textarea[name='comment']").val(),

            },
            success: function(response){
                if (response.status == "success") {
                    alert("Форма успешно отправлена!")
                }
            },
            error: function (response) {},
        })
    })
})

