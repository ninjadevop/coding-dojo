import './App.css';
import Person_card from './component/Person_card';
function App() {
  const value1={
    lastName : 'Doe',
    firstName: 'jane',
    age:45,
    haircolor: 'black'
  }
  const value2={
    lastName : 'Smith',
    firstName: 'John',
    age:88,
    haircolor: 'brown'
  }
  
  return (
    <div className="App">
      <Person_card prop1={ value1 } />
      
      <Person_card prop1={ value2 } />
    </div>
    
  );
}

export default App;
