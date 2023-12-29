import './App.css';
import axios from "axios";
import { useState } from 'react';

function App() {
  const [pokemons,setPokemons]=useState([])
  const fetchPokemon=(e)=>{
    e.preventDefault()
    axios
    .get("https://pokeapi.co/api/v2/pokemon/")
    .then((response) => {
      setPokemons(response.data.results);
      console.log(response);
    })
    .catch((error) => console.log(error));
    }
  return (
    <div className="App">
    <button onClick={fetchPokemon}>fetchPokemon jjj</button>
    <hr/>
    <div>
    {pokemons.map((onePokemon,idx)=>{
      return(
        <div key={idx}>
          <p>{onePokemon.name}</p>
        </div>
      );
    })}
    </div>
  </div>
  );
}
export default App;