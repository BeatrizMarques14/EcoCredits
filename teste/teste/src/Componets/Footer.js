import React from "react";
import { Button } from "./Button";
import './Footer.css';
import { Link } from "react-router-dom";

function Footer(){
return(
    <div className="footer-container">
        <div className="footer-links">
            <div className="footer-link-wrapper">
                <div className="footer-link-items">
                    <h2>Aplicação</h2>
                    <Link to='/Home'>Produtos inseridos</Link>
                    <Link to='/Precos'>Recompenças</Link>
                </div>
                
            </div>
        </div>
       
    </div>
)

}

export default Footer