// Debug 
console.log("Made by Mbonu Chinedum")

// Getting all the dom element 
const fullname = document.getElementById("fullname"); 
const email = document.getElementById("email"); 
const password = document.getElementById("password"); 
const signUpBtn = document.getElementById("signInBtn"); 

// Adding event listener for the signInBtn 
signUpBtn.addEventListener("click", (event) => {
    // Preventing default submission 
    event.preventDefault(); 

    // Getting the fullname, email and password value 
    if (fullname.value === '') {
        // 
        fullname.style.border = "2px solid #ec009b"; 
        return; 
    }

    else if (email.value === '') {
        email.style.border = "2px solid #ec009b"; 
        return; 
    }

    else if (password.value === '') {
        password.style.border = "2px solid #ec009b"; 
        return; 
    }

    // Else 
    else {
        // Get the data 
        let data = JSON.stringify({
            "fullname": fullname.value, 
            "email": email.value, 
            "password": password.value, 
        })

        /** Setting the request headers, the http verb, 
            * and the URL for the backend connection.  
        */
        const headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST', 
            'Access-Control-Allow-Headers': 'Content-Type',
        }; 

        // Using fetch request 
        fetch('/signUp', {
            method: 'POST', 
            headers: headers, 
            body: data
        })
        .then(response => response.json())
        .then(data => {
            console.log(data); 
        })
    }
})

