import React, { useState } from  'react';
import './form.css';
function Moreforms() {
    const [firstname, setFirstname] = useState("");
    const [lastname, setLastname] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmpassword, setCnfpassword] = useState("");
    const [error, setError] = useState("");
    const [error2, setError2] = useState("");
    const [error3, setError3] = useState("");
    const [error4, setError4] = useState("");
    const [error5, setError5] = useState("");
    const createUser = (e) => {
        e.preventDefault();
        const newUser = { firstname,lastname,email,password,confirmpassword };
        console.log("Welcome", newUser);
            setFirstname("");
            setLastname("");
            setEmail("");
            setPassword("");
            setCnfpassword("")
    };
    const checkLength = (value) => {
        setFirstname(value);
        if (value.length < 3) {
            setError("First name invalide🙅‍♂️🙅‍♂️");
        } else {
            setError("");
        }
    };
    const checkLength2 = (value) => {
        setLastname(value);
        if (value.length < 3) {
            setError2("First name invalidee🙅‍♂️🙅‍♂️");
        } else {
            setError2("");
        }
    };
    const checkLength3 = (value) => {
        setEmail(value);
        if (value.length < 3) {
            setError3("Email invalidee🙅‍♂️🙅‍♂️");
        } else {
            setError3("");
        }
    };
    const checkLength4 = (value) => {
        setPassword(value);
        if (value.length < 3) {
            setError4("Password invalidee🙅‍♂️🙅‍♂️");
        } else {
            setError4("");
        }
    };
    const checkLength5 = (value) => {
        setCnfpassword(value);
        if (value.length < 3) {
            setError5("Confirm password invalidee🙅‍♂️🙅‍♂️");
        } else {
            setError5("");
        }
    };
    return(
            <form onSubmit={ createUser }>
            <div>
                <label>First Name: </label>
                <p>{error}</p> 
                <input type="text" value={firstname} onChange={ (e) => checkLength(e.target.value) } />
            </div>
            <div>
                <label>Last Name: </label>
                <p>{error2}</p> 
                <input type="text" value={lastname} onChange={ (e) => checkLength2(e.target.value) } />
            </div>
            <div>
                <label>Email Address: </label>
                <p>{error3}</p> 
                <input type="text" value={email} onChange={ (e) => checkLength3(e.target.value) } />
            </div>
            <div>
                <label>Password: </label>
                <p>{error4}</p>
                <input type="password" value={password} onChange={ (e) => checkLength4(e.target.value) } />
            </div>
            <div>
                <label>Confrim Password: </label>
                <p>{error5}</p>
                <input type="password" value={confirmpassword} onChange={ (e) => checkLength5(e.target.value) } />
            </div>
            <button>Submit</button>
        </form>
    );
}
export default Moreforms