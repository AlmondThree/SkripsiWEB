function validateData(inputText) {
    var formatEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    // var formatPhone = 
    if (inputText.value.match(formatEmail)) {
        return true
    } else{
        alert("You have entered an invalid email address!");
        document.formData.email.focus();
        return false;
    }
}