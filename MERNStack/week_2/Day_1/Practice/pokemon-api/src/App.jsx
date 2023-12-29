import './App.css';
import { useState } from 'react';
function App() {
  const [pokemons,setPokemons]=useState([])
  const fetchPokemon=(e)=>{
    e.preventDefault()
    fetch("https://pokeapi.co/api/v2/pokemon/")
          .then((serverResponse) => serverResponse.json()) 
          .then((jsonResponse) => setPokemons(jsonResponse.results))
          .catch((error) => console.log(error));
    }
    console.log(pokemons)
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
