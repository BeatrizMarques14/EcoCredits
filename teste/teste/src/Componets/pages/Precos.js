
import React from "react";
import "../../App.css";
import "./Precos.css";

import Footer from "../Footer";

function Precos(){
  return (
    <>
    <div className="h1">
      <h1>Recompensas atribuidas cada categoria de Lixo:</h1>
    </div>
      <div className="tabela">
                <table>
                    <tr>
                        <th>Ecoponto</th>
                        <th>Recompensa</th>
                        
                    </tr>
                    <tr>
                        <td>Amarelo</td>
                        <td>2</td>
                        
                    </tr>
                    <tr>
                        <td>Verde</td>
                        <td>5</td>
                        
                    </tr>
                    <tr>
                        <td>Azul</td>
                        <td>3</td>
                        
                    </tr>
                </table>
            </div>
            
      <Footer/>
    </>
  );
}

export default Precos;