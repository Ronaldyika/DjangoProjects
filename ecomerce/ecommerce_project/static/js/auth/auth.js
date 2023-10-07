const usernameField = document.querySelector('#usernameField');

usernameField.addEventListener('keyup',function(e){
    const usernameVal = e.target.value;
    if(usernameVal.length > 0){
        fetch('/validate_username/',{
            body:JSON.stringify({username:usernameVal}),
            method:'POST',
        }).then((res)=>res.json()).then((data)=>{
            if(data.username_error){
                usernameField.classList.add('is-invalid');
            }
        });
    }
});