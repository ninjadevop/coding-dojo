import React from 'react'
import { useState } from 'react'
const Person_card = ({prop1}) => {
    
    const [newp,setNewp]=useState(prop1)
    console.log(newp)
    const increase=()=>{
        setNewp({...newp,age:newp.age+1})
    }
    return (
    <div>
        <h1>{newp.lastName} {newp.firstName}</h1>
        <p>age :{newp.age}</p>
        <p>hair color :{newp.haircolor}</p>
        <button onClick={increase}>Count</button>
    </div>
    )
}

export default Person_card
