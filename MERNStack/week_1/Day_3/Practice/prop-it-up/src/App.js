
import './App.css';
import Person from './components/Person';
function App() {
  const value1={
  firstName:'Jane',
  lastName:'Doe',
  age:45,
  hairColor:'Black'}
  
  const value2={
    firstName:'John' ,
    lastName:'Smith' ,
    age:88,
    hairColor:'Brown'
  }

  const value3={
    firstName:'maria',
    lastName:'smith',
    age:62,
    hairColor:'Brown'
  }
  return (
    <div className="App">
      <Person prop1={ value1 } />
      <Person prop1={ value2 } />
      <Person prop1={ value3 } />
    </div>
  );
}

export default App;
