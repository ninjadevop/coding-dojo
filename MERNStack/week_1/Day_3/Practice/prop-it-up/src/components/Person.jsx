import React from 'react'

const Person = (Props) => {
    const {prop1}=Props
    return (
    <div>
        <h1> {prop1.lastName}{prop1.firstName}</h1>
        <p>Age : {prop1.age}</p>
        <p>Hair color : {prop1.haircolor}</p>
    </div>
    )
}

export default Person