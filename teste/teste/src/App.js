import './App.css';
import Navg from './Componets/Navg';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Componets/pages/Home';
import Servicos from './Componets/pages/Precos';


function App() {
  return (
    <>
    <Router>
      <Navg/>
      <Routes>

      <Route path='/'  exact Component={Home}/>
      <Route path='/Precos'  exact Component={Servicos}/>

      
      </Routes>
    </Router>
    </>
  );
}

export default App;
