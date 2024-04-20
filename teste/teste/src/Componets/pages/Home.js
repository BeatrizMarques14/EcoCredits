
import React, { useState } from 'react';
import axios from 'axios';
import "../../App.css";




import Footer from "../Footer";

function Home (){

    const [result, setResult] = useState("");
return(
<>
<div className="App">
      <button id="meuBotao"onClick={() => axios.get('http://localhost:5000/run-script')
      .then(res => res? setResult(res.data):undefined)
      .catch(err => console.log("Ocorreu um erro ao ler a script!", err))}>Executar script Python</button>
      <div id="resposta"> {result && <p>Resultado: {result}</p>}</div>

    </div>
      

<Footer/>
</>

);
}


export default Home;