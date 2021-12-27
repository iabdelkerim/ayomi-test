

/*
$(document).on('submit','#post-form',function(e){
    e.preventDefault();

    $.ajax({
        type:'POST',
        url:'homepage/',
        data:{
            last_name:$('#last_name').val(),
            first_name:$('#first_name').val(),
            email:$('#email').val(),
            csrfmiddlewaretoken:$('input[csrfmiddlewaretoken]').val(),
        },
        success: function(){
            $('#last_name').val('');
            $('#first_name').val('');
        }
    })
})

<script>
	function changeEmail(){
			email = $("#email").val();
			$('#email').replaceWith(email);
			$.ajax({
					type: "POST",
					url: "/homepage/",
					data:{
							csrfmiddlewaretoken: '{{ csrf_token }}',
							email: email
					},
			});
	}
</script>*/