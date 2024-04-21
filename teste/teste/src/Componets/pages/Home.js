
import React, { useState } from 'react';
import axios from 'axios';
import "../../App.css";




import Footer from "../Footer";

function Home (){

    const [result, setResult] = useState("");
    const handleClick = () => {
        axios.get('http://localhost:5000/run-script')
            .then(res => {
                if (res.data) {
                    setResult(res.data); // Atualiza o estado com o resultado da solicitação
                }
            })
            .catch(err => {
                console.log("Ocorreu um erro ao ler a script!", err);
            });
    };

return(
<>
<div className="Appp">
      <button className="meuBotao"onClick={() => axios.get('http://localhost:5000/run-script')
      .then(res => res? setResult(res.data):undefined)
      .catch(err => console.log("Ocorreu um erro ao ler a script!", err))}>Executar script Python</button>
      <div id="resposta"> {result && <p>Resultado: {result}</p>}</div>

    </div>
      

<Footer/>
</>

);
}


export default Home;