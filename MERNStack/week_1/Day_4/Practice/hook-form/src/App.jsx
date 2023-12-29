import React, { useState } from  'react';
import "./form.css";
const Form = (props) => {
    const [firstname, setFirstname] = useState("");
    const [lastname, setLastname] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmpassword, setCnfpassword] = useState("");
    const createUser = (e) => {
        e.preventDefault();
        const newUser = { firstname,lastname,email,confirmpassword,password };
        console.log("Welcome", newUser);
            setFirstname("");
            setLastname("");
            setEmail("");
            setPassword("");
            setCnfpassword("")
    };
    return(
            <form onSubmit={ createUser }>
            <div>
                <label>First Name: </label> 
                <input type="text" value={firstname} onChange={ (e) => setFirstname(e.target.value) } />
            </div>
            <div>
                <label>Last Name: </label> 
                <input type="text" value={lastname} onChange={ (e) => setLastname(e.target.value) } />
            </div>
            <div>
                <label>Email Address: </label> 
                <input type="text" value={email} onChange={ (e) => setEmail(e.target.value) } />
            </div>
            <div>
                <label>Password: </label>
                <input type="text" value={password} onChange={ (e) => setPassword(e.target.value) } />
            </div>
            <div>
                <label>Confrim Password: </label>
                <input type="text" value={confirmpassword} onChange={ (e) => setCnfpassword(e.target.value) } />
            </div>
                <div className='js'>
                    <div>{JSON.stringify(firstname)}</div>
                    <div>{JSON.stringify(lastname)}</div>
                    <div>{JSON.stringify(email)}</div>
                    <div>{JSON.stringify(password)}</div>
                    <div>{JSON.stringify(confirmpassword)}</div>
                </div>
        </form>
    );
};
export default Form;