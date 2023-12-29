import './App.css';
import {Routes,Route,Link} from "react-router-dom";
import { useParams } from "react-router";


const Home = (props) => { 
  return (
    <h1>welcome 👋</h1>
  );
}
    
const Id = (props) => {
  const { id } = useParams();
  return (
    <h1>The Word is :{ id }</h1>
  );
}
const Colors = (props) => {
  const { id } = useParams();
  const {color} = useParams();
  return (
    <h1 style={{ background: color }}>
      The Word is :{ id }
    </h1>
  );
}
function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/home" element={<Home/>} />
        <Route path="/home/:id" element={<Id />}/>
        <Route path="/home/:id/:color" element={<Colors />}/>
      </Routes>
    </div>
  );
}
export default App;